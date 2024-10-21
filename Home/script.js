const noteSection = document.getElementById('note-taking');
const taskSection = document.getElementById('task-manager');
const calendarSection = document.getElementById('calendar-reminders');
const summarySection = document.getElementById('rag-summarizer');
const timerSection = document.getElementById('timer');
const chatSection = document.querySelector('.chatbot button');

noteSection.addEventListener('click', function() {
  window.location.href = '../Notes/index.html'; 
});

taskSection.addEventListener('click', function() {
  window.location.href = '../Tasks/index.html'; 
});

timerSection.addEventListener('click', function() {
  window.location.href = '../Pomodoro/index.html'; 
});

calendarSection.addEventListener('click', function() {
  window.location.href = '../Calendar/index.html'; 
});

chatSection.addEventListener('click', function() {
  window.open('http://localhost:3000', '_blank');
});

summarySection.addEventListener('click', function() {
  window.open('http://localhost:9000', '_blank');
});
