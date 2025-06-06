document.addEventListener('DOMContentLoaded', function () {
  const playBtn = document.querySelector('.play-btn');
  const mainBtn = document.querySelector('.main-btn');
  const gamesSection = document.querySelector('.games-container');

  function scrollToGames() {
    if (gamesSection) {
      const yOffset = -64;
      const y = gamesSection.getBoundingClientRect().top + window.pageYOffset + yOffset;
      window.scrollTo({ top: y, behavior: 'smooth' });
    }
  }

  if (playBtn) playBtn.addEventListener('click', scrollToGames);
  if (mainBtn) mainBtn.addEventListener('click', scrollToGames);
});