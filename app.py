import streamlit as st
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="Iman Perera - Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Custom CSS for professional styling with creative elements
def load_css():
    st.markdown("""
    <style>
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }

    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }

    @keyframes blink-caret {
        from, to { border-color: transparent; }
        50% { border-color: white; }
    }

    .main {
        padding-top: 2rem;
        animation: fadeInUp 0.8s ease-out;
    }

    .stApp > header {
        background-color: transparent;
    }

    .profile-header {
        text-align: center;
        padding: 3rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
        color: white;
        border-radius: 20px;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }

    .profile-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        animation: shimmer 3s infinite;
    }

    .profile-header h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .profile-photo {
    width: 180px;
    height: 180px;
    border-radius:50%;
    border:6px solid rgba(255,255,255,0.9);
    box-shadow:0 8px 32px rgba(0,0,0,0.3), 
                0 0 0 3px rgba(255,255,255,0.3);
    Transition:all 0.4s ease;
    margin:0 auto 2rem auto;
    display: block;
    object-fit: cover;
    position: relative;
    z-index:2;
    animation: fadeInUp 1s ease-out 0.3s both;
    }
    
    .profile-photo:hover {
    transform: scale(1.1) rotate(5deg);
    box-shadow: 0 12px 40px rgba(0,0,0,0.4), 
                0 0 0 5px rgba(255,255,255,0.5),
                0 0 30px rgba(102, 126, 234, 0.6);
    animation: float 3s ease-in-out infinite;
    }   
    
    .profile-photo-container {
    position: relative;
    z-index: 2;
    margin-bottom: 1rem;
}

.profile-photo-container::before {
    content: '';
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(255,255,255,0.1), transparent);
    z-index: -1;
    animation: pulse 4s ease-in-out infinite;
}          

    .section-header {
        color: #2E4057;
        border-bottom: 3px solid transparent;
        background: linear-gradient(90deg, #667eea, #764ba2) bottom;
        background-size: 100% 3px;
        background-repeat: no-repeat;
        padding-bottom: 0.5rem;
        margin: 2rem 0 1rem 0;
        animation: fadeInUp 0.6s ease-out;
    }

    .skill-tag {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 25px;
        margin: 0.25rem;
        display: inline-block;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .skill-tag:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        animation: pulse 0.6s ease;
    }

    .contact-item {
        padding: 0.8rem;
        border-bottom: 1px solid #f0f2f6;
        border-radius: 8px;
        margin: 0.5rem 0;
        background: linear-gradient(135deg, #f8f9fa, #ffffff);
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .contact-item:hover {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        transform: translateX(10px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }

    .project-card {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 1.5rem 0;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .project-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }

    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }

    .project-card:hover::before {
        transform: scaleX(1);
    }

    .metric-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }

    .metric-card::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        background: rgba(255,255,255,0.2);
        border-radius: 50%;
        transition: all 0.5s ease;
        transform: translate(-50%, -50%);
    }

    .metric-card:hover::before {
        width: 200px;
        height: 200px;
    }

    .metric-card:hover {
        transform: scale(1.05);
        animation: float 2s ease-in-out infinite;
    }

    .metric-card h3 {
        font-size: 2.5rem;
        margin: 0;
        position: relative;
        z-index: 1;
    }

    .metric-card p {
        margin: 0;
        position: relative;
        z-index: 1;
    }

    .animated-icon {
        display: inline-block;
        transition: transform 0.3s ease;
    }

    .animated-icon:hover {
        transform: rotate(360deg) scale(1.2);
    }

    .glow {
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.3);
        transition: box-shadow 0.3s ease;
    }

    .glow:hover {
        box-shadow: 0 0 30px rgba(102, 126, 234, 0.6);
    }

    .particles {
        position: absolute;
        width: 100%;
        height: 100%;
        overflow: hidden;
        top: 0;
        left: 0;
        z-index: 0;
    }

    .particle {
        position: absolute;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
        animation: float 6s ease-in-out infinite;
    }
    </style>
    """, unsafe_allow_html=True)


# Helper function to create downloadable link
def get_binary_file_downloader_html(bin_file, file_label='File'):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{bin_file}">{file_label}</a>'
        return href
    except:
        return "File not found"


# Main app
def main():
    load_css()

    # Sidebar navigation with enhanced styling
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea, #764ba2); color: white; border-radius: 10px; margin-bottom: 1rem;">
        <h2>🧭 Navigation</h2>
        <p style="margin: 0; opacity: 0.9;">Explore my portfolio</p>
    </div>
    """, unsafe_allow_html=True)

    page = st.sidebar.selectbox("Go to", ["👤 About Me", "🚀 Projects", "📄 Resume", "📞 Contact"])

    # Add sidebar extras
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #f093fb, #f5576c); color: white; border-radius: 10px; margin: 1rem 0;">
        <h4>💡 Quick Tip</h4>
        <p style="font-size: 0.9rem; margin: 0;">Hover over elements to see interactive effects!</p>
    </div>
    """, unsafe_allow_html=True)

    if page == "👤 About Me":
        show_about_me()
    elif page == "🚀 Projects":
        show_projects()
    elif page == "📄 Resume":
        show_resume()
    elif page == "📞 Contact":
        show_contact()
def show_about_me():
    # Profile Header with particles and animation
    try:
        profile_image = Image.open("../../../portfolio/assets/profile_photo.jpg")

        # Create columns to center the image
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image(profile_image, width=180, caption="")
    except:
        st.write("📸 Profile photo coming soon!")
    st.markdown("""
    <div class="profile-header glow">
        <div class="particles">
            <div class="particle" style="width:4px;height:4px;left:10%;animation-delay:-2s;"></div>
            <div class="particle" style="width:6px;height:6px;left:20%;animation-delay:-4s;"></div>
            <div class="particle" style="width:3px;height:3px;left:30%;animation-delay:-1s;"></div>
            <div class="particle" style="width:5px;height:5px;left:70%;animation-delay:-3s;"></div>
            <div class="particle" style="width:4px;height:4px;left:80%;animation-delay:-5s;"></div>
            <div class="particle" style="width:7px;height:7px;left:90%;animation-delay:-2.5s;"></div>
        </div> 
        <div style="text-align: center; color: white; padding: 2rem 0;">
        <h1><span class="animated-icon">👋</span> Hello, I'm Iman Perera</h1>
        <h3>Aspiring Data Science & Information Systems Student</h3>
        <p><span class="animated-icon">🚀</span> Passionate about data and every story that builds upon it! <span class="animated-icon">📊</span></p>
    </div>
    """, unsafe_allow_html=True)

    # About Me Content
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<h2 class="section-header"><span class="animated-icon">🎯</span> About Me</h2>',
                    unsafe_allow_html=True)

        st.write("""
        I'm an undergraduate student in Information students of Sabaragamuwa university of Sri Lanka.
        """)

        st.markdown('<h3 class="section-header"><span class="animated-icon">🛠️</span> Technical Skills</h3>',
                    unsafe_allow_html=True)

        # Skills in columns
        skills_col1, skills_col2, skills_col3 = st.columns(3)

        with skills_col1:
            st.markdown("**Programming Languages**")
            skills = ["Python", "C", "SQL", "HTML","Java"]
            for skill in skills:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

        with skills_col2:
            st.markdown("**Data Science & ML**")
            skills = ["Pandas", "NumPy", "Scikit-learn", "TensorFlow", "Matplotlib", "Seaborn"]
            for skill in skills:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

        with skills_col3:
            st.markdown("**Tools & Technologies**")
            skills = ["Streamlit", "Jupyter", "Git", "Tableau"]
            for skill in skills:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

    with col2:
        st.markdown('<h3 class="section-header"><span class="animated-icon">📊</span> Quick Stats</h3>',
                    unsafe_allow_html=True)

        # Enhanced metrics cards with hover effects
        st.markdown("""
        <div class="metric-card glow">
            <h3><span class="animated-icon">🚀</span> 5+</h3>
            <p>Projects Completed</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="metric-card glow">
            <h3><span class="animated-icon">📚</span> 1+</h3>
            <p>Years Learning</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="metric-card glow">
            <h3><span class="animated-icon">💡</span> ∞</h3>
            <p>Curiosity Level</p>
        </div>
        """, unsafe_allow_html=True)

        # Add a fun interactive element
        st.markdown("""
        <div class="metric-card glow" style="background: linear-gradient(135deg, #f093fb, #f5576c);">
            <h3><span class="animated-icon">☕</span> 100+</h3>
            <p>Cups of Coffee</p>
        </div>
        """, unsafe_allow_html=True)

    # Education & Certifications
    st.markdown('<h2 class="section-header"><span class="animated-icon">🎓</span> Education & Certifications</h2>',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="project-card" style="border-left: 4px solid #f093fb;">
            <h4><span class="animated-icon">🎓</span> Education</h4>
            <p>• Bachelor's in Information Systems (Current/Recent)<br>
            • Relevant coursework in Statistics, Database Management, Systems Analysis<br>
            • Strong foundation in analytical thinking and problem-solving</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="project-card" style="border-left: 4px solid #4ecdc4;">
            <h4><span class="animated-icon">🏆</span> Certifications & Learning</h4>
            <p>• Online Data Science Courses<br>
            • Python Programming Certifications<br>
            • Machine Learning Specializations<br>
            • Continuous learning through hands-on projects</p>
        </div>
        """, unsafe_allow_html=True)


def show_projects():
    st.markdown('<h1 class="section-header"><span class="animated-icon">🚀</span> My Projects Portfolio</h1>',
                unsafe_allow_html=True)

    st.write(
        "Here are some of the projects I've worked on. Each project demonstrates different aspects of data science and machine learning.")

    # Project 1 - Enhanced with more visual appeal
    st.markdown("""
    <div class="project-card glow">
        <h3><span class="animated-icon">📈</span> Sales Forecasting Dashboard</h3>
        <p><strong>🔧 Technologies:</strong> Python, Streamlit, Pandas, Plotly, Time Series Analysis</p>
        <p>Built an interactive dashboard for sales forecasting using advanced time series analysis. 
        Features real-time data processing, trend analysis, and predictive modeling with 95% accuracy.</p>
        <p><strong>✨ Key Features:</strong></p>
        <ul>
            <li>Interactive charts with real-time updates</li>
            <li>Seasonal decomposition analysis</li>
            <li>Export functionality for reports</li>
            <li>Mobile-responsive design</li>
        </ul>
        <p><strong>📊 Impact:</strong> Helped reduce forecasting errors by 30%</p>
    </div>
    """, unsafe_allow_html=True)

    # Project 2 - Enhanced
    st.markdown("""
    <div class="project-card glow" style="border-left: 4px solid #4ecdc4;">
        <h3><span class="animated-icon">🧠</span> Customer Segmentation Analysis</h3>
        <p><strong>🔧 Technologies:</strong> Python, Scikit-learn, Matplotlib, Seaborn, K-means Clustering</p>
        <p>Performed comprehensive customer segmentation using K-means clustering and RFM analysis 
        to help businesses understand their customer base and improve targeting strategies.</p>
        <p><strong>✨ Key Features:</strong></p>
        <ul>
            <li>Advanced cluster analysis with optimal K selection</li>
            <li>Customer persona development</li>
            <li>Actionable business insights and recommendations</li>
            <li>Interactive visualization dashboard</li>
        </ul>
        <p><strong>📊 Impact:</strong> Improved marketing campaign efficiency by 40%</p>
    </div>
    """, unsafe_allow_html=True)

    # Project 3 - Enhanced
    st.markdown("""
    <div class="project-card glow" style="border-left: 4px solid #f093fb;">
        <h3><span class="animated-icon">🎯</span> Predictive Analytics Model</h3>
        <p><strong>🔧 Technologies:</strong> Python, TensorFlow, Pandas, NumPy, Feature Engineering</p>
        <p>Developed a sophisticated machine learning model to predict customer churn with 87% accuracy. 
        Implemented advanced feature engineering and model optimization techniques.</p>
        <p><strong>✨ Key Features:</strong></p>
        <ul>
            <li>Feature importance analysis with SHAP values</li>
            <li>Multiple model comparison (Random Forest, XGBoost, Neural Networks)</li>
            <li>Real-time prediction API</li>
            <li>Comprehensive performance metrics dashboard</li>
        </ul>
        <p><strong>📊 Impact:</strong> Enabled proactive customer retention strategies</p>
    </div>
    """, unsafe_allow_html=True)

    # Coming Soon section with creativity
    st.markdown("""
    <div class="project-card" style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; text-align: center;">
        <h3><span class="animated-icon">🔮</span> Coming Soon Projects</h3>
        <p>🤖 <strong>AI-Powered Recommendation System</strong> - Building a collaborative filtering system</p>
        <p>📱 <strong>Real-time Analytics App</strong> - Live data processing with Apache Kafka</p>
        <p>🌐 <strong>Web Scraping & Sentiment Analysis</strong> - Social media sentiment tracking</p>
        <br>
        <p><em>Stay tuned for more exciting projects!</em> ✨</p>
    </div>
    """, unsafe_allow_html=True)


def show_resume():
    st.markdown('<h1 class="section-header"><span class="animated-icon">📄</span> Resume</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])

    with col1:
        st.write("View my complete professional background and experience.")

    with col2:
        if st.button("📥 Download PDF Resume", type="primary"):
            st.info("PDF download functionality will be implemented soon!")

    # Resume sections
    st.markdown('<h2 class="section-header">💼 Professional Summary</h2>', unsafe_allow_html=True)
    st.write("""
    Aspiring Data Scientist with strong analytical skills and experience in statistical analysis, 
    machine learning, and data visualization. Proficient in Python, R, and SQL with hands-on 
    experience in building predictive models and creating interactive dashboards.
    """)

    st.markdown('<h2 class="section-header">🎓 Education</h2>', unsafe_allow_html=True)
    st.write("""
    **Bachelor's Degree in Information Systems**  
    *University Name* | *Year*  
    Relevant Coursework: Statistics, Database Management, Systems Analysis, Data Structures
    """)

    st.markdown('<h2 class="section-header">🛠️ Technical Skills</h2>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Programming**")
        st.write("• Python\n• R\n• SQL\n• JavaScript")

    with col2:
        st.write("**Data Science**")
        st.write("• Machine Learning\n• Statistical Analysis\n• Data Visualization\n• Predictive Modeling")

    with col3:
        st.write("**Tools**")
        st.write("• Streamlit\n• Jupyter\n• Tableau\n• Git/GitHub")

    st.markdown('<h2 class="section-header">🚀 Projects</h2>', unsafe_allow_html=True)
    st.write("• Sales Forecasting Dashboard - Interactive analytics dashboard")
    st.write("• Customer Segmentation - ML-based customer analysis")
    st.write("• Predictive Analytics - Churn prediction model")


def show_contact():
    st.markdown('<h1 class="section-header"><span class="animated-icon">📞</span> Get In Touch</h1>',
                unsafe_allow_html=True)

    st.write(
        "I'm always excited to connect with fellow data enthusiasts, potential collaborators, or anyone interested !")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<h3 class="section-header"><span class="animated-icon">📧</span> Contact Information</h3>',
                    unsafe_allow_html=True)

        # Enhanced contact items with hover effects
        st.markdown("""
        <div class="contact-item">
            <strong><span class="animated-icon">📧</span> Email:</strong> kimanrandilaperera@gmail.com
        </div>
        <div class="contact-item">
            <strong><span class="animated-icon">💼</span> LinkedIn:</strong> www.linkedin.com/in/imanrandilaperera
        </div>
        <div class="contact-item">
            <strong><span class="animated-icon">🐙</span> GitHub:</strong> https://github.com/kirperera
        </div>
        <div class="contact-item">
            <strong><span class="animated-icon">📍</span> Location:</strong> Embilipitiya, Sabaragamuwa province, Sri Lanka
        </div>
        <div class="contact-item">
            <strong><span class="animated-icon">💬</span> Discord:</strong> Available upon request
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<h3 class="section-header"><span class="animated-icon"></span> Let\'s Connect!</h3>',
                    unsafe_allow_html=True)

        # Enhanced connection section
        st.markdown("""
        <div class="project-card" style="border-left: 4px solid #4ecdc4;">
            <h4><span class="animated-icon">🤝</span> I'm open to:</h4>
            <ul>
                <li><span class="animated-icon">🔬</span> Data Science collaborations</li>
                <li><span class="animated-icon">📚</span> Learning opportunities</li>
                <li><span class="animated-icon">💼</span> Career discussions</li>
                <li><span class="animated-icon">💭</span> Project feedback</li>
                <li><span class="animated-icon">🌐</span> Networking with professionals</li>
                <li><span class="animated-icon">☕</span> Coffee chats about data!</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Fun interactive element
        st.markdown("""
        <div class="metric-card glow" style="background: linear-gradient(135deg, #667eea, #764ba2);">
            <h4><span class="animated-icon">⚡</span> Response Time</h4>
            <h3>&lt; 24 hours</h3>
            <p>I typically respond quickly!</p>
        </div>
        """, unsafe_allow_html=True)

    # Add a call-to-action section
    st.markdown("---")
    st.markdown("""
    <div class="project-card" style="background: linear-gradient(135deg, #f093fb, #f5576c); color: white; text-align: center;">
        <h3><span class="animated-icon">🚀</span> Ready to Collaborate?</h3>
        <p>Whether you have a project idea, want to discuss data science trends, or just want to connect, I'd love to hear from you!</p>
        <p><strong>Let's build something amazing together! </strong><span class="animated-icon">✨</span></p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()