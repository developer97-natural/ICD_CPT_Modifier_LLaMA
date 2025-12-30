import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
MODEL = "meta-llama/Llama-3.3-70B-Instruct"
HF_TOKEN = os.getenv("HF_TOKEN")

def call_llama_api(prompt):
    API_URL = "https://router.huggingface.co/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code != 200:
            raise Exception(f"API error: {response.status_code} {response.text}")
        return response.json()

    # Deterministic parameters added
    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct",
        "messages": [
            {
                "role": "user", 
                "content": prompt,
            }
        ]
    }

    response = query(payload)

    # Extract model reply
    message = response["choices"][0]["message"]["content"]
    return message

def parse_llm_output(llm_text):
    try:
        # Extract JSON object from text
        start = llm_text.find("{")
        end = llm_text.rfind("}") + 1
        data = json.loads(llm_text[start:end])
        return data
    except Exception as e:
        print("Failed to parse LLM output:", e)
        return {"final_cpt": [], "modifiers": [], "rationale": ""}


def Main_Pipeline(input_text):
    result = call_llama_api(
        f'''{input_text} 

        

From the above clinical note, extract the ICD-10 codes, CPT codes, and possible modifier codes. 
Then give me the final output in JSON format as below:

{{
"ICD10_Codes": Ranked list of ICD-10 codes extracted with description, rationale and confidence score,
"CPT_Codes": Ranked list of CPT codes extracted with description, rationale and confidence score, 
"Modifier_Codes": Ranked list of possible modifier codes with description, rationale and confidence score,
}}.'''
    )


    parsed_data = parse_llm_output(result)
    return parsed_data

if __name__ == "__main__":
    input_text = "Blue Lotus Medical Group\n1\nPatient Name: Carolyn Almond\nDOB: 08/30/1936\nMRN: 67\nPrimary Insurance: TEXAS MEDICARE\nElectronically Signed by: JOHN PREDDY, MD\n10/21/2025\nAssessment Date: 10/21/2025 08:00:00\nSKIN GRAFT APPLICATION\nWOUND COUNT\nDIAGNOSIS\nL97.228 Non-pressure chronic ulcer of left calf with other specified severity\nL97.901Non-pressure chronic ulcer of unspecified part of unspecified lower leg limited to breakdown\nof skin\nI87.332 CHRONIC VENOUS HTN W ULCER AND INFLAMMATION OF L LOW EXTREM\nTREATMENT INTERVENTION\nMs. Almond is lying comfortably in bed with legs elevated. Old dressings removed. Wound care supplies are\nat the bedside. Wound cleaned with anasept-soaked gauze/trigger sprayer, removed debris from wound\nbed, cleansed a second time with anasept-soaked gauze/trigger sprayer, and allowed to dry.\nPerformed Mechanical debridement with debri-soft duo after appropriately numbing site.\nNext, applied allograft and maintained manufacturer's instructions for application\nReinforced with non-adherent Adaptic and super absorbent Zevitt pad.\nWrapped extremity with conforming gauze. Compression applied with Ace Wrap and secured with Tubi-grip\nGRAFTS ARE LISTED BELOW AND WERE SHARED AMONG WOUND. Due to size of wound grafts were applied\non consecutive days\n10/21/2025\nSIZE:4x8\nLOT #:516667-006\nEXP DATE:10/06/2026\n2\nCarolyn Almond - DOB: 08/30/1936\nSIZE:4x8\nLOT #:C25-2501-003\nEXP DATE:09/17/2028\nSIZE:4x8\nLOT #:506754-006\nEXP DATE09/11/2026\nSIZE:4x8\nLOT #:C25-2300-002\nEXP DATE:09/12/2028\nSIZE:4x8\nLOT #:506754-007\nEXP DATE:09/11/2026\nSIZE:4x8\nLOT #:516827-004\nEXP DATE:10/06/2026\nSIZE:4x6\nLOT #:C25-2270-005\nEXP DATE:09/10/2028\nSIZE:4x6\nLOT #:C25-2270-006\nEXP DATE:09/10/2028\nSIZE:4x6\nLOT #:C25-2264-004\nEXP DATE:09/11/2028\nSIZE:4x4\nLOT #:507532-002\nEXP DATE:09/11/2026\n3\nCarolyn Almond - DOB: 08/30/1936\nSIZE:2x3\nLOT #:500546-004\nEXP DATE:09/02/2026\nSIZE:2x3\nLOT #:508319-002\nEXP DATE:09/19/2026\nSIZE:2x3\nLOT #:497856-001\nEXP DATE:09/07/2026\nSIZE:2x2\nLOT #:C25-2332-010\nEXP DATE:09/12/2028\nSIZE:2x2\nLOT #:C25-2395-012\nEXP DATE:09/15/2028\nSIZE:2x2\nLOT #:C25-2416-017\nEXP DATE:09/14/2028\n10/22/2025\nSIZE:4x8\nLOT #:C25-2653-004\nEXP DATE:09/24/2028\nSIZE:4x8\nLOT #:C25-2642-001\nEXP DATE:09/23/2028\nSIZE:4x8\nLOT #:C25-2280-006\nEXP DATE:09/11/2028\n4\nCarolyn Almond - DOB: 08/30/1936\nSIZE:4x8\nLOT #:C25-2503-002\nEXP DATE:09/17/2028\nSIZE:4x8\nLOT #:C25-2513-001\nEXP DATE:09/17/2028\nSIZE:4x8\nLOT #:C24-2678-003\nEXP DATE:10/15/2027\nSIZE:4x8\nLOT #:C25-2352-002\nEXP DATE:09/13/2028\nSIZE:4x8\nLOT #:C25-2656-006\nEXP DATE:09/24/2028\nSIZE:4x8\nLOT #:C25-2655-001\nEXP DATE:09/24/2028\nSIZE:4x8\nLOT #:CV25-2503-003\nEXP DATE:09/17/2028\nSIZE:4x8\nLOT #:C25-2656-005\nEXP DATE:09/24/2028\nSIZE:4X8\nLOT #:C25-2641-002\nEXP DATE:09/23/2028\n5\nCarolyn Almond - DOB: 08/30/1936\nSIZE:4x6\nLOT #:C25-2272-004\nEXP DATE:09/11/2028\nSIZE:4x6\nLOT #:C25-2265-004\nEXP DATE:09/11/2028\nSIZE:4X4\nLOT #:489418-004\nEXP DATE:07/01/2026\nSIZE:4X4\nLOT #:489457-004\nEXP DATE:07/01/2026\nSIZE:2X3\nLOT #:505812-004\nEXP DATE:09/10/2026\nSIZE:2X2\nLOT #:C25-2414-012\nEXP DATE:09/14/2026\nTOTAL GRAFT USEAGE was 783.5\nWOUND 1 ASSESSMENT\nWound Type: ulcer- venous\nWound Site: left, posterior calf, heel and lower Achilles tendon area below previous graphs\nStage: None\nWound Duration: 8/15/2024\nMEASUREMENTS\nLength: 11.8 cm\nWidth: 3.8 cm\nDepth: 0.1 cm\nTotal Surface Area: 44.8\nExudate Type: serous\nExudate Amount: Moderate\nWound Bed: red tissue granulation\n6\nCarolyn Almond - DOB: 08/30/1936\nWound Edges: attached\nPeripheral Skin Appearance: macerated\nSigns and Symptoms of Infection Present: No\nPREPARATION: Wound Debrided\nType of Debridement Performed: Mechanical\nType of Instrument Used: Debri-Soft Duo\nDepth of Debridement:  Skin\nPost Debridement Wound Measurements:\nLength: 11.8 cm\nWidth: 3.8 cm\nDepth: 0.1 cm\nTotal Surface Area: 44.8\nPost Debridement Wound Details:\nWound Bed: red tissue granulation\nExudate Type: serous\nExudate Amount: Moderate\nPeripheral Skin Appearance: clear\nTREATMENT\nDressing: Urgo Clean, Superabsorbent\nCleanser: dermal cleanser spray\nWOUND 2 ASSESSMENT\nWound Type: ulcer- venous\nWound Site: left medial ankle/top left foot\nStage: None\nWound Duration: 8/4/2025\nMEASUREMENTS\nLength: 28.7 cm\nWidth: 27.3 cm\nDepth: 0.2 cm\nTotal Surface Area: 783.5\nExudate Type: serous\nExudate Amount: Moderate\nWound Bed: red tissue granulation\nWound Edges: attached\nPeripheral Skin Appearance: clear\nPREPARATION: Wound Debrided\nType of Debridement Performed: Mechanical\nType of Instrument Used: Debrisoft Duo\nDepth of Debridement: Subcutaneous Tissue\n7\nCarolyn Almond - DOB: 08/30/1936\nPost Debridement Wound Measurements:\nLength: 28.7 cm\nWidth: 27.3 cm\nDepth: 0.2 cm\nTotal Surface Area: 783.5\nPost Debridement Wound Details:\nWound Bed: red tissue granulation\nExudate Type: fresh blood\nExudate Amount: Moderate\nPeripheral Skin Appearance: clear\nAmount of Biologic Applied: 99.5 % of biologic applied to ulcer\nAmount of Product Discarded: 0.5 cm of biologic wasted or discarded\nReason for Wastage: No biologic discarded or wasted\nORDERS\nOrder Communication/Plan of Care: Leave graft in Place for 5-7days, DO Not remove until 10/27/2025.\nBandage checks can be completed, do not distrub graft\nWOUND #1\n1. Cleanse wound with anasept-soaked gauze/trigger sprayer, remove debris from wound\nbed, then cleanse site a second time with anasept-soaked gauze/trigger sprayer and allow to dry.\n2. Cleanse once again with debrisoft lolly using moderate pressure (if available) saturated in anasept.\n3. Apply URGOCleanAG directly to wound bed sticky side\nChange dressing 4x/week and as needed for saturation/soilage\nMist Therapy Treatment Plan\nWound(s) Covered by this Plan:\n___________________________________\nChronic, non-healing wound [ ] Venous\nMedical Necessity Reason For Mist Therapy (select all that apply):\n[\n[ ] Documented evidence of no signs of improvement after 30 days of standard wound care.\nDelegated Procedure:\nAuthorized: Non-contact LF ultrasound therapy using Qoustic Wound Therapy System (Arobella AR1000)\n- Saline mist delivery 12 cm hover above wound bed\n- Mesh or spiral pattern to entire wound/periwound\n- Duration per wound as per manufacturer guidance\nDelegated To: Trinity Nurse under this plan of care\nSupervision: Indirect; NP review progress at least every 30 days\nFrequency & Course:\nFrequency: 2___x per week (typically 23)\n8\nCarolyn Almond - DOB: 08/30/1936\nDuration: Up to _6 weeks (=18 sessions in 6 weeks unless improvement documented)\nReassessment: After 46 sessions, wound healing trajectory must be documented\nProvider Oversight:\nNP reviews RN documentation at least every 30 days.\nAdjust/discontinue therapy if no measurable improvement after 6 treatments or adverse events occur.\nDiscontinue upon wound closure, transition to other advanced therapy, or per provider judgment.\nProvide wound care as ordered, prevent infection, and heal wounds.\nTrinity MWC to see pt 3x/wk-NP every Monday.\nHH will see on T/TH\nMay change due to unforeseen circumstances as needed.\nDO NOT REMOVE COMPRESSION OR GRAFT UNTIL 10/27/2025 CAN DO BANDAGE CHECKS ONLY\nSigned By: Andrea Neve 10/27/2025 02:38 PM"
    
    result = call_llama_api(
        f'''{input_text} 

        

From the above clinical note, extract the ICD-10 codes, CPT codes, and possible modifier codes. 
Then give me the final output in JSON format as below:

{{
"ICD10_Codes": Ranked list of ICD-10 codes extracted with description, rationale and confidence score,
"CPT_Codes": Ranked list of CPT codes extracted with description, rationale and confidence score, 
"Modifier_Codes": Ranked list of possible modifier codes with description, rationale and confidence score,
}}.'''
    )

    print("LLM Output:")
    print(result)


