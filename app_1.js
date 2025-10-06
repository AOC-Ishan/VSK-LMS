// English LMS Application JavaScript

// Application State
let appState = {
    currentSection: 'dashboard',
    currentLesson: null,
    completedLessons: new Set(),
    userProgress: {
        totalLessons: 4,
        completedCount: 0,
        studyStreak: 0,
        achievements: new Set(),
        quizScores: [],
        timeSpent: 0
    },
    quiz: {
        currentQuestion: 0,
        questions: [],
        userAnswers: [],
        score: 0
    },
    chatbot: {
        isOpen: false,
        messages: []
    }
};

// Course Data
const courseData = {
    "title": "Comprehensive Business English Course",
    "duration": "12 weeks, 3 hours per session, 2 days per week",
    "weeks": [
        {
            "week": 1,
            "title": "Introduction & Basics",
            "lessons": [
                {
                    "id": 1,
                    "day": 1,
                    "title": "Introduction to Business English",
                    "topics": ["Basic greetings and introductions", "Common business phrases", "Job titles and workplace etiquette"],
                    "activity": "Practice introducing yourself professionally",
                    "content": "Welcome to Business English! This course will help you master professional communication skills. In this lesson, you'll learn the fundamentals of professional interactions, including proper greetings, introductions, and essential business vocabulary."
                },
                {
                    "id": 2,
                    "day": 2,
                    "title": "Conversational English Fundamentals",
                    "topics": ["Basic conversations for everyday situations", "Key phrases for polite conversation"],
                    "activity": "Role-playing basic conversations",
                    "content": "Master the art of small talk and professional conversations in various business settings. Learn how to maintain engaging conversations while being professional and courteous."
                }
            ]
        },
        {
            "week": 2,
            "title": "Workplace Communication",
            "lessons": [
                {
                    "id": 3,
                    "day": 1,
                    "title": "Email Writing in Business",
                    "topics": ["Professional email structure", "Writing formal and informal emails"],
                    "activity": "Write and reply to sample emails",
                    "content": "Learn to write clear, professional emails that get results in business environments. Master email etiquette, structure, and tone for different business situations."
                },
                {
                    "id": 4,
                    "day": 2,
                    "title": "Making Phone Calls and Presenting Ideas",
                    "topics": ["Business phone call phrases", "Presenting information clearly"],
                    "activity": "Role-play phone conversations",
                    "content": "Develop confidence in phone communication and presenting ideas effectively. Learn professional phone etiquette and presentation skills for business success."
                }
            ]
        }
    ]
};

// Achievements Data
const achievementsData = [
    {"id": 1, "name": "First Steps", "description": "Complete your first lesson", "icon": "🎯"},
    {"id": 2, "name": "Week Warrior", "description": "Complete a full week of lessons", "icon": "💪"},
    {"id": 3, "name": "Quiz Master", "description": "Score 100% on any quiz", "icon": "🏆"},
    {"id": 4, "name": "Streak Starter", "description": "Study for 7 consecutive days", "icon": "🔥"},
    {"id": 5, "name": "AI Helper", "description": "Ask VSK AI your first question", "icon": "🤖"},
    {"id": 6, "name": "Community Member", "description": "Make your first forum post", "icon": "👥"}
];

// Quiz Questions Data
const quizQuestions = {
    1: [
        {
            question: "What is the most appropriate way to introduce yourself in a business meeting?",
            options: [
                "Hi, I'm John",
                "Good morning, I'm John Smith from Marketing",
                "Hey there, John here",
                "What's up, I'm John"
            ],
            correct: 1
        },
        {
            question: "Which phrase is most professional for ending a business conversation?",
            options: [
                "See ya later",
                "It was a pleasure meeting you",
                "Bye bye",
                "Catch you later"
            ],
            correct: 1
        },
        {
            question: "What does 'workplace etiquette' mean?",
            options: [
                "Office decoration",
                "Professional behavior and manners",
                "Work schedule",
                "Company policies"
            ],
            correct: 1
        }
    ],
    2: [
        {
            question: "What is small talk in business contexts?",
            options: [
                "Important business discussions",
                "Light, casual conversation to build rapport",
                "Confidential information",
                "Technical jargon"
            ],
            correct: 1
        }
    ],
    3: [
        {
            question: "What should be the first line of a formal business email?",
            options: [
                "Hey!",
                "Dear [Name],",
                "Hi there,",
                "What's up?"
            ],
            correct: 1
        }
    ],
    4: [
        {
            question: "When making a business phone call, you should:",
            options: [
                "Speak as fast as possible",
                "Speak clearly and at a moderate pace",
                "Use only informal language",
                "Never introduce yourself"
            ],
            correct: 1
        }
    ]
};

// Chatbot Configuration - Enhanced with fallback responses
const GOOGLE_AI_API_KEY = 'AIzaSyDWsCMHcwldKR9cKROTGRIMmXD_OwUzv90';

// VSK AI Response Database for offline functionality
const vskAIResponses = {
    greetings: [
        "Hello! I'm VSK AI, your English learning assistant. How can I help you improve your English today? 😊",
        "Hi there! Ready to learn some English? I'm here to help with grammar, vocabulary, and business communication! 🎓"
    ],
    grammar: [
        "Great grammar question! Here are some tips: Remember that in business English, clarity is key. Use simple present tense for facts, present continuous for ongoing actions, and past tense for completed actions. Would you like me to explain a specific grammar rule? 📚",
        "Grammar is the foundation of good communication! For business English, focus on: 1) Subject-verb agreement, 2) Proper tense usage, 3) Clear sentence structure. What specific grammar area would you like to practice? 💪"
    ],
    vocabulary: [
        "Building vocabulary is essential! For business English, focus on: professional greetings, meeting phrases, email expressions, and presentation language. Try using new words in sentences to remember them better! 🔤",
        "Vocabulary tip: Learn words in context! Instead of memorizing isolated words, learn phrases like 'I'd like to schedule a meeting' or 'Could you please clarify...'. This makes your English sound more natural! ✨"
    ],
    pronunciation: [
        "Pronunciation tips for business English: 1) Speak clearly and slowly, 2) Practice common business phrases, 3) Focus on word stress, 4) Record yourself speaking. Remember, clarity is more important than perfect accent! 🎯",
        "For better pronunciation: Practice with tongue twisters, listen to business podcasts, and don't be afraid to ask people to repeat. Confidence is key in business communication! 🗣️"
    ],
    business: [
        "Business English essentials: 1) Professional greetings ('Good morning, how are you?'), 2) Polite requests ('Could you please...'), 3) Clear communication ('I'd like to clarify...'). Practice these daily! 💼",
        "In business settings, remember: Be polite, be clear, be concise. Use phrases like 'Thank you for your time', 'I appreciate your help', and 'Please let me know if you have questions'. Professional courtesy goes a long way! 🤝"
    ],
    encouragement: [
        "You're doing great! Learning English takes practice and patience. Every conversation is a chance to improve! Keep up the excellent work! 🌟",
        "Remember, making mistakes is part of learning! Even native speakers make errors. The important thing is to keep practicing and stay confident! 💪",
        "Your English journey is unique! Celebrate small wins, be patient with yourself, and remember that fluency comes with time and practice! 🎉"
    ],
    default: [
        "That's an interesting question! For business English, I recommend focusing on clear communication, professional tone, and practical phrases you can use in meetings and emails. What specific area would you like to work on? 🤔",
        "I'm here to help with your English learning! Whether it's grammar, vocabulary, pronunciation, or business communication - just ask! Every question helps you improve! 📈"
    ]
};

// Initialize Application
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
    loadUserData();
    renderDashboard();
    renderCourseModules();
    renderAchievements();
    setupEventListeners();
});

function initializeApp() {
    // Load any saved progress from localStorage
    const savedProgress = localStorage.getItem('englishLMSProgress');
    if (savedProgress) {
        try {
            const progress = JSON.parse(savedProgress);
            appState.userProgress = { ...appState.userProgress, ...progress };
            appState.completedLessons = new Set(progress.completedLessons || []);
        } catch (e) {
            console.log('No saved progress found');
        }
    }
}

function saveUserData() {
    const progressData = {
        ...appState.userProgress,
        completedLessons: Array.from(appState.completedLessons)
    };
    localStorage.setItem('englishLMSProgress', JSON.stringify(progressData));
}

function loadUserData() {
    // Update dashboard stats
    updateDashboardStats();
}

// Navigation Functions
function showSection(sectionId) {
    // Hide all sections
    document.querySelectorAll('.section').forEach(section => {
        section.classList.remove('active');
    });
    
    // Show target section
    const targetSection = document.getElementById(sectionId);
    if (targetSection) {
        targetSection.classList.add('active');
        targetSection.classList.add('fade-in');
    }
    
    // Update navigation buttons
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    const activeBtn = document.querySelector(`[data-section="${sectionId}"]`);
    if (activeBtn) {
        activeBtn.classList.add('active');
    }
    
    appState.currentSection = sectionId;
}

function setupEventListeners() {
    // Navigation buttons
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const section = btn.getAttribute('data-section');
            showSection(section);
        });
    });

    // Chatbot input
    const chatbotInput = document.getElementById('chatbot-input');
    if (chatbotInput) {
        chatbotInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }
}

// Dashboard Functions
function updateDashboardStats() {
    document.getElementById('completed-lessons').textContent = appState.userProgress.completedCount;
    document.getElementById('study-streak').textContent = appState.userProgress.studyStreak;
    document.getElementById('achievements-count').textContent = appState.userProgress.achievements.size;
    
    // Update progress bar
    const progressPercentage = (appState.userProgress.completedCount / appState.userProgress.totalLessons) * 100;
    document.getElementById('course-progress').textContent = Math.round(progressPercentage) + '%';
    document.getElementById('progress-fill').style.width = progressPercentage + '%';
}

function renderDashboard() {
    updateDashboardStats();
    renderRecentAchievements();
}

function renderRecentAchievements() {
    const achievementsContainer = document.getElementById('recent-achievements');
    const recentAchievements = Array.from(appState.userProgress.achievements)
        .map(id => achievementsData.find(a => a.id === id))
        .filter(Boolean)
        .slice(-3);
    
    if (recentAchievements.length === 0) {
        achievementsContainer.innerHTML = '<p class="no-achievements">Start learning to earn your first achievement!</p>';
        return;
    }
    
    achievementsContainer.innerHTML = recentAchievements.map(achievement => `
        <div class="achievement-item">
            <div class="achievement-icon">${achievement.icon}</div>
            <div class="achievement-info">
                <h4>${achievement.name}</h4>
                <p>${achievement.description}</p>
            </div>
        </div>
    `).join('');
}

// Course Functions
function renderCourseModules() {
    const modulesList = document.getElementById('modules-list');
    
    modulesList.innerHTML = courseData.weeks.map(week => `
        <div class="module-item">
            <div class="module-header" onclick="toggleModule(${week.week})">
                <span>Week ${week.week}: ${week.title}</span>
                <span class="module-toggle">▼</span>
            </div>
            <div class="lesson-list" id="module-${week.week}">
                ${week.lessons.map(lesson => `
                    <div class="lesson-item ${appState.completedLessons.has(lesson.id) ? 'completed' : ''}" 
                         onclick="loadLesson(${lesson.id})">
                        ${appState.completedLessons.has(lesson.id) ? '✓' : '○'} ${lesson.title}
                    </div>
                `).join('')}
            </div>
        </div>
    `).join('');
}

function toggleModule(weekNumber) {
    const moduleContent = document.getElementById(`module-${weekNumber}`);
    moduleContent.classList.toggle('expanded');
    
    const toggleIcon = moduleContent.parentElement.querySelector('.module-toggle');
    toggleIcon.textContent = moduleContent.classList.contains('expanded') ? '▲' : '▼';
}

function loadLesson(lessonId) {
    // Find the lesson
    let lesson = null;
    for (const week of courseData.weeks) {
        lesson = week.lessons.find(l => l.id === lessonId);
        if (lesson) break;
    }
    
    if (!lesson) return;
    
    appState.currentLesson = lessonId;
    
    // Update active lesson in sidebar
    document.querySelectorAll('.lesson-item').forEach(item => {
        item.classList.remove('active');
    });
    event.target.classList.add('active');
    
    // Render lesson content
    const lessonContent = document.getElementById('lesson-content');
    lessonContent.innerHTML = `
        <h2>${lesson.title}</h2>
        <p>${lesson.content}</p>
        
        <div class="lesson-topics">
            <h4>📝 Topics Covered:</h4>
            <ul>
                ${lesson.topics.map(topic => `<li>${topic}</li>`).join('')}
            </ul>
        </div>
        
        <div class="lesson-topics">
            <h4>🎯 Activity:</h4>
            <p>${lesson.activity}</p>
        </div>
        
        <div class="lesson-actions">
            <button class="btn btn--primary" onclick="completeLesson(${lessonId})">
                ${appState.completedLessons.has(lessonId) ? 'Lesson Completed ✓' : 'Mark as Complete'}
            </button>
            <button class="btn btn--outline" onclick="startQuiz(${lessonId})">Take Quiz 📝</button>
        </div>
    `;
}

function completeLesson(lessonId) {
    if (!appState.completedLessons.has(lessonId)) {
        appState.completedLessons.add(lessonId);
        appState.userProgress.completedCount++;
        
        // Check for achievements
        checkAchievements();
        
        // Update UI
        renderCourseModules();
        updateDashboardStats();
        saveUserData();
        
        // Show completion notification
        showNotification('Lesson completed! 🎉', 'success');
        
        // Update lesson button
        const button = event.target;
        button.textContent = 'Lesson Completed ✓';
        button.disabled = true;
    }
}

// Quiz Functions
function startQuiz(lessonId) {
    const questions = quizQuestions[lessonId];
    if (!questions) {
        showNotification('Quiz not available for this lesson yet.', 'info');
        return;
    }
    
    appState.quiz = {
        currentQuestion: 0,
        questions: questions,
        userAnswers: [],
        score: 0
    };
    
    document.getElementById('quiz-modal').classList.remove('hidden');
    renderQuizQuestion();
}

function renderQuizQuestion() {
    const quiz = appState.quiz;
    const question = quiz.questions[quiz.currentQuestion];
    
    document.getElementById('quiz-title').textContent = `Lesson ${appState.currentLesson} Quiz`;
    document.getElementById('quiz-progress').textContent = `Question ${quiz.currentQuestion + 1} of ${quiz.questions.length}`;
    
    const progressPercentage = ((quiz.currentQuestion + 1) / quiz.questions.length) * 100;
    document.getElementById('quiz-progress-fill').style.width = progressPercentage + '%';
    
    document.getElementById('quiz-question').innerHTML = `
        <div class="question-text">${question.question}</div>
        <div class="quiz-options">
            ${question.options.map((option, index) => `
                <div class="quiz-option" onclick="selectAnswer(${index})">
                    ${option}
                </div>
            `).join('')}
        </div>
    `;
}

function selectAnswer(answerIndex) {
    // Remove previous selection
    document.querySelectorAll('.quiz-option').forEach(option => {
        option.classList.remove('selected');
    });
    
    // Mark selected answer
    event.target.classList.add('selected');
    appState.quiz.selectedAnswer = answerIndex;
}

function submitAnswer() {
    if (appState.quiz.selectedAnswer === undefined) {
        showNotification('Please select an answer.', 'warning');
        return;
    }
    
    const quiz = appState.quiz;
    const question = quiz.questions[quiz.currentQuestion];
    const isCorrect = quiz.selectedAnswer === question.correct;
    
    quiz.userAnswers.push({
        question: quiz.currentQuestion,
        answer: quiz.selectedAnswer,
        correct: isCorrect
    });
    
    if (isCorrect) {
        quiz.score++;
    }
    
    // Show correct answer
    document.querySelectorAll('.quiz-option').forEach((option, index) => {
        if (index === question.correct) {
            option.classList.add('correct');
        } else if (index === quiz.selectedAnswer && !isCorrect) {
            option.classList.add('incorrect');
        }
    });
    
    // Update buttons
    document.getElementById('quiz-submit').classList.add('hidden');
    
    if (quiz.currentQuestion < quiz.questions.length - 1) {
        document.getElementById('quiz-next').classList.remove('hidden');
    } else {
        // Show finish button
        document.getElementById('quiz-next').textContent = 'Finish Quiz';
        document.getElementById('quiz-next').classList.remove('hidden');
    }
}

function nextQuestion() {
    const quiz = appState.quiz;
    
    if (quiz.currentQuestion < quiz.questions.length - 1) {
        quiz.currentQuestion++;
        quiz.selectedAnswer = undefined;
        
        // Reset buttons
        document.getElementById('quiz-submit').classList.remove('hidden');
        document.getElementById('quiz-next').classList.add('hidden');
        
        renderQuizQuestion();
    } else {
        finishQuiz();
    }
}

function finishQuiz() {
    const quiz = appState.quiz;
    const scorePercentage = Math.round((quiz.score / quiz.questions.length) * 100);
    
    // Save quiz score
    appState.userProgress.quizScores.push(scorePercentage);
    
    // Check for perfect score achievement
    if (scorePercentage === 100) {
        addAchievement(3); // Quiz Master achievement
    }
    
    // Show results
    document.getElementById('quiz-question').innerHTML = `
        <div class="quiz-results">
            <h3>Quiz Complete! 🎉</h3>
            <div class="score-display">
                <span class="score-number">${scorePercentage}%</span>
                <span class="score-text">Score</span>
            </div>
            <p>You got ${quiz.score} out of ${quiz.questions.length} questions correct.</p>
            <div class="score-message">
                ${scorePercentage >= 80 ? 'Excellent work! 🌟' : 
                  scorePercentage >= 60 ? 'Good job! Keep practicing! 👍' : 
                  'Keep studying and try again! 💪'}
            </div>
        </div>
    `;
    
    // Update buttons
    document.getElementById('quiz-submit').classList.add('hidden');
    document.getElementById('quiz-next').textContent = 'Close';
    document.getElementById('quiz-next').onclick = closeQuiz;
    
    saveUserData();
    updateProgressStats();
}

function closeQuiz() {
    document.getElementById('quiz-modal').classList.add('hidden');
    // Reset quiz state
    appState.quiz = {
        currentQuestion: 0,
        questions: [],
        userAnswers: [],
        score: 0
    };
}

// Achievement Functions
function checkAchievements() {
    // First Steps - Complete first lesson
    if (appState.completedLessons.size === 1) {
        addAchievement(1);
    }
    
    // Week Warrior - Complete a full week (2 lessons)
    if (appState.completedLessons.size >= 2) {
        addAchievement(2);
    }
}

function addAchievement(achievementId) {
    if (!appState.userProgress.achievements.has(achievementId)) {
        appState.userProgress.achievements.add(achievementId);
        const achievement = achievementsData.find(a => a.id === achievementId);
        if (achievement) {
            showNotification(`Achievement Unlocked: ${achievement.name} ${achievement.icon}`, 'success');
        }
        renderRecentAchievements();
        updateDashboardStats();
        saveUserData();
    }
}

function renderAchievements() {
    const achievementsContainer = document.getElementById('all-achievements');
    
    achievementsContainer.innerHTML = achievementsData.map(achievement => {
        const isEarned = appState.userProgress.achievements.has(achievement.id);
        return `
            <div class="achievement-badge ${isEarned ? 'earned' : 'locked'}">
                <span class="achievement-icon">${achievement.icon}</span>
                <div class="achievement-info">
                    <h4>${achievement.name}</h4>
                    <p>${achievement.description}</p>
                </div>
            </div>
        `;
    }).join('');
}

function updateProgressStats() {
    // Update progress section stats
    document.getElementById('completed-count').textContent = appState.userProgress.completedCount;
    
    if (appState.userProgress.quizScores.length > 0) {
        const average = Math.round(
            appState.userProgress.quizScores.reduce((a, b) => a + b, 0) / appState.userProgress.quizScores.length
        );
        document.getElementById('quiz-average').textContent = average + '%';
    }
    
    // Update profile stats
    document.getElementById('profile-lessons').textContent = appState.userProgress.completedCount;
    document.getElementById('profile-streak').textContent = appState.userProgress.studyStreak;
    document.getElementById('profile-achievements').textContent = appState.userProgress.achievements.size;
}

// Forum Functions
function showNewPostForm() {
    document.getElementById('new-post-form').classList.remove('hidden');
}

function hideNewPostForm() {
    document.getElementById('new-post-form').classList.add('hidden');
    document.getElementById('post-title').value = '';
    document.getElementById('post-content').value = '';
}

function submitPost() {
    const title = document.getElementById('post-title').value.trim();
    const content = document.getElementById('post-content').value.trim();
    
    if (!title || !content) {
        showNotification('Please fill in both title and content.', 'warning');
        return;
    }
    
    // Create new post element
    const postHTML = `
        <div class="forum-post card">
            <div class="card__body">
                <div class="post-header">
                    <h4>${title}</h4>
                    <span class="post-meta">By You • Just now</span>
                </div>
                <p>${content}</p>
                <div class="post-actions">
                    <button class="btn btn--sm btn--outline">👍 Like (0)</button>
                    <button class="btn btn--sm btn--outline">💬 Reply</button>
                </div>
            </div>
        </div>
    `;
    
    // Add to forum posts
    const forumPosts = document.getElementById('forum-posts');
    forumPosts.insertAdjacentHTML('afterbegin', postHTML);
    
    // Check for first post achievement
    addAchievement(6);
    
    hideNewPostForm();
    showNotification('Post created successfully! 🎉', 'success');
}

// Enhanced Chatbot Functions
function toggleChatbot() {
    const chatbotWindow = document.getElementById('chatbot-window');
    const isHidden = chatbotWindow.classList.contains('hidden');
    
    if (isHidden) {
        chatbotWindow.classList.remove('hidden');
        appState.chatbot.isOpen = true;
        
        // Check for first AI interaction achievement
        if (appState.chatbot.messages.length === 0) {
            addAchievement(5);
        }
    } else {
        chatbotWindow.classList.add('hidden');
        appState.chatbot.isOpen = false;
    }
}

async function sendMessage() {
    const input = document.getElementById('chatbot-input');
    const message = input.value.trim();
    
    if (!message) return;
    
    // Add user message to chat
    addMessageToChat(message, 'user');
    input.value = '';
    
    // Show typing indicator
    showTypingIndicator();
    
    // Try Google AI API first, fallback to local responses
    try {
        const response = await callGoogleAI(message);
        hideTypingIndicator();
        addMessageToChat(response, 'bot');
    } catch (error) {
        console.log('Google AI API unavailable, using local responses');
        hideTypingIndicator();
        
        // Use intelligent local response system
        const response = getVSKAIResponse(message);
        setTimeout(() => {
            addMessageToChat(response, 'bot');
        }, 1000); // Simulate thinking time
    }
}

function getVSKAIResponse(userMessage) {
    const message = userMessage.toLowerCase();
    
    // Check for specific keywords and return appropriate responses
    if (message.includes('hello') || message.includes('hi') || message.includes('hey') || message === '') {
        return getRandomResponse(vskAIResponses.greetings);
    }
    
    if (message.includes('grammar') || message.includes('tense') || message.includes('verb') || message.includes('sentence')) {
        return getRandomResponse(vskAIResponses.grammar);
    }
    
    if (message.includes('vocabulary') || message.includes('word') || message.includes('meaning') || message.includes('define')) {
        return getRandomResponse(vskAIResponses.vocabulary);
    }
    
    if (message.includes('pronunciation') || message.includes('pronounce') || message.includes('accent') || message.includes('speak')) {
        return getRandomResponse(vskAIResponses.pronunciation);
    }
    
    if (message.includes('business') || message.includes('professional') || message.includes('meeting') || message.includes('email') || message.includes('presentation')) {
        return getRandomResponse(vskAIResponses.business);
    }
    
    if (message.includes('help') || message.includes('learn') || message.includes('study') || message.includes('practice')) {
        return getRandomResponse(vskAIResponses.encouragement);
    }
    
    if (message.includes('thank') || message.includes('good') || message.includes('great')) {
        return "You're very welcome! I'm glad I could help. Keep up the excellent work with your English learning! 😊 Is there anything else you'd like to practice?";
    }
    
    // Default response for unrecognized input
    return getRandomResponse(vskAIResponses.default);
}

function getRandomResponse(responseArray) {
    return responseArray[Math.floor(Math.random() * responseArray.length)];
}

function addMessageToChat(message, sender) {
    const messagesContainer = document.getElementById('chatbot-messages');
    const messageHTML = `
        <div class="message ${sender}-message">
            <div class="message-content">
                <p>${message}</p>
            </div>
        </div>
    `;
    
    messagesContainer.insertAdjacentHTML('beforeend', messageHTML);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
    
    // Save to state
    appState.chatbot.messages.push({ message, sender, timestamp: Date.now() });
}

function showTypingIndicator() {
    document.getElementById('typing-indicator').classList.remove('hidden');
    const messagesContainer = document.getElementById('chatbot-messages');
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function hideTypingIndicator() {
    document.getElementById('typing-indicator').classList.add('hidden');
}

async function callGoogleAI(userMessage) {
    const prompt = `You are VSK AI, a friendly and encouraging English learning assistant. Your role is to help students learn English, particularly business English. You should:

1. Answer questions about grammar, vocabulary, pronunciation, and business communication
2. Provide explanations in simple, clear language
3. Be encouraging and supportive
4. Give practical examples
5. Keep responses concise but helpful
6. Use emojis sparingly and appropriately

User question: ${userMessage}

Please provide a helpful response:`;

    const requestBody = {
        contents: [{
            parts: [{
                text: prompt
            }]
        }]
    };

    const GOOGLE_AI_URL = `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${GOOGLE_AI_API_KEY}`;

    const response = await fetch(GOOGLE_AI_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
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

// Utility Functions
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification--${type}`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: var(--color-surface);
        border: 1px solid var(--color-border);
        border-radius: var(--radius-base);
        padding: var(--space-16);
        box-shadow: var(--shadow-lg);
        z-index: 1002;
        max-width: 300px;
        animation: slideIn 0.3s ease-out;
    `;
    
    // Set colors based on type
    const colors = {
        success: 'var(--color-success)',
        error: 'var(--color-error)',
        warning: 'var(--color-warning)',
        info: 'var(--color-info)'
    };
    
    notification.style.borderLeftColor = colors[type];
    notification.style.borderLeftWidth = '4px';
    
    notification.innerHTML = `
        <div style="display: flex; align-items: center; gap: var(--space-8);">
            <span>${message}</span>
            <button onclick="this.parentElement.parentElement.remove()" 
                    style="background: none; border: none; cursor: pointer; font-size: 18px; color: var(--color-text-secondary);">×</button>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentElement) {
            notification.remove();
        }
    }, 5000);
}

// Add CSS for notification animation
const notificationStyles = document.createElement('style');
notificationStyles.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
`;
document.head.appendChild(notificationStyles);

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    // Set initial progress stats
    updateProgressStats();
});