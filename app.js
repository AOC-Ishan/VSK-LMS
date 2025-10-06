// LMS Application JavaScript

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
                        <h3>Welcome to Business English!</h3>
                        <p>In this first lesson, we'll cover the fundamentals of professional communication in English. You'll learn how to introduce yourself confidently in business settings.</p>
                        
                        <h4>Key Learning Points:</h4>
                        <ul>
                            <li><strong>Professional Greetings:</strong> "Good morning/afternoon", "How do you do?", "Pleased to meet you"</li>
                            <li><strong>Self-Introduction:</strong> "My name is...", "I work for...", "I'm responsible for..."</li>
                            <li><strong>Job Titles:</strong> Manager, Director, Assistant, Coordinator, Analyst</li>
                            <li><strong>Workplace Etiquette:</strong> Punctuality, dress code, communication style</li>
                        </ul>
                        
                        <h4>Example Dialogue:</h4>
                        <div style="background: var(--color-bg-2); padding: 16px; border-radius: 8px; margin: 16px 0;">
                            <p><strong>Person A:</strong> "Good morning! I'm Sarah Johnson from the Marketing Department."</p>
                            <p><strong>Person B:</strong> "Pleased to meet you, Sarah. I'm Michael Chen, the new project coordinator."</p>
                            <p><strong>Person A:</strong> "Welcome to the team, Michael! How are you finding everything so far?"</p>
                        </div>
                        
                        <h4>Practice Exercise:</h4>
                        <p>Try introducing yourself using the format: "Good [morning/afternoon], I'm [your name]. I work as a [job title] at [company/department]."</p>
                    `
                },
                {
                    id: 2,
                    day: 2,
                    title: "Conversational English Fundamentals",
                    topics: ["Basic conversations for everyday situations", "Key phrases for polite conversation"],
                    activity: "Role-playing basic conversations",
                    content: `
                        <h3>Mastering Everyday Business Conversations</h3>
                        <p>Building on our introduction skills, let's explore how to maintain professional conversations in various business situations.</p>
                        
                        <h4>Essential Conversation Starters:</h4>
                        <ul>
                            <li>"How was your weekend?"</li>
                            <li>"Did you see the latest company announcement?"</li>
                            <li>"How's the project coming along?"</li>
                            <li>"Have you had a chance to review the proposal?"</li>
                        </ul>
                        
                        <h4>Polite Conversation Techniques:</h4>
                        <ul>
                            <li><strong>Active Listening:</strong> "That's interesting", "I see your point", "Could you tell me more about that?"</li>
                            <li><strong>Showing Interest:</strong> "Really?", "How fascinating!", "I hadn't thought of it that way"</li>
                            <li><strong>Transitioning Topics:</strong> "Speaking of which...", "That reminds me...", "On a related note..."</li>
                        </ul>
                        
                        <h4>Cultural Considerations:</h4>
                        <p>Remember that business conversations should maintain a professional tone while being friendly and approachable. Avoid overly personal topics in initial conversations.</p>
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
                        <h3>Professional Email Communication</h3>
                        <p>Email is one of the most important communication tools in modern business. Let's learn how to write clear, professional emails that get results.</p>
                        
                        <h4>Email Structure:</h4>
                        <ol>
                            <li><strong>Subject Line:</strong> Clear and specific</li>
                            <li><strong>Greeting:</strong> Dear Mr./Ms. [Name] or Hello [Name]</li>
                            <li><strong>Opening:</strong> State your purpose</li>
                            <li><strong>Body:</strong> Main message with details</li>
                            <li><strong>Closing:</strong> Next steps or call to action</li>
                            <li><strong>Sign-off:</strong> Best regards, Sincerely, etc.</li>
                        </ol>
                        
                        <h4>Formal vs. Informal Emails:</h4>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">
                            <div style="background: var(--color-bg-1); padding: 16px; border-radius: 8px;">
                                <h5>Formal Email</h5>
                                <p><strong>Subject:</strong> Meeting Request - Q4 Budget Review</p>
                                <p><strong>Greeting:</strong> Dear Ms. Anderson,</p>
                                <p><strong>Body:</strong> I would like to request a meeting to discuss...</p>
                                <p><strong>Sign-off:</strong> Sincerely, John Smith</p>
                            </div>
                            <div style="background: var(--color-bg-3); padding: 16px; border-radius: 8px;">
                                <h5>Informal Email</h5>
                                <p><strong>Subject:</strong> Quick question about the presentation</p>
                                <p><strong>Greeting:</strong> Hi Sarah,</p>
                                <p><strong>Body:</strong> Hope you're doing well! I wanted to ask...</p>
                                <p><strong>Sign-off:</strong> Thanks, John</p>
                            </div>
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
                        <h3>Effective Phone Communication and Presentations</h3>
                        <p>Phone calls and presentations are crucial skills in business. Let's learn how to communicate clearly and confidently.</p>
                        
                        <h4>Phone Call Structure:</h4>
                        <ul>
                            <li><strong>Opening:</strong> "Good morning, this is [Name] from [Company]"</li>
                            <li><strong>Purpose:</strong> "I'm calling about..." or "The reason for my call is..."</li>
                            <li><strong>Discussion:</strong> Main points with clear structure</li>
                            <li><strong>Closing:</strong> "Thank you for your time" and next steps</li>
                        </ul>
                        
                        <h4>Presentation Basics:</h4>
                        <ul>
                            <li><strong>Introduction:</strong> "Today I'd like to talk about..."</li>
                            <li><strong>Overview:</strong> "I'll cover three main points..."</li>
                            <li><strong>Main Content:</strong> "First, let me explain..."</li>
                            <li><strong>Conclusion:</strong> "To summarize..." and "Are there any questions?"</li>
                        </ul>
                        
                        <h4>Common Phone Phrases:</h4>
                        <ul>
                            <li>"Could you please hold for a moment?"</li>
                            <li>"I'm sorry, could you repeat that?"</li>
                            <li>"Let me transfer you to..."</li>
                            <li>"Thank you for calling, have a great day!"</li>
                        </ul>
                    `
                }
            ]
        }
    ]
};

// Sample quiz data
const quizData = {
    1: {
        id: 1,
        title: "Business Greetings Quiz",
        lessonId: 1,
        questions: [
            {
                id: 1,
                question: "What is the most formal way to greet someone in a business meeting?",
                type: "multiple-choice",
                options: ["Hi there!", "Good morning, Mr. Smith", "Hey!", "What's up?"],
                correct: 1,
                explanation: "Using titles and formal greetings shows professionalism in business settings."
            },
            {
                id: 2,
                question: "Complete the sentence: 'It's a _____ to meet you.'",
                type: "fill-blank",
                answer: "pleasure",
                explanation: "This is a standard polite phrase used when meeting someone for the first time."
            },
            {
                id: 3,
                question: "In business introductions, you should always mention your job title.",
                type: "true-false",
                correct: true,
                explanation: "Mentioning your job title helps establish context and credibility in business settings."
            }
        ]
    }
};

// Achievement data
const achievements = [
    {id: 1, name: "First Steps", description: "Complete your first lesson", icon: "🎯", earned: false},
    {id: 2, name: "Week Warrior", description: "Complete a full week of lessons", icon: "💪", earned: false},
    {id: 3, name: "Quiz Master", description: "Score 100% on any quiz", icon: "🏆", earned: false},
    {id: 4, name: "Streak Starter", description: "Study for 7 consecutive days", icon: "🔥", earned: false}
];

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
    updateDashboard();
    renderCourseModules();
    renderForumPosts('general');
    updateProgressView();
    updateProfileView();
});

// Initialize application
function initializeApp() {
    // Set up navigation
    const navLinks = document.querySelectorAll('.nav__link, [data-view]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const view = this.getAttribute('data-view');
            if (view) {
                navigateToView(view);
            }
        });
    });
    
    // Set up quiz form submission
    const newTopicForm = document.getElementById('newTopicForm');
    if (newTopicForm) {
        newTopicForm.addEventListener('submit', function(e) {
            e.preventDefault();
            submitNewTopic();
        });
    }
}

// Navigation functionality
function navigateToView(viewName) {
    // Update active nav link
    document.querySelectorAll('.nav__link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('data-view') === viewName) {
            link.classList.add('active');
        }
    });
    
    // Show/hide views
    document.querySelectorAll('.view').forEach(view => {
        view.classList.remove('active');
    });
    
    const targetView = document.getElementById(viewName);
    if (targetView) {
        targetView.classList.add('active');
        appState.currentView = viewName;
    }
    
    // Update view-specific content
    if (viewName === 'progress') {
        updateProgressView();
    } else if (viewName === 'profile') {
        updateProfileView();
    }
}

// Update dashboard content
function updateDashboard() {
    // Update stats
    document.getElementById('completedLessons').textContent = appState.userProgress.completedLessons;
    document.getElementById('streakDays').textContent = appState.userProgress.streakDays;
    document.getElementById('totalBadges').textContent = appState.userProgress.badges.length;
    
    // Update week progress
    const weekProgress = (appState.userProgress.completedLessons % 4) * 25; // 4 lessons per week
    document.getElementById('weekProgress').style.width = weekProgress + '%';
    
    // Render featured lessons
    renderFeaturedLessons();
}

// Render featured lessons
function renderFeaturedLessons() {
    const container = document.getElementById('featuredLessons');
    const featuredLessons = courseData.weeks.slice(0, 2).flatMap(week => 
        week.lessons.map(lesson => ({ ...lesson, weekTitle: week.title }))
    );
    
    container.innerHTML = featuredLessons.map(lesson => `
        <div class="lesson-card" onclick="openLesson(${lesson.id})">
            <h4>${lesson.title}</h4>
            <p>${lesson.topics.slice(0, 2).join(', ')}...</p>
            <div class="lesson-meta">
                <span>📅 Week ${Math.ceil(lesson.id / 2)}</span>
                <span>⏱️ 45 min</span>
                <span class="lesson-status ${getLessonStatus(lesson.id)}">${getLessonStatusText(lesson.id)}</span>
            </div>
        </div>
    `).join('');
}

// Get lesson status
function getLessonStatus(lessonId) {
    if (appState.userProgress.completedLessons >= lessonId) return 'completed';
    if (appState.userProgress.completedLessons + 1 === lessonId) return 'in-progress';
    return 'locked';
}

function getLessonStatusText(lessonId) {
    const status = getLessonStatus(lessonId);
    switch (status) {
        case 'completed': return '✅ Completed';
        case 'in-progress': return '📖 Available';
        case 'locked': return '🔒 Locked';
        default: return 'Available';
    }
}

// Render course modules
function renderCourseModules() {
    const container = document.getElementById('courseModules');
    
    container.innerHTML = courseData.weeks.map(week => `
        <div class="week-module">
            <div class="week-header">
                <h3>Week ${week.week}: ${week.title}</h3>
            </div>
            <div class="week-lessons">
                ${week.lessons.map(lesson => `
                    <div class="lesson-item" onclick="openLesson(${lesson.id})">
                        <div class="lesson-info">
                            <h4>${lesson.title}</h4>
                            <div class="lesson-topics">${lesson.topics.join(' • ')}</div>
                        </div>
                        <div class="lesson-status ${getLessonStatus(lesson.id)}">
                            ${getLessonStatusText(lesson.id)}
                        </div>
                    </div>
                `).join('')}
            </div>
        </div>
    `).join('');
}

// Open lesson interface
function openLesson(lessonId) {
    const lesson = findLessonById(lessonId);
    if (!lesson) return;
    
    // Check if lesson is accessible
    if (getLessonStatus(lessonId) === 'locked') {
        alert('Please complete previous lessons to unlock this one.');
        return;
    }
    
    appState.currentLesson = lesson;
    
    // Update breadcrumb
    const week = Math.ceil(lessonId / 2);
    document.getElementById('lessonBreadcrumb').innerHTML = `
        <a href="#" data-view="dashboard">Dashboard</a> > 
        <a href="#" data-view="courses">Courses</a> > 
        Week ${week} > ${lesson.title}
    `;
    
    // Update lesson content
    document.getElementById('lessonTitle').textContent = lesson.title;
    document.getElementById('lessonContent').innerHTML = lesson.content;
    
    // Update navigation buttons
    const prevBtn = document.getElementById('prevLessonBtn');
    const nextBtn = document.getElementById('nextLessonBtn');
    
    prevBtn.style.display = lessonId > 1 ? 'inline-block' : 'none';
    nextBtn.style.display = lessonId < getTotalLessons() ? 'inline-block' : 'none';
    
    navigateToView('lesson');
}

// Find lesson by ID
function findLessonById(lessonId) {
    for (const week of courseData.weeks) {
        const lesson = week.lessons.find(l => l.id === lessonId);
        if (lesson) return lesson;
    }
    return null;
}

function getTotalLessons() {
    return courseData.weeks.reduce((total, week) => total + week.lessons.length, 0);
}

// Navigation between lessons
function navigateLesson(direction) {
    const currentId = appState.currentLesson.id;
    const newId = direction === 'next' ? currentId + 1 : currentId - 1;
    
    if (newId >= 1 && newId <= getTotalLessons()) {
        openLesson(newId);
    }
}

// Complete lesson
function completeLesson() {
    if (!appState.currentLesson) return;
    
    const lessonId = appState.currentLesson.id;
    
    // Update progress
    if (appState.userProgress.completedLessons < lessonId) {
        appState.userProgress.completedLessons = lessonId;
        appState.userProgress.overallProgress = Math.round((lessonId / getTotalLessons()) * 100);
        
        // Check for achievements
        checkAchievements();
        
        // Show success message
        alert('Lesson completed! Great job! 🎉');
        
        // Offer to take quiz if available
        if (quizData[lessonId]) {
            const takeQuiz = confirm('Would you like to take the quiz for this lesson?');
            if (takeQuiz) {
                startQuiz(lessonId);
            }
        }
        
        updateDashboard();
    }
}

// Save lesson notes
function saveNotes() {
    const notes = document.getElementById('lessonNotes').value;
    if (notes.trim()) {
        alert('Notes saved successfully!');
    }
}

// Start quiz
function startQuiz(lessonId) {
    const quiz = quizData[lessonId];
    if (!quiz) return;
    
    appState.currentQuiz = quiz;
    appState.quizState = {
        currentQuestion: 0,
        answers: {},
        score: 0
    };
    
    document.getElementById('quizTitle').textContent = quiz.title;
    document.getElementById('totalQuestions').textContent = quiz.questions.length;
    
    renderCurrentQuestion();
    navigateToView('quiz');
}

// Render current quiz question
function renderCurrentQuestion() {
    const quiz = appState.currentQuiz;
    const questionIndex = appState.quizState.currentQuestion;
    const question = quiz.questions[questionIndex];
    
    document.getElementById('currentQuestion').textContent = questionIndex + 1;
    
    // Update progress bar
    const progress = ((questionIndex + 1) / quiz.questions.length) * 100;
    document.getElementById('quizProgress').style.width = progress + '%';
    
    const container = document.getElementById('quizContent');
    
    let questionHtml = `
        <div class="question">
            <h3>Question ${questionIndex + 1}</h3>
            <p>${question.question}</p>
    `;
    
    if (question.type === 'multiple-choice') {
        questionHtml += '<div class="question-options">';
        question.options.forEach((option, index) => {
            questionHtml += `
                <label class="option" data-option="${index}">
                    <input type="radio" name="question${question.id}" value="${index}">
                    ${option}
                </label>
            `;
        });
        questionHtml += '</div>';
    } else if (question.type === 'fill-blank') {
        questionHtml += `
            <div class="question-options">
                <input type="text" class="form-control fill-blank-input" id="fillBlank${question.id}" placeholder="Enter your answer">
            </div>
        `;
    } else if (question.type === 'true-false') {
        questionHtml += `
            <div class="question-options">
                <label class="option" data-option="true">
                    <input type="radio" name="question${question.id}" value="true">
                    True
                </label>
                <label class="option" data-option="false">
                    <input type="radio" name="question${question.id}" value="false">
                    False
                </label>
            </div>
        `;
    }
    
    questionHtml += '</div>';
    container.innerHTML = questionHtml;
    
    // Add click handlers for options
    const options = container.querySelectorAll('.option');
    options.forEach(option => {
        option.addEventListener('click', function() {
            // Remove selected class from all options
            options.forEach(opt => opt.classList.remove('selected'));
            // Add selected class to clicked option
            this.classList.add('selected');
            // Check the radio button
            const radio = this.querySelector('input[type="radio"]');
            if (radio) radio.checked = true;
        });
    });
    
    // Update navigation buttons
    document.getElementById('prevQuestionBtn').style.display = questionIndex > 0 ? 'inline-block' : 'none';
    document.getElementById('nextQuestionBtn').style.display = questionIndex < quiz.questions.length - 1 ? 'inline-block' : 'none';
    document.getElementById('submitQuizBtn').style.display = questionIndex === quiz.questions.length - 1 ? 'inline-block' : 'none';
}

// Navigate between quiz questions
function nextQuestion() {
    saveCurrentAnswer();
    if (appState.quizState.currentQuestion < appState.currentQuiz.questions.length - 1) {
        appState.quizState.currentQuestion++;
        renderCurrentQuestion();
    }
}

function previousQuestion() {
    saveCurrentAnswer();
    if (appState.quizState.currentQuestion > 0) {
        appState.quizState.currentQuestion--;
        renderCurrentQuestion();
    }
}

// Save current answer
function saveCurrentAnswer() {
    const questionIndex = appState.quizState.currentQuestion;
    const question = appState.currentQuiz.questions[questionIndex];
    
    if (question.type === 'multiple-choice' || question.type === 'true-false') {
        const selected = document.querySelector(`input[name="question${question.id}"]:checked`);
        if (selected) {
            appState.quizState.answers[question.id] = selected.value;
        }
    } else if (question.type === 'fill-blank') {
        const input = document.getElementById(`fillBlank${question.id}`);
        if (input) {
            appState.quizState.answers[question.id] = input.value.trim().toLowerCase();
        }
    }
}

// Submit quiz
function submitQuiz() {
    saveCurrentAnswer();
    
    // Calculate score
    let correctAnswers = 0;
    const totalQuestions = appState.currentQuiz.questions.length;
    
    appState.currentQuiz.questions.forEach(question => {
        const userAnswer = appState.quizState.answers[question.id];
        let isCorrect = false;
        
        if (question.type === 'multiple-choice') {
            isCorrect = parseInt(userAnswer) === question.correct;
        } else if (question.type === 'fill-blank') {
            isCorrect = userAnswer === question.answer.toLowerCase();
        } else if (question.type === 'true-false') {
            isCorrect = (userAnswer === 'true') === question.correct;
        }
        
        if (isCorrect) correctAnswers++;
    });
    
    const score = Math.round((correctAnswers / totalQuestions) * 100);
    appState.quizState.score = score;
    
    // Check for perfect score achievement
    if (score === 100) {
        unlockAchievement(3); // Quiz Master achievement
    }
    
    showQuizResults(score, correctAnswers, totalQuestions);
}

// Show quiz results
function showQuizResults(score, correct, total) {
    const modal = document.getElementById('quizResultsModal');
    const content = document.getElementById('resultsContent');
    
    let message = '';
    if (score >= 90) message = 'Excellent work! 🎉';
    else if (score >= 70) message = 'Good job! 👍';
    else if (score >= 50) message = 'Not bad, keep practicing! 📚';
    else message = 'Keep studying and try again! 💪';
    
    content.innerHTML = `
        <div class="results-score">${score}%</div>
        <div class="results-message">${message}</div>
        <p>You got ${correct} out of ${total} questions correct.</p>
    `;
    
    modal.classList.remove('hidden');
}

// Close quiz results
function closeQuizResults() {
    document.getElementById('quizResultsModal').classList.add('hidden');
}

// Retry quiz
function retryQuiz() {
    closeQuizResults();
    appState.quizState = {
        currentQuestion: 0,
        answers: {},
        score: 0
    };
    renderCurrentQuestion();
}

// Continue to next lesson
function continueToNextLesson() {
    closeQuizResults();
    const nextLessonId = appState.currentLesson.id + 1;
    if (nextLessonId <= getTotalLessons()) {
        openLesson(nextLessonId);
    } else {
        navigateToView('courses');
    }
}

// Enroll in course
function enrollInCourse() {
    alert('Welcome to the Business English Course! Let\'s start with your first lesson.');
    openLesson(1);
}

// Check and unlock achievements
function checkAchievements() {
    // First Steps - Complete first lesson
    if (appState.userProgress.completedLessons >= 1 && !achievements[0].earned) {
        unlockAchievement(1);
    }
    
    // Week Warrior - Complete 4 lessons (1 week)
    if (appState.userProgress.completedLessons >= 4 && !achievements[1].earned) {
        unlockAchievement(2);
    }
}

function unlockAchievement(achievementId) {
    const achievement = achievements.find(a => a.id === achievementId);
    if (achievement && !achievement.earned) {
        achievement.earned = true;
        appState.userProgress.badges.push(achievement);
        
        // Show achievement notification
        alert(`🎉 Achievement Unlocked: ${achievement.name}! ${achievement.description}`);
        
        updateDashboard();
    }
}

// Update progress view
function updateProgressView() {
    // Update overall progress
    document.getElementById('overallProgress').textContent = appState.userProgress.overallProgress + '%';
    
    // Update circular progress (simplified)
    const progressCircle = document.querySelector('.circular-progress');
    if (progressCircle) {
        const percentage = appState.userProgress.overallProgress;
        progressCircle.style.background = `conic-gradient(var(--color-primary) ${percentage * 3.6}deg, var(--color-secondary) 0deg)`;
    }
    
    // Update weekly stats
    const currentWeek = Math.ceil((appState.userProgress.completedLessons + 1) / 2);
    const weekLessons = Math.min(appState.userProgress.completedLessons - ((currentWeek - 1) * 2), 2);
    document.getElementById('weekLessons').textContent = Math.max(weekLessons, 0);
    document.getElementById('weekQuizzes').textContent = Math.floor(appState.userProgress.completedLessons / 2);
    
    // Update badge showcase
    const badgeContainer = document.getElementById('badgeShowcase');
    badgeContainer.innerHTML = achievements.map(achievement => `
        <div class="badge ${achievement.earned ? 'earned' : ''}">
            <span>${achievement.icon}</span>
            <span>${achievement.name}</span>
        </div>
    `).join('');
    
    // Update weekly progress list
    renderWeeklyProgress();
}

function renderWeeklyProgress() {
    const container = document.getElementById('weekProgressList');
    
    container.innerHTML = courseData.weeks.map(week => {
        const weekLessons = week.lessons.length;
        const completedInWeek = week.lessons.filter(lesson => 
            appState.userProgress.completedLessons >= lesson.id
        ).length;
        const progressPercentage = (completedInWeek / weekLessons) * 100;
        
        return `
            <div class="week-progress-item">
                <div class="week-progress-header">
                    <h4>Week ${week.week}: ${week.title}</h4>
                    <span>${completedInWeek}/${weekLessons} lessons</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: ${progressPercentage}%"></div>
                </div>
            </div>
        `;
    }).join('');
}

// Update profile view
function updateProfileView() {
    // Update achievement gallery
    const gallery = document.getElementById('achievementGallery');
    gallery.innerHTML = achievements.map(achievement => `
        <div class="achievement-item ${achievement.earned ? 'earned' : ''}">
            <div class="achievement-icon">${achievement.icon}</div>
            <div class="achievement-name">${achievement.name}</div>
            <div class="achievement-description">${achievement.description}</div>
        </div>
    `).join('');
}

// Save profile settings
function saveProfile() {
    const studyTime = document.getElementById('studyTimeGoal').value;
    const weeklyGoal = document.getElementById('weeklyGoal').value;
    
    alert(`Profile updated! Study time goal: ${studyTime} minutes, Weekly goal: ${weeklyGoal} lessons`);
}

// Forum functionality
function renderForumPosts(category = 'general') {
    const container = document.getElementById('forumPosts');
    const filteredPosts = appState.forumPosts.filter(post => 
        category === 'all' || post.category === category
    );
    
    container.innerHTML = filteredPosts.map(post => `
        <div class="forum-post">
            <div class="post-header">
                <h4 class="post-title">${post.title}</h4>
                <div class="post-meta">
                    <span>by ${post.author}</span> • 
                    <span>${post.date}</span> • 
                    <span>${post.replies} replies</span>
                </div>
            </div>
            <div class="post-content">
                ${post.content}
            </div>
        </div>
    `).join('');
    
    // Update active category
    document.querySelectorAll('.category-card').forEach(card => {
        card.classList.remove('active');
        if (card.getAttribute('data-category') === category) {
            card.classList.add('active');
        }
    });
    
    // Add category click handlers
    document.querySelectorAll('.category-card').forEach(card => {
        card.addEventListener('click', function() {
            const category = this.getAttribute('data-category');
            renderForumPosts(category);
        });
    });
}

// Open new topic modal
function openNewTopicModal() {
    document.getElementById('newTopicModal').classList.remove('hidden');
}

// Close new topic modal
function closeNewTopicModal() {
    document.getElementById('newTopicModal').classList.add('hidden');
    document.getElementById('newTopicForm').reset();
}

// Submit new topic
function submitNewTopic() {
    const title = document.getElementById('topicTitle').value;
    const category = document.getElementById('topicCategory').value;
    const message = document.getElementById('topicMessage').value;
    
    if (!title.trim() || !message.trim()) {
        alert('Please fill in all fields');
        return;
    }
    
    // Add new post to the beginning of the array
    appState.forumPosts.unshift({
        id: appState.forumPosts.length + 1,
        title: title,
        author: "You",
        category: category,
        content: message,
        date: "Just now",
        replies: 0
    });
    
    // Close modal and refresh posts
    closeNewTopicModal();
    renderForumPosts(category);
    
    alert('Topic created successfully!');
}

// Close modals when clicking outside
window.addEventListener('click', function(e) {
    if (e.target.classList.contains('modal')) {
        e.target.classList.add('hidden');
    }
});