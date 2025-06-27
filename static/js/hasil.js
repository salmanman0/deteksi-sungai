function openModal(src) {
  const modal = document.getElementById('imageModal');
  const image = document.getElementById('modalImage');
  image.src = src;
  modal.classList.remove('hidden');
  modal.classList.add('flex');
}

function closeModal() {
  const modal = document.getElementById('imageModal');
  modal.classList.add('hidden');
  modal.classList.remove('flex');
  document.getElementById('modalImage').src = '';
}

// Optional: close modal when clicking outside image
document.getElementById('imageModal').addEventListener('click', function (e) {
  if (e.target === this) {
    closeModal();
  }
});