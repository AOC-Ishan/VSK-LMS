# Create enhanced CSS with chatbot styling

css_content = """:root {
  /* Primitive Color Tokens */
  --color-white: rgba(255, 255, 255, 1);
  --color-black: rgba(0, 0, 0, 1);
  --color-cream-50: rgba(252, 252, 249, 1);
  --color-cream-100: rgba(255, 255, 253, 1);
  --color-gray-200: rgba(245, 245, 245, 1);
  --color-gray-300: rgba(167, 169, 169, 1);
  --color-gray-400: rgba(119, 124, 124, 1);
  --color-slate-500: rgba(98, 108, 113, 1);
  --color-brown-600: rgba(94, 82, 64, 1);
  --color-charcoal-700: rgba(31, 33, 33, 1);
  --color-charcoal-800: rgba(38, 40, 40, 1);
  --color-slate-900: rgba(19, 52, 59, 1);
  --color-teal-300: rgba(50, 184, 198, 1);
  --color-teal-400: rgba(45, 166, 178, 1);
  --color-teal-500: rgba(33, 128, 141, 1);
  --color-teal-600: rgba(29, 116, 128, 1);
  --color-teal-700: rgba(26, 104, 115, 1);
  --color-teal-800: rgba(41, 150, 161, 1);
  --color-red-400: rgba(255, 84, 89, 1);
  --color-red-500: rgba(192, 21, 47, 1);
  --color-orange-400: rgba(230, 129, 97, 1);
  --color-orange-500: rgba(168, 75, 47, 1);
  --color-blue-500: rgba(59, 130, 246, 1);
  --color-green-500: rgba(34, 197, 94, 1);

  /* Semantic Color Tokens */
  --color-background: var(--color-cream-50);
  --color-surface: var(--color-cream-100);
  --color-text: var(--color-charcoal-700);
  --color-text-muted: var(--color-slate-500);
  --color-primary: var(--color-teal-600);
  --color-primary-hover: var(--color-teal-700);
  --color-success: var(--color-green-500);
  --color-error: var(--color-red-500);
}

/* Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: var(--color-text);
  background-color: var(--color-background);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Header Styles */
.header {
  background: var(--color-surface);
  padding: 1rem 0;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav__brand h2 {
  color: var(--color-primary);
  font-size: 1.5rem;
}

.nav__menu {
  display: flex;
  list-style: none;
  gap: 2rem;
}

.nav__link {
  text-decoration: none;
  color: var(--color-text);
  font-weight: 500;
  transition: color 0.3s ease;
  cursor: pointer;
}

.nav__link:hover {
  color: var(--color-primary);
}

/* View Management */
.view {
  display: none;
  min-height: calc(100vh - 80px);
}

.view.active {
  display: block;
}

/* Hero Section */
.hero {
  background: linear-gradient(135deg, var(--color-teal-600), var(--color-teal-800));
  color: white;
  padding: 4rem 0;
  text-align: center;
}

.hero__content h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.hero__content p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.hero__actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 3rem;
}

.hero__stats {
  display: flex;
  justify-content: center;
  gap: 3rem;
  margin-top: 3rem;
}

.stat-card {
  text-align: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: bold;
  display: block;
}

.stat-label {
  font-size: 0.9rem;
  opacity: 0.9;
}

/* Button Styles */
.btn {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.btn--primary {
  background-color: var(--color-primary);
  color: white;
}

.btn--primary:hover {
  background-color: var(--color-primary-hover);
  transform: translateY(-2px);
}

.btn--outline {
  background-color: transparent;
  color: var(--color-primary);
  border: 2px solid var(--color-primary);
}

.btn--outline:hover {
  background-color: var(--color-primary);
  color: white;
}

.btn--success {
  background-color: var(--color-success);
  color: white;
}

.btn--lg {
  padding: 1rem 2rem;
  font-size: 1.1rem;
}

.btn--sm {
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
}

.btn--back {
  background: none;
  color: var(--color-text-muted);
  padding: 0.5rem;
  margin-bottom: 1rem;
}

/* Quick Access Section */
.quick-access {
  padding: 4rem 0;
}

.quick-access h2 {
  text-align: center;
  margin-bottom: 3rem;
  color: var(--color-text);
}

.quick-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.quick-card {
  background: var(--color-surface);
  padding: 2rem;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
  cursor: pointer;
}

.quick-card:hover {
  transform: translateY(-5px);
}

.quick-card__icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.quick-card h3 {
  color: var(--color-text);
  margin-bottom: 0.5rem;
}

.quick-card p {
  color: var(--color-text-muted);
}

/* Course Modules */
.course-header {
  text-align: center;
  padding: 3rem 0;
}

.course-header h1 {
  color: var(--color-text);
  margin-bottom: 1rem;
}

.course-modules {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  padding-bottom: 3rem;
}

.module-card {
  background: var(--color-surface);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.module-card:hover {
  transform: translateY(-2px);
}

.module-card.completed {
  border-left: 4px solid var(--color-success);
}

.module-card.active {
  border-left: 4px solid var(--color-primary);
}

.module-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  background: rgba(0,0,0,0.02);
}

.module-info h3 {
  color: var(--color-text);
  margin-bottom: 0.5rem;
}

.module-info p {
  color: var(--color-text-muted);
  font-size: 0.9rem;
}

.status-badge {
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
}

.status-badge.completed {
  background-color: rgba(34, 197, 94, 0.1);
  color: var(--color-success);
}

.status-badge.active {
  background-color: rgba(59, 130, 246, 0.1);
  color: var(--color-blue-500);
}

.status-badge.locked {
  background-color: rgba(119, 124, 124, 0.1);
  color: var(--color-gray-400);
}

.lessons-list {
  padding: 0 1.5rem 1.5rem;
}

.lesson-item {
  display: flex;
  align-items: center;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 0.5rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.lesson-item:hover {
  background-color: rgba(0,0,0,0.05);
}

.lesson-icon {
  font-size: 1.5rem;
  margin-right: 1rem;
}

.lesson-details {
  flex-grow: 1;
}

.lesson-details h4 {
  color: var(--color-text);
  margin-bottom: 0.25rem;
}

.lesson-details p {
  color: var(--color-text-muted);
  font-size: 0.9rem;
}

.lesson-action {
  font-size: 1.5rem;
}

/* Lesson View */
.lesson-header {
  display: flex;
  align-items: center;
  gap: 2rem;
  padding: 2rem 0;
}

.lesson-info h1 {
  color: var(--color-text);
  margin-bottom: 0.5rem;
}

.lesson-info p {
  color: var(--color-text-muted);
}

.lesson-content {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 3rem;
  padding-bottom: 3rem;
}

.lesson-main {
  background: var(--color-surface);
  padding: 2rem;
  border-radius: 12px;
}

.lesson-text {
  margin-bottom: 2rem;
}

.lesson-text h2 {
  color: var(--color-primary);
  margin-bottom: 1rem;
}

.lesson-text h3 {
  color: var(--color-text);
  margin: 2rem 0 1rem;
}

.lesson-text p {
  margin-bottom: 1rem;
  line-height: 1.8;
}

.lesson-text ul, .lesson-text ol {
  margin: 1rem 0 1rem 2rem;
}

.lesson-text li {
  margin-bottom: 0.5rem;
}

.example-box {
  background-color: rgba(33, 128, 141, 0.1);
  border-left: 4px solid var(--color-primary);
  padding: 1.5rem;
  margin: 1.5rem 0;
  border-radius: 0 8px 8px 0;
}

.lesson-media {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.media-placeholder {
  flex: 1;
  background: rgba(0,0,0,0.05);
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
  border: 2px dashed rgba(0,0,0,0.2);
}

.media-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.lesson-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.lesson-sidebar {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.lesson-notes, .lesson-resources {
  background: var(--color-surface);
  padding: 1.5rem;
  border-radius: 12px;
}

.lesson-notes h3, .lesson-resources h3 {
  margin-bottom: 1rem;
  color: var(--color-text);
}

.lesson-notes textarea {
  width: 100%;
  height: 120px;
  padding: 1rem;
  border: 1px solid rgba(0,0,0,0.2);
  border-radius: 8px;
  resize: vertical;
  margin-bottom: 1rem;
}

.lesson-resources ul {
  list-style: none;
}

.lesson-resources li {
  margin-bottom: 0.75rem;
}

.resource-link {
  text-decoration: none;
  color: var(--color-primary);
  transition: color 0.3s ease;
}

.resource-link:hover {
  color: var(--color-primary-hover);
}

/* Quiz Styles */
.quiz-header {
  text-align: center;
  padding: 2rem 0;
}

.quiz-progress {
  max-width: 400px;
  margin: 1rem auto;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background-color: rgba(0,0,0,0.1);
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 0.5rem;
}

.progress-fill {
  height: 100%;
  background-color: var(--color-primary);
  transition: width 0.3s ease;
  width: 0%;
}

#questionCounter {
  color: var(--color-text-muted);
  font-size: 0.9rem;
}

.quiz-content {
  max-width: 600px;
  margin: 0 auto;
  padding-bottom: 2rem;
}

.question-card {
  background: var(--color-surface);
  padding: 2rem;
  border-radius: 12px;
  margin-bottom: 2rem;
}

.question-card h3 {
  color: var(--color-text);
  margin-bottom: 1.5rem;
  font-size: 1.2rem;
}

.question-options {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.option-label {
  display: flex;
  align-items: center;
  padding: 1rem;
  background-color: rgba(0,0,0,0.03);
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.option-label:hover {
  background-color: rgba(0,0,0,0.05);
}

.option-label input[type="radio"] {
  margin-right: 1rem;
}

.fill-blank-input {
  width: 100%;
  padding: 1rem;
  border: 2px solid rgba(0,0,0,0.2);
  border-radius: 8px;
  font-size: 1rem;
}

.quiz-actions {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.quiz-results {
  max-width: 400px;
  margin: 0 auto;
  text-align: center;
}

.results-card {
  background: var(--color-surface);
  padding: 3rem;
  border-radius: 12px;
}

.score-display {
  margin: 2rem 0;
}

.score-circle {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: conic-gradient(var(--color-success) 0deg, rgba(0,0,0,0.1) 0deg);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

.score-circle span {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--color-text);
}

.results-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

/* Progress Styles */
.progress-overview {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 3rem;
  margin: 3rem 0;
}

.progress-card {
  text-align: center;
}

.progress-circle {
  margin: 2rem 0;
}

.circle {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background: conic-gradient(var(--color-primary) 0deg, rgba(0,0,0,0.1) 0deg);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

.circle span {
  font-size: 2rem;
  font-weight: bold;
  color: var(--color-text);
}

.progress-stats {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
}

.stat-item {
  background: var(--color-surface);
  padding: 2rem;
  border-radius: 12px;
  text-align: center;
}

.stat-value {
  display: block;
  font-size: 2rem;
  font-weight: bold;
  color: var(--color-primary);
  margin-bottom: 0.5rem;
}

.stat-label {
  color: var(--color-text-muted);
  font-size: 0.9rem;
}

.achievements-section {
  margin: 4rem 0;
}

.achievements-section h2 {
  margin-bottom: 2rem;
  color: var(--color-text);
}

.badges-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.badge-item {
  display: flex;
  align-items: center;
  background: var(--color-surface);
  padding: 1.5rem;
  border-radius: 12px;
  transition: transform 0.3s ease;
}

.badge-item.unlocked {
  box-shadow: 0 4px 20px rgba(33, 128, 141, 0.3);
}

.badge-item.locked {
  opacity: 0.6;
}

.badge-item:hover {
  transform: translateY(-2px);
}

.badge-icon {
  font-size: 2rem;
  margin-right: 1rem;
}

.badge-info h4 {
  color: var(--color-text);
  margin-bottom: 0.25rem;
}

.badge-info p {
  color: var(--color-text-muted);
  font-size: 0.9rem;
}

.weekly-progress {
  margin: 4rem 0;
}

.weekly-progress h2 {
  margin-bottom: 2rem;
  color: var(--color-text);
}

.weeks-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

/* Profile Styles */
.profile-header {
  display: flex;
  align-items: center;
  gap: 2rem;
  padding: 3rem 0;
}

.profile-avatar {
  width: 80px;
  height: 80px;
}

.avatar-circle {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  color: white;
}

.profile-info h1 {
  color: var(--color-text);
  margin-bottom: 0.5rem;
}

.profile-info p {
  color: var(--color-text-muted);
}

.profile-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  padding-bottom: 3rem;
}

.profile-section {
  background: var(--color-surface);
  padding: 2rem;
  border-radius: 12px;
}

.profile-section h2 {
  color: var(--color-text);
  margin-bottom: 1.5rem;
}

.goals-list, .preferences-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.goal-item, .preference-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.goal-item label, .preference-item label {
  color: var(--color-text);
  cursor: pointer;
}

.schedule-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.schedule-item {
  display: flex;
  justify-content: space-between;
  padding: 1rem;
  background-color: rgba(0,0,0,0.03);
  border-radius: 8px;
}

.day {
  font-weight: 500;
  color: var(--color-text);
}

.time {
  color: var(--color-text-muted);
}

/* Forum Styles */
.forums-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 3rem 0 2rem;
}

.forums-header h1 {
  color: var(--color-text);
}

.forum-categories {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  overflow-x: auto;
}

.category-btn {
  padding: 0.75rem 1.5rem;
  border: none;
  background: rgba(0,0,0,0.05);
  border-radius: 20px;
  color: var(--color-text-muted);
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.3s ease;
}

.category-btn.active,
.category-btn:hover {
  background: var(--color-primary);
  color: white;
}

.forum-posts {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  padding-bottom: 3rem;
}

.forum-post {
  background: var(--color-surface);
  padding: 2rem;
  border-radius: 12px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.forum-post:hover {
  transform: translateY(-2px);
}

.post-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 1rem;
}

.post-header h3 {
  color: var(--color-text);
  margin-bottom: 0.5rem;
}

.post-category {
  background: var(--color-primary);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.8rem;
}

.post-meta {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1rem;
  font-size: 0.9rem;
  color: var(--color-text-muted);
}

.post-content {
  color: var(--color-text);
  line-height: 1.6;
}

/* Chatbot Styles */
.chatbot-container {
  position: fixed;
  bottom: 100px;
  right: 30px;
  width: 400px;
  height: 600px;
  background: var(--color-surface);
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.2);
  display: flex;
  flex-direction: column;
  transform: translateY(100%) scale(0.8);
  opacity: 0;
  transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  z-index: 1000;
}

.chatbot-container.active {
  transform: translateY(0) scale(1);
  opacity: 1;
}

.chatbot-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  background: var(--color-primary);
  color: white;
  border-radius: 20px 20px 0 0;
}

.chatbot-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.chatbot-avatar {
  font-size: 1.5rem;
}

.chatbot-info h3 {
  margin-bottom: 0.25rem;
  font-size: 1.1rem;
}

.chatbot-info p {
  font-size: 0.8rem;
  opacity: 0.9;
}

.chatbot-close {
  background: none;
  border: none;
  color: white;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 50%;
  transition: background-color 0.3s ease;
}

.chatbot-close:hover {
  background-color: rgba(255,255,255,0.2);
}

.chatbot-messages {
  flex: 1;
  overflow-y: auto;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.message {
  display: flex;
  gap: 0.75rem;
  align-items: flex-start;
}

.message-avatar {
  font-size: 1.2rem;
  flex-shrink: 0;
}

.message-content {
  flex: 1;
}

.message-content p {
  background: rgba(0,0,0,0.05);
  padding: 0.75rem 1rem;
  border-radius: 18px;
  margin: 0;
  line-height: 1.5;
}

.user-message {
  flex-direction: row-reverse;
}

.user-message .message-content p {
  background: var(--color-primary);
  color: white;
}

.message-time {
  font-size: 0.75rem;
  color: var(--color-text-muted);
  margin-top: 0.5rem;
  display: block;
}

.typing-indicator .message-content {
  background: rgba(0,0,0,0.05);
  border-radius: 18px;
  padding: 0.75rem 1rem;
}

.typing-dots {
  display: flex;
  gap: 4px;
}

.typing-dots span {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-text-muted);
  animation: typing 1.4s infinite ease-in-out;
}

.typing-dots span:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-dots span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typing {
  0%, 80%, 100% {
    transform: scale(0.8);
    opacity: 0.5;
  }
  40% {
    transform: scale(1);
    opacity: 1;
  }
}

.chatbot-input {
  display: flex;
  padding: 1.5rem;
  gap: 1rem;
  border-top: 1px solid rgba(0,0,0,0.1);
}

.chatbot-input input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 1px solid rgba(0,0,0,0.2);
  border-radius: 20px;
  outline: none;
  font-size: 0.9rem;
}

.chatbot-input input:focus {
  border-color: var(--color-primary);
}

.chatbot-input button {
  background: var(--color-primary);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 20px;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.3s ease;
}

.chatbot-input button:hover {
  background: var(--color-primary-hover);
}

.chatbot-toggle {
  position: fixed;
  bottom: 30px;
  right: 30px;
  background: var(--color-primary);
  color: white;
  border: none;
  padding: 1rem 1.5rem;
  border-radius: 50px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  box-shadow: 0 8px 32px rgba(33, 128, 141, 0.4);
  transition: all 0.3s ease;
  z-index: 999;
}

.chatbot-toggle:hover {
  background: var(--color-primary-hover);
  transform: translateY(-2px);
  box-shadow: 0 12px 40px rgba(33, 128, 141, 0.5);
}

.chatbot-toggle-icon {
  font-size: 1.2rem;
}

.chatbot-toggle span {
  font-weight: 500;
}

/* Modal Styles */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 2000;
}

.modal-content {
  background: var(--color-surface);
  max-width: 500px;
  width: 90%;
  border-radius: 12px;
  overflow: hidden;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  background: rgba(0,0,0,0.05);
}

.modal-header h2 {
  color: var(--color-text);
}

.modal-close {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: var(--color-text-muted);
}

.modal-body {
  padding: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: var(--color-text);
  font-weight: 500;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid rgba(0,0,0,0.2);
  border-radius: 8px;
  font-size: 1rem;
}

.form-group textarea {
  resize: vertical;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  padding: 1.5rem;
  background: rgba(0,0,0,0.05);
}

/* Notification Styles */
.notification {
  position: fixed;
  top: 100px;
  right: 30px;
  background: var(--color-success);
  color: white;
  padding: 1rem 1.5rem;
  border-radius: 8px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.2);
  transform: translateX(400px);
  opacity: 0;
  transition: all 0.3s ease;
  z-index: 3000;
  max-width: 300px;
}

.notification.show {
  transform: translateX(0);
  opacity: 1;
}

.notification--success {
  background: var(--color-success);
}

.notification--error {
  background: var(--color-error);
}

.notification--achievement {
  background: linear-gradient(135deg, #FFD700, #FFA500);
  color: var(--color-text);
}

/* Responsive Design */
@media (max-width: 768px) {
  .container {
    padding: 0 15px;
  }
  
  .nav__menu {
    flex-wrap: wrap;
    gap: 1rem;
  }
  
  .hero__content h1 {
    font-size: 2rem;
  }
  
  .hero__stats {
    flex-wrap: wrap;
    gap: 2rem;
  }
  
  .hero__actions {
    flex-direction: column;
    align-items: center;
  }
  
  .quick-cards {
    grid-template-columns: 1fr;
  }
  
  .lesson-content {
    grid-template-columns: 1fr;
  }
  
  .progress-overview {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .progress-stats {
    grid-template-columns: 1fr;
  }
  
  .profile-header {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .profile-content {
    grid-template-columns: 1fr;
  }
  
  .forums-header {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .chatbot-container {
    right: 15px;
    left: 15px;
    width: auto;
    bottom: 90px;
  }
  
  .chatbot-toggle {
    right: 15px;
    padding: 0.75rem 1rem;
  }
  
  .chatbot-toggle span {
    display: none;
  }
}

@media (max-width: 480px) {
  .hero__content h1 {
    font-size: 1.5rem;
  }
  
  .hero__actions {
    gap: 0.5rem;
  }
  
  .btn--lg {
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
  }
  
  .module-header {
    flex-direction: column;
    gap: 1rem;
    align-items: flex-start;
  }
  
  .lesson-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .quiz-actions {
    flex-direction: column;
  }
  
  .results-actions {
    flex-direction: column;
  }
}

/* Print Styles */
@media print {
  .header,
  .chatbot-container,
  .chatbot-toggle,
  .btn,
  .modal {
    display: none;
  }
  
  .view {
    display: block !important;
  }
  
  body {
    background: white;
    color: black;
  }
}
"""

print("Enhanced CSS with comprehensive chatbot styling created successfully!")
print("Key styling features added:")
print("- Professional chatbot interface with animations")
print("- Floating chatbot toggle button with hover effects")
print("- Typing indicator animation")
print("- Message bubbles with proper styling")
print("- Mobile-responsive chatbot design")
print("- Smooth transitions and animations")
print("- Achievement notification styling")
print("- Complete modal system styling")