# Human Review Required

AI review cannot certify local policy, device behavior, exact anatomy, legal requirements or specialty-level contested recommendations. The items below remain explicit blockers to a 4/5 or 5/5 final score.

| Topic | Statement or asset requiring review | Reason | Evidence / source status | Suggested reviewer specialty |
|---|---|---|---|---|
| All clinical pages | Claim-to-reference support and recommendation strength | URL presence does not establish that a source supports the exact claim | `REFERENCE_AUDIT.md`; re-verification pending | Evidence methodologist + relevant specialist |
| Mechanical ventilation | PEEP, plateau pressure, driving pressure, compliance, resistance and waveform interpretation | Thresholds and causal wording can be overgeneralized; ventilator behavior varies | ATS/AARC and primary studies must be mapped | Intensivist + respiratory therapist |
| Ventilator waveforms | All pressure/flow/volume/asynchrony SVGs | Mathematical shape, timing and labels require physiology validation | Programmatic assets; evidence match score 2 | Respiratory physiologist |
| Hemodynamics | MAP, perfusion, PLR, Frank–Starling and pressure/flow diagrams | Measurement validity and phenotype/context determine interpretation | ESICM 2025 official guidance identified | Cardiovascular intensivist + POCUS expert |
| ECMO | VV/VA circuits, drainage/return, recirculation, differential hypoxemia and emergencies | Configuration and direction errors are high-consequence | ELSO guidance re-verification pending | ECMO specialist + perfusionist/clinical engineer |
| CRRT | Circuit paths, diffusion/convection, dose, anticoagulation and alarms | Device configuration and prescription are high-consequence | KDIGO 2012 final; 2026 document is public-review draft | Nephrologist + CRRT nurse/engineer + pharmacist |
| Neurocritical care | ICP/CPP, Monro–Kellie, herniation, stroke, SAH and prognostication | Disease-specific thresholds, timing and confounding require specialist interpretation | NCS/BTF/AHA-ASA and Japanese guideline status to verify | Neurointensivist + neurosurgeon |
| Cardiac arrest / PCAS | Oxygen/ventilation, temperature, coronary strategy, seizure and prognostication claims | 2025 AHA changed/updated several recommendations; class/LOE must be exact | AHA 2025 official source confirmed | Emergency physician + cardiac/neurointensivist |
| Sepsis | Antibiotic timing, fluids, vasopressors, steroids, source control and de-escalation | SSC 2026 and J-SSCG2024 differ in scope/context; claim mapping absent | Both official sources identified | Intensivist + infectious disease + pharmacist |
| Pharmacology | Drug mechanisms, interactions, dose adjustment and extracorporeal support | Patient/device-specific PK/PD cannot be certified generically | Primary monographs/guidelines not yet mapped | ICU pharmacist |
| Obstetric critical care | Maternal arrest, hemorrhage, hypertensive emergency, imaging and medications | Maternal/fetal and legal/local pathways vary | Current specialty guidance not yet fully audited | Maternal–fetal medicine + obstetric anesthesiologist |
| Pediatrics | Weight-based dosing, device sizing and age-specific thresholds | Adult simplification is unsafe | Pediatric primary guidelines not fully audited | Pediatric intensivist |
| Transfusion | Component selection, reaction response and massive transfusion | Blood service policy and product availability vary | AABB/Japanese blood service verification required | Transfusion medicine specialist |
| Procedures | Sterile technique, imaging, contraindications and complication response | Credentialing and local procedure policy are essential | Local policy not represented | Procedural specialist + infection prevention |
| Ethics/end of life | Capacity, surrogate, DNAR, withdrawal and donation | Jurisdiction, law and institutional policy cannot be generalized | Legal/local policy review required | Clinical ethicist + legal counsel + palliative care |
| Infection control | Isolation, device bundles, outbreak and occupational exposure | Local epidemiology and policy can supersede generic text | CDC/Japanese guidance and local IPC policy | Infection prevention specialist |
| AI raster anatomy (7 files) | Airway, cardiopulmonary, endocrine, hemostasis, hepatobiliary, intracranial and renal images | Generated anatomy lacks traceable source layers and independent anatomic sign-off | `VISUAL_AUDIT.md`: REDRAW | Medical illustrator + relevant anatomist/specialist |
| Artificial ventilation overview (ILL-VENT-002) | Ventilator, two-limb circuit, patient connection, endotracheal tube, trachea and lungs | AI-assisted illustration improved after one rejected draft and a targeted correction, but it is not a device connection guide and still lacks independent sign-off | `VISUAL_AUDIT.md`: REVISE / HUMAN REVIEW REQUIRED | Respiratory therapist + clinical engineer + airway specialist + medical illustrator |

## Sign-off record requirements

Record reviewer name, role/specialty, date, version/commit, reviewed claims/figures, unresolved dissent and required changes. “Looks correct” without scope is not sufficient.
