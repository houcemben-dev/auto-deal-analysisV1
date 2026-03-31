import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd

st.set_page_config(
    page_title="Auto Deal Analysis",
    page_icon="🚘",
    layout="wide"
)

# =============================
# STYLE ULTRA PREMIUM
# =============================
st.markdown("""
<style>
:root {
    --bg: #08111f;
    --card: rgba(18, 26, 43, 0.72);
    --card-strong: rgba(16, 24, 40, 0.9);
    --stroke: rgba(255,255,255,0.08);
    --text: #f8fafc;
    --muted: #b6c2d1;
    --green: #34d399;
    --green-soft: rgba(52, 211, 153, 0.12);
    --blue-soft: rgba(96, 165, 250, 0.12);
    --shadow: 0 20px 50px rgba(0,0,0,0.28);
}

.block-container {
    padding-top: 1.6rem;
    padding-bottom: 2.2rem;
    max-width: 1320px;
}

html, body, [data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at top left, rgba(52, 211, 153, 0.08), transparent 25%),
        radial-gradient(circle at top right, rgba(59, 130, 246, 0.10), transparent 30%),
        linear-gradient(180deg, #07101d 0%, #08111f 100%);
}

[data-testid="stHeader"] {
    background: transparent;
}

.hero {
    position: relative;
    overflow: hidden;
    background:
        linear-gradient(135deg, rgba(10,17,30,0.95), rgba(17,24,39,0.92) 55%, rgba(10,17,30,0.98)),
        radial-gradient(circle at top right, rgba(52,211,153,0.12), transparent 30%);
    border: 1px solid var(--stroke);
    border-radius: 30px;
    padding: 42px 42px 36px 42px;
    box-shadow: var(--shadow);
    margin-bottom: 24px;
}

.hero::after {
    content: "";
    position: absolute;
    right: -120px;
    top: -120px;
    width: 320px;
    height: 320px;
    background: radial-gradient(circle, rgba(52,211,153,0.16), transparent 65%);
    pointer-events: none;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 9px 14px;
    border-radius: 999px;
    background: var(--green-soft);
    color: #67f0bf;
    font-size: 0.92rem;
    font-weight: 700;
    margin-bottom: 16px;
}

.hero-title {
    font-size: 3.5rem;
    line-height: 1;
    font-weight: 850;
    letter-spacing: -0.04em;
    color: white;
    margin-bottom: 14px;
    max-width: 760px;
}

.hero-subtitle {
    color: var(--muted);
    font-size: 1.13rem;
    line-height: 1.8;
    max-width: 760px;
}

.hero-grid {
    display: grid;
    grid-template-columns: 1.35fr 0.85fr;
    gap: 26px;
    align-items: start;
}

.hero-side {
    display: flex;
    flex-direction: column;
    gap: 14px;
}

.glass-mini {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 22px;
    padding: 18px;
    backdrop-filter: blur(8px);
}

.glass-mini-title {
    color: white;
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 8px;
}

.glass-mini-text {
    color: var(--muted);
    line-height: 1.6;
    font-size: 0.97rem;
}

.section-card {
    background: var(--card);
    border: 1px solid var(--stroke);
    border-radius: 26px;
    padding: 26px;
    box-shadow: var(--shadow);
    backdrop-filter: blur(8px);
    margin-bottom: 18px;
}

.section-title {
    color: white;
    font-size: 1.26rem;
    font-weight: 800;
    margin-bottom: 10px;
}

.section-text {
    color: var(--muted);
    line-height: 1.75;
    font-size: 1rem;
}

.metric-card {
    background: linear-gradient(180deg, rgba(20,29,48,0.92), rgba(15,23,38,0.92));
    border: 1px solid var(--stroke);
    border-radius: 24px;
    padding: 20px;
    text-align: center;
    box-shadow: var(--shadow);
    min-height: 112px;
}

.metric-label {
    color: #95a4b8;
    font-size: 0.92rem;
    margin-bottom: 8px;
}

.metric-number {
    color: white;
    font-size: 1.65rem;
    font-weight: 850;
    line-height: 1.1;
}

.highlight-card {
    background: linear-gradient(135deg, rgba(52,211,153,0.08), rgba(59,130,246,0.06));
    border: 1px solid rgba(52,211,153,0.14);
    border-radius: 24px;
    padding: 22px;
    margin-bottom: 16px;
}

.highlight-title {
    color: white;
    font-size: 1.08rem;
    font-weight: 800;
    margin-bottom: 6px;
}

.highlight-text {
    color: var(--muted);
    line-height: 1.65;
}

.result-box {
    background: linear-gradient(180deg, rgba(16,24,40,0.98), rgba(13,20,34,0.96));
    border: 1px solid var(--stroke);
    border-radius: 28px;
    padding: 30px;
    box-shadow: var(--shadow);
    margin-top: 8px;
}

.result-title {
    color: white;
    font-size: 1.55rem;
    font-weight: 850;
    margin-bottom: 16px;
}

.subtle-note {
    color: #8da0b7;
    font-size: 0.92rem;
    margin-top: 8px;
}

.small-stat {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 20px;
    padding: 16px 18px;
    height: 100%;
}

.small-stat-title {
    color: #d8e1eb;
    font-size: 1rem;
    font-weight: 800;
    margin-bottom: 6px;
}

.small-stat-text {
    color: var(--muted);
    font-size: 0.96rem;
    line-height: 1.6;
}

.lang-wrap {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 10px;
}

[data-testid="stSelectbox"] label {
    font-weight: 700 !important;
}

[data-testid="stNumberInput"] label {
    font-weight: 700 !important;
}

.stButton > button {
    border-radius: 16px !important;
    height: 3.1rem !important;
    font-weight: 750 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

.stButton > button[kind="primary"] {
    box-shadow: 0 10px 25px rgba(52, 211, 153, 0.16);
}

hr {
    border-color: rgba(255,255,255,0.08) !important;
}
</style>
""", unsafe_allow_html=True)

# =============================
# SESSION
# =============================
if "compteur" not in st.session_state:
    st.session_state.compteur = 0

if "lang" not in st.session_state:
    st.session_state.lang = "fr"

if "is_premium" not in st.session_state:
    st.session_state.is_premium = False

if "comparaison" not in st.session_state:
    st.session_state.comparaison = []
# =============================
# CHARGEMENT EXCEL
# =============================
@st.cache_data
def charger_donnees_excel():
    df = pd.read_excel("auto_deal.xlsx", sheet_name="Prix_Indicatifs")

    # Nettoyage des noms de colonnes
    df.columns = df.columns.str.strip()

    # Nettoyage des données
    df["Marque"] = df["Marque"].astype(str).str.strip()
    df["Modele"] = df["Modele"].astype(str).str.strip()
    df["Année"] = df["Année"].astype(int)
    df["Prix_indicatif_eur"] = (
        df["Prix_indicatif_eur"]
        .astype(str)
        .str.replace("€", "", regex=False)
        .str.replace(" ", "", regex=False)
        .str.replace(",", ".", regex=False)
    )
    df["Prix_indicatif_eur"] = pd.to_numeric(df["Prix_indicatif_eur"], errors="coerce")

    # On enlève les lignes invalides
    df = df.dropna(subset=["Marque", "Modele", "Année", "Prix_indicatif_eur"])

    # Conversion finale
    df["Année"] = df["Année"].astype(int)
    df["Prix_indicatif_eur"] = df["Prix_indicatif_eur"].astype(int)

    return df

df_prix = charger_donnees_excel()


def recuperer_prix_reference(marque, modele, annee):
    resultat = df_prix[
        (df_prix["Marque"] == marque) &
        (df_prix["Modele"] == modele) &
        (df_prix["Année"] == int(annee))
    ]

    if not resultat.empty:
        return int(resultat.iloc[0]["Prix_indicatif_eur"])

    return None
# =============================
# I18N
# =============================
I18N = {
    "fr": {
        "lang_label": "Langue",
        "hero_badge": "Analyse intelligente de véhicules d'occasion",
        "hero_title": "Achetez votre voiture au bon prix.",
        "hero_title_2": "En quelques secondes.",
        "hero_subtitle": "Auto Deal Analysis vous aide à détecter les bonnes affaires en analysant le prix du véhicule, son kilométrage, son âge et les réparations à prévoir.",
        "hero_card_1_title": "Décision rapide",
        "hero_card_1_text": "Obtenez un verdict clair sans perdre du temps à tout comparer manuellement.",
        "hero_card_2_title": "Vision plus complète",
        "hero_card_2_text": "Le score prend en compte le prix, l'âge, le kilométrage et le coût réel des réparations.",
        "plan_free": "Plan gratuit",
        "remaining": "Analyses restantes",
        "premium": "Version premium bientôt disponible",
        "reset": "Réinitialiser",
        "vehicle_info": "Informations du véhicule",
        "brand": "Marque",
        "model": "Modele",
        "year": "Année",
        "mileage": "Kilométrage",
        "listed_price": "Prix affiché (€)",
        "ref_price": "Prix moyen de référence",
        "no_ref_price": "Aucun prix de référence défini pour ce véhicule.",
        "repairs": "Réparations à prévoir",
        "other_repairs": "Autres réparations estimées (€)",
        "analyze": "Lancer l’analyse 🚀",
        "benefits_title": "Pourquoi utiliser Auto Deal Analysis ?",
        "benefits_text": "Évitez les mauvaises affaires, gagnez du temps et prenez une décision d’achat plus sereine grâce à une analyse structurée.",
        "benefit_1_title": "Évitez les pièges",
        "benefit_1_text": "Repérez rapidement les véhicules surévalués ou trop coûteux à remettre en état.",
        "benefit_2_title": "Gagnez du temps",
        "benefit_2_text": "Plus besoin de comparer manuellement tous les critères à chaque annonce.",
        "benefit_3_title": "Décidez plus vite",
        "benefit_3_text": "Un verdict lisible et un score clair pour savoir où concentrer votre attention.",
        "premium_roadmap": "Ce qui arrive ensuite",
        "premium_roadmap_text": "• Comparaison multi-véhicules\n• Analyses illimitées\n• Intégration Excel\n• Historique et rapports",
        "result": "Résultat de l’analyse",
        "listed_price_metric": "Prix affiché",
        "ref_price_metric": "Prix référence",
        "repairs_metric": "Réparations",
        "gap_metric": "Écart final",
        "breakdown": "Détail du calcul",
        "vehicle": "Véhicule",
        "base_corrected": "Valeur corrigée brute",
        "global_adjustment": "Ajustement global",
        "adjusted_final": "Valeur ajustée finale",
        "why": "Pourquoi ce verdict ?",
        "selected_repairs": "Réparations sélectionnées",
        "none": "Aucune",
        "other_repairs_line": "Autres réparations",
        "disclaimer": "Cette estimation est indicative et ne remplace pas une expertise professionnelle.",
        "excellent_deal": "Excellente affaire",
        "fair_deal": "Affaire correcte",
        "avoid": "À éviter",
        "excellent_msg": "Vous achetez ce véhicule environ {amount} € sous sa valeur estimée ajustée.",
        "fair_msg": "Le prix semble globalement cohérent, mais la marge de sécurité reste limitée.",
        "avoid_msg": "Vous payez environ {amount} € de trop par rapport à la valeur estimée ajustée.",
        "err_limit": "Vous avez atteint la limite gratuite de 3 analyses.",
        "err_brand": "Veuillez sélectionner une marque.",
        "err_model": "Veuillez sélectionner un modèle.",
        "err_year": "Veuillez sélectionner une année.",
        "err_price": "Le prix affiché doit être supérieur à 0.",
        "err_ref": "Aucun prix de référence n'est disponible pour ce véhicule.",
        "low_mileage": "Faible kilométrage : bonus",
        "reasonable_mileage": "Kilométrage raisonnable : léger bonus",
        "standard_mileage": "Kilométrage standard : neutre",
        "high_mileage": "Kilométrage élevé : pénalité",
        "very_high_mileage": "Kilométrage très élevé : forte pénalité",
        "critical_mileage": "Kilométrage critique : très forte pénalité",
        "recent_vehicle": "Véhicule récent ({age} ans) : bonus",
        "fairly_recent_vehicle": "Véhicule assez récent ({age} ans) : léger bonus",
        "standard_age": "Âge standard ({age} ans) : neutre",
        "old_vehicle": "Véhicule ancien ({age} ans) : pénalité",
        "very_old_vehicle": "Véhicule très ancien ({age} ans) : forte pénalité",
        "no_repairs": "Aucune réparation déclarée : bonus",
        "minor_repairs": "Petites réparations : léger bonus",
        "moderate_repairs": "Réparations modérées : neutre",
        "heavy_repairs": "Réparations lourdes : pénalité",
        "very_heavy_repairs": "Réparations très lourdes : forte pénalité",
        "deal_score": "Score de l'affaire",
    },
    "en": {
        "lang_label": "Language",
        "hero_badge": "Smart used-car analysis",
        "hero_title": "Buy your next car",
        "hero_title_2": "at the right price.",
        "hero_subtitle": "Auto Deal Analysis helps you detect real opportunities by analyzing vehicle price, mileage, age, and repair costs.",
        "hero_card_1_title": "Fast decision",
        "hero_card_1_text": "Get a clear verdict without manually comparing every detail.",
        "hero_card_2_title": "More complete view",
        "hero_card_2_text": "The score includes price, age, mileage and the real cost of repairs.",
        "plan_free": "Free plan",
        "remaining": "Remaining analyses",
        "premium": "Premium version coming soon",
        "reset": "Reset",
        "vehicle_info": "Vehicle information",
        "brand": "Brand",
        "model": "Model",
        "year": "Year",
        "mileage": "Mileage",
        "listed_price": "Listed price (€)",
        "ref_price": "Reference market price",
        "no_ref_price": "No reference price defined for this vehicle.",
        "repairs": "Repairs to anticipate",
        "other_repairs": "Other estimated repairs (€)",
        "analyze": "Launch analysis 🚀",
        "benefits_title": "Why use Auto Deal Analysis?",
        "benefits_text": "Avoid bad deals, save time and make more confident buying decisions with a structured analysis.",
        "benefit_1_title": "Avoid traps",
        "benefit_1_text": "Quickly identify overpriced vehicles or those that will cost too much to repair.",
        "benefit_2_title": "Save time",
        "benefit_2_text": "No need to manually compare every criterion for each listing.",
        "benefit_3_title": "Decide faster",
        "benefit_3_text": "A readable verdict and a clear score to focus on the right opportunities.",
        "premium_roadmap": "What comes next",
        "premium_roadmap_text": "• Multi-vehicle comparison\n• Unlimited analyses\n• Excel integration\n• History and reports",
        "result": "Analysis result",
        "listed_price_metric": "Listed price",
        "ref_price_metric": "Reference price",
        "repairs_metric": "Repairs",
        "gap_metric": "Final gap",
        "breakdown": "Breakdown",
        "vehicle": "Vehicle",
        "base_corrected": "Base corrected value",
        "global_adjustment": "Global adjustment",
        "adjusted_final": "Adjusted final value",
        "why": "Why this verdict?",
        "selected_repairs": "Selected repairs",
        "none": "None",
        "other_repairs_line": "Other repairs",
        "disclaimer": "This estimate is indicative and does not replace a professional inspection.",
        "excellent_deal": "Excellent deal",
        "fair_deal": "Fair deal",
        "avoid": "Avoid",
        "excellent_msg": "You are buying this vehicle about {amount} € below its adjusted estimated value.",
        "fair_msg": "The price seems broadly consistent, but the safety margin remains limited.",
        "avoid_msg": "You are paying about {amount} € too much compared with the adjusted estimated value.",
        "err_limit": "You have reached the free limit of 3 analyses.",
        "err_brand": "Please select a brand.",
        "err_model": "Please select a model.",
        "err_year": "Please select a year.",
        "err_price": "Listed price must be greater than 0.",
        "err_ref": "No reference market price is available for this vehicle.",
        "low_mileage": "Low mileage: bonus",
        "reasonable_mileage": "Reasonable mileage: slight bonus",
        "standard_mileage": "Standard mileage: neutral",
        "high_mileage": "High mileage: penalty",
        "very_high_mileage": "Very high mileage: strong penalty",
        "critical_mileage": "Critical mileage: very strong penalty",
        "recent_vehicle": "Recent vehicle ({age} years): bonus",
        "fairly_recent_vehicle": "Fairly recent vehicle ({age} years): slight bonus",
        "standard_age": "Standard age ({age} years): neutral",
        "old_vehicle": "Old vehicle ({age} years): penalty",
        "very_old_vehicle": "Very old vehicle ({age} years): strong penalty",
        "no_repairs": "No repairs declared: bonus",
        "minor_repairs": "Minor repairs: slight bonus",
        "moderate_repairs": "Moderate repairs: neutral",
        "heavy_repairs": "Heavy repairs: penalty",
        "very_heavy_repairs": "Very heavy repairs: strong penalty",
        "deal_score": "Deal score",
    },
    "de": {
        "lang_label": "Sprache",
        "hero_badge": "Intelligente Gebrauchtwagenanalyse",
        "hero_title": "Kaufen Sie Ihr nächstes Auto",
        "hero_title_2": "zum richtigen Preis.",
        "hero_subtitle": "Auto Deal Analysis hilft Ihnen, echte Chancen zu erkennen, indem Preis, Kilometerstand, Alter und Reparaturkosten analysiert werden.",
        "hero_card_1_title": "Schnelle Entscheidung",
        "hero_card_1_text": "Erhalten Sie ein klares Urteil, ohne alles manuell vergleichen zu müssen.",
        "hero_card_2_title": "Umfassendere Sicht",
        "hero_card_2_text": "Der Score berücksichtigt Preis, Alter, Kilometerstand und die echten Reparaturkosten.",
        "plan_free": "Kostenloser Plan",
        "remaining": "Verbleibende Analysen",
        "premium": "Premium-Version bald verfügbar",
        "reset": "Zurücksetzen",
        "vehicle_info": "Fahrzeuginformationen",
        "brand": "Marke",
        "model": "Modell",
        "year": "Jahr",
        "mileage": "Kilometerstand",
        "listed_price": "Angebotspreis (€)",
        "ref_price": "Referenzmarktpreis",
        "no_ref_price": "Kein Referenzpreis für dieses Fahrzeug definiert.",
        "repairs": "Geplante Reparaturen",
        "other_repairs": "Weitere geschätzte Reparaturen (€)",
        "analyze": "Analyse starten 🚀",
        "benefits_title": "Warum Auto Deal Analysis nutzen?",
        "benefits_text": "Vermeiden Sie schlechte Käufe, sparen Sie Zeit und treffen Sie sicherere Entscheidungen dank einer strukturierten Analyse.",
        "benefit_1_title": "Fallen vermeiden",
        "benefit_1_text": "Erkennen Sie schnell überteuerte Fahrzeuge oder Modelle mit hohen Reparaturkosten.",
        "benefit_2_title": "Zeit sparen",
        "benefit_2_text": "Kein manuelles Vergleichen aller Kriterien bei jeder Anzeige mehr.",
        "benefit_3_title": "Schneller entscheiden",
        "benefit_3_text": "Ein verständliches Urteil und ein klarer Score helfen Ihnen, sich auf die richtigen Fahrzeuge zu konzentrieren.",
        "premium_roadmap": "Was als Nächstes kommt",
        "premium_roadmap_text": "• Vergleich mehrerer Fahrzeuge\n• Unbegrenzte Analysen\n• Excel-Integration\n• Verlauf und Berichte",
        "result": "Analyseergebnis",
        "listed_price_metric": "Angebotspreis",
        "ref_price_metric": "Referenzpreis",
        "repairs_metric": "Reparaturen",
        "gap_metric": "Enddifferenz",
        "breakdown": "Berechnungsdetails",
        "vehicle": "Fahrzeug",
        "base_corrected": "Roh korrigierter Wert",
        "global_adjustment": "Gesamtanpassung",
        "adjusted_final": "Endgültig angepasster Wert",
        "why": "Warum dieses Urteil?",
        "selected_repairs": "Ausgewählte Reparaturen",
        "none": "Keine",
        "other_repairs_line": "Weitere Reparaturen",
        "disclaimer": "Diese Schätzung ist unverbindlich und ersetzt keine professionelle Begutachtung.",
        "excellent_deal": "Sehr gutes Geschäft",
        "fair_deal": "Ordentliches Geschäft",
        "avoid": "Vermeiden",
        "excellent_msg": "Sie kaufen dieses Fahrzeug etwa {amount} € unter seinem angepassten geschätzten Wert.",
        "fair_msg": "Der Preis wirkt insgesamt stimmig, aber die Sicherheitsmarge bleibt begrenzt.",
        "avoid_msg": "Sie zahlen etwa {amount} € zu viel im Vergleich zum angepassten geschätzten Wert.",
        "err_limit": "Sie haben das kostenlose Limit von 3 Analysen erreicht.",
        "err_brand": "Bitte wählen Sie eine Marke aus.",
        "err_model": "Bitte wählen Sie ein Modell aus.",
        "err_year": "Bitte wählen Sie ein Jahr aus.",
        "err_price": "Der Angebotspreis muss größer als 0 sein.",
        "err_ref": "Für dieses Fahrzeug ist kein Referenzmarktpreis verfügbar.",
        "low_mileage": "Niedriger Kilometerstand: Bonus",
        "reasonable_mileage": "Angemessener Kilometerstand: kleiner Bonus",
        "standard_mileage": "Standard-Kilometerstand: neutral",
        "high_mileage": "Hoher Kilometerstand: Malus",
        "very_high_mileage": "Sehr hoher Kilometerstand: starker Malus",
        "critical_mileage": "Kritischer Kilometerstand: sehr starker Malus",
        "recent_vehicle": "Neues Fahrzeug ({age} Jahre): Bonus",
        "fairly_recent_vehicle": "Relativ neues Fahrzeug ({age} Jahre): kleiner Bonus",
        "standard_age": "Normales Alter ({age} Jahre): neutral",
        "old_vehicle": "Altes Fahrzeug ({age} Jahre): Malus",
        "very_old_vehicle": "Sehr altes Fahrzeug ({age} Jahre): starker Malus",
        "no_repairs": "Keine Reparaturen angegeben: Bonus",
        "minor_repairs": "Kleine Reparaturen: leichter Bonus",
        "moderate_repairs": "Mittlere Reparaturen: neutral",
        "heavy_repairs": "Schwere Reparaturen: Malus",
        "very_heavy_repairs": "Sehr schwere Reparaturen: starker Malus",
        "deal_score": "Deal-Score",
    }
}

def tr(key, **kwargs):
    txt = I18N[st.session_state.lang][key]
    return txt.format(**kwargs) if kwargs else txt




reparations_disponibles = {
    "Pneus": 400,
    "Freinage": 500,
    "Distribution": 700,
    "Embrayage": 900,
    "Carrosserie": 1200,
    "Amortisseurs": 600,
    "Vidange / entretien": 150
}

# =============================
# FONCTIONS
# =============================
def reinitialiser():
    compteur_actuel = st.session_state.get("compteur", 0)
    lang_actuelle = st.session_state.get("lang", "fr")
    premium_actuel = st.session_state.get("is_premium", False)
    if "comparaison" not in st.session_state:
        for cle in list(st.session_state.keys()):
            del st.session_state[cle]

    st.session_state.compteur = compteur_actuel
    st.session_state.lang = lang_actuelle
    st.session_state.is_premium = premium_actuel

def recuperer_prix_reference(marque, modele, annee):
    resultat = df_prix[
        (df_prix["Marque"] == marque) &
        (df_prix["Modele"] == modele) &
        (df_prix["Année"] == int(annee))
    ]

    if not resultat.empty:
        return int(resultat.iloc[0]["Prix_indicatif_eur"])
    return None

def calcul_bonus_malus_km(kilometrage):
    if kilometrage <= 30000:
        return 700, tr("low_mileage")
    elif kilometrage <= 60000:
        return 400, tr("reasonable_mileage")
    elif kilometrage <= 100000:
        return 0, tr("standard_mileage")
    elif kilometrage <= 150000:
        return -500, tr("high_mileage")
    elif kilometrage <= 200000:
        return -1200, tr("very_high_mileage")
    else:
        return -2200, tr("critical_mileage")

def calcul_bonus_malus_age(annee):
    annee_actuelle = datetime.now().year
    age = annee_actuelle - annee
    if age <= 2:
        return 800, tr("recent_vehicle", age=age)
    elif age <= 5:
        return 300, tr("fairly_recent_vehicle", age=age)
    elif age <= 8:
        return 0, tr("standard_age", age=age)
    elif age <= 12:
        return -700, tr("old_vehicle", age=age)
    else:
        return -1500, tr("very_old_vehicle", age=age)

def calcul_penalite_reparations(cout_reparations):
    if cout_reparations == 0:
        return 300, tr("no_repairs")
    elif cout_reparations <= 500:
        return 100, tr("minor_repairs")
    elif cout_reparations <= 1500:
        return 0, tr("moderate_repairs")
    elif cout_reparations <= 3000:
        return -700, tr("heavy_repairs")
    else:
        return -1500, tr("very_heavy_repairs")

def convertir_difference_en_score(difference_finale):
    if difference_finale >= 4000:
        return 10
    elif difference_finale >= 2500:
        return 9
    elif difference_finale >= 1500:
        return 8
    elif difference_finale >= 500:
        return 7
    elif difference_finale >= 0:
        return 6
    elif difference_finale >= -1000:
        return 5
    elif difference_finale >= -2000:
        return 4
    elif difference_finale >= -3500:
        return 3
    elif difference_finale >= -5000:
        return 2
    else:
        return 1

def afficher_jauge(score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": tr("deal_score")},
        gauge={
            "axis": {"range": [0, 10]},
            "bar": {"color": "#34D399"},
            "steps": [
                {"range": [0, 4], "color": "#7f1d1d"},
                {"range": [4, 7], "color": "#9a6a12"},
                {"range": [7, 10], "color": "#14532d"},
            ],
        }
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font={"color": "white", "size": 16},
        margin=dict(l=20, r=20, t=50, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

# =============================
# LANGUE
# =============================
lang_col1, lang_col2 = st.columns([8, 2])
with lang_col2:
    st.markdown('<div class="lang-wrap">', unsafe_allow_html=True)
    choix_lang = st.selectbox(
        tr("lang_label"),
        ["🇫🇷 Français", "🇬🇧 English", "🇩🇪 Deutsch"],
        index={"fr": 0, "en": 1, "de": 2}[st.session_state.lang]
    )
    if "Français" in choix_lang:
        st.session_state.lang = "fr"
    elif "English" in choix_lang:
        st.session_state.lang = "en"
    else:
        st.session_state.lang = "de"
    st.markdown('</div>', unsafe_allow_html=True)

# =============================
# HERO
# =============================
st.markdown(f"""
<div class="hero">
    <div class="hero-grid">
        <div>
            <div class="hero-badge">🚘 {tr("hero_badge")}</div>
            <div class="hero-title">{tr("hero_title")}<br>{tr("hero_title_2")}</div>
            <div class="hero-subtitle">{tr("hero_subtitle")}</div>
        </div>
        <div class="hero-side">
            <div class="glass-mini">
                <div class="glass-mini-title">{tr("hero_card_1_title")}</div>
                <div class="glass-mini-text">{tr("hero_card_1_text")}</div>
            </div>
            <div class="glass-mini">
                <div class="glass-mini-title">{tr("hero_card_2_title")}</div>
                <div class="glass-mini-text">{tr("hero_card_2_text")}</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

analyses_restantes = "Illimitées" if st.session_state.is_premium else max(0, 3 - st.session_state.compteur)
nom_plan = "Plan Premium" if st.session_state.is_premium else tr("plan_free")

top1, top2, top3 = st.columns([1.2, 1, 1])

with top1:
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">{nom_plan}</div>
        <div class="section-text">{tr("remaining")} : <b>{analyses_restantes}</b></div>
    </div>
    """, unsafe_allow_html=True)

with top2:
    if st.button(tr("reset"), use_container_width=True, type="secondary"):
        reinitialiser()
        st.rerun()

with top3:
    if st.session_state.is_premium:
        st.button("Premium activé ✅", use_container_width=True, disabled=True)
    else:
        if st.button("Passer au Premium ⭐", use_container_width=True):
            st.session_state.is_premium = True
            st.rerun()

left, right = st.columns([1.2, 0.8], gap="large")

with left:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.markdown(f'<div class="section-title">{tr("vehicle_info")}</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        marques = sorted(df_prix["Marque"].unique())
        marque = st.selectbox(tr("brand"), [""] + marques)

    with c2:
        if marque:
            modeles = sorted(
                df_prix[df_prix["Marque"] == marque]["Modele"].unique()
            )
            modele = st.selectbox(tr("model"), [""] + modeles)
        else:
            modele = st.selectbox(tr("model"), [""])

    c3, c4 = st.columns(2)

    with c3:
        if marque and modele:
            annees = sorted(
                df_prix[
                    (df_prix["Marque"] == marque) &
                    (df_prix["Modele"] == modele)
                ]["Année"].unique(),
                reverse=True
            )
            annee = st.selectbox(tr("year"), annees)
        else:
            annee = st.selectbox(tr("year"), [""])

    with c4:
        kilometrage = st.number_input(
            tr("mileage"),
            min_value=0,
            value=120000,
            step=1000
        )

    prix_affiche = st.number_input(
        tr("listed_price"),
        min_value=0,
        value=8000,
        step=100
    )

    st.markdown('</div>', unsafe_allow_html=True)

    prix_marche = None
    if marque and modele and annee:
        prix_marche = recuperer_prix_reference(marque, modele, annee)
        if prix_marche is not None:
            st.success(f"{tr('ref_price')} : {prix_marche} €")
        else:
            st.warning(tr("no_ref_price"))

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{tr("repairs")}</div>', unsafe_allow_html=True)

    cout_total_reparations = 0
    reparations_selectionnees = []

    rc1, rc2 = st.columns(2)
    items = list(reparations_disponibles.items())

    for i, (nom, prix) in enumerate(items):
        target = rc1 if i % 2 == 0 else rc2
        with target:
            if st.checkbox(f"{nom} ({prix} €)"):
                cout_total_reparations += prix
                reparations_selectionnees.append(f"{nom} ({prix} €)")

    autres_reparations = st.number_input(tr("other_repairs"), min_value=0, value=0, step=50)
    cout_total_reparations += autres_reparations


    analyser = st.button(tr("analyze"), use_container_width=True, type="primary")

st.markdown('</div>', unsafe_allow_html=True)

# =============================
# RESULTATS
# =============================
if analyser:
    erreurs = []

    if not st.session_state.is_premium and st.session_state.compteur >= 3:
        erreurs.append(tr("err_limit"))

    if not marque:
        erreurs.append(tr("err_brand"))

    if marque and not modele:
        erreurs.append(tr("err_model"))

    if annee is None:
        erreurs.append(tr("err_year"))

    if prix_affiche <= 0:
        erreurs.append(tr("err_price"))

    if prix_marche is None:
        erreurs.append(tr("err_ref"))

    if erreurs:
        for erreur in erreurs:
            st.error(erreur)
    else:
        if not st.session_state.is_premium:
            st.session_state.compteur += 1

        st.success("Analyse OK")  # TEMPORAIRE POUR TEST

with right:
    st.markdown(f"""
    <div class="highlight-card">
        <div class="highlight-title">{tr("benefits_title")}</div>
        <div class="highlight-text">{tr("benefits_text")}</div>
    </div>
    """, unsafe_allow_html=True)

    b1, b2, b3 = st.columns(1), st.columns(1), st.columns(1)
    st.markdown(f"""
    <div class="small-stat">
        <div class="small-stat-title">{tr("benefit_1_title")}</div>
        <div class="small-stat-text">{tr("benefit_1_text")}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class="small-stat">
        <div class="small-stat-title">{tr("benefit_2_title")}</div>
        <div class="small-stat-text">{tr("benefit_2_text")}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="small-stat">
        <div class="small-stat-title">{tr("benefit_3_title")}</div>
        <div class="small-stat-text">{tr("benefit_3_text")}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">{tr("premium_roadmap")}</div>
        <div class="section-text" style="white-space: pre-line;">{tr("premium_roadmap_text")}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
st.markdown("---")

# =============================
# RESULTAT
# =============================
if analyser:
    erreurs = []

    if not st.session_state.is_premium and st.session_state.compteur >= 3:
        erreurs.append(tr("err_limit"))

    if not marque:
        erreurs.append(tr("err_brand"))

    if marque and not modele:
        erreurs.append(tr("err_model"))

    if annee is None:
        erreurs.append(tr("err_year"))

    if prix_affiche <= 0:
        erreurs.append(tr("err_price"))

    if prix_marche is None:
        erreurs.append(tr("err_ref"))

    if erreurs:
        for erreur in erreurs:
            st.error(erreur)

    else:
        if not st.session_state.is_premium:
            st.session_state.compteur += 1

        bonus_malus_km, explication_km = calcul_bonus_malus_km(kilometrage)
        bonus_malus_age, explication_age = calcul_bonus_malus_age(annee)
        bonus_malus_reparations, explication_reparations = calcul_penalite_reparations(cout_total_reparations)

        valeur_corrigee_brute = prix_marche - cout_total_reparations
        ajustement_global = bonus_malus_km + bonus_malus_age + bonus_malus_reparations
        valeur_corrigee_finale = valeur_corrigee_brute + ajustement_global
        difference_finale = valeur_corrigee_finale - prix_affiche
        score = convertir_difference_en_score(difference_finale)

        if score >= 8:
            verdict = tr("excellent_deal")
            message = tr("excellent_msg", amount=abs(difference_finale))
            level = "success"
        elif score >= 5:
            verdict = tr("fair_deal")
            message = tr("fair_msg")
            level = "warning"
        else:
            verdict = tr("avoid")
            message = tr("avoid_msg", amount=abs(difference_finale))
            level = "error"

        st.success("Analyse OK")

      
        st.write(st.session_state.comparaison)

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(f'<div class="result-title">{tr("result")}</div>', unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(f'<div class="metric-card"><div class="metric-label">{tr("listed_price_metric")}</div><div class="metric-number">{prix_affiche} €</div></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="metric-card"><div class="metric-label">{tr("ref_price_metric")}</div><div class="metric-number">{prix_marche} €</div></div>', unsafe_allow_html=True)
        with m3:
            st.markdown(f'<div class="metric-card"><div class="metric-label">{tr("repairs_metric")}</div><div class="metric-number">{cout_total_reparations} €</div></div>', unsafe_allow_html=True)
        with m4:
            st.markdown(f'<div class="metric-card"><div class="metric-label">{tr("gap_metric")}</div><div class="metric-number">{difference_finale} €</div></div>', unsafe_allow_html=True)

        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        res1, res2 = st.columns([1, 1], gap="large")
        with res1:
            st.subheader(verdict)
            if level == "success":
                st.success(message)
            elif level == "warning":
                st.warning(message)
            else:
                st.error(message)

            st.markdown(f"### {tr('breakdown')}")
            st.write(f"**{tr('vehicle')} :** {marque} {modele} ({annee})")
            st.write(f"**{tr('mileage')} :** {kilometrage} km")
            st.write(f"**{tr('base_corrected')} :** {valeur_corrigee_brute} €")
            st.write(f"**{tr('global_adjustment')} :** {ajustement_global} €")
            st.write(f"**{tr('adjusted_final')} :** {valeur_corrigee_finale} €")

        with res2:
            afficher_jauge(score)

        st.markdown(f"### {tr('why')}")
        e1, e2, e3 = st.columns(3)
        with e1:
            st.info(explication_km)
        with e2:
            st.info(explication_age)
        with e3:
            st.info(explication_reparations)

        st.markdown(f"### {tr('selected_repairs')}")
        if reparations_selectionnees:
            for rep in reparations_selectionnees:
                st.write(f"- {rep}")
        else:
            st.write(f"- {tr('none')}")

        if autres_reparations > 0:
            st.write(f"- {tr('other_repairs_line')} : {autres_reparations} €")

        st.markdown(f'<div class="subtle-note">{tr("disclaimer")}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("---")

if st.session_state.comparaison:
    import pandas as pd

    df_compare = pd.DataFrame(st.session_state.comparaison)
    df_compare = df_compare.sort_values(by="Score", ascending=False).reset_index(drop=True)

    meilleur = df_compare.iloc[0]
    pire = df_compare.iloc[-1]

    c1, c2 = st.columns(2)

    with c1:
        st.success(
            f"🏆 Meilleure affaire : {meilleur['Marque']} {meilleur['Modele']} ({meilleur['Année']}) "
            f"— Score {meilleur['Score']}/10"
        )

    with c2:
        st.error(
            f"⚠️ Moins bonne affaire : {pire['Marque']} {pire['Modele']} ({pire['Année']}) "
            f"— Score {pire['Score']}/10"
        )

    st.dataframe(df_compare, use_container_width=True)

    if st.button("Vider la comparaison", key="btn_clear_compare"):
        st.session_state.comparaison = []
        st.rerun()
else:
    st.write("Aucun véhicule ajouté pour le moment.")