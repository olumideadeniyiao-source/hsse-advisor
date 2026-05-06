import datetime
from typing import Dict, List, Optional, Tuple
import uuid

class HSSEAdvisorSystem:
    def __init__(self):
        # HSSE Policies: {policy_id: {"title": str, "description": str, "compliance_requirements": List[str], "status": str}}
        self.hsse_policies: Dict[str, Dict] = {}

        # Contractors: {contractor_id: {"name": str, "services": List[str], "compliance_status": str, "audit_history": List[Dict]}}
        self.contractors: Dict[str, Dict] = {}

        # Fire Safety Equipment: {equipment_id: {"name": str, "location": str, "last_inspection": str, "status": str}}
        self.fire_safety_equipment: Dict[str, Dict] = {}

        # Emergency Preparedness: {plan_id: {"name": str, "type": str, "last_drill": str, "status": str}}
        self.emergency_plans: Dict[str, Dict] = {}

        # Toolbox Meetings: {meeting_id: {"topic": str, "date": str, "attendees": List[str], "notes": str, "status": str}}
        self.toolbox_meetings: Dict[str, Dict] = {}

        # Safety Training Programs: {program_id: {"title": str, "duration": str, "participants": List[str], "completion_status": Dict}}
        self.safety_training: Dict[str, Dict] = {}

        # Audit Logs: List[Dict]
        self.audit_logs: List[Dict] = {}

    # --- HSSE Policy Management ---
    def add_hsse_policy(self, title: str, description: str, compliance_requirements: List[str]) -> str:
        """Add a new HSSE policy."""
        policy_id = f"POL{str(uuid.uuid4())[:6]}"
        self.hsse_policies[policy_id] = {
            "title": title,
            "description": description,
            "compliance_requirements": compliance_requirements,
            "status": "Active"
        }
        self._log_activity("policy_added", {"policy_id": policy_id, "title": title})
        return f"HSSE Policy '{title}' added with ID: {policy_id}"

    def update_policy_status(self, policy_id: str, status: str) -> str:
        """Update the status of an HSSE policy (e.g., Active, Under Review, Retired)."""
        if policy_id in self.hsse_policies:
            self.hsse_policies[policy_id]["status"] = status
            self._log_activity("policy_updated", {"policy_id": policy_id, "status": status})
            return f"Policy {policy_id} status updated to: {status}"
        return f"Policy ID {policy_id} not found."

    # --- Contractor Safety Audits ---
    def add_contractor(self, name: str, services: List[str]) -> str:
        """Add a new contractor to the system."""
        contractor_id = f"CON{str(uuid.uuid4())[:6]}"
        self.contractors[contractor_id] = {
            "name": name,
            "services": services,
            "compliance_status": "Pending",
            "audit_history": []
        }
        self._log_activity("contractor_added", {"contractor_id": contractor_id, "name": name})
        return f"Contractor '{name}' added with ID: {contractor_id}"

    def conduct_contractor_audit(self, contractor_id: str, findings: List[Dict], compliance_status: str) -> str:
        """Conduct a safety audit for a contractor."""
        if contractor_id in self.contractors:
            audit_id = f"AUD{str(uuid.uuid4())[:6]}"
            audit_entry = {
                "audit_id": audit_id,
                "date": datetime.datetime.now().strftime("%Y-%m-%d"),
                "findings": findings,
                "compliance_status": compliance_status
            }
            self.contractors[contractor_id]["audit_history"].append(audit_entry)
            self.contractors[contractor_id]["compliance_status"] = compliance_status
            self._log_activity("contractor_audit_conducted", {"contractor_id": contractor_id, "audit_id": audit_id, "status": compliance_status})
            return f"Audit conducted for contractor {contractor_id} with ID: {audit_id}. Compliance Status: {compliance_status}"
        return f"Contractor ID {contractor_id} not found."

    def get_contractor_compliance(self, contractor_id: str) -> Optional[Dict]:
        """Retrieve the compliance status and audit history of a contractor."""
        if contractor_id in self.contractors:
            return {
                "name": self.contractors[contractor_id]["name"],
                "compliance_status": self.contractors[contractor_id]["compliance_status"],
                "audit_history": self.contractors[contractor_id]["audit_history"]
            }
        return None

    # --- Fire Safety Equipment Monitoring ---
    def add_fire_safety_equipment(self, name: str, location: str) -> str:
        """Add a new piece of fire safety equipment."""
        equipment_id = f"FSE{str(uuid.uuid4())[:6]}"
        self.fire_safety_equipment[equipment_id] = {
            "name": name,
            "location": location,
            "last_inspection": datetime.datetime.now().strftime("%Y-%m-%d"),
            "status": "Operational"
        }
        self._log_activity("fire_equipment_added", {"equipment_id": equipment_id, "name": name})
        return f"Fire Safety Equipment '{name}' added with ID: {equipment_id}"

    def inspect_fire_equipment(self, equipment_id: str, status: str) -> str:
        """Inspect and update the status of fire safety equipment."""
        if equipment_id in self.fire_safety_equipment:
            self.fire_safety_equipment[equipment_id]["last_inspection"] = datetime.datetime.now().strftime("%Y-%m-%d")
            self.fire_safety_equipment[equipment_id]["status"] = status
            self._log_activity("fire_equipment_inspected", {"equipment_id": equipment_id, "status": status})
            return f"Fire Safety Equipment {equipment_id} inspected. Status: {status}"
        return f"Equipment ID {equipment_id} not found."

    def get_fire_equipment_status(self, equipment_id: str) -> Optional[Dict]:
        """Retrieve the status of a piece of fire safety equipment."""
        return self.fire_safety_equipment.get(equipment_id)

    # --- Emergency Preparedness ---
    def add_emergency_plan(self, name: str, plan_type: str) -> str:
        """Add a new emergency preparedness plan."""
        plan_id = f"EP{str(uuid.uuid4())[:6]}"
        self.emergency_plans[plan_id] = {
            "name": name,
            "type": plan_type,
            "last_drill": None,
            "status": "Active"
        }
        self._log_activity("emergency_plan_added", {"plan_id": plan_id, "name": name})
        return f"Emergency Plan '{name}' added with ID: {plan_id}"

    def conduct_emergency_drill(self, plan_id: str, drill_date: str) -> str:
        """Conduct an emergency drill and update the plan's last drill date."""
        if plan_id in self.emergency_plans:
            self.emergency_plans[plan_id]["last_drill"] = drill_date
            self._log_activity("emergency_drill_conducted", {"plan_id": plan_id, "drill_date": drill_date})
            return f"Emergency drill conducted for plan {plan_id} on {drill_date}"
        return f"Emergency Plan ID {plan_id} not found."

    def get_emergency_plan(self, plan_id: str) -> Optional[Dict]:
        """Retrieve an emergency preparedness plan by ID."""
        return self.emergency_plans.get(plan_id)

    # --- Toolbox Safety Meetings ---
    def schedule_toolbox_meeting(self, topic: str, attendees: List[str], notes: str) -> str:
        """Schedule a toolbox safety meeting."""
        meeting_id = f"TB{str(uuid.uuid4())[:6]}"
        self.toolbox_meetings[meeting_id] = {
            "topic": topic,
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "attendees": attendees,
            "notes": notes,
            "status": "Scheduled"
        }
        self._log_activity("toolbox_meeting_scheduled", {"meeting_id": meeting_id, "topic": topic})
        return f"Toolbox Meeting on '{topic}' scheduled with ID: {meeting_id}"

    def conduct_toolbox_meeting(self, meeting_id: str) -> str:
        """Mark a toolbox meeting as conducted."""
        if meeting_id in self.toolbox_meetings:
            self.toolbox_meetings[meeting_id]["status"] = "Conducted"
            self._log_activity("toolbox_meeting_conducted", {"meeting_id": meeting_id})
            return f"Toolbox Meeting {meeting_id} marked as conducted."
        return f"Toolbox Meeting ID {meeting_id} not found."

    def get_toolbox_meeting(self, meeting_id: str) -> Optional[Dict]:
        """Retrieve a toolbox meeting by ID."""
        return self.toolbox_meetings.get(meeting_id)

    # --- Safety Training Programs ---
    def create_safety_training_program(self, title: str, duration: str, participants: List[str]) -> str:
        """Create a new safety training program."""
        program_id = f"ST{str(uuid.uuid4())[:6]}"
        self.safety_training[program_id] = {
            "title": title,
            "duration": duration,
            "participants": participants,
            "completion_status": {participant: False for participant in participants}
        }
        self._log_activity("safety_training_created", {"program_id": program_id, "title": title})
        return f"Safety Training Program '{title}' created with ID: {program_id}"

    def mark_training_completion(self, program_id: str, participant: str) -> str:
        """Mark a participant as having completed a safety training program."""
        if program_id in self.safety_training and participant in self.safety_training[program_id]["participants"]:
            self.safety_training[program_id]["completion_status"][participant] = True
            self._log_activity("training_completed", {"program_id": program_id, "participant": participant})
            return f"Participant {participant} marked as completed for program {program_id}"
        return f"Program ID {program_id} or participant {participant} not found."

    def get_training_status(self, program_id: str) -> Optional[Dict]:
        """Retrieve the status of a safety training program."""
        return self.safety_training.get(program_id)

    # --- Audit Logging ---
    def _log_activity(self, action: str, details: Dict) -> None:
        """Log an activity to the audit trail."""
        log_entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "details": details
        }
        self.audit_logs.append(log_entry)

    def get_audit_logs(self) -> List[Dict]:
        """Retrieve all audit logs."""
        return self.audit_logs

    # --- Reporting ---
    def generate_compliance_report(self) -> Dict:
        """Generate a compliance report for all contractors."""
        report = {
            "total_contractors": len(self.contractors),
            "compliant_contractors": sum(1 for contractor in self.contractors.values() if contractor["compliance_status"] == "Compliant"),
            "non_compliant_contractors": sum(1 for contractor in self.contractors.values() if contractor["compliance_status"] == "Non-Compliant"),
            "pending_contractors": sum(1 for contractor in self.contractors.values() if contractor["compliance_status"] == "Pending"),
            "contractor_details": [
                {
                    "name": contractor["name"],
                    "compliance_status": contractor["compliance_status"],
                    "audit_count": len(contractor["audit_history"])
                }
                for contractor in self.contractors.values()
            ]
        }
        return report

    def generate_fire_safety_report(self) -> Dict:
        """Generate a report on the status of all fire safety equipment."""
        report = {
            "total_equipment": len(self.fire_safety_equipment),
            "operational": sum(1 for eq in self.fire_safety_equipment.values() if eq["status"] == "Operational"),
            "non_operational": sum(1 for eq in self.fire_safety_equipment.values() if eq["status"] != "Operational"),
            "equipment_details": [
                {
                    "name": eq["name"],
                    "location": eq["location"],
                    "status": eq["status"],
                    "last_inspection": eq["last_inspection"]
                }
                for eq in self.fire_safety_equipment.values()
            ]
        }
        return report

    def generate_training_report(self) -> Dict:
        """Generate a report on safety training programs and completion status."""
        report = {
            "total_programs": len(self.safety_training),
            "programs": [
                {
                    "title": program["title"],
                    "duration": program["duration"],
                    "total_participants": len(program["participants"]),
                    "completed_participants": sum(program["completion_status"].values()),
                    "completion_rate": sum(program["completion_status"].values()) / len(program["participants"]) if program["participants"] else 0
                }
                for program in self.safety_training.values()
            ]
        }
        return report

# --- Example Usage ---
if __name__ == "__main__":
    hsse_system = HSSEAdvisorSystem()

    # Add HSSE policies
    print("=== HSSE Policy Management ===")
    print(hsse_system.add_hsse_policy(
        "Mining Safety Policy",
        "Ensures safety of workers and equipment in mining operations.",
        ["PPE Usage", "Equipment Inspection", "Emergency Procedures"]
    ))

    # Add contractors and conduct audits
    print("\n=== Contractor Safety Audits ===")
    print(hsse_system.add_contractor("ABC Mining Contractors", ["Drilling", "Blasting"]))
    findings = [
        {"issue": "Inadequate PPE", "severity": "High", "action": "Provide training"},
        {"issue": "Equipment Maintenance", "severity": "Medium", "action": "Schedule inspection"}
    ]
    print(hsse_system.conduct_contractor_audit("CON1", findings, "Non-Compliant"))

    # Add and inspect fire safety equipment
    print("\n=== Fire Safety Equipment Monitoring ===")
    print(hsse_system.add_fire_safety_equipment("Fire Extinguisher", "Main Workshop"))
    print(hsse_system.add_fire_safety_equipment("Smoke Detector", "Control Room"))
    print(hsse_system.inspect_fire_equipment("FSE1", "Operational"))

    # Add emergency preparedness plans and conduct drills
    print("\n=== Emergency Preparedness ===")
    print(hsse_system.add_emergency_plan("Fire Evacuation Plan", "Fire"))
    print(hsse_system.conduct_emergency_drill("EP1", "2026-05-10"))

    # Schedule and conduct toolbox meetings
    print("\n=== Toolbox Safety Meetings ===")
    print(hsse_system.schedule_toolbox_meeting(
        "Electrical Safety",
        ["Alice", "Bob", "Charlie"],
        "Discussed PPE and lockout-tagout procedures"
    ))
    print(hsse_system.conduct_toolbox_meeting("TB1"))

    # Create and manage safety training programs
    print("\n=== Safety Training Programs ===")
    print(hsse_system.create_safety_training_program(
        "Mining Safety Training",
        "8 hours",
        ["Alice", "Bob", "Charlie", "David"]
    ))
    print(hsse_system.mark_training_completion("ST1", "Alice"))
    print(hsse_system.mark_training_completion("ST1", "Bob"))

    # Generate reports
    print("\n=== Compliance Report ===")
    compliance_report = hsse_system.generate_compliance_report()
    for key, value in compliance_report.items():
        print(f"{key}: {value}")

    print("\n=== Fire Safety Report ===")
    fire_safety_report = hsse_system.generate_fire_safety_report()
    for key, value in fire_safety_report.items():
        print(f"{key}: {value}")

    print("\n=== Training Report ===")
    training_report = hsse_system.generate_training_report()
    for key, value in training_report.items():
        print(f"{key}: {value}")
