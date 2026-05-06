# HSSE Advisor System

---

## ** Overview**

The **HSSE Advisor System** is a **Python-based automation tool** designed to streamline **Health, Safety, Security, and Environment (HSSE) oversight** for mining operations. Developed for use in **Liberia (Sept 2012 – April 2015)**, this system supports the implementation of **HSSE policies**, **contractor safety audits**, **fire safety equipment monitoring**, **emergency preparedness**, **toolbox safety meetings**, and **safety training programs**. It ensures compliance with safety regulations, mitigates risks, and protects workers, equipment, and environmental resources in major mining projects.

---

## **🛡️ Features**

### **HSSE Policy Management**

- **Policy Creation**: Add and manage **HSSE policies** with descriptions and compliance requirements.
- **Status Tracking**: Monitor policy statuses (e.g., Active, Under Review, Retired).
- **Compliance Requirements**: Define and track **mandatory compliance requirements** for each policy.

### **Contractor Safety Audits**

- **Contractor Management**: Add contractors and track their **services and compliance status**.
- **Audit Workflows**: Conduct **safety audits** for contractors, record findings, and update compliance statuses.
- **Audit History**: Maintain a log of all audits for **traceability and accountability**.

### **Fire Safety Equipment Monitoring**

- **Equipment Tracking**: Add and monitor **fire safety equipment** (e.g., extinguishers, smoke detectors).
- **Inspection Logging**: Record **inspection dates and statuses** (Operational, Non-Operational).
- **Location Management**: Track equipment by **location** for quick access during emergencies.

### **Emergency Preparedness**

- **Emergency Plans**: Create and manage **emergency preparedness plans** (e.g., fire evacuation, medical response).
- **Drill Scheduling**: Conduct and log **emergency drills** to ensure readiness.
- **Plan Status**: Track the **status and last drill date** for each emergency plan.

### **Toolbox Safety Meetings**

- **Meeting Scheduling**: Schedule **toolbox safety meetings** with topics, attendees, and notes.
- **Meeting Status**: Track meeting statuses (Scheduled, Conducted).
- **Documentation**: Store **notes and action items** from each meeting.

### **Safety Training Programs**

- **Program Creation**: Create **safety training programs** with titles, durations, and participant lists.
- **Completion Tracking**: Mark participants as **completed** and track completion rates.
- **Status Reporting**: Generate reports on **training completion status**.

### **Audit Logging**

- **Activity Tracking**: Automatically log all actions (e.g., policy updates, audits, drills) for **compliance and traceability**.
- **Comprehensive Logs**: Retrieve logs for **auditing and reporting purposes**.

### **Reporting & Analytics**

- **Compliance Reports**: Generate reports on **contractor compliance statuses** and audit histories.
- **Fire Safety Reports**: Overview of **fire safety equipment statuses** and inspection dates.
- **Training Reports**: Track **safety training program completion rates** and participant statuses.

---

## ** Installation**

### **Prerequisites**

- **Python 3.8+**
- **Dependencies**: None (uses Python’s built-in libraries)

### **Setup**

1. **Clone the repository**:
  ```bash
   git clone https://github.com/olumideadeniyiao-source/hsse-advisor/
   cd hsse-advisor
  ```
2. **Run the system**:
  ```bash
   python hsse_advisor_system.py
  ```

---

## **🛠️ Usage**

### **1. Initialize the System**

```python
hsse_system = HSSEAdvisorSystem()
```

### **2. HSSE Policy Management**

```python
# Add an HSSE policy
policy_id = hsse_system.add_hsse_policy(
    "Mining Safety Policy",
    "Ensures safety of workers and equipment in mining operations.",
    ["PPE Usage", "Equipment Inspection", "Emergency Procedures"]
)

# Update policy status
hsse_system.update_policy_status(policy_id, "Active")
```

### **3. Contractor Safety Audits**

```python
# Add a contractor
contractor_id = hsse_system.add_contractor("ABC Mining Contractors", ["Drilling", "Blasting"])

# Conduct a safety audit
findings = [
    {"issue": "Inadequate PPE", "severity": "High", "action": "Provide training"},
    {"issue": "Equipment Maintenance", "severity": "Medium", "action": "Schedule inspection"}
]
hsse_system.conduct_contractor_audit(contractor_id, findings, "Non-Compliant")

# Retrieve contractor compliance status
compliance_status = hsse_system.get_contractor_compliance(contractor_id)
```

### **4. Fire Safety Equipment Monitoring**

```python
# Add fire safety equipment
equipment_id_1 = hsse_system.add_fire_safety_equipment("Fire Extinguisher", "Main Workshop")
equipment_id_2 = hsse_system.add_fire_safety_equipment("Smoke Detector", "Control Room")

# Inspect equipment
hsse_system.inspect_fire_equipment(equipment_id_1, "Operational")

# Retrieve equipment status
equipment_status = hsse_system.get_fire_equipment_status(equipment_id_1)
```

### **5. Emergency Preparedness**

```python
# Add an emergency plan
plan_id = hsse_system.add_emergency_plan("Fire Evacuation Plan", "Fire")

# Conduct an emergency drill
hsse_system.conduct_emergency_drill(plan_id, "2026-05-10")

# Retrieve emergency plan details
emergency_plan = hsse_system.get_emergency_plan(plan_id)
```

### **6. Toolbox Safety Meetings**

```python
# Schedule a toolbox meeting
meeting_id = hsse_system.schedule_toolbox_meeting(
    "Electrical Safety",
    ["Alice", "Bob", "Charlie"],
    "Discussed PPE and lockout-tagout procedures"
)

# Conduct the meeting
hsse_system.conduct_toolbox_meeting(meeting_id)

# Retrieve meeting details
meeting_details = hsse_system.get_toolbox_meeting(meeting_id)
```

### **7. Safety Training Programs**

```python
# Create a safety training program
program_id = hsse_system.create_safety_training_program(
    "Mining Safety Training",
    "8 hours",
    ["Alice", "Bob", "Charlie", "David"]
)

# Mark participants as completed
hsse_system.mark_training_completion(program_id, "Alice")
hsse_system.mark_training_completion(program_id, "Bob")

# Retrieve training status
training_status = hsse_system.get_training_status(program_id)
```

### **8. Generate Reports**

```python
# Generate compliance report
compliance_report = hsse_system.generate_compliance_report()

# Generate fire safety report
fire_safety_report = hsse_system.generate_fire_safety_report()

# Generate training report
training_report = hsse_system.generate_training_report()
```

---

## ** Repository Structure**

```
.
├── hsse_advisor.py  # Main system code
├── README.md               # Project documentation
└── requirements.txt        # Dependencies (if any)
```

---

## ** Technical Details**

### **Architecture**

- **Class-Based Design**: The `HSSEAdvisorSystem` class encapsulates all functionalities.
- **Data Storage**: Uses **dictionaries and lists** for in-memory storage (suitable for small-to-medium datasets).
- **Unique Identifiers**: UUIDs ensure **collision-free IDs** for policies, contractors, equipment, and training programs.
- **Audit Logging**: Tracks all actions for **compliance and traceability**.

### **Extensibility**

Future enhancements could include:

- **Database Integration**: Use `sqlite3` or `PostgreSQL` for persistent storage.
- **Data Visualization**: Integrate `matplotlib` or `seaborn` for generating **safety trend charts**.
- **Web Interface**: Deploy with **Flask/Django** for a user-friendly dashboard.
- **Mobile App**: Extend to mobile for **field inspections and real-time reporting**.
- **API Integration**: Connect with **GIS systems** for site location mapping.

---

## ** Example Output**

Running the example usage in `__main__` produces:

```
=== HSSE Policy Management ===
HSSE Policy 'Mining Safety Policy' added with ID: POL1

=== Contractor Safety Audits ===
Contractor 'ABC Mining Contractors' added with ID: CON1
Audit conducted for contractor CON1 with ID: AUD1. Compliance Status: Non-Compliant

=== Fire Safety Equipment Monitoring ===
Fire Safety Equipment 'Fire Extinguisher' added with ID: FSE1
Fire Safety Equipment 'Smoke Detector' added with ID: FSE2
Fire Safety Equipment FSE1 inspected. Status: Operational

=== Emergency Preparedness ===
Emergency Plan 'Fire Evacuation Plan' added with ID: EP1
Emergency drill conducted for plan EP1 on 2026-05-10

=== Toolbox Safety Meetings ===
Toolbox Meeting on 'Electrical Safety' scheduled with ID: TB1
Toolbox Meeting TB1 marked as conducted.

=== Safety Training Programs ===
Safety Training Program 'Mining Safety Training' created with ID: ST1
Participant Alice marked as completed for program ST1
Participant Bob marked as completed for program ST1

=== Compliance Report ===
total_contractors: 1
compliant_contractors: 0
non_compliant_contractors: 1
pending_contractors: 0
contractor_details: [{'name': 'ABC Mining Contractors', 'compliance_status': 'Non-Compliant', 'audit_count': 1}]

=== Fire Safety Report ===
total_equipment: 2
operational: 1
non_operational: 0
equipment_details: [{'name': 'Fire Extinguisher', 'location': 'Main Workshop', 'status': 'Operational', ...}, ...]

=== Training Report ===
total_programs: 1
programs: [{'title': 'Mining Safety Training', 'duration': '8 hours', 'total_participants': 4, 'completed_participants': 2, 'completion_rate': 0.5}]
```

---

## ** Contributing**

Contributions are welcome! To contribute:

1. **Fork the repository** and create a feature branch.
2. **Add improvements**:
  - Database integration (e.g., SQLite).
  - Advanced analytics (e.g., predictive risk modeling).
  - API endpoints for external systems.
3. **Submit a pull request** with a clear description of changes.

---

## ** License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## ** Acknowledgments**

- Inspired by **HSSE standards** and **mining safety regulations** in Liberia.
- Designed to **protect workers, equipment, and environmental resources** in major mining projects.
- Built to support **contractor compliance, fire safety, emergency preparedness, and safety training** for operational excellence.
