"""
Generate recommendations based on maturity assessment results.
"""

# Define improvement recommendations for each question based on selected answer level
RECOMMENDATIONS = {
    "cicd_coverage": {
        "low": {
            "title": "Expand CI/CD Coverage",
            "details": "Your CI/CD pipeline currently covers limited applications. Consider extending your pipeline to include more critical applications, starting with one additional app (CRM or BRM).",
            "actions": [
                "Create a proof-of-concept CI/CD pipeline for CRM application",
                "Standardize Jenkinsfiles across applications",
                "Implement shared Jenkins libraries for common pipeline steps"
            ],
            "timeframe": "0-3 months",
            "priority": "High"
        },
        "medium": {
            "title": "Standardize CI/CD Across Apps",
            "details": "You've made good progress with CI/CD adoption. Work on standardization and extending coverage to all critical applications.",
            "actions": [
                "Extend CI/CD pipeline to remaining critical applications",
                "Implement centralized pipeline templates",
                "Establish deployment metrics dashboard"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Enable Autonomous Deployments",
            "details": "Your CI/CD coverage is strong. Focus now on enabling more autonomous deployments through advanced automation.",
            "actions": [
                "Implement progressive delivery with canary deployments",
                "Add automated quality gates",
                "Integrate AI-assisted deployment decisions"
            ],
            "timeframe": "6-12 months",
            "priority": "Low"
        }
    },
    "pipeline_config": {
        "low": {
            "title": "Implement Pipeline Reusability",
            "details": "Your pipeline configurations have significant duplication. Implement shared pipeline components to improve maintainability.",
            "actions": [
                "Extract common pipeline steps into shared libraries",
                "Create a central Git repository for pipeline components",
                "Implement version control for pipeline configurations"
            ],
            "timeframe": "0-3 months",
            "priority": "Medium"
        },
        "medium": {
            "title": "Parameterize Pipeline Templates",
            "details": "Enhance your templates with parameters to make them more flexible across applications.",
            "actions": [
                "Convert existing templates to parameterized versions",
                "Implement pipeline configuration validation",
                "Create documentation for template usage"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Create Self-Service Pipeline System",
            "details": "Implement a self-service system for teams to easily create standardized pipelines.",
            "actions": [
                "Build a pipeline generator UI/API",
                "Establish governance for template modifications",
                "Implement metrics for pipeline usage and performance"
            ],
            "timeframe": "6-12 months",
            "priority": "Low"
        }
    },
    "downtime_impact": {
        "low": {
            "title": "Establish Deployment Impact Metrics",
            "details": "Implement basic metrics to quantify the impact of deployment failures.",
            "actions": [
                "Track deployment-related outage durations",
                "Establish baseline costs for different types of failures",
                "Create a simple dashboard for deployment reliability"
            ],
            "timeframe": "0-3 months",
            "priority": "Medium"
        },
        "medium": {
            "title": "Enhance Impact Analysis",
            "details": "Improve your deployment impact metrics with more detailed analysis.",
            "actions": [
                "Link business transactions to deployment events",
                "Implement SLA tracking for deployments",
                "Create automated impact reports"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Optimize Based on Impact Data",
            "details": "Use your comprehensive impact data to make strategic improvements.",
            "actions": [
                "Prioritize pipeline improvements based on impact data",
                "Implement predictive analysis for deployment risk",
                "Automate mitigation strategies for high-risk deployments"
            ],
            "timeframe": "6-12 months",
            "priority": "Low"
        }
    },
    "gitops_readiness": {
        "low": {
            "title": "Implement GitOps for First Application",
            "details": "Start your GitOps journey by implementing ArgoCD for one application.",
            "actions": [
                "Set up ArgoCD in your OpenShift cluster",
                "Convert one application to GitOps deployment model",
                "Establish Git workflow for configuration changes"
            ],
            "timeframe": "0-3 months",
            "priority": "High"
        },
        "medium": {
            "title": "Expand GitOps Adoption",
            "details": "Extend GitOps to all critical applications for consistent deployment.",
            "actions": [
                "Convert remaining applications to GitOps model",
                "Implement app-of-apps pattern for orchestration",
                "Establish GitOps governance model"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Implement Multi-Cluster GitOps",
            "details": "Enhance your GitOps implementation with multi-cluster capabilities.",
            "actions": [
                "Set up fleet management for multiple clusters",
                "Implement promotion workflows across environments",
                "Create GitOps dashboard for deployment visualization"
            ],
            "timeframe": "6-12 months",
            "priority": "Low"
        }
    },
    "secrets_mgmt": {
        "low": {
            "title": "Implement Basic Secrets Management",
            "details": "Move away from hardcoded secrets to a more secure approach using Kubernetes Secrets.",
            "actions": [
                "Audit applications for hardcoded secrets",
                "Migrate secrets to Kubernetes Secrets",
                "Implement RBAC for secrets access control"
            ],
            "timeframe": "0-3 months",
            "priority": "High"
        },
        "medium": {
            "title": "Implement Vault for All Applications",
            "details": "Extend Vault usage to all applications and implement dynamic secrets.",
            "actions": [
                "Set up Vault for remaining applications",
                "Implement dynamic secret rotation",
                "Create automated onboarding process for new apps"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Implement Identity-Based Access",
            "details": "Move towards identity-based access control with SPIFFE.",
            "actions": [
                "Implement SPIFFE/SPIRE for service identity",
                "Integrate with service mesh for mTLS",
                "Implement zero-trust access patterns"
            ],
            "timeframe": "6-12 months",
            "priority": "Medium"
        }
    },
    "central_logging": {
        "low": {
            "title": "Implement Centralized Logging",
            "details": "Set up basic centralized logging with EFK stack.",
            "actions": [
                "Deploy Elasticsearch, Fluentd, and Kibana",
                "Configure log forwarding for all applications",
                "Create basic log dashboards for common scenarios"
            ],
            "timeframe": "0-3 months",
            "priority": "High"
        },
        "medium": {
            "title": "Enhance Logging with Alerts",
            "details": "Add alerting capabilities to your logging infrastructure.",
            "actions": [
                "Define alert criteria for critical log patterns",
                "Integrate alerts with notification systems",
                "Create runbooks for common alert scenarios"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Implement Advanced Log Analytics",
            "details": "Enhance your logging system with advanced analytics capabilities.",
            "actions": [
                "Set up log correlation with Dynatrace",
                "Implement machine learning for anomaly detection",
                "Create business-impact dashboards based on log data"
            ],
            "timeframe": "6-12 months",
            "priority": "Medium"
        }
    },
    "apm_monitoring": {
        "low": {
            "title": "Implement Basic APM Monitoring",
            "details": "Set up basic APM monitoring for your applications.",
            "actions": [
                "Install Dynatrace agents on OpenShift nodes",
                "Implement basic application instrumentation",
                "Create baseline performance dashboards"
            ],
            "timeframe": "0-3 months",
            "priority": "High"
        },
        "medium": {
            "title": "Enhance Application Monitoring",
            "details": "Expand your monitoring coverage to include detailed application metrics and traces.",
            "actions": [
                "Implement distributed tracing across applications",
                "Set up custom business metrics in Dynatrace",
                "Create SLA-based alerts and dashboards"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Implement Auto-Remediation",
            "details": "Leverage advanced monitoring for automated issue resolution.",
            "actions": [
                "Define auto-remediation actions for common problems",
                "Integrate Dynatrace with service management tools",
                "Implement AI-assisted problem resolution"
            ],    
                "timeframe": "6-12 months",
            "priority": "Medium"
        }
    },
    "failure_logs": {
        "low": {
            "title": "Improve Deployment Failure Visibility",
            "details": "Enhance visibility into deployment failures to improve troubleshooting.",
            "actions": [
                "Configure Jenkins to forward logs to EFK",
                "Create specific log dashboards for deployment failures",
                "Implement log retention policies for audit purposes"
            ],
            "timeframe": "0-3 months",
            "priority": "Medium"
        },
        "medium": {
            "title": "Enhance Failure Analysis",
            "details": "Improve your ability to analyze deployment failures.",
            "actions": [
                "Set up log correlation between Jenkins and application logs",
                "Create failure pattern recognition",
                "Implement automated failure classification"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Implement Full Traceability",
            "details": "Create end-to-end traceability for deployment failures.",
            "actions": [
                "Integrate Dynatrace with ServiceDesk for automated tickets",
                "Implement deployment audit trails",
                "Create executive dashboards for deployment reliability"
            ],
            "timeframe": "6-12 months",
            "priority": "Low"
        }
    },
    "failure_tracking": {
        "low": {
            "title": "Implement Basic Incident Management",
            "details": "Set up basic incident tracking for CI/CD failures.",
            "actions": [
                "Create ServiceDesk integration for manual ticket creation",
                "Define severity levels for different failure types",
                "Establish basic failure response procedures"
            ],
            "timeframe": "0-3 months",
            "priority": "High"
        },
        "medium": {
            "title": "Automate Incident Management",
            "details": "Implement automated incident creation and tracking.",
            "actions": [
                "Configure Jenkins to auto-create tickets on failure",
                "Implement automatic assignment based on failure type",
                "Create dashboards for incident trends and metrics"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Implement AI-Assisted Incident Management",
            "details": "Enhance incident management with AI assistance.",
            "actions": [
                "Implement root-cause analysis with Dynatrace",
                "Configure AI-assisted ticket classification",
                "Create predictive failure models"
            ],
            "timeframe": "6-12 months",
            "priority": "Low"
        }
    },
    "post_mortem": {
        "low": {
            "title": "Implement Basic Post-Mortem Process",
            "details": "Establish a basic post-mortem process for significant failures.",
            "actions": [
                "Create a post-mortem template",
                "Schedule regular post-mortem meetings",
                "Capture lessons learned in a knowledge base"
            ],
            "timeframe": "0-3 months",
            "priority": "Medium"
        },
        "medium": {
            "title": "Enhance Post-Mortem Effectiveness",
            "details": "Improve your post-mortem process for better learning.",
            "actions": [
                "Implement blameless post-mortem culture",
                "Create action tracking for post-mortem outcomes",
                "Analyze trends across multiple post-mortems"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Automate Remediation Playbooks",
            "details": "Convert post-mortem learnings into automated remediation.",
            "actions": [
                "Create automated remediation playbooks",
                "Implement automated testing of remediation procedures",
                "Build self-healing capabilities into pipelines"
            ],
            "timeframe": "6-12 months",
            "priority": "Low"
        }
    },
    "compliance_auditing": {
        "low": {
            "title": "Implement Basic Compliance Scanning",
            "details": "Set up basic compliance scanning for your applications.",
            "actions": [
                "Implement Trivy for container scanning",
                "Create baseline compliance requirements",
                "Document manual compliance procedures"
            ],
            "timeframe": "0-3 months",
            "priority": "High"
        },
        "medium": {
            "title": "Enhance Compliance Automation",
            "details": "Improve compliance automation in your pipelines.",
            "actions": [
                "Implement OPA policies in ArgoCD",
                "Create automated compliance reports",
                "Set up compliance gates in CI/CD pipelines"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Implement Continuous Compliance",
            "details": "Move towards continuous compliance monitoring and enforcement.",
            "actions": [
                "Create compliance dashboards in Dynatrace",
                "Implement real-time compliance monitoring",
                "Set up automated remediation for compliance issues"
            ],
            "timeframe": "6-12 months",
            "priority": "Medium"
        }
    },
    "tekton_structure": {
        "low": {
            "title": "Modularize Tekton Tasks",
            "details": "Break down monolithic Tekton tasks into modular components.",
            "actions": [
                "Identify common pipeline steps across applications",
                "Create reusable Tekton Tasks for common operations",
                "Implement version control for Tekton resources"
            ],
            "timeframe": "0-3 months",
            "priority": "Medium"
        },
        "medium": {
            "title": "Standardize Pipeline Components",
            "details": "Create standardized pipeline components for reuse.",
            "actions": [
                "Create a central repository for shared Tasks",
                "Implement governance process for shared components",
                "Create documentation for component usage"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Create Self-Service Pipeline Platform",
            "details": "Implement a self-service platform for Tekton pipelines.",
            "actions": [
                "Create parameterized Pipeline templates",
                "Build a web UI for pipeline generation",
                "Implement metrics and governance for pipeline usage"
            ],
            "timeframe": "6-12 months",
            "priority": "Low"
        }
    },
    "pipeline_triggers": {
        "low": {
            "title": "Implement Automated Pipeline Triggers",
            "details": "Move from manual pipeline execution to automated triggers.",
            "actions": [
                "Configure Git webhooks for Tekton",
                "Implement basic validation before pipeline execution",
                "Create documentation for trigger setup"
            ],
            "timeframe": "0-3 months",
            "priority": "Medium"
        },
        "medium": {
            "title": "Enhance Pipeline Governance",
            "details": "Improve pipeline triggers with proper governance.",
            "actions": [
                "Implement PR-based triggers with approval gates",
                "Create role-based access for pipeline execution",
                "Set up audit trails for pipeline execution"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Implement Event-Driven Pipelines",
            "details": "Move towards event-driven pipeline architecture.",
            "actions": [
                "Implement Tekton triggers for event-based execution",
                "Set up Kafka integration for event-driven pipelines",
                "Create automated promotion workflows across environments"
            ],
            "timeframe": "6-12 months",
            "priority": "Low"
        }
    },
    "cluster_provisioning": {
        "low": {
            "title": "Automate Cluster Provisioning",
            "details": "Move from manual cluster provisioning to automation.",
            "actions": [
                "Implement Terraform for cluster provisioning",
                "Create infrastructure-as-code repositories",
                "Document automated provisioning procedures"
            ],
            "timeframe": "0-3 months",
            "priority": "Medium"
        },
        "medium": {
            "title": "Implement GitOps for Clusters",
            "details": "Adopt GitOps practices for cluster management.",
            "actions": [
                "Implement Cluster API with ArgoCD",
                "Create GitOps workflows for cluster configuration",
                "Set up validation for cluster changes"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Create Multi-Cluster Management",
            "details": "Implement advanced multi-cluster management capabilities.",
            "actions": [
                "Set up federation across clusters",
                "Implement centralized policy management",
                "Create self-service capabilities for cluster provisioning"
            ],
            "timeframe": "6-12 months",
            "priority": "Low"
        }
    },
    "workload_scaling": {
        "low": {
            "title": "Implement Basic Autoscaling",
            "details": "Move from manual scaling to basic autoscaling.",
            "actions": [
                "Configure Horizontal Pod Autoscaler for applications",
                "Define appropriate resource requests and limits",
                "Create baseline monitoring for resource usage"
            ],
            "timeframe": "0-3 months",
            "priority": "Medium"
        },
        "medium": {
            "title": "Implement Advanced Scaling",
            "details": "Enhance scaling with more sophisticated approaches.",
            "actions": [
                "Implement KEDA for event-based scaling",
                "Create custom metrics for application-specific scaling",
                "Set up vertical pod autoscaling where appropriate"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Implement Predictive Scaling",
            "details": "Move towards predictive and AI-driven scaling.",
            "actions": [
                "Integrate Dynatrace data for predictive scaling",
                "Implement machine learning models for workload prediction",
                "Create cost optimization based on scaling patterns"
            ],
            "timeframe": "6-12 months",
            "priority": "Low"
        }
    },
    "service_mesh": {
        "low": {
            "title": "Implement Basic Service Mesh",
            "details": "Set up a basic service mesh for your applications.",
            "actions": [
                "Install OpenShift Service Mesh",
                "Configure basic traffic routing",
                "Implement basic observability features"
            ],
            "timeframe": "0-3 months",
            "priority": "Medium"
        },
        "medium": {
            "title": "Enhance Service Mesh Security",
            "details": "Improve service mesh with enhanced security features.",
            "actions": [
                "Implement mTLS for service-to-service communication",
                "Create service-level access policies",
                "Configure authentication and authorization"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Implement Advanced Mesh Features",
            "details": "Add advanced service mesh capabilities for sophisticated deployments.",
            "actions": [
                "Configure multi-cluster mesh",
                "Implement automated traffic shifting for deployments",
                "Create advanced observability dashboards"
            ],
            "timeframe": "6-12 months",
            "priority": "Low"
        }
    },
    "env_config_mgmt": {
        "low": {
            "title": "Improve Configuration Management",
            "details": "Move from manual configuration to more structured approaches.",
            "actions": [
                "Implement Helm charts for application configuration",
                "Create separate values files for different environments",
                "Implement version control for configuration"
            ],
            "timeframe": "0-3 months",
            "priority": "Medium"
        },
        "medium": {
            "title": "Enhance Configuration Structure",
            "details": "Improve configuration management with better structure.",
            "actions": [
                "Implement Kustomize overlays for environment differences",
                "Create validation for configuration changes",
                "Set up configuration drift detection"
            ],
            "timeframe": "3-6 months",
            "priority": "Medium"
        },
        "high": {
            "title": "Implement Dynamic Configuration",
            "details": "Move towards dynamic, secure configuration management.",
            "actions": [
                "Integrate Vault for secret injection",
                "Implement GitOps app-of-apps pattern",
                "Create self-service configuration capabilities"
            ],
            "timeframe": "6-12 months",
            "priority": "Low"
        }
    }
}

# Helper function to categorize scores
def get_recommendation_category(score, max_score=5):
    """Categorize scores into low, medium, or high."""
    percentage = score / max_score
    if percentage < 0.4:
        return "low"
    elif percentage < 0.7:
        return "medium"
    else:
        return "high"

# Function to generate recommendations based on assessment results
def generate_recommendations(answers, questions):
    """Generate targeted recommendations based on assessment results."""
    recommendations = []
    priorities = {"High": 3, "Medium": 2, "Low": 1}
    
    # Process each question to generate recommendations
    for section in questions:
        for question in section["questions"]:
            question_id = question["id"]
            
            # Skip if question wasn't answered
            if question_id not in answers:
                continue
                
            # Get the selected answer and its score
            answer_idx = int(answers[question_id])
            if 0 <= answer_idx < len(question["options"]):
                score = question["options"][answer_idx]["score"]
                max_score = 5  # Assuming max score is 5
                
                # Skip high scores that don't need improvement
                if score >= 4:  # Only recommend for scores below 4
                    continue
                    
                # Determine category (low, medium, high)
                category = get_recommendation_category(score, max_score)
                
                # Add recommendation if available
                if question_id in RECOMMENDATIONS and category in RECOMMENDATIONS[question_id]:
                    rec = RECOMMENDATIONS[question_id][category]
                    rec["question_id"] = question_id
                    rec["category"] = category
                    rec["question_text"] = question["question"]
                    rec["current_score"] = score
                    rec["priority_value"] = priorities.get(rec["priority"], 0)
                    recommendations.append(rec)
    
    # Sort recommendations by priority (high to low)
    recommendations.sort(key=lambda x: x["priority_value"], reverse=True)
    
    # Group recommendations by phase
    phases = {
        "0-3 months": [],
        "3-6 months": [],
        "6-12 months": []
    }
    
    for rec in recommendations:
        if rec["timeframe"] in phases:
            phases[rec["timeframe"]].append(rec)
    
    return phases