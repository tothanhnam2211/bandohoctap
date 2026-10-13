// BANDOHOCTAP.VN - Client Application Logic
let currentDay = 1;
let currentDayData = null;
let curriculum = [];
let userQuizAnswers = {};

// On Load
document.addEventListener("DOMContentLoaded", async () => {
  setupSidebarToggle();
  await loadCurriculum();
  await loadDay(1);
});

// Sidebar Mobile Toggle
function setupSidebarToggle() {
  const toggleBtn = document.getElementById("toggle-sidebar");
  const sidebar = document.getElementById("sidebar");
  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener("click", () => {
      sidebar.classList.toggle("-translate-x-full");
    });
  }
}

// 1. Load 30 Days Curriculum
async function loadCurriculum() {
  try {
    const res = await fetch("data/curriculum.json");
    curriculum = await res.json();
    renderCurriculumList();
  } catch (err) {
    console.error("Lỗi tải curriculum.json:", err);
  }
}

function renderCurriculumList() {
  const listEl = document.getElementById("curriculum-list");
  if (!listEl) return;
  listEl.innerHTML = "";

  curriculum.forEach(item => {
    const btn = document.createElement("button");
    btn.className = `w-full text-left px-3 py-2.5 rounded-lg flex items-center justify-between transition ${
      item.day === currentDay 
        ? "bg-sky-50 text-sky-800 font-bold border border-sky-200" 
        : "text-slate-600 hover:bg-slate-100"
    }`;

    const isLocked = item.status === "locked" && item.day !== 1;
    btn.innerHTML = `
      <div class="flex items-center space-x-2 truncate">
        <i class="fa-solid ${isLocked ? 'fa-lock text-slate-400' : 'fa-circle-check text-emerald-500'} text-xs"></i>
        <span class="truncate">${item.title}</span>
      </div>
      <span class="text-[11px] font-mono ${isLocked ? 'text-slate-400' : 'text-sky-600'} shrink-0 ml-1">
        ${item.day < 10 ? '0' + item.day : item.day}
      </span>
    `;

    btn.onclick = () => {
      if (isLocked) {
        alert(`Bài học ${item.title} đang ở trạng thái khóa. Hoàn thành Ngày 01 để mở khóa tiếp theo!`);
        return;
      }
      loadDay(item.day);
      // Close mobile sidebar if open
      const sidebar = document.getElementById("sidebar");
      if (sidebar && !sidebar.classList.contains("-translate-x-full")) {
        sidebar.classList.add("-translate-x-full");
      }
    };

    listEl.appendChild(btn);
  });
}

// 2. Load Single Day Data
async function loadDay(dayNumber) {
  currentDay = dayNumber;
  renderCurriculumList();

  try {
    const res = await fetch(`data/day-${dayNumber < 10 ? '0' + dayNumber : dayNumber}.json`);
    currentDayData = await res.json();
    populateDayData(currentDayData);
  } catch (err) {
    console.error(`Lỗi tải dữ liệu ngày ${dayNumber}:`, err);
  }
}

function populateDayData(data) {
  // Title & ID
  document.getElementById("lesson-id").textContent = data.id;
  document.getElementById("lesson-title").textContent = data.title;
  
  if (data.download_links) {
    document.getElementById("btn-download-docx").href = data.download_links.docx || "#";
    document.getElementById("btn-download-word-box").href = data.download_links.docx || "#";
    document.getElementById("btn-download-png").href = data.download_links.infographic || "#";
  }

  // Populate Tab 1: Shorts
  populateShorts(data.shorts);

  // Populate Tab 2: Infographic & Theory
  populateInfographic(data.infographic_tab);

  // Populate Tab 3: Skeleton
  populateSkeleton(data.skeleton_tab);

  // Populate Tab 4: Quiz
  populateQuiz(data.quiz_tab);

  // Math re-render
  if (window.renderMathInElement) {
    setTimeout(() => {
      renderMathInElement(document.body, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "$", right: "$", display: false }
        ]
      });
    }, 100);
  }
}

// 3. TAB 1: POPULATE SHORTS
function populateShorts(shortsData) {
  if (!shortsData) return;
  document.getElementById("shorts-heading").innerHTML = `
    <i class="fa-solid fa-clapperboard text-red-500 mr-2"></i> ${shortsData.heading}
  `;
  document.getElementById("shorts-subheading").textContent = shortsData.subheading;

  const grid = document.getElementById("shorts-grid");
  grid.innerHTML = "";

  shortsData.clips.forEach(clip => {
    const card = document.createElement("div");
    card.className = "bg-slate-50 border border-slate-200 hover:border-sky-400 rounded-xl p-4 flex flex-col justify-between transition hover:shadow-md";

    const badgeColor = clip.badge.includes("Zombie") 
      ? "bg-red-100 text-red-700 border-red-200" 
      : "bg-sky-100 text-sky-700 border-sky-200";

    card.innerHTML = `
      <div>
        <div class="relative aspect-[9/16] max-h-64 bg-slate-900 rounded-lg overflow-hidden flex items-center justify-center group cursor-pointer mb-3">
          <img src="${clip.thumbnail || 'assets/day-01/infographic.png'}" alt="${clip.title}" class="w-full h-full object-cover opacity-80 group-hover:scale-105 transition duration-300">
          <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
            <div class="w-12 h-12 rounded-full bg-red-600 text-white flex items-center justify-center shadow-lg group-hover:scale-110 transition">
              <i class="fa-solid fa-play ml-0.5"></i>
            </div>
          </div>
          <span class="absolute top-2 left-2 text-[11px] font-bold px-2 py-0.5 rounded-full border ${badgeColor}">
            ${clip.badge}
          </span>
        </div>
        <h4 class="font-bold text-slate-800 text-sm leading-snug mb-1">${clip.title}</h4>
        <p class="text-xs text-slate-500">${clip.desc}</p>
      </div>

      <button onclick="playClip('${clip.video_url || 'assets/day-01/clip1.mp4'}', '${clip.title}')" 
              class="mt-4 w-full bg-white hover:bg-sky-50 text-sky-700 border border-sky-300 font-bold py-1.5 px-3 rounded-lg text-xs flex items-center justify-center space-x-1 transition">
        <i class="fa-solid fa-play text-[10px]"></i>
        <span>Xem Video (30s)</span>
      </button>
    `;
    grid.appendChild(card);
  });
}

function playClip(videoUrl, title) {
  const container = document.getElementById("video-player-container");
  const player = document.getElementById("main-video-player");
  const titleEl = document.getElementById("current-playing-title");

  container.classList.remove("hidden");
  titleEl.textContent = title;
  player.src = videoUrl;
  player.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  player.play().catch(e => console.log("Auto-play prevented", e));
}

function closeVideoPlayer() {
  const container = document.getElementById("video-player-container");
  const player = document.getElementById("main-video-player");
  player.pause();
  container.classList.add("hidden");
}

// 4. TAB 2: POPULATE INFOGRAPHIC & THEORY
function populateInfographic(infoData) {
  if (!infoData) return;
  const img = document.getElementById("infographic-img");
  img.src = infoData.image_url || "assets/day-01/infographic.png";

  const theoryContainer = document.getElementById("theory-container");
  theoryContainer.innerHTML = "";

  infoData.theory_sections.forEach(sec => {
    const block = document.createElement("div");
    block.className = "bg-slate-50 border border-slate-200 rounded-xl p-5";

    const titleH3 = document.createElement("h3");
    titleH3.className = "text-md font-bold text-sky-800 mb-3 flex items-center";
    titleH3.innerHTML = `<i class="fa-solid fa-bookmark text-sky-600 mr-2"></i> ${sec.title}`;
    block.appendChild(titleH3);

    const ul = document.createElement("ul");
    ul.className = "space-y-2 text-sm text-slate-700 leading-relaxed list-disc list-inside";

    sec.rules.forEach(rule => {
      const li = document.createElement("li");
      // Replace markdown bold **text** with <strong>
      let formatted = rule.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
      li.innerHTML = formatted;
      ul.appendChild(li);
    });

    block.appendChild(ul);
    theoryContainer.appendChild(block);
  });
}

function zoomImage(src) {
  const modal = document.getElementById("image-modal");
  const modalImg = document.getElementById("modal-img");
  modalImg.src = src;
  modal.classList.remove("hidden");
}

function closeImageModal() {
  document.getElementById("image-modal").classList.add("hidden");
}

// 5. TAB 3: POPULATE SKELETON
function populateSkeleton(skeletonData) {
  if (!skeletonData) return;
  const container = document.getElementById("skeleton-questions-list");
  container.innerHTML = "";
  document.getElementById("skeleton-score").textContent = "Chưa làm";

  skeletonData.questions.forEach((q, idx) => {
    const item = document.createElement("div");
    item.className = "bg-slate-50 border border-slate-200 rounded-xl p-4";
    item.id = `skeleton-item-${q.id}`;

    item.innerHTML = `
      <div class="text-sm text-slate-800 leading-loose flex flex-wrap items-center gap-2">
        <span>${q.text_before}</span>
        <input type="text" id="sk-input-${q.id}" 
               class="skeleton-input px-3 py-1 font-mono font-bold text-slate-900 rounded border border-slate-300 w-36 text-center" 
               placeholder="Điền đáp án...">
        <span>${q.text_after}</span>
      </div>
      <div id="sk-feedback-${q.id}" class="mt-2 text-xs font-semibold hidden"></div>
    `;
    container.appendChild(item);
  });
}

function checkSkeletonAnswers() {
  if (!currentDayData || !currentDayData.skeleton_tab) return;
  const questions = currentDayData.skeleton_tab.questions;
  let correctCount = 0;

  questions.forEach(q => {
    const input = document.getElementById(`sk-input-${q.id}`);
    const feedback = document.getElementById(`sk-feedback-${q.id}`);
    const userVal = input.value.trim().toLowerCase().replace(/\s+/g, '');
    
    // Check against acceptable answers
    const isCorrect = q.acceptable.some(ans => ans.toLowerCase().replace(/\s+/g, '') === userVal);

    feedback.classList.remove("hidden");
    if (isCorrect) {
      correctCount++;
      input.classList.remove("border-red-500", "bg-red-50");
      input.classList.add("border-emerald-500", "bg-emerald-50");
      feedback.className = "mt-2 text-xs font-semibold text-emerald-600 flex items-center";
      feedback.innerHTML = `<i class="fa-solid fa-circle-check mr-1"></i> Chính xác! ${q.hint}`;
    } else {
      input.classList.remove("border-emerald-500", "bg-emerald-50");
      input.classList.add("border-red-500", "bg-red-50");
      feedback.className = "mt-2 text-xs font-semibold text-red-600 flex items-center";
      feedback.innerHTML = `<i class="fa-solid fa-triangle-exclamation mr-1"></i> Chưa đúng! Gợi ý: ${q.hint}`;
    }
  });

  const scoreBadge = document.getElementById("skeleton-score");
  scoreBadge.textContent = `${correctCount}/${questions.length} Hoàn Thành`;
  if (correctCount === questions.length) {
    scoreBadge.className = "text-xs font-bold text-emerald-700 bg-emerald-50 border border-emerald-300 px-3 py-1 rounded-full";
  } else {
    scoreBadge.className = "text-xs font-bold text-amber-700 bg-amber-50 border border-amber-300 px-3 py-1 rounded-full";
  }
}

function resetSkeleton() {
  if (!currentDayData || !currentDayData.skeleton_tab) return;
  currentDayData.skeleton_tab.questions.forEach(q => {
    const input = document.getElementById(`sk-input-${q.id}`);
    const feedback = document.getElementById(`sk-feedback-${q.id}`);
    input.value = "";
    input.className = "skeleton-input px-3 py-1 font-mono font-bold text-slate-900 rounded border border-slate-300 w-36 text-center";
    feedback.classList.add("hidden");
  });
  document.getElementById("skeleton-score").textContent = "Chưa làm";
}

// 6. TAB 4: POPULATE QUIZ
function populateQuiz(quizData) {
  if (!quizData) return;
  const container = document.getElementById("quiz-questions-list");
  container.innerHTML = "";
  userQuizAnswers = {};
  document.getElementById("quiz-result-badge").classList.add("hidden");

  quizData.questions.forEach((q, qIndex) => {
    const item = document.createElement("div");
    item.className = "bg-slate-50 border border-slate-200 rounded-xl p-5";
    item.id = `quiz-card-${q.id}`;

    const levelBadge = q.level.includes("Zombie") || q.level.includes("bẫy")
      ? `<span class="bg-red-100 text-red-700 border border-red-300 text-[11px] font-bold px-2 py-0.5 rounded-full"><i class="fa-solid fa-triangle-exclamation mr-1"></i>${q.level}</span>`
      : `<span class="bg-sky-100 text-sky-700 border border-sky-300 text-[11px] font-bold px-2 py-0.5 rounded-full">${q.level}</span>`;

    let optionsHtml = q.options.map((opt, optIndex) => `
      <div onclick="selectQuizOption('${q.id}', ${optIndex})" 
           id="opt-${q.id}-${optIndex}" 
           class="quiz-option cursor-pointer p-3 border border-slate-200 rounded-lg bg-white text-sm transition flex items-center space-x-3">
        <span class="w-6 h-6 rounded-full border border-slate-300 flex items-center justify-center font-bold text-xs text-slate-600 opt-letter">
          ${String.fromCharCode(65 + optIndex)}
        </span>
        <span class="text-slate-800">${opt}</span>
      </div>
    `).join("");

    item.innerHTML = `
      <div class="flex items-center justify-between mb-2">
        <h4 class="font-bold text-slate-900 text-sm sm:text-base">${q.question}</h4>
        ${levelBadge}
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-3">
        ${optionsHtml}
      </div>
      <div id="quiz-explanation-${q.id}" class="mt-4 p-3 bg-amber-50 border border-amber-200 rounded-lg text-xs text-slate-800 hidden">
        <b>💡 Giải thích chi tiết:</b> ${q.explanation}
      </div>
    `;

    container.appendChild(item);
  });
}

function selectQuizOption(questionId, optionIndex) {
  userQuizAnswers[questionId] = optionIndex;
  
  // Update selection UI
  const qData = currentDayData.quiz_tab.questions.find(q => q.id === questionId);
  qData.options.forEach((_, idx) => {
    const el = document.getElementById(`opt-${questionId}-${idx}`);
    if (idx === optionIndex) {
      el.classList.add("selected");
    } else {
      el.classList.remove("selected");
    }
  });
}

function gradeQuiz() {
  if (!currentDayData || !currentDayData.quiz_tab) return;
  const questions = currentDayData.quiz_tab.questions;
  let correctCount = 0;

  questions.forEach(q => {
    const userSelected = userQuizAnswers[q.id];
    const explanation = document.getElementById(`quiz-explanation-${q.id}`);
    explanation.classList.remove("hidden");

    q.options.forEach((_, optIdx) => {
      const optEl = document.getElementById(`opt-${q.id}-${optIdx}`);
      optEl.classList.remove("correct", "incorrect", "selected");

      if (optIdx === q.correct_index) {
        optEl.classList.add("correct");
      } else if (userSelected === optIdx) {
        optEl.classList.add("incorrect");
      }
    });

    if (userSelected === q.correct_index) {
      correctCount++;
    }
  });

  const score = ((correctCount / questions.length) * 10).toFixed(1);
  const badge = document.getElementById("quiz-result-badge");
  badge.classList.remove("hidden");
  badge.textContent = `Điểm số: ${score}/10 (${correctCount}/${questions.length} câu đúng)`;
  
  if (score >= 8.0) {
    badge.className = "text-sm font-bold bg-emerald-100 text-emerald-800 border border-emerald-300 px-3 py-1 rounded-full";
  } else {
    badge.className = "text-sm font-bold bg-amber-100 text-amber-800 border border-amber-300 px-3 py-1 rounded-full";
  }

  // Math re-render in explanation
  if (window.renderMathInElement) {
    renderMathInElement(document.getElementById("quiz-questions-list"));
  }
}

function resetQuiz() {
  userQuizAnswers = {};
  if (!currentDayData || !currentDayData.quiz_tab) return;
  populateQuiz(currentDayData.quiz_tab);
  if (window.renderMathInElement) {
    renderMathInElement(document.getElementById("quiz-questions-list"));
  }
}

// 7. SWITCH TABS
function switchTab(tabName) {
  const tabs = ['shorts', 'infographic', 'skeleton', 'quiz', 'stem3d'];
  tabs.forEach(t => {
    const content = document.getElementById(`tab-${t}`);
    const btn = document.getElementById(`tab-btn-${t}`);
    if (t === tabName) {
      content.classList.remove('hidden');
      btn.classList.add('active');
    } else {
      content.classList.add('hidden');
      btn.classList.remove('active');
    }
  });

  // If switching away from shorts, pause video
  if (tabName !== 'shorts') {
    closeVideoPlayer();
  }
}
