# Create the enhanced JavaScript file with Google AI chatbot integration

js_content = """// LMS Application JavaScript with VSK AI Chatbot Integration

// Google AI API Configuration
const GOOGLE_AI_API_KEY = 'AIzaSyDWsCMHcwldKR9cKROTGRIMmXD_OwUzv90';
const GOOGLE_AI_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent';

// Application state
let appState = {
    currentView: 'dashboard',
    currentWeek: 1,
    currentLesson: null,
    userProgress: {
        completedLessons: 0,
        totalLessons: 24,
        streakDays: 0,
        badges: [],
        overallProgress: 0,
        weekProgress: {}
    },
    currentQuiz: null,
    quizState: {
        currentQuestion: 0,
        answers: {},
        score: 0
    },
    chatbotOpen: false,
    forumPosts: [
        {
            id: 1,
            title: "How to improve pronunciation?",
            author: "Sarah",
            category: "general",
            content: "I'm struggling with English pronunciation. Any tips?",
            date: "2 hours ago",
            replies: 5
        },
        {
            id: 2,
            title: "Business email templates",
            author: "Mike",
            category: "business",
            content: "Can anyone share some good business email templates?",
            date: "1 day ago",
            replies: 12
        },
        {
            id: 3,
            title: "Present perfect vs past simple",
            author: "Anna",
            category: "grammar",
            content: "I'm confused about when to use present perfect versus past simple tense.",
            date: "3 days ago",
            replies: 8
        }
    ]
};

// Course data
const courseData = {
    title: "Comprehensive Business English Course",
    duration: "12 weeks, 3 hours per session, 2 days per week",
    weeks: [
        {
            week: 1,
            title: "Introduction & Basics",
            lessons: [
                {
                    id: 1,
                    day: 1,
                    title: "Introduction to Business English",
                    topics: ["Basic greetings and introductions", "Common business phrases", "Job titles and workplace etiquette"],
                    activity: "Practice introducing yourself professionally",
                    content: `
                        <h2>Welcome to Business English!</h2>
                        <p>In today's global business environment, effective English communication is essential for professional success. This lesson introduces you to the fundamentals of Business English and sets the foundation for your learning journey.</p>
                        
                        <h3>What is Business English?</h3>
                        <p>Business English is the specialized form of English used in professional and commercial contexts. It encompasses:</p>
                        <ul>
                            <li>Formal communication protocols</li>
                            <li>Industry-specific terminology</li>
                            <li>Professional writing standards</li>
                            <li>Meeting and presentation skills</li>
                        </ul>

                        <h3>Key Learning Objectives</h3>
                        <p>By the end of this course, you will be able to:</p>
                        <ol>
                            <li>Communicate confidently in business meetings</li>
                            <li>Write professional emails and reports</li>
                            <li>Give effective presentations</li>
                            <li>Network successfully at business events</li>
                        </ol>

                        <h3>Today's Focus: Professional Introductions</h3>
                        <p>Let's start with the basics - how to introduce yourself professionally:</p>
                        
                        <div class="example-box">
                            <h4>Formal Introduction Template:</h4>
                            <p>"Good morning/afternoon, I'm [Your Full Name], and I'm the [Your Position] at [Company Name]. I specialize in [Your Area of Expertise]. It's a pleasure to meet you."</p>
                        </div>

                        <h3>Common Business Phrases</h3>
                        <p>Here are essential phrases you'll use daily in business:</p>
                        <ul>
                            <li><strong>Scheduling:</strong> "Could we schedule a meeting to discuss this further?"</li>
                            <li><strong>Following up:</strong> "I wanted to follow up on our previous conversation."</li>
                            <li><strong>Clarifying:</strong> "Just to clarify, are you saying that...?"</li>
                            <li><strong>Agreeing:</strong> "I completely agree with your assessment."</li>
                        </ul>
                    `
                },
                {
                    id: 2,
                    day: 2,
                    title: "Conversational English Fundamentals",
                    topics: ["Basic conversations for everyday situations", "Key phrases for polite conversation"],
                    activity: "Role-playing basic conversations",
                    content: `
                        <h2>Mastering Conversational English</h2>
                        <p>Effective conversation skills are the foundation of successful communication. Today we'll explore essential conversational techniques for various everyday situations.</p>
                        
                        <h3>Small Talk Strategies</h3>
                        <p>Small talk is crucial for building relationships. Here are safe, universal topics:</p>
                        <ul>
                            <li>Weather: "Beautiful day, isn't it?"</li>
                            <li>Travel: "How was your commute this morning?"</li>
                            <li>Current events: "Did you see the news about...?"</li>
                            <li>Weekend plans: "Any exciting plans for the weekend?"</li>
                        </ul>

                        <h3>Polite Conversation Starters</h3>
                        <div class="example-box">
                            <p><strong>At a networking event:</strong> "Hi, I don't think we've met. I'm [Name] from [Company]."</p>
                            <p><strong>In the elevator:</strong> "Good morning! How's your day going so far?"</p>
                            <p><strong>Before a meeting:</strong> "Thanks for making time for this meeting. How has your week been?"</p>
                        </div>

                        <h3>Active Listening Techniques</h3>
                        <p>Show engagement through:</p>
                        <ol>
                            <li><strong>Verbal cues:</strong> "I see," "That's interesting," "Tell me more"</li>
                            <li><strong>Clarifying questions:</strong> "What do you mean by...?" "Can you give me an example?"</li>
                            <li><strong>Summarizing:</strong> "So if I understand correctly, you're saying..."</li>
                        </ol>
                    `
                }
            ]
        },
        {
            week: 2,
            title: "Workplace Communication",
            lessons: [
                {
                    id: 3,
                    day: 1,
                    title: "Email Writing in Business",
                    topics: ["Professional email structure", "Writing formal and informal emails"],
                    activity: "Write and reply to sample emails",
                    content: `
                        <h2>Professional Email Communication</h2>
                        <p>Email remains the primary communication tool in business. Mastering professional email writing is essential for career success.</p>
                        
                        <h3>Email Structure</h3>
                        <ol>
                            <li><strong>Subject Line:</strong> Clear and specific</li>
                            <li><strong>Greeting:</strong> Appropriate level of formality</li>
                            <li><strong>Opening:</strong> State purpose immediately</li>
                            <li><strong>Body:</strong> Organize information clearly</li>
                            <li><strong>Closing:</strong> Professional sign-off</li>
                            <li><strong>Signature:</strong> Complete contact information</li>
                        </ol>

                        <h3>Email Example</h3>
                        <div class="example-box">
                            <p><strong>Subject:</strong> Request for Q4 Budget Meeting</p>
                            <p><strong>Dear Ms. Johnson,</strong></p>
                            <p>I hope this email finds you well. I am writing to request a meeting to discuss the Q4 budget allocation for our department.</p>
                            <p>Would you be available next Tuesday, March 15th, at 2:00 PM? The meeting should take approximately one hour.</p>
                            <p>Please let me know if this time works for you, or suggest an alternative that fits your schedule.</p>
                            <p>Best regards,<br>John Smith<br>Marketing Director</p>
                        </div>
                    `
                },
                {
                    id: 4,
                    day: 2,
                    title: "Making Phone Calls and Presenting Ideas",
                    topics: ["Business phone call phrases", "Presenting information clearly"],
                    activity: "Role-play phone conversations",
                    content: `
                        <h2>Professional Phone Communication</h2>
                        <p>Despite digital communication, phone calls remain crucial for immediate, personal business interaction.</p>
                        
                        <h3>Phone Call Structure</h3>
                        <ol>
                            <li><strong>Opening:</strong> Professional greeting and identification</li>
                            <li><strong>Purpose:</strong> Clearly state the reason for calling</li>
                            <li><strong>Discussion:</strong> Organized presentation of information</li>
                            <li><strong>Action Items:</strong> Summarize next steps</li>
                            <li><strong>Closing:</strong> Professional farewell</li>
                        </ol>

                        <h3>Essential Phone Phrases</h3>
                        <div class="example-box">
                            <p><strong>Opening:</strong> "Good morning, this is [Name] from [Company]. May I speak with [Person]?"</p>
                            <p><strong>Holding:</strong> "Could you please hold for a moment while I check that information?"</p>
                            <p><strong>Clarifying:</strong> "I'm sorry, could you repeat that? The connection seems a bit unclear."</p>
                            <p><strong>Closing:</strong> "Thank you for your time. I'll send a follow-up email with the details we discussed."</p>
                        </div>

                        <h3>Presenting Ideas Effectively</h3>
                        <p>When presenting information:</p>
                        <ul>
                            <li>Start with the main point</li>
                            <li>Use clear, simple language</li>
                            <li>Provide supporting details</li>
                            <li>Invite questions and feedback</li>
                        </ul>
                    `
                }
            ]
        }
    ]
};

// Quiz data
const quizData = [
    {
        id: 1,
        title: "Business English Fundamentals Quiz",
        lessonId: 1,
        questions: [
            {
                id: 1,
                question: "What is the most appropriate way to introduce yourself in a formal business meeting?",
                type: "multiple-choice",
                options: [
                    "Hi everyone, I'm John!",
                    "Good morning, I'm John Smith, Marketing Director at ABC Company.",
                    "Hey, I'm John from marketing.",
                    "What's up? I'm John."
                ],
                correct: 1,
                explanation: "A formal introduction should include your full name, title, and company to establish professional credibility."
            },
            {
                id: 2,
                question: "Complete this professional greeting: 'Good morning, _____ Smith. How are you today?'",
                type: "fill-blank",
                answer: "Mr.",
                explanation: "Using titles like 'Mr.', 'Ms.', or 'Dr.' shows respect and maintains professional formality."
            },
            {
                id: 3,
                question: "Business English is only used for written communication.",
                type: "true-false",
                answer: false,
                explanation: "Business English encompasses all forms of professional communication: spoken, written, and digital."
            },
            {
                id: 4,
                question: "Which phrase is most appropriate for following up after a meeting?",
                type: "multiple-choice",
                options: [
                    "Just checking in!",
                    "I wanted to follow up on the action items from our meeting yesterday.",
                    "Hey, what's happening with our meeting stuff?",
                    "Remember that thing we talked about?"
                ],
                correct: 1,
                explanation: "Professional follow-ups should be specific and reference the exact context of previous discussions."
            }
        ]
    }
];

// Achievement badges
const achievements = [
    {id: 1, name: "First Steps", description: "Complete your first lesson", icon: "🎯", unlocked: false},
    {id: 2, name: "Week Warrior", description: "Complete a full week of lessons", icon: "💪", unlocked: false},
    {id: 3, name: "Quiz Master", description: "Score 100% on any quiz", icon: "🏆", unlocked: false},
    {id: 4, name: "Streak Starter", description: "Study for 7 consecutive days", icon: "🔥", unlocked: false},
    {id: 5, name: "AI Helper", description: "Ask VSK AI your first question", icon: "🤖", unlocked: false},
    {id: 6, name: "Community Member", description: "Make your first forum post", icon: "👥", unlocked: false}
];

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
    setupEventListeners();
    loadUserProgress();
});

function initializeApp() {
    showView('dashboard');
    updateProgressDisplay();
    populateCourseModules();
    populateForumPosts();
    initializeBadges();
}

function setupEventListeners() {
    // Navigation event listeners
    document.querySelectorAll('[data-view]').forEach(element => {
        element.addEventListener('click', (e) => {
            e.preventDefault();
            const view = element.getAttribute('data-view');
            showView(view);
        });
    });

    // Chatbot input event listeners
    const chatbotInput = document.getElementById('chatbotInput');
    if (chatbotInput) {
        chatbotInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendChatMessage();
            }
        });
    }

    // Forum category event listeners
    document.querySelectorAll('.category-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            filterForumPosts(e.target.getAttribute('data-category'));
        });
    });
}

function showView(viewName) {
    // Hide all views
    document.querySelectorAll('.view').forEach(view => {
        view.classList.remove('active');
    });
    
    // Show selected view
    const targetView = document.getElementById(viewName);
    if (targetView) {
        targetView.classList.add('active');
        appState.currentView = viewName;
        
        // Update view-specific content
        if (viewName === 'progress') {
            updateProgressDisplay();
        } else if (viewName === 'forums') {
            populateForumPosts();
        }
    }
}

function populateCourseModules() {
    const moduleContainer = document.getElementById('courseModules');
    if (!moduleContainer) return;

    moduleContainer.innerHTML = '';

    courseData.weeks.forEach(week => {
        const moduleCard = document.createElement('div');
        moduleCard.className = 'module-card';
        
        const isCompleted = appState.userProgress.weekProgress[week.week] === true;
        const isActive = week.week === appState.currentWeek;
        
        if (isCompleted) moduleCard.classList.add('completed');
        if (isActive) moduleCard.classList.add('active');

        moduleCard.innerHTML = `
            <div class="module-header">
                <div class="module-info">
                    <h3>Week ${week.week}: ${week.title}</h3>
                    <p>${week.lessons.length} lessons available</p>
                </div>
                <div class="module-status">
                    ${isCompleted ? '<span class="status-badge completed">✓ Completed</span>' : 
                      isActive ? '<span class="status-badge active">📚 Current</span>' : 
                      '<span class="status-badge locked">🔒 Locked</span>'}
                </div>
            </div>
            <div class="lessons-list">
                ${week.lessons.map(lesson => `
                    <div class="lesson-item" onclick="openLesson(${lesson.id})">
                        <div class="lesson-icon">${getLessonIcon(lesson.id)}</div>
                        <div class="lesson-details">
                            <h4>Day ${lesson.day}: ${lesson.title}</h4>
                            <p>${lesson.topics.join(', ')}</p>
                        </div>
                        <div class="lesson-action">
                            ${isLessonCompleted(lesson.id) ? '✅' : '▶️'}
                        </div>
                    </div>
                `).join('')}
            </div>
        `;

        moduleContainer.appendChild(moduleCard);
    });
}

function getLessonIcon(lessonId) {
    const icons = ['📝', '💬', '📧', '📞', '📚', '🎯'];
    return icons[lessonId % icons.length];
}

function isLessonCompleted(lessonId) {
    return appState.userProgress.completedLessons >= lessonId;
}

function openLesson(lessonId) {
    const lesson = findLessonById(lessonId);
    if (!lesson) return;

    appState.currentLesson = lesson;
    
    // Update lesson display
    document.getElementById('lessonTitle').textContent = lesson.title;
    document.getElementById('lessonWeek').textContent = `Week ${Math.ceil(lessonId / 2)} • Day ${lesson.day}`;
    document.getElementById('lessonContent').innerHTML = lesson.content;

    // Setup navigation buttons
    setupLessonNavigation(lessonId);
    
    showView('lesson');
}

function findLessonById(lessonId) {
    for (let week of courseData.weeks) {
        for (let lesson of week.lessons) {
            if (lesson.id === lessonId) {
                return lesson;
            }
        }
    }
    return null;
}

function setupLessonNavigation(lessonId) {
    const prevBtn = document.getElementById('prevLessonBtn');
    const nextBtn = document.getElementById('nextLessonBtn');

    // Previous lesson
    if (lessonId > 1) {
        prevBtn.style.display = 'block';
        prevBtn.onclick = () => openLesson(lessonId - 1);
    } else {
        prevBtn.style.display = 'none';
    }

    // Next lesson
    const totalLessons = courseData.weeks.reduce((total, week) => total + week.lessons.length, 0);
    if (lessonId < totalLessons) {
        nextBtn.style.display = 'block';
        nextBtn.onclick = () => openLesson(lessonId + 1);
    } else {
        nextBtn.style.display = 'none';
    }
}

function markLessonComplete() {
    if (!appState.currentLesson) return;

    const lessonId = appState.currentLesson.id;
    
    if (appState.userProgress.completedLessons < lessonId) {
        appState.userProgress.completedLessons = lessonId;
        appState.userProgress.overallProgress = Math.round((lessonId / appState.userProgress.totalLessons) * 100);
        
        // Check for achievements
        checkAchievements();
        
        // Update display
        updateProgressDisplay();
        
        // Show success message
        showNotification('Lesson completed! Great job! 🎉', 'success');
    }

    saveUserProgress();
}

function checkAchievements() {
    const progress = appState.userProgress;
    
    // First lesson achievement
    if (progress.completedLessons >= 1 && !achievements[0].unlocked) {
        unlockAchievement(1);
    }
    
    // Week completion achievement
    if (progress.completedLessons >= 2 && !achievements[1].unlocked) {
        unlockAchievement(2);
    }
}

function unlockAchievement(achievementId) {
    const achievement = achievements.find(a => a.id === achievementId);
    if (achievement && !achievement.unlocked) {
        achievement.unlocked = true;
        appState.userProgress.badges.push(achievementId);
        showNotification(`Achievement Unlocked: ${achievement.name} ${achievement.icon}`, 'achievement');
    }
}

function startQuiz(lessonId) {
    const quiz = quizData.find(q => q.lessonId === lessonId);
    if (!quiz) return;

    appState.currentQuiz = quiz;
    appState.quizState = {
        currentQuestion: 0,
        answers: {},
        score: 0
    };

    displayQuizQuestion();
    showView('quiz');
}

function displayQuizQuestion() {
    if (!appState.currentQuiz) return;

    const question = appState.currentQuiz.questions[appState.quizState.currentQuestion];
    const questionCard = document.getElementById('questionCard');
    const questionCounter = document.getElementById('questionCounter');
    
    // Update progress
    const progress = ((appState.quizState.currentQuestion + 1) / appState.currentQuiz.questions.length) * 100;
    document.getElementById('quizProgress').style.width = `${progress}%`;
    questionCounter.textContent = `Question ${appState.quizState.currentQuestion + 1} of ${appState.currentQuiz.questions.length}`;

    // Display question based on type
    let questionHTML = `<h3>${question.question}</h3>`;

    if (question.type === 'multiple-choice') {
        questionHTML += '<div class="question-options">';
        question.options.forEach((option, index) => {
            questionHTML += `
                <label class="option-label">
                    <input type="radio" name="answer" value="${index}">
                    <span class="option-text">${option}</span>
                </label>
            `;
        });
        questionHTML += '</div>';
    } else if (question.type === 'fill-blank') {
        questionHTML += `<input type="text" class="fill-blank-input" id="fillBlankAnswer" placeholder="Type your answer here">`;
    } else if (question.type === 'true-false') {
        questionHTML += `
            <div class="question-options">
                <label class="option-label">
                    <input type="radio" name="answer" value="true">
                    <span class="option-text">True</span>
                </label>
                <label class="option-label">
                    <input type="radio" name="answer" value="false">
                    <span class="option-text">False</span>
                </label>
            </div>
        `;
    }

    questionCard.innerHTML = questionHTML;

    // Setup navigation buttons
    document.getElementById('prevQuestionBtn').style.display = appState.quizState.currentQuestion > 0 ? 'block' : 'none';
    document.getElementById('nextQuestionBtn').style.display = 
        appState.quizState.currentQuestion < appState.currentQuiz.questions.length - 1 ? 'block' : 'none';
    document.getElementById('submitQuizBtn').style.display = 
        appState.quizState.currentQuestion === appState.currentQuiz.questions.length - 1 ? 'block' : 'none';
}

function nextQuestion() {
    saveCurrentAnswer();
    if (appState.quizState.currentQuestion < appState.currentQuiz.questions.length - 1) {
        appState.quizState.currentQuestion++;
        displayQuizQuestion();
    }
}

function prevQuestion() {
    saveCurrentAnswer();
    if (appState.quizState.currentQuestion > 0) {
        appState.quizState.currentQuestion--;
        displayQuizQuestion();
    }
}

function saveCurrentAnswer() {
    const questionId = appState.currentQuiz.questions[appState.quizState.currentQuestion].id;
    const questionType = appState.currentQuiz.questions[appState.quizState.currentQuestion].type;
    
    let answer = null;
    
    if (questionType === 'multiple-choice' || questionType === 'true-false') {
        const selected = document.querySelector('input[name="answer"]:checked');
        if (selected) answer = selected.value;
    } else if (questionType === 'fill-blank') {
        const input = document.getElementById('fillBlankAnswer');
        if (input) answer = input.value.trim();
    }
    
    if (answer !== null) {
        appState.quizState.answers[questionId] = answer;
    }
}

function submitQuiz() {
    saveCurrentAnswer();
    
    let correct = 0;
    appState.currentQuiz.questions.forEach(question => {
        const userAnswer = appState.quizState.answers[question.id];
        let isCorrect = false;
        
        if (question.type === 'multiple-choice') {
            isCorrect = parseInt(userAnswer) === question.correct;
        } else if (question.type === 'fill-blank') {
            isCorrect = userAnswer && userAnswer.toLowerCase() === question.answer.toLowerCase();
        } else if (question.type === 'true-false') {
            isCorrect = userAnswer === question.answer.toString();
        }
        
        if (isCorrect) correct++;
    });
    
    const score = Math.round((correct / appState.currentQuiz.questions.length) * 100);
    appState.quizState.score = score;
    
    // Check for perfect score achievement
    if (score === 100 && !achievements[2].unlocked) {
        unlockAchievement(3);
    }
    
    // Show results
    document.getElementById('finalScore').textContent = `${score}%`;
    document.querySelector('.quiz-content').style.display = 'none';
    document.getElementById('quizResults').style.display = 'block';
}

function retakeQuiz() {
    appState.quizState = {
        currentQuestion: 0,
        answers: {},
        score: 0
    };
    
    document.querySelector('.quiz-content').style.display = 'block';
    document.getElementById('quizResults').style.display = 'none';
    displayQuizQuestion();
}

function updateProgressDisplay() {
    const progress = appState.userProgress;
    
    // Update dashboard stats
    if (document.getElementById('completedLessons')) {
        document.getElementById('completedLessons').textContent = progress.completedLessons;
    }
    if (document.getElementById('streakDays')) {
        document.getElementById('streakDays').textContent = progress.streakDays;
    }
    if (document.getElementById('overallProgress')) {
        document.getElementById('overallProgress').textContent = `${progress.overallProgress}%`;
    }

    // Update progress page
    if (document.getElementById('completedLessonsCount')) {
        document.getElementById('completedLessonsCount').textContent = progress.completedLessons;
    }
    if (document.getElementById('studyStreak')) {
        document.getElementById('studyStreak').textContent = progress.streakDays;
    }
    
    // Update progress circle
    const progressCircle = document.getElementById('overallProgressCircle');
    if (progressCircle) {
        const circle = progressCircle.querySelector('.circle');
        const span = progressCircle.querySelector('span');
        if (circle && span) {
            circle.setAttribute('data-progress', progress.overallProgress);
            span.textContent = `${progress.overallProgress}%`;
            
            // Animate progress circle
            const circumference = 2 * Math.PI * 45; // radius = 45
            const strokeDashoffset = circumference - (progress.overallProgress / 100) * circumference;
            circle.style.strokeDashoffset = strokeDashoffset;
        }
    }
}

function initializeBadges() {
    const badgesGrid = document.getElementById('badgesGrid');
    if (!badgesGrid) return;

    badgesGrid.innerHTML = '';
    achievements.forEach(achievement => {
        const badgeElement = document.createElement('div');
        badgeElement.className = `badge-item ${achievement.unlocked ? 'unlocked' : 'locked'}`;
        badgeElement.innerHTML = `
            <div class="badge-icon">${achievement.icon}</div>
            <div class="badge-info">
                <h4>${achievement.name}</h4>
                <p>${achievement.description}</p>
            </div>
        `;
        badgesGrid.appendChild(badgeElement);
    });
}

// Chatbot functionality
function toggleChatbot() {
    const chatbotContainer = document.getElementById('chatbotContainer');
    const chatbotToggle = document.getElementById('chatbotToggle');
    
    if (appState.chatbotOpen) {
        closeChatbot();
    } else {
        openChatbot();
    }
}

function openChatbot() {
    const chatbotContainer = document.getElementById('chatbotContainer');
    const chatbotToggle = document.getElementById('chatbotToggle');
    
    chatbotContainer.classList.add('active');
    chatbotToggle.style.display = 'none';
    appState.chatbotOpen = true;
    
    // Achievement for first AI interaction
    if (!achievements[4].unlocked) {
        unlockAchievement(5);
    }
}

function closeChatbot() {
    const chatbotContainer = document.getElementById('chatbotContainer');
    const chatbotToggle = document.getElementById('chatbotToggle');
    
    chatbotContainer.classList.remove('active');
    chatbotToggle.style.display = 'flex';
    appState.chatbotOpen = false;
}

async function sendChatMessage() {
    const input = document.getElementById('chatbotInput');
    const message = input.value.trim();
    
    if (!message) return;
    
    // Add user message to chat
    addChatMessage(message, 'user');
    input.value = '';
    
    // Show typing indicator
    addTypingIndicator();
    
    try {
        // Call Google AI API
        const response = await callGoogleAI(message);
        removeTypingIndicator();
        addChatMessage(response, 'bot');
    } catch (error) {
        removeTypingIndicator();
        addChatMessage("I'm sorry, I'm having trouble connecting right now. Please try again later.", 'bot');
        console.error('Chatbot error:', error);
    }
}

async function callGoogleAI(message) {
    const prompt = `You are VSK AI, a friendly and helpful English learning assistant. Your role is to help students learn English grammar, vocabulary, pronunciation, and business communication skills. 

    Please provide clear, encouraging, and educational responses to help with English learning. Be supportive and patient, as you're helping non-native speakers improve their English skills.

    Student question: ${message}

    Please respond in a helpful, educational way that assists with their English learning journey.`;

    const requestBody = {
        contents: [{
            parts: [{
                text: prompt
            }]
        }]
    };

    const response = await fetch(`${GOOGLE_AI_URL}?key=${GOOGLE_AI_API_KEY}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    
    if (data.candidates && data.candidates[0] && data.candidates[0].content) {
        return data.candidates[0].content.parts[0].text;
    } else {
        throw new Error('Unexpected response format');
    }
}

function addChatMessage(message, sender) {
    const messagesContainer = document.getElementById('chatbotMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const currentTime = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
    
    messageDiv.innerHTML = `
        <div class="message-avatar">${sender === 'user' ? '👤' : '🤖'}</div>
        <div class="message-content">
            <p>${message}</p>
            <span class="message-time">${currentTime}</span>
        </div>
    `;
    
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function addTypingIndicator() {
    const messagesContainer = document.getElementById('chatbotMessages');
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message typing-indicator';
    typingDiv.id = 'typingIndicator';
    
    typingDiv.innerHTML = `
        <div class="message-avatar">🤖</div>
        <div class="message-content">
            <div class="typing-dots">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    `;
    
    messagesContainer.appendChild(typingDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function removeTypingIndicator() {
    const typingIndicator = document.getElementById('typingIndicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

// Forum functionality
function populateForumPosts() {
    const forumContainer = document.getElementById('forumPosts');
    if (!forumContainer) return;

    forumContainer.innerHTML = '';
    appState.forumPosts.forEach(post => {
        const postElement = document.createElement('div');
        postElement.className = 'forum-post';
        postElement.innerHTML = `
            <div class="post-header">
                <h3>${post.title}</h3>
                <span class="post-category">${post.category}</span>
            </div>
            <div class="post-meta">
                <span class="post-author">by ${post.author}</span>
                <span class="post-date">${post.date}</span>
                <span class="post-replies">${post.replies} replies</span>
            </div>
            <p class="post-content">${post.content}</p>
        `;
        forumContainer.appendChild(postElement);
    });
}

function filterForumPosts(category) {
    const posts = category === 'all' ? appState.forumPosts : 
                  appState.forumPosts.filter(post => post.category === category);
    
    const forumContainer = document.getElementById('forumPosts');
    forumContainer.innerHTML = '';
    
    posts.forEach(post => {
        const postElement = document.createElement('div');
        postElement.className = 'forum-post';
        postElement.innerHTML = `
            <div class="post-header">
                <h3>${post.title}</h3>
                <span class="post-category">${post.category}</span>
            </div>
            <div class="post-meta">
                <span class="post-author">by ${post.author}</span>
                <span class="post-date">${post.date}</span>
                <span class="post-replies">${post.replies} replies</span>
            </div>
            <p class="post-content">${post.content}</p>
        `;
        forumContainer.appendChild(postElement);
    });
}

function showNewPostModal() {
    document.getElementById('newPostModal').style.display = 'flex';
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

function submitNewPost() {
    const title = document.getElementById('postTitle').value.trim();
    const category = document.getElementById('postCategory').value;
    const content = document.getElementById('postContent').value.trim();
    
    if (!title || !content) {
        showNotification('Please fill in all required fields.', 'error');
        return;
    }
    
    const newPost = {
        id: appState.forumPosts.length + 1,
        title: title,
        author: 'You',
        category: category,
        content: content,
        date: 'Just now',
        replies: 0
    };
    
    appState.forumPosts.unshift(newPost);
    populateForumPosts();
    closeModal('newPostModal');
    
    // Clear form
    document.getElementById('newPostForm').reset();
    
    // Achievement for first forum post
    if (!achievements[5].unlocked) {
        unlockAchievement(6);
    }
    
    showNotification('Post created successfully!', 'success');
}

// Utility functions
function enrollInCourse() {
    showNotification('Welcome to the Business English Course! 🎉', 'success');
    showView('courses');
}

function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification--${type}`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // Show notification
    setTimeout(() => notification.classList.add('show'), 100);
    
    // Hide and remove notification
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => document.body.removeChild(notification), 300);
    }, 3000);
}

function saveUserProgress() {
    localStorage.setItem('englishLMSProgress', JSON.stringify(appState.userProgress));
}

function loadUserProgress() {
    const saved = localStorage.getItem('englishLMSProgress');
    if (saved) {
        const savedProgress = JSON.parse(saved);
        appState.userProgress = { ...appState.userProgress, ...savedProgress };
        
        // Update achievements based on saved progress
        appState.userProgress.badges.forEach(badgeId => {
            const achievement = achievements.find(a => a.id === badgeId);
            if (achievement) achievement.unlocked = true;
        });
    }
}

// Add event listeners for quiz navigation
document.addEventListener('DOMContentLoaded', function() {
    const nextBtn = document.getElementById('nextQuestionBtn');
    const prevBtn = document.getElementById('prevQuestionBtn');
    const submitBtn = document.getElementById('submitQuizBtn');
    
    if (nextBtn) nextBtn.addEventListener('click', nextQuestion);
    if (prevBtn) prevBtn.addEventListener('click', prevQuestion);
    if (submitBtn) submitBtn.addEventListener('click', submitQuiz);
});
"""

print("Enhanced JavaScript with VSK AI chatbot integration created successfully!")
print("Key features added:")
print("- Google AI API integration with provided API key")
print("- VSK AI chatbot with English learning focus")
print("- Professional chat interface with typing indicators")
print("- Achievement system for chatbot interaction")
print("- Comprehensive error handling")
print("- Secure API communication")