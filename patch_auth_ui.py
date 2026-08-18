from pathlib import Path
import re

path = Path('app.py')
text = path.read_text(encoding='utf-8')
lines = text.splitlines()

sections = {
    'def login_page():': [
        'def login_page():',
        '    # Login Form',
        '''def login_page():

    # Background image

    login_bg = get_base64(
        ASSETS_DIR / "background2.jpg"
    )


    st.markdown(f"""

    <style>

    .auth-page{{
        min-height:90vh;
        background:
        linear-gradient(
        rgba(5,15,40,.80),
        rgba(5,15,40,.90)
        ),
        url("data:image/jpeg;base64,{login_bg}");
        background-size:cover;
        background-position:center;
        display:flex;
        justify-content:center;
        align-items:center;
        padding:40px;
    }}

    .auth-card{{
        width:460px;
        max-width:100%;
        padding:45px;
        background:rgba(255,255,255,.14);
        backdrop-filter:blur(24px);
        border-radius:32px;
        border:1px solid rgba(255,255,255,.18);
        box-shadow:0 35px 70px rgba(0,0,0,.20);
        text-align:center;
    }}

    .auth-logo{{
        font-size:52px;
        margin-bottom:16px;
    }}

    .auth-title{{
        font-size:36px;
        font-weight:800;
        color:white;
        margin-bottom:12px;
    }}

    .auth-subtitle{{
        color:#CBD5E1;
        font-size:16px;
        line-height:1.8;
        margin-bottom:30px;
    }}

    .stTextInput>div>div>input{{
        border-radius:16px !important;
        border:1px solid rgba(255,255,255,.35) !important;
        background:rgba(255,255,255,.92) !important;
        color:#0F172A !important;
    }}

    .stButton>button{{
        border-radius:14px !important;
        height:52px !important;
        font-size:16px !important;
        font-weight:700 !important;
    }}

    .stButton>button:hover{{
        transform:translateY(-1px);
        box-shadow:0 16px 32px rgba(56,189,248,.28);
    }}

    .auth-info{{
        color:#E2E8F0;
        font-size:14px;
        margin-top:22px;
    }}

    </style>

    """, unsafe_allow_html=True)


    st.markdown(f"""

    <div class="auth-page">

        <div class="auth-card">

            <div class="auth-logo">🌸</div>

            <div class="auth-title">Welcome back to IrisVision AI</div>

            <div class="auth-subtitle">
                Securely access your prediction dashboard and AI analytics.
            </div>

        </div>

    </div>

    """, unsafe_allow_html=True)


    # Login Form'''
    ],
    'def register_page():': [
        'def register_page():',
        '    col1,col2,col3 = st.columns([1,2,1])',
        '''def register_page():

    register_bg = get_base64(
        ASSETS_DIR / "background3.jpg"
    )


    st.markdown(f"""

    <style>

    .auth-page{{
        min-height:90vh;
        background:
        linear-gradient(
        rgba(5,15,40,.82),
        rgba(5,15,40,.90)
        ),
        url("data:image/jpeg;base64,{register_bg}");
        background-size:cover;
        background-position:center;
        display:flex;
        justify-content:center;
        align-items:center;
        padding:40px;
    }}

    .auth-card{{
        width:460px;
        max-width:100%;
        padding:46px;
        background:rgba(255,255,255,.14);
        backdrop-filter:blur(24px);
        border-radius:32px;
        border:1px solid rgba(255,255,255,.18);
        box-shadow:0 35px 70px rgba(0,0,0,.20);
        text-align:center;
    }}

    .auth-logo{{
        font-size:54px;
        margin-bottom:16px;
    }}

    .auth-title{{
        font-size:36px;
        font-weight:800;
        color:white;
        margin-bottom:12px;
    }}

    .auth-subtitle{{
        color:#CBD5E1;
        font-size:16px;
        line-height:1.8;
        margin-bottom:30px;
    }}

    .stTextInput>div>div>input{{
        border-radius:16px !important;
        border:1px solid rgba(255,255,255,.35) !important;
        background:rgba(255,255,255,.92) !important;
        color:#0F172A !important;
    }}

    .stButton>button{{
        border-radius:14px !important;
        height:52px !important;
        font-size:16px !important;
        font-weight:700 !important;
    }}

    .stButton>button:hover{{
        transform:translateY(-1px);
        box-shadow:0 16px 32px rgba(16,185,129,.28);
    }}

    .auth-footer{{
        color:#E2E8F0;
        font-size:14px;
        margin-top:20px;
    }}

    </style>

    """, unsafe_allow_html=True)


    st.markdown(f"""

    <div class="auth-page">

        <div class="auth-card">

            <div class="auth-logo">🌸</div>

            <div class="auth-title">Create your IrisVision account</div>

            <div class="auth-subtitle">
                Sign up to save predictions, access analytics, and manage your profile.
            </div>

        </div>

    </div>

    """, unsafe_allow_html=True)
'''
    ],
    'def forgot_password_page():': [
        'def forgot_password_page():',
        '    col1,col2,col3 = st.columns([1,2,1])',
        '''def forgot_password_page():

    forgot_bg = get_base64(
        ASSETS_DIR / "background4.jpg"
    )


    st.markdown(f"""

    <style>

    .auth-page{{
        min-height:90vh;
        background:
        linear-gradient(
        rgba(3,25,68,.82),
        rgba(7,41,105,.88)
        ),
        url("data:image/jpeg;base64,{forgot_bg}");
        background-size:cover;
        background-position:center;
        display:flex;
        justify-content:center;
        align-items:center;
        padding:40px;
    }}

    .auth-card{{
        width:460px;
        max-width:100%;
        padding:48px;
        background:rgba(255,255,255,.12);
        backdrop-filter:blur(24px);
        border-radius:32px;
        border:1px solid rgba(255,255,255,.18);
        box-shadow:0 28px 62px rgba(0,0,0,.20);
        text-align:center;
    }}

    .auth-logo{{
        font-size:54px;
        margin-bottom:16px;
    }}

    .auth-title{{
        font-size:36px;
        font-weight:800;
        color:white;
        margin-bottom:12px;
    }}

    .auth-subtitle{{
        color:#CBD5E1;
        font-size:16px;
        line-height:1.8;
        margin-bottom:30px;
    }}

    .stTextInput>div>div>input{{
        border-radius:16px !important;
        border:1px solid rgba(255,255,255,.35) !important;
        background:rgba(255,255,255,.92) !important;
        color:#0F172A !important;
    }}

    .stButton>button{{
        border-radius:14px !important;
        height:52px !important;
        font-size:16px !important;
        font-weight:700 !important;
    }}

    .auth-footer{{
        color:#E2E8F0;
        font-size:14px;
        margin-top:18px;
    }}

    </style>

    """, unsafe_allow_html=True)


    st.markdown("""

    <div class="auth-page">

        <div class="auth-card">

            <div class="auth-logo">🔑</div>

            <div class="auth-title">Reset your IrisVision password</div>

            <div class="auth-subtitle">
                Enter your username and choose a strong new password to regain access.
            </div>

        </div>

    </div>

    """, unsafe_allow_html=True)
'''
    ],
    'def guest_profile():': [
        'def guest_profile():',
        '    st.markdown("<br>",unsafe_allow_html=True)',
        '''def guest_profile():

    guest_bg = get_base64(
        ASSETS_DIR / "background1.jpg"
    )


    st.markdown(f"""

    <style>

    .auth-page{{
        min-height:85vh;
        background:
        linear-gradient(
        rgba(2,18,47,.82),
        rgba(5,37,89,.88)
        ),
        url("data:image/jpeg;base64,{guest_bg}");
        background-size:cover;
        background-position:center;
        display:flex;
        justify-content:center;
        align-items:center;
        padding:40px;
    }}

    .auth-card{{
        width:520px;
        max-width:100%;
        padding:50px;
        background:rgba(255,255,255,.14);
        backdrop-filter:blur(22px);
        border-radius:32px;
        border:1px solid rgba(255,255,255,.18);
        box-shadow:0 30px 68px rgba(0,0,0,.20);
        text-align:center;
        color:white;
    }}

    .auth-logo{{
        font-size:80px;
        margin-bottom:18px;
    }}

    .auth-title{{
        font-size:40px;
        font-weight:800;
        margin-bottom:12px;
    }}

    .auth-subtitle{{
        font-size:17px;
        line-height:1.8;
        color:#CBD5E1;
        margin-bottom:24px;
    }}

    .auth-badge{{
        display:inline-block;
        margin-bottom:24px;
        padding:12px 30px;
        border-radius:999px;
        background:rgba(255,255,255,.18);
        color:white;
        font-weight:700;
    }}

    .stButton>button{{
        border-radius:14px !important;
        height:52px !important;
        font-size:16px !important;
        font-weight:700 !important;
    }}

    .stButton>button:hover{{
        transform:translateY(-1px);
        box-shadow:0 16px 32px rgba(59,130,246,.28);
    }}

    .guest-note{{
        color:#E2E8F0;
        font-size:15px;
        margin-top:22px;
        line-height:1.8;
    }}

    </style>

    """, unsafe_allow_html=True)


    st.markdown("""

    <div class="auth-page">

        <div class="auth-card">

            <div class="auth-logo">🌐</div>

            <div class="auth-title">Welcome Guest</div>

            <div class="auth-badge">Guest Access</div>

            <div class="auth-subtitle">
                Explore IrisVision AI with limited personalization. Register anytime to unlock full history and profile management.
            </div>

        </div>

    </div>

    """, unsafe_allow_html=True)
'''
    ],
}

occurrences = {k: [i for i,l in enumerate(lines) if l.strip()==k] for k in sections}
for k, idxs in occurrences.items():
    if len(idxs) < 2:
        raise SystemExit(f'Expected at least 2 occurrences of {k}, found {len(idxs)}')

for key, (func, end_marker, replacement) in sections.items():
    occ = occurrences[func]
    start = occ[1]
    end = None
    for i in range(start+1, len(lines)):
        if lines[i].strip() == end_marker:
            end = i
            break
    if end is None:
        raise SystemExit(f'End marker {end_marker} not found for {func}')
    lines = lines[:start] + replacement.splitlines() + lines[end:]

path.write_text('\n'.join(lines), encoding='utf-8')
print('Updated auth sections')"