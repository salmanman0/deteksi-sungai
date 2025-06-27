const fileInput = document.getElementById('zipfile');
  const filenameDisplay = document.getElementById('filename');
  const dropzone = document.getElementById('dropzone');
  const submitBtn = document.getElementById('submitBtn');
  const uploadForm = document.getElementById('uploadForm');

// Fungsi Aktif/Nonaktif Tombol
function enableSubmit() {
  submitBtn.disabled = false;
  submitBtn.classList.remove('bg-stone-300', 'cursor-not-allowed');
  submitBtn.classList.add('bg-amber-500', 'hover:bg-amber-600', 'cursor-pointer');
}

function disableSubmit() {
  submitBtn.disabled = true;
  submitBtn.classList.remove('bg-amber-500', 'hover:bg-amber-600', 'cursor-pointer');
  submitBtn.classList.add('bg-stone-300', 'cursor-not-allowed');
}

// Saat File Dipilih dari Input
fileInput.addEventListener('change', function () {
  if (fileInput.files.length > 0 && fileInput.files[0].name.endsWith('.zip')) {
    const name = fileInput.files[0].name;
    filenameDisplay.textContent = name;
    document.getElementById('iconDropZone').classList.add('hidden');
    document.getElementById('textDropZone1').classList.add('hidden');
    document.getElementById('textDropZone2').classList.add('hidden');
    enableSubmit();
  } else {
    filenameDisplay.textContent = '';
    disableSubmit();
  }
});

// Drag & Drop Events
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  dropzone.addEventListener(eventName, e => {
    e.preventDefault();
    e.stopPropagation();
  });
});

// Highlight Dropzone
['dragenter', 'dragover'].forEach(eventName => {
  dropzone.addEventListener(eventName, () => {
    dropzone.classList.add('bg-amber-100');
  });
});

['dragleave', 'drop'].forEach(eventName => {
  dropzone.addEventListener(eventName, () => {
    dropzone.classList.remove('bg-amber-100');
  });
});

//  Saat File Ditarik Masuk
dropzone.addEventListener('drop', e => {
  const files = e.dataTransfer.files;
  if (files.length > 0 && files[0].name.endsWith('.zip')) {
    fileInput.files = files;
    filenameDisplay.textContent = files[0].name;
    document.getElementById('iconDropZone').classList.add('hidden');
    document.getElementById('textDropZone1').classList.add('hidden');
    document.getElementById('textDropZone2').classList.add('hidden');
    enableSubmit();
  } else {
    alert('Hanya file .zip yang diizinkan!');
    disableSubmit();
  }
});

// Saat Form Disubmit
uploadForm.addEventListener('submit', function () {
  submitBtn.disabled = true;
  submitBtn.innerHTML = `
    <svg class="animate-spin h-5 w-5 mx-auto text-white" xmlns="http://www.w3.org/2000/svg" fill="none"
         viewBox="0 0 24 24">
      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"></path>
    </svg>
  `;
});