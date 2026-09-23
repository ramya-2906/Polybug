CUSTOM_CSS = """
<style>
#MainMenu {visibility: hidden !important;}
footer {visibility: hidden !important;}
header {visibility: hidden !important;}
.stDeployButton {display: none !important;}
div[data-testid="stToolbar"] {visibility: hidden !important;}
div[data-testid="stDecoration"] {visibility: hidden !important;}
div[data-testid="stStatusWidget"] {visibility: hidden !important;}

[data-testid="stAppViewContainer"] {
    background: #f3f0ff!important;
    background-image:
        radial-gradient(at 15% 25%, rgba(167,139,250,0.35) 0px, transparent 50%),
        radial-gradient(at 85% 25%, rgba(103,232,249,0.35) 0px, transparent 50%),
        radial-gradient(at 50% 85%, rgba(251,146,60,0.15) 0px, transparent 50%)!important;
}
[data-testid="stHeader"] { background: transparent!important; }
textarea { background: #ffffff!important; border: 2px solid #c4b5fd!important; border-radius: 16px!important; }
input { background: #ffffff!important; border-radius: 12px!important; }
.stButton > button { background: linear-gradient(90deg, #7c3aed 0%, #a855f7 100%)!important; color: white!important; border: none!important; border-radius: 12px!important; font-weight: bold!important; width: 100%!important; }
</style>
"""
