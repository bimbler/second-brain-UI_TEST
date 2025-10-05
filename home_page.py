import streamlit as st
import base64
from pathlib import Path
import textwrap


def render_home_page():
    # --- Load assets from assets folder ---
    assets_dir = Path(__file__).parent / "assets"
    logo_path = assets_dir / "brain.svg"
    demo_path = assets_dir / "Demo.svg"   # CHANGED: use the SVG asset

    logo_b64 = base64.b64encode(logo_path.read_bytes()).decode("utf-8")
    demo_b64 = base64.b64encode(demo_path.read_bytes()).decode("utf-8")  # encode SVG as base64

    # --- CSS (transparent container, image right, text left) ---
    st.markdown("""
    <style>
      .hero-transparent {
        background: transparent;
        border: none;
        padding: 4rem 2rem 3rem;
        color: #fff;
      }

      .hero-container {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 2.5rem;
        flex-wrap: wrap;
        background: transparent;
      }

      .hero-left {
        flex: 1 1 48%;
        min-width: 320px;
        text-align: left;
        background: transparent;
      }

      .brand {
        display: flex;
        align-items: center;
        gap: .6rem;
        margin-bottom: 1.25rem;
        background: transparent;
      }

      .brand img {
        width: 32px;
        height: 32px;
        filter: brightness(0) invert(1);
      }

      .brand .name {
        font-weight: 700;
        color: #fff;
        font-size: 1.15rem;
      }

      .hero-title {
        font-size: clamp(2.4rem, 6vw, 4.5rem);
        font-weight: 800;
        line-height: 1.05;
        margin-bottom: 1rem;
        text-align: left;
        background: transparent;
      }

      .hero-subtitle {
        margin: 0 0 2rem;
        color: rgba(255,255,255,.9);
        font-size: 1.1rem;
        max-width: 500px;
        background: transparent;
      }

      .hero-buttons {
        display: flex;
        gap: .75rem;
        flex-wrap: wrap;
        margin-bottom: 1.5rem;
        background: transparent;
      }

      .btn {
        display:inline-flex;
        align-items:center;
        justify-content:center;
        padding:.8rem 1.2rem;
        border-radius:.75rem;
        font-weight:700;
        text-decoration:none;
        border:1px solid transparent;
        transition: 0.2s;
      }

      .btn-primary {
        background:#fff;
        color:#0ea5e9;
      }

      .btn-secondary {
        background:#fff;
        color:#0ea5e9;
      }

      .btn-primary:hover { background:#f0f9ff; }
      .btn-secondary:hover { background:#f0f9ff; }

      .mini-feats {
        display:flex;
        gap:1.25rem;
        flex-wrap:wrap;
        color: rgba(255,255,255,0.9);
        font-size: 0.95rem;
        background: transparent;
      }

      .hero-right {
        flex: 1 1 46%;
        min-width: 300px;
        text-align: right;
        background: transparent;
      }

      .hero-right img {
        max-width: 100%;
        height: auto;
        border-radius: 1rem;
        box-shadow: 0 12px 40px rgba(0,0,0,0.35);
      }

      /* Buttons row BELOW the hero, left-aligned to same container */
      .hero-actions {
          max-width: 1200px;
          margin: 1.5rem auto 0;
          display: flex;
          gap: .75rem;
      }

      .btn {
          display:inline-flex;
          align-items:center;
          justify-content:center;
          padding:.8rem 1.2rem;
          border-radius:.75rem;
          font-weight:700;
          text-decoration:none;
          border:1px solid transparent;
          transition: 0.2s;
      }

      .btn-primary { background:#fff; color:#0ea5e9; }
      .btn-secondary { background:#fff; color:#0ea5e9; }
      .btn-primary:hover, .btn-secondary:hover { background:#f0f9ff; }
    </style>
    """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    html = f"""
<div class="hero-transparent">
  <div class="hero-container">
    <div class="hero-left">
      <div class="brand">
        <img src="data:image/svg+xml;base64,{logo_b64}" alt="Second Brain logo" />
        <div class="name">Second Brain</div>
      </div>
      <div class="hero-title">Your Business<br>Optimization<br>Engine</div>
      <div class="hero-subtitle">
        Skip the prescriptive processes. Let AI make intelligent decisions for your business.
        From inventory optimization to operational efficiency – your second brain handles it all.
      </div>
      <div class="hero-buttons">
        <a href="#" class="btn btn-primary">Get Started Today →</a>
        <a href="#" class="btn btn-secondary">Watch Demo</a>
      </div>
      <div class="mini-feats">
        <span>📊 Real-time Analytics</span>
        <span>⚡ Instant Optimization</span>
      </div>
    </div>
  </div>
</div>
"""
    # --- FEATURE CARDS SECTION ---
    st.markdown("""
    <style>
      .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.75rem;
        margin-top: 4rem;
      }
    </style>

    <div class="feature-grid">
      <!-- Card 1 -->
      <div class="rounded-lg text-card-foreground shadow-sm relative group hover:shadow-elegant transition-all duration-300 border-0 bg-card/80 backdrop-blur-sm">
        <div class="flex flex-col space-y-1.5 p-6 pb-4">
          <div class="flex items-center justify-between mb-4">
            <div class="p-3 bg-gradient-primary rounded-xl">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                   viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                   stroke-linecap="round" stroke-linejoin="round"
                   class="lucide lucide-brain h-6 w-6 text-primary-foreground">
                <path d="M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z"></path>
                <path d="M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z"></path>
                <path d="M15 13a4.5 4.5 0 0 1-3-4 4.5 4.5 0 0 1-3 4"></path>
                <path d="M17.599 6.5a3 3 0 0 0 .399-1.375"></path>
                <path d="M6.003 5.125A3 3 0 0 0 6.401 6.5"></path>
                <path d="M3.477 10.896a4 4 0 0 1 .585-.396"></path>
                <path d="M19.938 10.5a4 4 0 0 1 .585.396"></path>
                <path d="M6 18a4 4 0 0 1-1.967-.516"></path>
                <path d="M19.967 17.484A4 4 0 0 1 18 18"></path>
              </svg>
            </div>
            <div class="inline-flex items-center rounded-full border px-2.5 py-0.5 font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80 text-xs">
              Core Feature
            </div>
          </div>
          <h3 class="font-semibold tracking-tight text-xl group-hover:text-primary transition-colors">
            AI-Powered Decision Making
          </h3>
        </div>
        <div class="p-6 pt-0">
          <p class="text-muted-foreground text-base leading-relaxed">
            Advanced algorithms analyze your business patterns and make optimal decisions automatically.
          </p>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="rounded-lg text-card-foreground shadow-sm relative group hover:shadow-elegant transition-all duration-300 border-0 bg-card/80 backdrop-blur-sm">
        <div class="flex flex-col space-y-1.5 p-6 pb-4">
          <div class="flex items-center justify-between mb-4">
            <div class="p-3 bg-gradient-primary rounded-xl">
              📈
            </div>
            <div class="inline-flex items-center rounded-full border px-2.5 py-0.5 font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80 text-xs">
              Optimization
            </div>
          </div>
          <h3 class="font-semibold tracking-tight text-xl group-hover:text-primary transition-colors">
            Inventory Optimization
          </h3>
        </div>
        <div class="p-6 pt-0">
          <p class="text-muted-foreground text-base leading-relaxed">
            Know exactly when to order, how much to order, and in what combinations for maximum efficiency.
          </p>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="rounded-lg text-card-foreground shadow-sm relative group hover:shadow-elegant transition-all duration-300 border-0 bg-card/80 backdrop-blur-sm">
        <div class="flex flex-col space-y-1.5 p-6 pb-4">
          <div class="flex items-center justify-between mb-4">
            <div class="p-3 bg-gradient-primary rounded-xl">
              ⏱️
            </div>
            <div class="inline-flex items-center rounded-full border px-2.5 py-0.5 font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80 text-xs">
              Real-Time
            </div>
          </div>
          <h3 class="font-semibold tracking-tight text-xl group-hover:text-primary transition-colors">
            Real-Time Monitoring
          </h3>
        </div>
        <div class="p-6 pt-0">
          <p class="text-muted-foreground text-base leading-relaxed">
            Continuous tracking of your business metrics with instant alerts when action is needed.
          </p>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # --- CTA Section ---
    st.markdown("""
    <div class="cta-section" style="margin-top: 4rem; text-align: center;">
        <h2 class="cta-title" style="font-size: 2.5rem; color: var(--gray-900); font-weight: 700;">
            Ready to Build Your<br>
            <span style="color: #ffffff;">Second Brain?</span>
        </h2>
        <p class="cta-subtitle" style="color: #475569; max-width: 700px; margin: 1rem auto;">
            Join forward-thinking businesses that have eliminated manual decision-making. 
            Start optimizing your operations with AI today.
        </p>
        <div class="hero-buttons" style="justify-content: center;">
            <a href="#" class="btn btn-primary">Start Free Trial →</a>
            <a href="#" class="btn btn-secondary">Schedule Demo</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
