# -*- coding: utf-8 -*-
"""Generates the static site for Milena Stanislavova (colour_blue template)."""
import os, re, shutil, sys

SRC = "/sessions/funny-wizardly-goodall/mnt"
OUT = "/sessions/funny-wizardly-goodall/mnt/outputs/MilenaStanislavovaAI"

WB18 = "https://web.archive.org/web/2018/http://www.math.ku.edu/~stanis/"
WB24 = "https://web.archive.org/web/2024/https://stanis.ku.edu/"

WBMAP = {
 "DIE.pdf": "20240615212258/https://stanis.ku.edu/DIE.pdf",
 "Math221Spring2018.html": "20240729050343/https://stanis.ku.edu/Math221Spring2018.html",
 "Math800Spring2020.html": "20240729053523/https://stanis.ku.edu/Math800Spring2020.html",
 "shortpulse_periodic_v10.pdf": "20240605190541/https://stanis.ku.edu/shortpulse_periodic_v10.pdf",
 "KS_AIMS.pdf": "20240729160751/https://stanis.ku.edu/~stanis/KS_AIMS.pdf",
 "PHYSD30722.pdf": "20240616091927/https://stanis.ku.edu/PHYSD30722.pdf",
 "ks_stefanov_stanislavova_JEE.pdf": "20240729071122/https://stanis.ku.edu/~stanis/ks_stefanov_stanislavova_JEE.pdf",
 "stability_standing_waves.pdf": "20240729165120/https://stanis.ku.edu/~stanis/stability_standing_waves.pdf",
 "JMathPhys_52_112703.pdf": "20240616075342/https://stanis.ku.edu/JMathPhys_52_112703.pdf",
 "KGZ_final.pdf": "20240415055420/https://stanis.ku.edu/~stanis/KGZ_final.pdf",
 "CMP.pdf": "20240729211939/https://stanis.ku.edu/~stanis/CMP.pdf",
 "BL_KG.pdf": "20240730042046/https://stanis.ku.edu/~stanis/BL_KG.pdf",
 "648_syllabus.pdf": "20240729134135/https://stanis.ku.edu/~stanis/648_syllabus.pdf",
 "765Fall16.html": "20180711231320/http://www.math.ku.edu:80/~stanis/765Fall16.html",
 "Applied%20PDE.html": "20180711231751/http://www.math.ku.edu:80/~stanis/Applied%20PDE.html",
 "439%20Anschutz%20SP14.xls": "20180324164544/http://www.math.ku.edu:80/~stanis/439%20Anschutz%20SP14.xls",
 "950hw1_F15.pdf": "20180324164549/http://www.math.ku.edu:80/~stanis/950hw1_F15.pdf",
 "950hw2_F15.pdf": "20180324164554/http://www.math.ku.edu:80/~stanis/950hw2_F15.pdf",
 "950hw3_F15.pdf": "20180324164559/http://www.math.ku.edu:80/~stanis/950hw3_F15.pdf",
 "950hw4_F15.pdf": "20180324164604/http://www.math.ku.edu:80/~stanis/950hw4_F15.pdf",
 "950hw5_F15.pdf": "20180324164611/http://www.math.ku.edu:80/~stanis/950hw5_F15.pdf",
 "Final_S14_Sample.pdf": "20180324164615/http://www.math.ku.edu:80/~stanis/Final_S14_Sample.pdf",
 "MakeupMidterm_S2011.pdf": "20180324164621/http://www.math.ku.edu:80/~stanis/MakeupMidterm_S2011.pdf",
 "Midterm_S2011.pdf": "20180324164626/http://www.math.ku.edu:80/~stanis/Midterm_S2011.pdf",
 "Quick_Start_Guide.pdf": "20180324164632/http://www.math.ku.edu:80/~stanis/Quick_Start_Guide.pdf",
 "121_class_meetings.pdf": "20180324164534/http://www.math.ku.edu:80/~stanis/121_class_meetings.pdf",
 "GT_ode.pdf": "20170808162601/http://www.math.ku.edu/%7Estanis/GT_ode.pdf",
}
def wb(name):
    return "https://web.archive.org/web/" + WBMAP[name] if name in WBMAP else WB18 + name

def fix_ku(html):
    def rep(m):
        return wb(m.group(2))
    html = re.sub(r'https?://(stanis\.ku\.edu/~stanis|(?:www\.)?math\.ku\.edu/~stanis|stanis\.ku\.edu)/([A-Za-z0-9_%.\-]+)', rep, html)
    return html

MENU = [("index.html", "Home"), ("CV.pdf", "Vita"), ("publications.html", "Publications"),
        ("grants.html", "Grants"), ("classes.html", "Classes"),
        ("conferences.html", "Conferences"), ("service.html", "Service"), ("news.html", "News")]

SIDEBAR = """
        <div align="center">
          <h3>Contact &amp; Links</h3>
          <div class="when"><img src="style/Milena_Stanislavova_1.jpg" width="250" height="195" alt="Milena Stanislavova"><br>
            <p>
              <a href="https://www.uab.edu/cas/mathematics/people/faculty-directory/milena-stanislavova">UAB Faculty Profile</a><br>
              <a href="https://mathscinet.ams.org/mathscinet/search/author.html?mrauthid=367464">MathSciNet</a><br>
              <a href="https://scholar.google.com/citations?user=Eqs80esAAAAJ&amp;hl=en&amp;oi=ao">Google Scholar</a><br>
              <a href="https://arxiv.org/search/?searchtype=author&amp;query=Stanislavova%2C+Milena">arXiv</a><br>
              <a href="https://orcid.org/0000-0002-7144-3613">ORCID</a><br>
            </p>
            <p><b><u>E-mail:</u></b><br>
              <a href="mailto:mstanisl@uab.edu">mstanisl@uab.edu</a></p>
            <p><b><u>Office:</u></b><br>
              University Hall, Room 4005</p>
            <p><b><u>Phone:</u></b><br>
              (205) 934-8641</p>
            <p><b><u>Mailing Address:</u></b><br>
              <a href="https://www.uab.edu/cas/mathematics/">Department of Mathematics</a><br>
              <a href="https://www.uab.edu/">University of Alabama at Birmingham</a><br>
              1402 10th Avenue South<br>
              Birmingham, AL 35294-1241</p>
          </div>
        </div>"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <title>{title}</title>
  <meta charset="utf-8">
  <meta name="description" content="Milena Stanislavova, Professor and Chair, Department of Mathematics, University of Alabama at Birmingham">
  <meta name="keywords" content="Milena Stanislavova, mathematics, partial differential equations, dynamical systems, stability of waves, UAB">
  <link rel="stylesheet" type="text/css" href="style/style.css" title="style">
</head>
<body>
  <div id="main">
    <div id="header">
      <div id="logo">
        <div id="logo_text">
          <h1><a href="index.html">Milena Stanislavova<span class="logo_colour"></span></a></h1>
          <h2>Professor and Chair, <a href="https://www.uab.edu/cas/mathematics/">Department of Mathematics</a></h2>
          <h2>University of Alabama at Birmingham</h2>
        </div>
      </div>
      <div id="menubar">
        <ul id="menu">
{menu}
        </ul>
      </div>
    </div>
    <div id="site_content">
      <div class="sidebar">{sidebar}
      </div>
      <div id="content">
{content}
      </div>
    </div>
    <div id="content_footer"></div>
    <div id="footer">
      Copyright &copy; Milena Stanislavova | <a href="http://www.html5webtemplates.co.uk">design from HTML5webtemplates.co.uk</a>
    </div>
  </div>
</body>
</html>
"""

def page(fname, title, content):
    menu = "\n".join('          <li%s><a href="%s">%s</a></li>' % (' class="selected"' if h == fname else "", h, t)
                     for h, t in MENU)
    html = PAGE.format(title=title, menu=menu, sidebar=SIDEBAR, content=content)
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)

# ---------------------------------------------------------------- HOME
HOME = """
        <h1>Professor Milena Stanislavova</h1>
        <p>Milena Stanislavova is a Professor of Mathematics and Chair of the
          <a href="https://www.uab.edu/cas/mathematics/">Department of Mathematics</a> at the
          University of Alabama at Birmingham (UAB). Before joining UAB in 2021, she was a faculty member
          at the University of Kansas (KU) from 2002 to 2021, where she served as Director of Graduate Studies
          in the Mathematics Department from 2012 to 2017 and as Chair of the Economics Department from 2017 to 2021.
          Professor Stanislavova received her M.S. in Mathematics from Sofia University in Bulgaria in 1993 and her
          Ph.D. from the University of Missouri in 2000. She was a Visiting Assistant Professor at the University of
          Massachusetts-Amherst before joining KU as Assistant Professor in 2002.</p>
        <p>Her major fields of study are Dynamical Systems and Partial Differential Equations. More specifically,
          she is investigating the stability and long time behavior of special solutions of nonlinear equations of
          mathematical physics. Stanislavova's research deals with a variety of problems concerning solutions of a
          large class of PDE's, which can be viewed as dynamical systems on an infinite-dimensional space.
          Hamiltonian PDE's support coherent structures like solitary or periodic traveling waves, as well as wave
          trains and multi-pulses. These are very important objects when modeling physical processes and their
          stability is essential in practical applications.</p>
        <p>Stanislavova has published in journals such as Nonlinearity, Journal of Nonlinear Science, Studies in
          Applied Math, Physica D, Communications in Math Physics, Mathematische Annalen, SIAM Journal of Applied Math,
          SIAM Journal on Applied Dynamical Systems, Journal of Math Physics, ZAMP, Proc. Roy. Soc. Edinburgh A,
          Journal of Evolution Equations, etc. Her research has been continuously funded by the National Science
          Foundation since 2004. She is a member of the Editorial Board of <i>Studies in Applied Mathematics</i>.
          She is the founder and co-organizer of the annual KUMUNU PDE conference and a co-organizer of the
          Joint Alabama-Florida (JAF) Conference on Differential Equations, Dynamical Systems and Applications.</p>
        <p>Stanislavova teaches undergraduate courses in differential equations, complex analysis and mathematical
          game theory, as well as graduate courses in analysis, dynamical systems and PDEs. At KU she was a faculty
          fellow in the Honors Program and developed a freshman seminar for honors students. She is the recipient of
          the Don and Pat Morrison Award for Excellence in Teaching Mathematics.</p>

        <h4>Research Interests</h4>
        <ul>
          <li><b>Partial Differential Equations:</b> Stability of Waves, Nonlinear Wave Equations</li>
          <li><b>Dynamical Systems:</b> Invariant Manifolds, Hamiltonian Systems, Control</li>
          <li><b>Analysis:</b> Semigroups of Linear Operators, Spectral Mapping Theorems</li>
        </ul>

        <h4>Education</h4>
        <ul>
          <li>2000, Ph.D., Department of Mathematics, University of Missouri, Columbia</li>
          <li>1993, M.S. in Mathematics, Sofia University, Sofia, Bulgaria</li>
        </ul>

        <h4>Professional Experience</h4>
        <ul>
          <li>2021-present, Professor, Department of Mathematics, University of Alabama at Birmingham</li>
          <li>2013-2021, Professor, Department of Mathematics, University of Kansas</li>
          <li>2007-2013, Associate Professor, Department of Mathematics, University of Kansas</li>
          <li>2002-2007, Assistant Professor, Department of Mathematics, University of Kansas</li>
          <li>2000-2002, Visiting Assistant Professor, University of Massachusetts-Amherst</li>
          <li>1996-2000, Graduate Teaching Assistant, University of Missouri-Columbia</li>
          <li>1994-1996, Researcher, Bulgarian Academy of Sciences</li>
        </ul>

        <h4>Administrative Experience</h4>
        <ul>
          <li>Chair, Department of Mathematics, UAB, 2021-present</li>
          <li>Chair, Department of Economics, KU, 2017-2021</li>
          <li>Director of Graduate Studies, KU Department of Mathematics, 2012-2017</li>
        </ul>

        <h4>Teaching Awards and Grants</h4>
        <ul>
          <li>2012, Don and Pat Morrison Award for Excellence in Teaching Mathematics</li>
          <li>2009, Faculty seminar grant from the Center for Teaching Excellence</li>
          <li>2005, Teaching Grant from the Center for Teaching Excellence</li>
          <li>2003, Center for Teaching Excellence Grant for the Best Practices Institute</li>
        </ul>
"""

# ---------------------------------------------------------------- PUBLICATIONS
AX = "https://arxiv.org/abs/"
DOI = "https://doi.org/"
LOC = "style/"

# (citation-before-title, title, citation-after-title, main_link, [extra (label,url)])
PUBS = [
 ("A. Stefanov, M. Stanislavova, J. Cuevas-Maraver, P.G. Kevrekidis,", "On a Klein-Gordon reduction for oscillons",
  "Journal of Nonlinear Waves, 2 (2026).", DOI+"10.1017/jnw.2026.10037",
  [("Open Access", DOI+"10.1017/jnw.2026.10037"), ("arXiv", AX+"2508.12142")]),
 ("M. Stanislavova, A. Stefanov,", "Asymptotic attraction with algebraic rates toward fronts of dispersive-diffusive Burgers equations",
  "Journal of Nonlinear Waves, 1, no. 7 (2025).", DOI+"10.1017/jnw.2025.10013",
  [("Open Access", DOI+"10.1017/jnw.2025.10013"), ("arXiv", AX+"2504.17745")]),
 ("S. Hakkaev, M. Stanislavova, A. Stefanov,", "On the spectral instability of some cnoidal and snoidal waves of the full Klein-Gordon-Zakharov system",
  "Dynamics of PDE, 22, no. 2 (2025), pp. 107-133.", DOI+"10.4310/dpde.250407211150",
  [("Journal", DOI+"10.4310/dpde.250407211150")]),
 ("S. Hakkaev, M. Stanislavova, A. Stefanov,", "Existence and stability for the traveling waves of the Benjamin equation",
  "Nonlinearity, 38 (2025), 025020 (33pp).", DOI+"10.1088/1361-6544/adabaa",
  [("Open Access", DOI+"10.1088/1361-6544/adabaa"), ("arXiv", AX+"2408.16715")]),
 ("S. Hakkaev, M. Stanislavova, A. Stefanov,", "Spectral stability of periodic waves for the Zakharov system",
  "J. Math. Phys. 64, no. 8 (2023).", AX+"2303.12778",
  [("arXiv", AX+"2303.12778"), ("Journal", DOI+"10.1063/5.0106133")]),
 ("M. Stanislavova, A. Stefanov,", "On the long time dynamics of the Landau-De Gennes gradient flow",
  "Journal of Statistical Physics, 190, no. 1 (2023).", DOI+"10.1007/s10955-022-03046-7",
  [("Journal", DOI+"10.1007/s10955-022-03046-7")]),
 ("S. Hakkaev, M. Stanislavova, A. Stefanov,", "On the stability of the periodic waves for the Benney system",
  "SIAM J. Appl. Dyn. Systems, 21, no. 3 (2022), pp. 1726-1747.", AX+"2204.01628",
  [("arXiv", AX+"2204.01628"), ("Journal", DOI+"10.1137/21M1461630")]),
 ("W. Feng, M. Stanislavova, A. Stefanov,", "On the Barashenkov-Bogdan-Zhanlav solitons and their stability",
  "Chaos, Solitons and Fractals, Vol. 152 (2021), 111467.", AX+"2004.10866",
  [("arXiv", AX+"2004.10866"), ("Journal", DOI+"10.1016/j.chaos.2021.111467")]),
 ("S. Hakkaev, M. Stanislavova, A. Stefanov,", "On the stability of periodic waves for the cubic derivative NLS and the quintic NLS",
  "Journal of Nonlinear Science, 31, no. 3 (2021).", AX+"2006.13658",
  [("arXiv", AX+"2006.13658"), ("Journal", DOI+"10.1007/s00332-021-09712-6")]),
 ("H. Gaebler, M. Stanislavova,", "NLS and KdV Hamiltonian linearized operators: bounds on the spectra and optimal L<sup>2</sup> estimates for the semigroups",
  "Physica D, Vol. 416 (2021), 132738.", LOC+"NLS_And_KDV_Hamiltonian.pdf",
  [("PDF", LOC+"NLS_And_KDV_Hamiltonian.pdf"), ("Journal", DOI+"10.1016/j.physd.2020.132738")]),
 ("M. Stanislavova, A. Stefanov,", "Ground states for the nonlinear Schr&ouml;dinger equation under a general trapping potential",
  "Journal of Evolution Equations, 21, no. 1 (2021), pp. 671-697.", AX+"2002.03822",
  [("arXiv", AX+"2002.03822"), ("Journal", DOI+"10.1007/s00028-020-00596-9")]),
 ("W. Feng, M. Stanislavova,", "On the spectral stability of standing waves of nonlocal PT-symmetric systems",
  "in: Mathematics of Wave Phenomena, Trends in Mathematics, Birkh&auml;user (2020), pp. 145-162.", DOI+"10.1007/978-3-030-47174-3_9",
  [("Journal", DOI+"10.1007/978-3-030-47174-3_9")]),
 ("S. Malhi, M. Stanislavova,", "On the energy decay rates for the 1D damped fractional Klein-Gordon equation",
  "Mathematische Nachrichten, 293, no. 2 (2020), pp. 363-375.", AX+"1809.09531",
  [("arXiv", AX+"1809.09531"), ("Journal", DOI+"10.1002/mana.201800417")]),
 ("S. Hakkaev, M. Stanislavova, A. Stefanov,", "On the generation of stable Kerr frequency combs in the Lugiato-Lefever model of periodic optical waveguides",
  "SIAM Journal of Applied Math, Vol. 79, No. 2 (2019), pp. 477-505.", AX+"1806.04821",
  [("arXiv", AX+"1806.04821"), ("Journal", DOI+"10.1137/18M1192767")]),
 ("A. Demirkaya, M. Stanislavova,", "Numerical results on existence and stability of standing and traveling waves for the fourth order beam equation",
  "DCDS-B, 24, no. 1 (2019), pp. 197-209.", DOI+"10.3934/dcdsb.2018097",
  [("Open Access", DOI+"10.3934/dcdsb.2018097"), ("PDF", LOC+"Numerical_Results_On_Existence.pdf")]),
 ("M. Stanislavova, A. Stefanov,", "Asymptotic stability for spectrally stable Lugiato-Lefever solutions in periodic waveguides",
  "Journal of Math Physics, 59, no. 10 (2018), 101502, 12pp.", DOI+"10.1063/1.5048017",
  [("Journal", DOI+"10.1063/1.5048017")]),
 ("S. Malhi, M. Stanislavova,", "When is the energy of the 1D damped Klein-Gordon equation decaying?",
  "Mathematische Annalen, v. 372, 3-4 (2018), pp. 1459-1479.", LOC+"Damped_Klein_Gordon.pdf",
  [("PDF", LOC+"Damped_Klein_Gordon.pdf"), ("Journal", DOI+"10.1007/s00208-018-1725-5")]),
 ("W. Feng, M. Stanislavova,", "On the vortices for the NLS in higher dimensions",
  "Phil. Trans. R. Soc. A, v. 376 (2018), 20170189.", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5869610/",
  [("Open Access (PMC)", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5869610/"), ("Journal", DOI+"10.1098/rsta.2017.0189")]),
 ("W. Feng, M. Stanislavova, A. Stefanov,", "On the spectral stability of ground states of semi-linear Schr&ouml;dinger and Klein-Gordon equations with fractional dispersion",
  "Communications in Pure and Appl. Analysis, 17, no. 4 (2018), pp. 1371-1385.", DOI+"10.3934/cpaa.2018067",
  [("Open Access", DOI+"10.3934/cpaa.2018067"), ("PDF", LOC+"On_the_spectral_stability_of_ground_states_of_semi.pdf")]),
 ("M. Stanislavova, A. Stefanov,", "On the stability of standing waves for PT symmetric Schr&ouml;dinger and Klein-Gordon equations in higher space dimensions",
  "Proceedings of the AMS, 145 (2017), pp. 5273-5285.", "https://www.ams.org/proc/2017-145-12/S0002-9939-2017-13746-0/S0002-9939-2017-13746-0.pdf",
  [("Open Access", "https://www.ams.org/proc/2017-145-12/S0002-9939-2017-13746-0/S0002-9939-2017-13746-0.pdf"), ("PDF", LOC+"PAMS_2017.pdf")]),
 ("S. Hakkaev, M. Stanislavova, A. Stefanov,", "Spectral stability for classical periodic waves of the Ostrovsky and short pulse models",
  "Studies in Applied Math, 139, no. 3 (2017), pp. 405-433.", AX+"1604.03024",
  [("arXiv", AX+"1604.03024"), ("Journal", DOI+"10.1111/sapm.12166")]),
 ("S. Hakkaev, M. Stanislavova, A. Stefanov,", "Periodic traveling waves of the regularized short pulse and Ostrovsky equations: existence and stability",
  "SIAM Journal of Math Analysis, 49, no. 1 (2017), pp. 674-698.", wb("shortpulse_periodic_v10.pdf"),
  [("PDF", wb("shortpulse_periodic_v10.pdf")), ("Journal", DOI+"10.1137/15M1037901")]),
 ("M. Stanislavova, A. Stefanov,", "On the spectral problem L u = &lambda; u' and applications",
  "Communications in Math Physics, v. 343, 2 (2016), pp. 361-391.", wb("CMP.pdf"), [("PDF", wb("CMP.pdf"))]),
 ("A. Demirkaya, P.G. Kevrekidis, M. Stanislavova, A. Stefanov,", "Spectral stability analysis for standing waves of a perturbed Klein-Gordon equation",
  "DCDS-A (2015), pp. 359-368.", AX+"1409.7095", [("arXiv", AX+"1409.7095")]),
 ("A. Demirkaya, S. Hakkaev, M. Stanislavova, A. Stefanov,", "On the spectral stability of periodic waves of the Klein-Gordon equation",
  "Diff. Int. Equations, V. 28, no. 5-6 (2015), pp. 431-454.", wb("DIE.pdf"), [("PDF", wb("DIE.pdf"))]),
 ("M. Stanislavova,", "Linear stability of solitary waves for the one-dimensional Benney-Luke and Klein-Gordon equations",
  "Studies in Applied Mathematics, v. 134, no. 1 (2015), pp. 1-23.", wb("BL_KG.pdf"), [("PDF", wb("BL_KG.pdf"))]),
 ("A. Demirkaya, T. Kapitula, P.G. Kevrekidis, M. Stanislavova, A. Stefanov,", "On the spectral stability of kinks in some PT-symmetric variants of the classical Klein-Gordon field theories",
  "Studies in Applied Mathematics, v. 133, 3 (2014), pp. 298-317.", AX+"1402.2942", [("arXiv", AX+"1402.2942")]),
 ("S. Hakkaev, M. Stanislavova, A. Stefanov,", "Linear stability analysis for periodic traveling waves of the Boussinesq equation and the KGZ system",
  "Proc. Roy. Soc. Edinburgh A, v. 144, no. 3 (2014), pp. 455-489.", AX+"1202.2133", [("arXiv", AX+"1202.2133")]),
 ("M. Stanislavova, A. Stefanov,", "Spectral stability analysis for special solutions of second order in time PDE's: the higher dimensional case",
  "Physica D, 262 (2013), pp. 1-13.", wb("stability_standing_waves.pdf"), [("PDF", wb("stability_standing_waves.pdf"))]),
 ("S. Hakkaev, M. Stanislavova, A. Stefanov,", "Spectral stability for traveling pulses of the Boussinesq 'abc' system",
  "SIAM J. Appl. Dyn. Systems, v. 12, 2 (2013), pp. 878-898.", AX+"1209.3666", [("arXiv", AX+"1209.3666")]),
 ("S. Hakkaev, M. Stanislavova, A. Stefanov,", "Orbital stability for periodic standing waves of the Klein-Gordon-Zakharov system and the beam equation",
  "ZAMP - Zeitschrift fuer Angewandte Mathematik und Physik, v. 64, 2 (2013), pp. 265-282.", wb("KGZ_final.pdf"), [("PDF", wb("KGZ_final.pdf"))]),
 ("M. Stanislavova, A. Stefanov,", "Linear stability analysis for traveling waves of second order in time PDEs",
  "Nonlinearity v. 25 (2012), pp. 2625-2654.", AX+"1108.2417", [("arXiv", AX+"1108.2417")]),
 ("S. Hakkaev, M. Stanislavova, A. Stefanov,", "Transverse instability for periodic waves of KP-I and Schr&ouml;dinger equations",
  "Indiana Univ. Math. J. v. 61 (2012), pp. 461-492.", AX+"1012.3065", [("arXiv", AX+"1012.3065")]),
 ("A. Demirkaya, M. Stanislavova,", "Conditional stability theorem for the one dimensional Klein-Gordon equation",
  "J. Math. Phys., 52 (2011).", wb("JMathPhys_52_112703.pdf"), [("PDF", wb("JMathPhys_52_112703.pdf"))]),
 ("M. Stanislavova, A. Stefanov,", "Asymptotic estimates and stability analysis of Kuramoto-Sivashinsky type models",
  "Journal of Evolution Equations, 11 (2011), no. 3, pp. 605-635; Erratum: J. Evol. Equ. 11 (2011), no. 3, pp. 637-639.",
  wb("ks_stefanov_stanislavova_JEE.pdf"), [("PDF", wb("ks_stefanov_stanislavova_JEE.pdf"))]),
 ("A. Demirkaya, M. Stanislavova,", "Long time behavior for radially symmetric solutions of the Kuramoto-Sivashinsky equation",
  "Dynamics of PDEs, v. 7, 2 (2010), pp. 161-175.", LOC+"Long_Time_Behavior_for_Radially_Symmetric_Solution.pdf",
  [("PDF", LOC+"Long_Time_Behavior_for_Radially_Symmetric_Solution.pdf")]),
 ("M. Stanislavova, A. Stefanov,", "Effective estimates of the higher Sobolev norms for the Kuramoto-Sivashinsky equation",
  "DCDS (2009), pp. 729-738.", wb("KS_AIMS.pdf"), [("PDF", wb("KS_AIMS.pdf")), ("arXiv", AX+"0711.4005")]),
 ("M. Stanislavova, A. Stefanov,", "On precise center stable manifold theorems for certain reaction-diffusion and Klein-Gordon equations",
  "Physica D: Nonlinear Phenomena 238 (2009), pp. 2298-2307.", wb("PHYSD30722.pdf"), [("PDF", wb("PHYSD30722.pdf"))]),
 ("M. Stanislavova,", "Diffraction managed solitons with zero-mean diffraction",
  "Journal of Dynamics and Differential Equations, 19 (2007), no. 2, pp. 295-307.", LOC+"Stanislavova2007_Article_DiffractionManagedSolitonsWith.pdf",
  [("PDF", LOC+"Stanislavova2007_Article_DiffractionManagedSolitonsWith.pdf")]),
 ("M. Stanislavova, A. Stefanov,", "Attractors for the viscous Camassa-Holm equation",
  "DCDS-A 18 (2007), pp. 159-186.", AX+"math/0612321", [("arXiv", AX+"math/0612321")]),
 ("M. Stanislavova,", "On the global attractor for the damped BBM equation",
  "Discrete and Continuous Dynamical Systems Suppl. Volume (2005), pp. 824-832.", LOC+"On_Global_Attractor_BBM.pdf",
  [("PDF", LOC+"On_Global_Attractor_BBM.pdf")]),
 ("M. Stanislavova, A. Stefanov, B. Wang,", "Asymptotic smoothing and attractors for the generalized Benjamin-Bona-Mahony equation on R<sup>3</sup>",
  "J. Diff. Eq. 219 (2005), no. 2, pp. 451-483.", LOC+"Asymptotic_Smoothing_BBM.pdf", [("PDF", LOC+"Asymptotic_Smoothing_BBM.pdf")]),
 ("M. Stanislavova,", "Regularity of ground state solutions of dispersion managed nonlinear Schr&ouml;dinger equations",
  "J. Diff. Eq., 210, 1 (2005), pp. 87-105.", LOC+"Regularity_Ground_States_DMNLS.pdf", [("PDF", LOC+"Regularity_Ground_States_DMNLS.pdf")]),
 ("M. Stanislavova, A. Stefanov,", "On global finite energy solutions of the Camassa-Holm equation",
  "Journal of Fourier Analysis and Applications 11 (2005), no. 5, pp. 511-531.", LOC+"On_Global_Finite_Energy_Solutions_of_the_Camassa-H.pdf",
  [("PDF", LOC+"On_Global_Finite_Energy_Solutions_of_the_Camassa-H.pdf")]),
 ("Y. Latushkin, C. Li, M. Stanislavova,", "The spectrum of a linearized 2D-Euler operator",
  "Studies in Applied Mathematics, 112 (2004), pp. 259-270.", AX+"math/0107125", [("arXiv", AX+"math/0107125")]),
 ("F. Gesztesy, C.K.R.T. Jones, Y. Latushkin, M. Stanislavova,", "A spectral mapping theorem and invariant manifolds for nonlinear Schr&ouml;dinger equations",
  "Indiana Univ. Math. J., 49 (2000), pp. 221-243.", AX+"solv-int/9907017", [("arXiv", AX+"solv-int/9907017")]),
 ("M. Konstantinov, M. Stanislavova, P. Petkov,", "Perturbation bounds and characterization of the solution of the associated algebraic Riccati equation",
  "Linear Algebra and its Applications, 285 (1998), pp. 7-31.", LOC+"Perturbation_Bounds.pdf", [("PDF", LOC+"Perturbation_Bounds.pdf")]),
 ("M. Stanislavova, A. Zhivkov,", "On the dynamics of the four dimensional rigid body in a quadratic potential field",
  "J. Math. Phys. 36 (1995), pp. 5760-5788.", DOI+"10.1063/1.531285", [("Journal", DOI+"10.1063/1.531285")]),
]

def pubs_html():
    out = ['        <h1>Publications</h1>',
           '        <p>Links point to an open-access or arXiv version whenever one is available; '
           'otherwise to the journal (DOI) page.</p>',
           '        <ul>']
    for auth, title, cite, main, extra in PUBS:
        tags = " ".join('[<a href="%s">%s</a>]' % (u, l) for l, u in extra)
        out.append('          <li>%s <a href="%s">%s</a>, %s %s</li>' % (auth, main, title, cite, tags))
    out.append('        </ul>')
    return "\n".join(out)

# ---------------------------------------------------------------- GRANTS
GRANTS = [
 "2025, NSF DMS-2447687 Third Joint Alabama-Florida (JAF) Conference on Differential Equations, Dynamical Systems and Applications ($41,600)",
 "2021-2026, NSF DMS-2108285 Infinite-Dimensional Dynamical Systems - Stability and Long-Time Behavior ($197,000)",
 "2015-2019, NSF DMS-1516245 Stability and Long-Time Behavior for Infinite-Dimensional Dynamical Systems ($195,000)",
 "2018, NSF DMS-1753332 KUMUNU PDE Conference Proposal ($17,500)",
 "2017, IMA funding ($3,500) for KUMUNU PDE Conference, April 2018",
 "2012-2016, NSF DMS-1211315 Linear and Nonlinear Stability for Infinite-Dimensional Dynamical Systems ($215,157)",
 "2015, NSF DMS-1500607 KUMU PDE Conference Proposal ($15,500)",
 "2015, IMA funding ($4,500) for KUMU PDE Conference, April 2015, co-PI M. Johnson",
 "2008-2012, NSF DMS-0807894 Long-Time Behavior and Stability of Infinite-Dimensional Dynamical Systems ($141,199)",
 "2005-2008, NSF DMS-0508184 Stability and Long-Time Behavior of Hamiltonian Partial Differential Equations ($116,181)",
 "2004-2005, NSF First Award EPS-0236913 Analytical Studies of Regularity and Stability of Hamiltonian PDE's ($72,750)",
 "2003, KUCR NFGRF-2301720 Infinite-Dimensional Hamiltonian Systems and Stability of Special Solutions with Applications in Nonlinear Optics ($7,995)",
]
ADD_FUND = [
 "2011, Support from the IMA, Minneapolis, to participate in the &ldquo;Invariant Objects in Dynamical Systems&rdquo; short course (invitation only)",
 "2003, Support from the IMA, Minneapolis, to participate in the New Directions Short Course on Math Biology (invitation only)",
 "2002, Association for Women in Mathematics Travel Grant",
 "2000-2001, Faculty Research Travel Grant, University of Massachusetts",
 "1996-2000, Doctoral Fellowship, University of Missouri-Columbia",
 "1994-1996, Research grant of the Bulgarian Government, co-PI",
 "1988-1993, State scholarship for excellence in academic work, Sofia University",
]
def ul(items, sep=False):
    return "        <ul>\n" + "\n".join("          <li>%s</li>" % i for i in items) + "\n        </ul>"

GRANTS_HTML = ("        <h1>Research &amp; Conference Grants</h1>\n" + ul(GRANTS) +
               "\n        <h4>Additional Research Funding</h4>\n" + ul(ADD_FUND))

# ---------------------------------------------------------------- CLASSES
CLASSES = """
        <h1>Classes</h1>
        <h4>Courses Taught at UAB:</h4>
        <p></p>
        <h5><b>MA 650 - Differential Equations</b></h5>
        <p></p>
        <h5><b>MA 252 - Introduction to Differential Equations</b></h5>
        <p></p>
        <h5><b>MA 419 - Game Theory</b></h5>
        <p></p>
        <h4>Previously Taught at KU (with course pages):</h4>
        <p></p>
        <h5><a href="math121.html"><b>Math 121 - Calculus I</b></a></h5>
        <p><b>Course Description:</b></p>
        <p>This is a first course in differentiation and integration of algebraic and
          trigonometric functions with applications to physical sciences and engineering.</p>
        <h5><a href="{w221}"><b>Math 221 - Honors Applied Differential Equations</b></a></h5>
        <p><b>Course Description:</b></p>
        <p>Topics include first and second order ordinary differential equations and models, higher order equations,
          Laplace transforms, and systems of linear equations.</p>
        <h5><a href="{w647}"><b>Math 647 - Applied Partial Differential Equations</b></a></h5>
        <p><b>Course Description:</b></p>
        <p>Boundary value problems; topics on partial differentiation; theory of characteristic curves; partial
          differential equations of mathematical physics.</p>
        <h5><a href="{w648}"><b>Math 648 - Calculus of Variations and Integral Equations</b></a></h5>
        <p><b>Course Description:</b></p>
        <p>Topics in the calculus of variations, integral equations and applications.</p>
        <h5><a href="{w765}"><b>Math 765 - Mathematical Analysis I</b></a></h5>
        <p><b>Course Description:</b></p>
        <p>Math 765 and Math 766 are theoretical courses on the fundamental concepts of analysis and the methods of
          proof. These two courses include the concept of a real number; limits, continuity, and uniform convergence;
          and derivatives and integrals of functions of one and of several real variables.</p>
        <h5><a href="{w800}"><b>Math 800 - Complex Analysis I</b></a></h5>
        <p><b>Course Description:</b></p>
        <p>Complex numbers and functions; complex differential operators; Cauchy-Riemann equations; analytic and
          harmonic functions; Cauchy formula; power series representation of analytic functions; Liouville's theorem;
          zeros of analytic functions; Laurent series and meromorphic functions; argument principle, the residue
          theorem and applications; counting zeros and poles of meromorphic functions; maximum modulus principle and
          Schwarz lemma; Riemann mapping theorem.</p>
        <h5><a href="math850.html"><b>Math 850 - Differential Equations and Dynamical Systems</b></a></h5>
        <p><b>Course Description:</b></p>
        <p>Discrete and differentiable dynamical systems with an emphasis on the qualitative theory. Topics include
          review of linear systems, existence and uniqueness theorems, flows and discrete dynamical systems,
          linearization (Hartman-Grobman theorem), stable and unstable manifolds, Poincar&eacute; sections, normal forms,
          Hamiltonian systems, and an introduction to bifurcation theory and chaos.</p>
        <h5><a href="math950.html"><b>Math 950 - Partial Differential Equations</b></a></h5>
        <p><b>Course Description:</b></p>
        <p>Introduction; equations of mathematical physics; classification of linear equations and systems. Existence
          and uniqueness problems for elliptic, parabolic, and hyperbolic equations. Eigenvalue problems for elliptic
          operators; numerical methods.</p>
        <h4>All Courses Taught at KU:</h4>
        <ul>
          <li>Math 115, 116 Applied Calculus I, II</li>
          <li>Math 125, 126 Calculus I, II</li>
          <li>Math 143 Honors Multivariable Calculus</li>
          <li>Math 177 First Year Seminar</li>
          <li>Honors 195 Honors Seminar</li>
          <li>Math 220 Applied ODEs</li>
          <li>Math 221 Honors ODEs</li>
          <li>Math 290 Linear Algebra</li>
          <li>Math 320 Differential Equations</li>
          <li>Math 647 Applied PDEs</li>
          <li>Math 648 Calculus of Variations and Integral Equations</li>
          <li>Math 765 Real Analysis I</li>
          <li>Math 800 Complex Analysis</li>
          <li>Math 850 Advanced ODEs and Dynamical Systems</li>
          <li>Math 851 Spectral Theory and Stability</li>
          <li>Math 950 Advanced PDEs</li>
        </ul>
        <p><i>Links to KU course pages point to archived copies on the Internet Archive.</i></p>
""".format(w221=wb("Math221Spring2018.html"), w647=wb("Applied%20PDE.html"), w648=wb("648_syllabus.pdf"), w765=wb("765Fall16.html"), w800=wb("Math800Spring2020.html"))

# ---------------------------------------------------------------- CONFERENCES
TALKS = """Invited Talk, Fifth International Conference &ldquo;Mathematics Days in Sofia&rdquo;, Sofia, Bulgaria, July 6-10, 2026
Invited Talk, SIAM Conference on Analysis of Partial Differential Equations (PD25), Pittsburgh, Pennsylvania, November 17-20, 2025
Invited Talk, SIAM Conference on Applications of Dynamical Systems (DS25), Denver, Colorado, May 11-15, 2025
Invited Talk, The Thirteenth International Conference on Nonlinear Evolution Equations and Wave Phenomena: Computation and Theory, Athens, GA, April 14-16, 2025
Invited Talk, AMS Sectional Meeting, Special Session &ldquo;Analysis on Nonlinear Wave Models&rdquo;, Lawrence, KS, March 29-30, 2025
Invited Talk, SIAM Conference on Nonlinear Waves and Coherent Structures, Session on &ldquo;Advances in Stability Analysis for Nonlinear Waves&rdquo;, Baltimore, June 24-27, 2024
Invited Talk, KUMUNU PDE Conference, University of Kansas, Lawrence, KS, April 5-7, 2024
Invited Talk, Session &ldquo;Theory of Nonlinear Waves&rdquo;, Spring AMS Sectional Meeting, Florida State University, Tallahassee, FL, March 23-24, 2024
Plenary Talk, The 49th Annual Mathematics Conference, Department of Mathematics, Miami University, Oxford, Ohio, September 29-30, 2023
Invited Talk, Mathematics Days in Sofia 2023 (MDS 2023), Sofia, Bulgaria, July 10-14, 2023
Invited Talk, Session &ldquo;Geometric methods in spectral theory of traveling waves and patterns&rdquo;, 13th AIMS Conference, Wilmington, NC, May 31 - June 5, 2023
Invited Colloquium Talk, University of Memphis, October 28, 2022
Invited Talk, AMS Fall Southeastern Sectional Meeting, Special Session on &ldquo;Deterministic and Stochastic PDEs: Theoretical and Numerical Analyses&rdquo;, University of Tennessee at Chattanooga, October 2022
Invited Talk, BIRS Workshop &ldquo;Mathematical aspects of the physics with non-self-adjoint operators&rdquo;, Banff, Canada, July 2022
Invited Talk, 12th IMACS International Conference on Nonlinear Evolution Equations and Wave Phenomena: Computation and Theory, Athens, GA, April 2022
Invited Talk, Conference on Mathematics of Wave Phenomena, Special Session on &ldquo;The Stability of Nonlinear Waves&rdquo;, Karlsruhe, Germany (virtual), February 14-18, 2022
Invited Talk, AMS Fall Central Sectional Meeting, Special Session on Progress in Nonlinear Waves, virtual, October 9-10, 2021
Invited Talk, IFIP TC7 Conference on System Modeling and Optimization, Special Session on &ldquo;Qualitative and quantitative analysis of nonlinear evolutionary partial differential equations&rdquo;, virtual, September 1-3, 2021
Invited Talk, SIAM Conference on Applications of Dynamical Systems, virtual, May 23-27, 2021
Invited Talk, Session on &ldquo;Existence and stability of nonlinear waves&rdquo;, ICIAM, Valencia, Spain, July 15-19, 2019
Invited Talk, Session on &ldquo;Stability of nonlinear waves and coherent structures&rdquo;, Equadiff 2019, Leiden, July 8-12, 2019
Invited Talk, 11th IMACS International Conference on Nonlinear Evolution Equations and Wave Phenomena: Computation and Theory, Athens, GA, April 2019
Invited Speaker, Midwest PDE Conference, Bloomington, Indiana, March 30-31, 2019
Invited Talk, Special Session on Mathematical Analysis and Control Theory of Coupled Partial Differential Equation Models, AMS Spring Southeastern Sectional Meeting, Auburn, Alabama, March 2019
Invited Speaker, SIAM Conference on Nonlinear Waves and Coherent Structures, Special Session on Existence and Stability of Traveling Waves, Orange County, June 2018
Invited Speaker, Special Session on Nonlinear Waves and Patterns, AMS Sectional Meeting, Ohio State University, March 2018
Invited Speaker, International Conference &ldquo;Mathematics Days in Sofia&rdquo;, Differential Equations and Mathematical Physics section, Sofia, Bulgaria, July 2017
&ldquo;Geometrical Methods, Non Self-adjoint Spectral Problems, and Stability of Periodic Structures&rdquo; workshop, BIRS, Oaxaca, Mexico, June 2017
Invited Talk, Special Session on &ldquo;Recent Advances on Traveling Waves in Systems of Partial Differential Equations&rdquo;, SIAM Conference on Applications of Dynamical Systems, Snowbird, Utah, May 2017
Invited Talk, Special Session on &ldquo;Nonlinear waves: analysis and computation&rdquo;, AMS Sectional Meeting, College of Charleston, Charleston, SC, March 10-12, 2017
Invited Talk, Special Session on &ldquo;Problems in Partial Differential Equations&rdquo;, Joint Mathematics Meetings, Atlanta, January 4-7, 2017
Invited Talk, Special Session on &ldquo;Existence and Stability of Nonlinear Waves and Patterns&rdquo;, SIAM Conference on Nonlinear Waves and Coherent Structures (NWCS16), Philadelphia, August 8-11, 2016
Invited Talk, Special Session on &ldquo;Evolution of Partial Differential Equations and their Control&rdquo;, Spring Eastern Sectional Meeting, SUNY Stony Brook, NY, March 2016
Invited Talk, Special Session on &ldquo;Recent Developments in Dispersive Partial Differential Equations and Harmonic Analysis&rdquo;, Joint Mathematics Meetings, Seattle, Washington, January 6-9, 2016
Invited Talk, Special Session on &ldquo;Spectral methods in Stability of Traveling Waves&rdquo;, 9th IMACS International Conference on Nonlinear Evolution Equations and Wave Phenomena: Computation and Theory, The University of Georgia, Athens, April 2015
Invited Talk, Mini-symposium on &ldquo;Spectral and geometric methods in stability of waves and patterns&rdquo;, SIAM Conference on Nonlinear Waves and Coherent Structures, University of Cambridge, UK, August 11-14, 2014
Invited Talk, 10th AIMS Conference on Dynamical Systems, Differential Equations and Applications, Madrid, July 7-11, 2014
Invited Talk, &ldquo;Stability of solitary waves&rdquo; workshop, De Giorgi Center, Scuola Normale Superiore, Pisa, May 24-31, 2014
Invited Talk, SIAM Conference on Analysis of PDEs, Lake Buena Vista, Florida, December 2013
Invited Talk, Special Session &ldquo;Existence and stability of traveling wave solutions&rdquo;, SIAM Conference on Applications of Dynamical Systems, Snowbird, UT, May 2013
Invited Talk, AMS Meeting, University of Iowa, April 2013
Invited Talk, Special Session on &ldquo;Nonlinear Evolution Equations&rdquo;, Joint Mathematics Meetings, San Diego, January 9-12, 2013
Invited Talk, Special Session on &ldquo;Traveling Waves&rdquo;, AMS Central Section Meeting, University of Akron, Akron, OH, October 20-21, 2012
Invited Talk, 38th International Conference &ldquo;Applications of Mathematics in Engineering and Economics&rdquo; (AMEE'12), Sozopol, Bulgaria, June 8-13, 2012
&ldquo;Linear Stability Analysis for Periodic Traveling Waves of the Boussinesq Equation and the KGZ System&rdquo;, AMS Sectional Meeting, University of Kansas, Lawrence, March 2012
Invited Talk, &ldquo;Geometric Methods for Infinite-Dimensional Dynamical Systems&rdquo; conference, Brown University, November 4-6, 2011
Invited Talk, AMS Sectional Meeting, University of Nebraska, October 2011
Invited Talk, Special Session on &ldquo;Nonlinear Waves&rdquo;, SIAM Conference on Applications of Dynamical Systems, Snowbird, UT, May 2011
Invited Talk, 7th IMACS Conference on Nonlinear Evolution Equations and Wave Phenomena: Computation and Theory, The University of Georgia, Athens, April 2011
Invited Talk, SIAM Conference on Nonlinear Waves and Coherent Structures (NW10), Philadelphia, August 16-19, 2010
Invited Talk, 36th International Conference &ldquo;Applications of Mathematics in Engineering and Economics&rdquo; (AMEE'10), Sozopol, Bulgaria, June 5-10, 2010
Special Session Talk, Joint SIAM/RSME-SCM-SEMA Meeting &ldquo;Emerging Topics in Dynamical Systems and Partial Differential Equations&rdquo; (DSPDEs), Barcelona, Spain, 2010
Invited Talk, Conference on &ldquo;Harmonic Analysis and PDEs&rdquo;, University of Nebraska-Lincoln, April 17-18, 2010
Invited Talk, First Oklahoma PDE Workshop, Oklahoma State University, November 21-22, 2009
Invited Participant, BIRS Workshop &ldquo;Analysis of nonlinear wave equations and applications in engineering&rdquo;, Banff, Alberta, Canada, August 2009
&ldquo;On precise center stable manifold theorems for reaction diffusion equations&rdquo;, 6th IMACS International Conference on Nonlinear Evolution Equations and Wave Phenomena: Computation and Theory, The University of Georgia, Athens, March 2009
&ldquo;On the Kuramoto-Sivashinsky equation in R<sup>1</sup> and R<sup>2</sup>: effective estimates of the high-frequency tails&rdquo;, Special Session on Long time behavior for Hamiltonian and dissipative systems, 7th AIMS Conference, University of Texas, Arlington, May 2008
&ldquo;Applications of Discrete and Continuous Nonlinear Schr&ouml;dinger Equations&rdquo;, Pioneers of Bulgarian Mathematics International Conference, Section on Dynamical Systems, Sofia, Bulgaria, July 2006
&ldquo;Attractors for evolution equations - a Fourier-Analytic Approach&rdquo;, Dynamical Systems Weekend, Columbia, MO, May 2006
&ldquo;Recent Developments in Applications of Discrete and Continuous Nonlinear Schr&ouml;dinger Equations in Nonlinear Optics&rdquo;, Kansas Center for Advanced Scientific Computing, KU, April 2006
&ldquo;Attractors for the viscous Camassa-Holm equation&rdquo;, AMS Sectional Meeting, Special Session on Analysis and Geometry of Non-linear Evolution Equations, University of Notre Dame, April 2006
&ldquo;Diffraction Managed Nonlinear Schr&ouml;dinger equation, localization and ground states&rdquo;, PASI 2005, Workshop on Differential Equations and Nonlinear Analysis, Santiago, Chile, January 2005
&ldquo;On the Global Attractor for the Damped Benjamin-Bona-Mahony Equation&rdquo;, Special Session on Dynamical Systems and Applications, Fifth AIMS Conference, California State Polytechnic University, Pomona, June 2004
&ldquo;The Dispersion Managed Nonlinear Schr&ouml;dinger Equation in one and two dimensions&rdquo;, AMS Sectional Meeting, Special Session on Current Topics in Optical Communication Systems, University of North Carolina, October 2003
&ldquo;Regularity of Ground States for DMNLS&rdquo;, SIAM Conference on Applications of Dynamical Systems, Snowbird, UT, May 2003
&ldquo;Time-smoothing Techniques and Applications to the Camassa-Holm Equation&rdquo;, SIAM 50th Annual Meeting, Philadelphia, July 2002
&ldquo;Stability of Evolution Equations&rdquo;, University of New Mexico, February 2002
&ldquo;Global Well-Posedness for the Camassa-Holm Equation in the Energy Norm&rdquo;, SEARCDE, Wake Forest University, November 2001
&ldquo;Spectral Mapping Theorem for the 2D Euler Equation&rdquo;, Dynamical Systems Seminar, Georgia Institute of Technology, April 2001
&ldquo;Invariant Manifolds and Spectral Mapping Theorems&rdquo;, AMS Meeting, Special Session on Semigroups and Evolution Equations, March 2001
&ldquo;Spectral Mapping Theorem for the 2D Euler Equation&rdquo;, Southeastern-Atlantic Regional Conference on Differential Equations, Virginia Tech, October 2000
&ldquo;Spectral Theory for Perturbed Semigroups&rdquo;, International Conference on Spectral Theory and Asymptotic Behavior of Semigroups, Blaubeuren, Germany, June 1999
&ldquo;Dynamics of the four-dimensional rigid body in a quadratic potential field&rdquo;, International Conference on Differential Equations and Mathematical Physics, University of Alabama at Birmingham, March 1999
&ldquo;Spectral Mapping Theorem for the Nonlinear Schr&ouml;dinger Equation&rdquo;, Brown University, November 1998
&ldquo;Invariant Manifolds for the Nonlinear Schr&ouml;dinger Equation&rdquo;, Southeastern-Atlantic Regional Conference on Differential Equations, Auburn University, October 1998
&ldquo;Perturbation Bounds for the Associated Algebraic Riccati Equation&rdquo;, International Conference on Differential Equations, Varna, Bulgaria, August 1995""".split("\n")

CONF = """
        <h1>Conferences</h1>
        <h4>Joint Alabama-Florida (JAF) Conference on Differential Equations, Dynamical Systems and Applications (co-organizer):</h4>
        <ul>
          <li><a href="https://case.fiu.edu/mathstat/news-events/may-26-conference/">4th JAF Conference - Florida International University, Miami, FL, May 2026</a></li>
          <li><a href="https://www.uab.edu/cas/mathematics/events/past-conferences/third-joint-alabama-florida-conference-on-differential-equations-dynamical-systems-and-applications">3rd JAF Conference - University of Alabama at Birmingham, Birmingham, AL, May 20-22, 2025</a></li>
          <li><a href="https://artsandsciences.fsu.edu/galleries/gallery-second-joint-alabama-florida-conference-differential-equations-dynamical-systems">2nd JAF Conference - Florida State University, Tallahassee, FL, May 17-19, 2024</a></li>
          <li><a href="https://www.auburn.edu/cosam/al_fl_differential_conference/index.htm">1st JAF Conference - Auburn University, Auburn, AL, May 13-14, 2023</a></li>
        </ul>
        <h4>KUMUNU PDE, Dynamical Systems and Applications Conference (founder and co-organizer, 2015-2021):</h4>
        <ul>
          <li><a href="https://www.math.unl.edu/kumunu-2020">KUMUNU-ISU PDE Conference - Lincoln, NE, 2021</a></li>
          <li><a href="https://faculty.missouri.edu/~walshsa/kumunu2019/">5th KUMUNU PDE Conference - Columbia, MO, April 27-28, 2019</a></li>
          <li><a href="http://kumunu2018pde.ku.edu/">4th KUMUNU PDE Conference - Lawrence, KS, April 21-22, 2018</a></li>
          <li><a href="http://www.math.unl.edu/events/special/kumunu2017">3rd KUMUNU PDE Conference - Lincoln, NE, April 21-23, 2017</a></li>
          <li><a href="http://faculty.missouri.edu/~walshsa/kumu2016/">2nd KUMU PDE Conference - Columbia, MO, April 23-24, 2016</a></li>
          <li><a href="http://www.dept.ku.edu/~math/conferences/2015/KUMUPDE/">1st KUMU PDE Conference - Lawrence, KS, April 18-19, 2015</a></li>
        </ul>
        <h4>Other Sessions Organized:</h4>
        <ul>
          <li>Special session &ldquo;Progress in Nonlinear Waves&rdquo;, Mathematics Days in Sofia, July 10-14, 2023</li>
          <li>Special session, AMS Sectional Meeting, University of Kansas, March 2012</li>
          <li>Special session on Linear and Nonlinear Stability of Coherent Structures, Eighth AIMS Conference, Dresden, Germany, May 2010</li>
          <li>Special session on Long Time Behavior for Hamiltonian and Dissipative Systems, Seventh AIMS Conference, University of Texas, Arlington, May 2008</li>
          <li>Mini-symposium, SIAM Conference on Applications of Dynamical Systems, Snowbird, UT, May 2005</li>
          <li>Mini-symposium, SIAM Conference on Applications of Dynamical Systems, Snowbird, UT, May 2003</li>
        </ul>
        <h1>Invited Talks</h1>
""" + ul(TALKS)

# ---------------------------------------------------------------- SERVICE
SERVICE = """
        <h1>Service &amp; Mentoring</h1>
        <h4>Postdoctoral Fellows and Graduate Students Supervised:</h4>
        <ul>
          <li>Anna Ghazaryan, postdoc 2008-2010; now Professor and Chair, Miami University, Ohio</li>
          <li>Harrison Gaebler, Ph.D. 2021; University of Oklahoma</li>
          <li>Satbir Malhi, Ph.D. 2019; Franklin and Marshall College</li>
          <li>Wen Feng, Ph.D. 2018; Sam Houston State University</li>
          <li>Aslihan Demirkaya, Ph.D. 2011; Amazon</li>
          <li>Weinan Wang, M.A. 2014; Assistant Professor, University of Oklahoma</li>
          <li>Ayse Esen, M.A. 2012</li>
        </ul>
        <h4>Scholarly Service:</h4>
        <ul>
          <li>Member of the Editorial Board, <a href="https://onlinelibrary.wiley.com/journal/14679590">Studies in Applied Mathematics</a>, 2020-present</li>
          <li>Co-organizer, Joint Alabama-Florida (JAF) Conference in Differential Equations and Dynamical Systems: 2023 at Auburn University, 2024 at Florida State University, 2025 at UAB, 2026 at Florida International University</li>
          <li>NSF grant-review panels in Applied Mathematics, NSF Postdoctoral Research Fellowships and Graduate Research Fellowships, 2009, 2010, 2012, 2016, 2022, 2024</li>
          <li>Co-organizer, Mathematics Days in Sofia 2023, special session &ldquo;Progress in Nonlinear Waves&rdquo;, July 10-14, 2023</li>
          <li>Member of the selection committee for the Martin Kruskal Prize, SIAM Activity Group on Nonlinear Waves and Coherent Structures, 2020</li>
          <li>Co-organizer and founder, KUMUNU PDE, Dynamical Systems and Applications Conference, 2015-2021</li>
          <li>Member of the selection committee for the Crawford Prize, SIAM Activity Group on Dynamical Systems, 2013</li>
          <li>Guest editor, Discrete and Continuous Dynamical Systems - Series S, Vol. 5, 5</li>
          <li>Referee for Proceedings of the AMS, SIAM Journal of Math Analysis, Proceedings of the Royal Society A, Nonlinearity, Applied Mathematics Letters, Dynamics of PDE, Communications on Pure and Applied Analysis, ADMA, International Journal of Mathematics and Mathematical Sciences, JMAA, AMS Contemporary Mathematics, Journal of Applied Mathematics and Stochastic Analysis, Annali di Matematica Pura ed Applicata</li>
          <li>Reviewer for Mathematical Reviews</li>
        </ul>
        <h4>College and University Service, UAB:</h4>
        <ul>
          <li>Chair, Department of Mathematics, 2021-present</li>
          <li>Member of the CAS working group on NTE faculty</li>
        </ul>
        <h4>College and University Service, KU:</h4>
        <ul>
          <li>Chair, Department of Economics, 2017-2021</li>
          <li>Honors Program Faculty Fellow, 2020-2021</li>
          <li>Executive Council of Graduate Studies member, 2015-2018</li>
          <li>Senior Administrative Fellows Program, AY 2016-2017</li>
          <li>Self Fellowship Faculty Evaluation Committee, 2017-2020</li>
          <li>Graduate Studies Departmental Scholarships Committee, 2016-2021</li>
          <li>University Committee on Sabbatical Leaves, 2014-2017</li>
          <li>College Committee on Graduate Studies, 2012-2015, chair in AY 13-14</li>
          <li>First Year Seminar Proposal Review Committee, 2014</li>
          <li>Documenting and Advancing Learning Faculty Seminar, CTE, 2012-2014</li>
          <li>First Year Seminar steering committee member, AY 11-12</li>
          <li>Member of Faculty Senate, 2009-2012</li>
        </ul>
        <h4>Departmental Service, KU Mathematics Department:</h4>
        <ul>
          <li>Director of Graduate Studies, Spring 2012-2017</li>
          <li>Faculty Advisor of Graduate Student Organization, Spring 2012-2017</li>
          <li>Admissions Director of Graduate Studies, 2010-2012</li>
          <li>Coordinator responsible for scholarship requirements, 2011-2017</li>
          <li>Analysis qualifying examinations, 2002-2017</li>
          <li>P&amp;T Committee Member, Fall 2014 and Fall 2020</li>
          <li>Member of the self-study committee, 2016</li>
          <li>Member of the Executive Committee, 2009-2010 and Spring 2014</li>
          <li>Sabbatical Committee, Fall 2013</li>
          <li>Wells-Morrison Committee, 2012-2014</li>
          <li>Chair Search Committee, 2011-2012</li>
          <li>Long Range Planning Committee, 2003-2004 and 2011-2012</li>
          <li>Member of the Outreach Committee, 2008-2010</li>
          <li>Chair of the Elementary Algebra Courses Committee, 2006-2010</li>
          <li>Member of the Lower Division of the Undergraduate Committee, 2002-2010</li>
          <li>Colloquium Co-chair, 2002-2007</li>
          <li>Ambassador for the Center for Teaching Excellence, 2004-2007</li>
        </ul>
        <h4>Outreach:</h4>
        <ul>
          <li>International Math Kangaroo competition for K-12 students, 2007-present</li>
          <li>KU Mini-Math Club for Elementary School students, 2014-2015</li>
        </ul>
        <h4>Graduate Examination Committees:</h4>
        <ul>
          <li>Dissertation committees: Wesley Perkins; Jingxian Hu (Economics); Ayse Esen (School of Education); Xi Li; Minji Zhang; Tim Dorn; Andrew Monaco (Economics)</li>
          <li>Prelim committees: Connor Smith; Kyle Claassen; Mohamed Badawy</li>
          <li>Master's committees: Joel Klipfel; Melinda Montgomery; Michael Bateman</li>
        </ul>
"""

# ---------------------------------------------------------------- NEWS
NEWS = """
        <h1>News</h1>
        <ul>
          <li><a href="https://case.fiu.edu/mathstat/news-events/may-26-conference/jaf-recap/">Recap of the 2026 JAF Conference at Florida International University</a></li>
          <li><a href="https://www.uab.edu/cas/mathematics/events/past-conferences/third-joint-alabama-florida-conference-on-differential-equations-dynamical-systems-and-applications">UAB hosts the Third Joint Alabama-Florida Conference, May 2025</a></li>
          <li><a href="https://www.uab.edu/cas/news/announcements/milena-stanislavova-named-chair-uab-mathematics">Stanislavova selected to lead UAB Department of Mathematics</a></li>
          <li><a href="https://honors.ku.edu/honors-program-welcomes-new-faculty-fellows-fall-2020">KU Honors Faculty Fellow, 2020</a></li>
          <li><a href="https://mathematics.ku.edu/milena-stanislavovas-and-atanas-stefanovs-recent-paper-featured-cover-journal">Recent Paper Featured on a Journal Cover</a></li>
          <li><a href="https://cte.ku.edu/portfolios/stanislavova2010">CTE Teaching Portfolio</a></li>
        </ul>
"""

def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree(os.path.join(SRC, "style"), os.path.join(OUT, "style"))
    os.makedirs(os.path.join(OUT, "images"))
    shutil.copy(os.path.join(SRC, "Math 850", "Figds51.jpg"), os.path.join(OUT, "images", "Figds51.jpg"))
    shutil.copy(os.path.join(SRC, "Math 850", "pulse-evans.gif"), os.path.join(OUT, "images", "pulse-evans.gif"))
    shutil.copy(os.path.join(SRC, "uploads", "StanislavovaCV_3_26.pdf"), os.path.join(OUT, "CV.pdf"))
    # widen menu to fit 8 items
    css = open(os.path.join(OUT, "style", "style.css"), encoding="latin-1").read()
    css = css.replace("padding: 29px 26px 6px 26px;", "padding: 29px 21px 6px 21px;")
    css += "\n#logo_text h2 a, #logo_text h2 a:hover\n{ color: #EEE;}\n"
    open(os.path.join(OUT, "style", "style.css"), "w", encoding="latin-1").write(css)

    page("index.html", "Milena Stanislavova", HOME)
    page("publications.html", "Publications - Milena Stanislavova", pubs_html())
    page("grants.html", "Grants - Milena Stanislavova", GRANTS_HTML)
    page("classes.html", "Classes - Milena Stanislavova", CLASSES)
    page("conferences.html", "Conferences - Milena Stanislavova", CONF)
    page("service.html", "Service - Milena Stanislavova", SERVICE)
    page("news.html", "News - Milena Stanislavova", NEWS)

    # legacy course pages
    for src, dst in [("Math 121.html", "math121.html"), ("Math 850.html", "math850.html"), ("Math 950.html", "math950.html")]:
        h = open(os.path.join(SRC, "uploads", src), encoding="cp1252").read()
        h = h.replace("./Math 850/", "images/").replace("./Math 950/", "images/")
        h = re.sub(r'href="https://stanis\.ku\.edu/"', 'href="index.html"', h)
        h = fix_ku(h)
        h = h.replace('href="mailto:stanis@ku.edu"', 'href="mailto:mstanisl@uab.edu"')
        h = h.replace("charset=windows-1252", "charset=utf-8")
        open(os.path.join(OUT, dst), "w", encoding="utf-8").write(h)

    open(os.path.join(OUT, ".nojekyll"), "w").close()
    open(os.path.join(OUT, "README.md"), "w").write(
        "# Milena Stanislavova - homepage\n\nStatic website (HTML/CSS). Entry point: `index.html`.\n"
        "Served with GitHub Pages from the root of the `main` branch.\n")

main()
