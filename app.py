"""
DevOps Maturity Assessment Tool - Main Application
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from questions import QUESTIONS, calculate_maturity
from recommendations import generate_recommendations
from pdf_generator import generate_pdf_report
import base64
import os

# Page configuration
st.set_page_config(
    page_title="DevOps Maturity Assessment",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for tracking answers and progress
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "current_section" not in st.session_state:
    st.session_state.current_section = 0
if "results" not in st.session_state:
    st.session_state.results = None
if "show_results" not in st.session_state:
    st.session_state.show_results = False
if "phases" not in st.session_state:
    st.session_state.phases = None

# Function to create a download link for PDF
def get_pdf_download_link(file_path):
    with open(file_path, "rb") as f:
        pdf_bytes = f.read()
    b64 = base64.b64encode(pdf_bytes).decode()
    filename = os.path.basename(file_path)
    return f'<a href="data:application/pdf;base64,{b64}" download="{filename}">Download PDF Report</a>'

# Function to create maturity gauge chart
def create_gauge_chart(percentage):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=percentage,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "DevOps Maturity"},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 20], 'color': 'red'},
                {'range': [20, 40], 'color': 'orange'},
                {'range': [40, 60], 'color': 'yellow'},
                {'range': [60, 80], 'color': 'lightgreen'},
                {'range': [80, 100], 'color': 'green'}
            ],
        }
    ))
    fig.update_layout(height=300)
    return fig

# Function to create radar chart for section scores
def create_radar_chart(section_scores):
    categories = list(section_scores.keys())
    values = list(section_scores.values())
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Current Maturity'
    ))
    
    # Add ideal state (all 5's)
    fig.add_trace(go.Scatterpolar(
        r=[5] * len(categories),
        theta=categories,
        fill='toself',
        name='Ideal State',
        opacity=0.2
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )),
        showlegend=True,
        height=500
    )
    
    return fig

# Main application layout
def main():
    # Header
    st.title("DevOps Maturity Assessment Tool")
    st.markdown("This tool will help you assess your DevOps maturity and provide recommendations for improvement.")
    
    # Sidebar for progress and navigation
    with st.sidebar:
        st.header("Assessment Progress")
        progress = (len(st.session_state.answers) / sum(len(section["questions"]) for section in QUESTIONS) * 100)
        st.progress(progress/100)
        st.write(f"{progress:.1f}% complete")
        
        # Navigation buttons
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Previous Section", disabled=st.session_state.current_section == 0):
                st.session_state.current_section = max(0, st.session_state.current_section - 1)
                
        with col2:
            if st.button("Next Section", disabled=st.session_state.current_section >= len(QUESTIONS) - 1):
                if all_required_answered(QUESTIONS[st.session_state.current_section]["questions"]):
                    st.session_state.current_section = min(len(QUESTIONS) - 1, st.session_state.current_section + 1)
                else:
                    st.error("Please answer all required questions before proceeding.")
        
        # Submit button
        if st.button("Submit Assessment", disabled=not all_required_answered_all_sections()):
            st.session_state.results = calculate_maturity(st.session_state.answers)
            st.session_state.phases = generate_recommendations(
                st.session_state.answers, 
                QUESTIONS
            )
            st.session_state.show_results = True
    
    # If showing results, display the results page
    if st.session_state.show_results and st.session_state.results:
        show_results_page()
    else:
        # Safety check to prevent index errors
        if st.session_state.current_section >= len(QUESTIONS):
            st.session_state.current_section = len(QUESTIONS) - 1
        elif st.session_state.current_section < 0:
            st.session_state.current_section = 0
        # Otherwise, show the current section of questions
        current_section = QUESTIONS[st.session_state.current_section]
        st.header(current_section["section"])
        
        # Display questions for current section
        for i, question in enumerate(current_section["questions"]):
            question_id = question["id"]
            
            # Create a unique key for this question
            question_key = f"{question_id}_radio"
            
            # Add required indicator if needed
            question_text = question["question"]
            if question.get("required", False):
                question_text += " *"
            
            # Radio button for options
            options = [opt["text"] for opt in question["options"]]
            selected = st.radio(
                question_text,
                options=options,
                index=int(st.session_state.answers.get(question_id, 0)) if question_id in st.session_state.answers else 0,
                key=question_key
            )
            
            # Store answer when selected
            if selected:
                selected_index = options.index(selected)
                st.session_state.answers[question_id] = selected_index
                
                # Show explanation in an expandable section
                with st.expander("Why is this important?"):
                    st.write(question["options"][selected_index]["explanation"])
            
            st.markdown("---")
        
        # Navigation buttons at bottom of page
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.button("Previous", disabled=st.session_state.current_section == 0):
                st.session_state.current_section = max(0, st.session_state.current_section - 1)
                
        with col3:
            if st.button("Next", disabled=st.session_state.current_section >= len(QUESTIONS) - 1):
                if all_required_answered(QUESTIONS[st.session_state.current_section]["questions"]):
                    st.session_state.current_section = min(len(QUESTIONS) - 1, st.session_state.current_section + 1)
                else:
                    st.error("Please answer all required questions before proceeding.")

# Function to display results page
def show_results_page():
    st.header("DevOps Maturity Assessment Results")
    
    results = st.session_state.results
    phases = st.session_state.phases
    
    # Display overall score
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Overall Maturity")
        st.plotly_chart(create_gauge_chart(results["percentage"]), use_container_width=True)
        st.write(f"Overall Maturity Level: {results['overall_level']}/5")
        
    with col2:
        st.subheader("Maturity by Section")
        st.plotly_chart(create_radar_chart(results["section_scores"]), use_container_width=True)
    
    # Display recommendations by phase
    st.header("Improvement Roadmap")
    
    # Create tabs for each phase
    tab1, tab2, tab3 = st.tabs(["Phase 1 (0-3 Months)", "Phase 2 (3-6 Months)", "Phase 3 (6-12 Months)"])
    
    # Phase 1
    with tab1:
        display_phase_recommendations(phases.get("0-3 months", []))
        
    # Phase 2
    with tab2:
        display_phase_recommendations(phases.get("3-6 months", []))
        
    # Phase 3
    with tab3:
        display_phase_recommendations(phases.get("6-12 months", []))
    
    # Generate and allow download of PDF report
    if st.button("Generate PDF Report"):
        with st.spinner("Generating PDF report..."):
            pdf_file = generate_pdf_report(
                results, 
                st.session_state.answers, 
                QUESTIONS,
                phases
            )
            st.success(f"PDF report generated: {pdf_file}")
            st.markdown(get_pdf_download_link(pdf_file), unsafe_allow_html=True)
    
    # Option to restart assessment
    if st.button("Restart Assessment"):
        st.session_state.answers = {}
        st.session_state.current_section = 0
        st.session_state.results = None
        st.session_state.show_results = False
        st.session_state.phases = None
        st.experimental_rerun()

# Helper function to display recommendations for a phase
def display_phase_recommendations(recommendations):
    if not recommendations:
        st.write("No recommendations for this phase.")
        return
    
    for i, rec in enumerate(recommendations, 1):
        with st.expander(f"{i}. {rec['title']} (Priority: {rec['priority']})"):
            st.write(rec["details"])
            
            st.subheader("Recommended Actions:")
            for action in rec["actions"]:
                st.write(f"• {action}")

# Check if all required questions in a section are answered
def all_required_answered(questions):
    for q in questions:
        if q.get("required", False) and q["id"] not in st.session_state.answers:
            return False
    return True

# Check if all required questions in all sections are answered
def all_required_answered_all_sections():
    for section in QUESTIONS:
        if not all_required_answered(section["questions"]):
            return False
    return True

if __name__ == "__main__":
    main()