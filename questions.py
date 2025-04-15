"""
DevOps Maturity Model Questions and Scoring Logic
"""

# Define the questions structure
QUESTIONS = [
    {
        "section": "CI/CD Pipeline Maturity",
        "questions": [
            {
                "id": "cicd_coverage",
                "question": "Which applications are currently in the CI/CD pipeline?",
                "options": [
                    {"text": "Only Fuse", "level": 1, "score": 1, 
                     "explanation": "Having only one application in the CI/CD pipeline limits the benefits of automation across your organization."},
                    {"text": "Fuse + 1 other app (e.g., CRM)", "level": 2, "score": 2,
                     "explanation": "Adding a second application shows progress but still leaves most systems using manual processes."},
                    {"text": "Fuse + 2-3 telecom apps", "level": 3, "score": 3,
                     "explanation": "Having multiple apps demonstrates good adoption of CI/CD practices."},
                    {"text": "All critical apps (Fuse, CRM, BRM, EPC)", "level": 4, "score": 4,
                     "explanation": "Including all critical apps shows strong DevOps maturity."},
                    {"text": "Full telecom stack + autonomous deployments", "level": 5, "score": 5,
                     "explanation": "This represents best-in-class DevOps implementation with full automation."}
                ],
                "required": True,
                "weight": 2.0  # Higher weight for critical questions
            },
            {
                "id": "pipeline_config",
                "question": "How are pipeline configurations shared across apps?",
                "options": [
                    {"text": "No reuse (per-app Jenkinsfiles)", "level": 1, "score": 1,
                     "explanation": "This approach leads to significant duplication and maintenance overhead."},
                    {"text": "Basic shared snippets", "level": 2, "score": 2,
                     "explanation": "Some reuse is happening but isn't formalized or consistent."},
                    {"text": "Centralized template library", "level": 3, "score": 3,
                     "explanation": "Having a centralized approach improves consistency and maintenance."},
                    {"text": "Parameterized multi-app pipelines", "level": 4, "score": 4,
                     "explanation": "This approach significantly reduces duplication and improves maintainability."},
                    {"text": "Self-service pipeline generator", "level": 5, "score": 5,
                     "explanation": "This represents an optimal approach where teams can easily create standardized pipelines."}
                ],
                "required": True,
                "weight": 1.5
            },
            {
                "id": "downtime_impact",
                "question": "Have you quantified downtime costs for failed deployments?",
                "options": [
                    {"text": "No data", "level": 1, "score": 1,
                     "explanation": "Without impact data, it's difficult to prioritize improvements effectively."},
                    {"text": "Rough estimates", "level": 2, "score": 2,
                     "explanation": "Having estimates is a good start, but more precise data would be beneficial."},
                    {"text": "SLA-based metrics (e.g., $/minute downtime)", "level": 4, "score": 4,
                     "explanation": "Having formal metrics allows for data-driven improvement decisions."}
                ],
                "required": False,
                "weight": 1.0
            }
        ]
    },
    {
        "section": "GitOps & Environment Management",
        "questions": [
            {
                "id": "gitops_readiness",
                "question": "Are CRM/BRM/COM/EPC deployments GitOps-ready?",
                "options": [
                    {"text": "No GitOps", "level": 1, "score": 1,
                     "explanation": "Without GitOps, you miss key benefits like automated reconciliation and audit trails."},
                    {"text": "Only Fuse uses ArgoCD", "level": 2, "score": 2,
                     "explanation": "Limited adoption means inconsistent deployment approaches across applications."},
                    {"text": "Fuse + 1 telecom app in ArgoCD", "level": 3, "score": 3,
                     "explanation": "Expanding GitOps adoption is a positive sign of maturing practices."},
                    {"text": "All apps use GitOps", "level": 4, "score": 4,
                     "explanation": "Full adoption enables consistent deployment approaches and better compliance."},
                    {"text": "GitOps with multi-cluster management", "level": 5, "score": 5,
                     "explanation": "This is the most advanced approach, enabling complex multi-environment orchestration."}
                ],
                "required": True,
                "weight": 1.5
            },
            {
                "id": "env_config_mgmt",
                "question": "How are environment-specific configs (dev/stage/prod) managed?",
                "options": [
                    {"text": "Manual edits per env", "level": 1, "score": 1,
                     "explanation": "Manual configuration is error-prone and not scalable."},
                    {"text": "Helm values.yaml per env", "level": 2, "score": 2,
                     "explanation": "Using Helm improves consistency but still requires manual updates per environment."},
                    {"text": "Kustomize overlays", "level": 3, "score": 3,
                     "explanation": "Kustomize provides a more structured approach to configuration management."},
                    {"text": "GitOps app-of-apps pattern", "level": 4, "score": 4,
                     "explanation": "This approach provides better orchestration of multiple applications."},
                    {"text": "Dynamic config injection (Vault + ArgoCD)", "level": 5, "score": 5,
                     "explanation": "This represents best practice with secure, dynamic configuration management."}
                ],
                "required": True,
                "weight": 1.0
            }
        ]
    },
    {
        "section": "Monitoring & Observability",
        "questions": [
            {
                "id": "central_logging",
                "question": "How are logs centralized for Fuse/CRM/EPC apps?",
                "options": [
                    {"text": "No central logging", "level": 1, "score": 1,
                     "explanation": "Without centralized logging, troubleshooting is significantly more difficult."},
                    {"text": "Basic EFK (Fluentd → Elasticsearch)", "level": 2, "score": 2,
                     "explanation": "Basic EFK provides log aggregation but limited analytics capabilities."},
                    {"text": "EFK with log alerts", "level": 3, "score": 3,
                     "explanation": "Adding alerting improves proactive issue detection."},
                    {"text": "EFK + Dynatrace log correlation", "level": 4, "score": 4,
                     "explanation": "Correlation between logs and other telemetry provides much deeper insights."},
                    {"text": "AI-driven log anomaly detection", "level": 5, "score": 5,
                     "explanation": "Automated anomaly detection represents best-in-class observability."}
                ],
                "required": True,
                "weight": 1.5
            },
            {
                "id": "apm_monitoring",
                "question": "Does Dynatrace monitor OpenShift + Fuse?",
                "options": [
                    {"text": "No Dynatrace", "level": 1, "score": 1,
                     "explanation": "Without APM, you have limited visibility into application performance."},
                    {"text": "Only infra monitoring", "level": 2, "score": 2,
                     "explanation": "Infrastructure monitoring is important but misses application-level insights."},
                    {"text": "Fuse app metrics + traces", "level": 3, "score": 3,
                     "explanation": "Application monitoring provides better visibility into user experience issues."},
                    {"text": "End-to-end telecom app tracing", "level": 4, "score": 4,
                     "explanation": "End-to-end tracing shows the complete picture of request flows."},
                    {"text": "Dynatrace-driven auto-remediation", "level": 5, "score": 5,
                     "explanation": "Automated remediation represents the highest level of operational maturity."}
                ],
                "required": True,
                "weight": 1.0
            },
            {
                "id": "failure_logs",
                "question": "Where are deployment failure logs stored?",
                "options": [
                    {"text": "Jenkins console only", "level": 1, "score": 1,
                     "explanation": "Console-only logs are difficult to analyze and don't persist reliably."},
                    {"text": "EFK (Elasticsearch)", "level": 3, "score": 3,
                     "explanation": "Central logging improves troubleshooting capabilities."},
                    {"text": "Dynatrace + ServiceDesk tickets", "level": 5, "score": 5,
                     "explanation": "Integration with tickets provides full traceability for audit purposes."}
                ],
                "required": False,
                "weight": 1.0
            }
        ]
    },
    {
        "section": "Incident Management",
        "questions": [
            {
                "id": "failure_tracking",
                "question": "How are CI/CD failures tracked?",
                "options": [
                    {"text": "No ticketing", "level": 1, "score": 1,
                     "explanation": "Without formal tracking, failures can be missed or forgotten."},
                    {"text": "Manual ServiceDesk tickets", "level": 2, "score": 2,
                     "explanation": "Manual tickets are better than nothing but prone to inconsistency."},
                    {"text": "Auto-tickets via Jenkins plugin", "level": 3, "score": 3,
                     "explanation": "Automation ensures consistent tracking of all failures."},
                    {"text": "ServiceDesk + Dynatrace integration", "level": 4, "score": 4,
                     "explanation": "Integration enriches tickets with detailed diagnostic information."},
                    {"text": "AI-driven root-cause tickets", "level": 5, "score": 5,
                     "explanation": "AI assistance significantly speeds up troubleshooting."}
                ],
                "required": True,
                "weight": 1.0
            },
            {
                "id": "post_mortem",
                "question": "What deployment failure post-mortem processes exist?",
                "options": [
                    {"text": "No formal process", "level": 1, "score": 1,
                     "explanation": "Without post-mortems, teams miss learning opportunities."},
                    {"text": "Ad-hoc discussions", "level": 2, "score": 2,
                     "explanation": "Informal discussions help but lack structure and follow-through."},
                    {"text": "Documented in ServiceDesk", "level": 3, "score": 3,
                     "explanation": "Documentation improves knowledge sharing and future reference."},
                    {"text": "Blameless retrospectives", "level": 4, "score": 4,
                     "explanation": "Blameless culture encourages honest analysis and improvement."},
                    {"text": "Automated remediation playbooks", "level": 5, "score": 5,
                     "explanation": "Capturing remediation steps as code represents the highest maturity."}
                ],
                "required": True,
                "weight": 1.0
            }
        ]
    },
    {
        "section": "Security & Compliance",
        "questions": [
            {
                "id": "secrets_mgmt",
                "question": "How are secrets managed for telecom apps?",
                "options": [
                    {"text": "Hardcoded in Fuse configs", "level": 1, "score": 1,
                     "explanation": "Hardcoded secrets represent a significant security risk."},
                    {"text": "Kubernetes Secrets", "level": 2, "score": 2,
                     "explanation": "Basic K8s secrets improve security but have limitations."},
                    {"text": "Vault for Fuse only", "level": 3, "score": 3,
                     "explanation": "Using Vault is a good practice but should be expanded to all apps."},
                    {"text": "Vault + Dynamic secrets for all apps", "level": 4, "score": 4,
                     "explanation": "Dynamic secrets significantly reduce the risk of credential exposure."},
                    {"text": "SPIFFE identities", "level": 5, "score": 5,
                     "explanation": "Identity-based access removes the need for many traditional secrets."}
                ],
                "required": True,
                "weight": 1.5
            },
            {
                "id": "compliance_auditing",
                "question": "Is compliance auditing automated?",
                "options": [
                    {"text": "Manual checks", "level": 1, "score": 1,
                     "explanation": "Manual auditing is time-consuming and often inconsistent."},
                    {"text": "Static scans (Trivy)", "level": 2, "score": 2,
                     "explanation": "Static scanning is important but only one part of compliance."},
                    {"text": "OPA policies in ArgoCD", "level": 3, "score": 3,
                     "explanation": "Policy enforcement prevents non-compliant deployments."},
                    {"text": "Dynatrace compliance dashboards", "level": 4, "score": 4,
                     "explanation": "Dashboards provide continuous visibility into compliance status."},
                    {"text": "Real-time compliance enforcement", "level": 5, "score": 5,
                     "explanation": "Real-time enforcement ensures continuous compliance."}
                ],
                "required": True,
                "weight": 1.0
            }
        ]
    },
    {
        "section": "OpenShift Tekton Pipelines",
        "questions": [
            {
                "id": "tekton_structure",
                "question": "How are Tekton pipelines structured?",
                "options": [
                    {"text": "Single monolithic Task for all steps", "level": 1, "score": 1,
                     "explanation": "Monolithic tasks are difficult to maintain and reuse."},
                    {"text": "Modular Tasks but no reuse across apps", "level": 2, "score": 2,
                     "explanation": "Modular tasks improve maintainability but lack reusability."},
                    {"text": "Shared Tasks in a central repo", "level": 3, "score": 3,
                     "explanation": "Shared tasks improve consistency and reduce duplication."},
                    {"text": "Parameterized Pipelines for multi-app use", "level": 4, "score": 4,
                     "explanation": "Parameterized pipelines enable widespread standardization."},
                    {"text": "Self-service pipeline templates", "level": 5, "score": 5,
                     "explanation": "Self-service enables teams to adopt best practices easily."}
                ],
                "required": True,
                "weight": 1.0
            },
            {
                "id": "pipeline_triggers",
                "question": "How is pipeline execution triggered?",
                "options": [
                    {"text": "Manual tkn CLI runs", "level": 1, "score": 1,
                     "explanation": "Manual triggering reduces the benefits of automation."},
                    {"text": "Git webhooks (no approval gates)", "level": 2, "score": 2,
                     "explanation": "Automation is good but lacks important governance controls."},
                    {"text": "PR-based triggers with manual approval", "level": 3, "score": 3,
                     "explanation": "Balances automation with appropriate governance."},
                    {"text": "Automated promotion across envs", "level": 4, "score": 4,
                     "explanation": "Automated promotion improves delivery speed while maintaining control."},
                    {"text": "Event-driven triggers (e.g., Kafka messages)", "level": 5, "score": 5,
                     "explanation": "Event-driven architecture enables sophisticated automation."}
                ],
                "required": True,
                "weight": 1.0
            }
        ]
    },
    {
        "section": "Kubernetes/OpenShift Infrastructure",
        "questions": [
            {
                "id": "cluster_provisioning",
                "question": "How are OpenShift clusters provisioned?",
                "options": [
                    {"text": "Manual install (IPI)", "level": 1, "score": 1,
                     "explanation": "Manual provisioning is time-consuming and inconsistent."},
                    {"text": "Basic Terraform/Ansible", "level": 2, "score": 2,
                     "explanation": "Automation tools improve consistency but may lack full integration."},
                    {"text": "GitOps-managed clusters (ArgoCD + Cluster API)", "level": 3, "score": 3,
                     "explanation": "GitOps for clusters provides consistency and auditability."},
                    {"text": "Multi-cluster federation", "level": 4, "score": 4,
                     "explanation": "Federation improves scalability and resilience."},
                    {"text": "Self-service cluster provisioning", "level": 5, "score": 5,
                     "explanation": "Self-service balances control with autonomy for teams."}
                ],
                "required": True,
                "weight": 1.0
            },
            {
                "id": "workload_scaling",
                "question": "How is workload scaling handled?",
                "options": [
                    {"text": "Manual oc scale commands", "level": 1, "score": 1,
                     "explanation": "Manual scaling is reactive and labor-intensive."},
                    {"text": "Horizontal Pod Autoscaler (HPA)", "level": 2, "score": 2,
                     "explanation": "Basic HPA provides reactive scaling based on simple metrics."},
                    {"text": "KEDA with custom metrics", "level": 3, "score": 3,
                     "explanation": "KEDA enables more sophisticated scaling based on business metrics."},
                    {"text": "Predictive scaling (Dynatrace-driven)", "level": 4, "score": 4,
                     "explanation": "Predictive scaling anticipates needs before they occur."},
                    {"text": "AI-driven burst scaling", "level": 5, "score": 5,
                     "explanation": "AI optimization represents the highest level of scaling sophistication."}
                ],
                "required": True,
                "weight": 1.0
            },
            {
                "id": "service_mesh",
                "question": "Is Istio/Service Mesh implemented?",
                "options": [
                    {"text": "No service mesh", "level": 1, "score": 1,
                     "explanation": "Without a service mesh, you miss important security and observability features."},
                    {"text": "Basic OpenShift Service Mesh", "level": 2, "score": 2,
                     "explanation": "Basic implementation provides foundational capabilities."},
                    {"text": "Istio with mTLS for Fuse/Camel", "level": 3, "score": 3,
                     "explanation": "Adding mTLS significantly improves security posture."},
                    {"text": "Multi-cluster mesh", "level": 4, "score": 4,
                     "explanation": "Multi-cluster mesh enables sophisticated distributed architectures."},
                    {"text": "Automated traffic shifting", "level": 5, "score": 5,
                     "explanation": "Advanced traffic control enables sophisticated deployment strategies."}
                ],
                "required": True,
                "weight": 1.0
            }
        ]
    }
]

# Helper function to calculate section score
def calculate_section_score(answers, section_questions):
    """Calculate the score for a section based on answers."""
    total_score = 0
    total_weight = 0
    
    for question in section_questions:
        question_id = question["id"]
        if question_id in answers:
            answer_idx = int(answers[question_id])
            if 0 <= answer_idx < len(question["options"]):
                score = question["options"][answer_idx]["score"]
                weight = question["weight"]
                total_score += score * weight
                total_weight += weight
    
    return (total_score / total_weight) if total_weight > 0 else 0

# Calculate overall maturity level and percentage
def calculate_maturity(answers):
    """Calculate overall maturity level and percentage."""
    section_scores = {}
    total_score = 0
    total_possible = 0
    
    for section in QUESTIONS:
        section_name = section["section"]
        section_score = calculate_section_score(answers, section["questions"])
        section_scores[section_name] = section_score
        
        # Add to total (assuming max score per question is 5)
        section_weight = sum(q["weight"] for q in section["questions"] if q["id"] in answers)
        total_score += section_score * section_weight
        total_possible += 5 * section_weight  # 5 is max level
    
    # Calculate percentage and overall level
    percentage = (total_score / total_possible * 100) if total_possible > 0 else 0
    overall_level = round(total_score / total_possible * 5) if total_possible > 0 else 0
    
    return {
        "section_scores": section_scores,
        "percentage": percentage,
        "overall_level": overall_level
    }