alert("s")
let cropper;
const image = document.createElement('img');

// Preview when the user selects a file
$('.item-img6').on('change', function (e) {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function (event) {
        // Show the image preview before cropping
        image.src = event.target.result;
        $('#upload-demo6').html('');  // Clear previous content
        $('#upload-demo6').append(image);  // Add the image to the preview container
        $('#cropImagePop6').modal('show');  // Show the modal for cropping
    };
    reader.readAsDataURL(file);
});

// Initialize cropper once the modal is shown
$('#cropImagePop6').on('shown.bs.modal', function () {
    cropper = new Cropper(image, {
        aspectRatio: 1,
        viewMode: 1,
        background: false,
        zoomable: true,
        scalable: true,
        movable: true,
        dragMode: 'move',
        cropBoxMovable: true,
        cropBoxResizable: true
    });
});

// When the crop button is clicked, show the cropped image as a preview
$('#cropImageBtn6').on('click', function () {
    const canvas = cropper.getCroppedCanvas({
        width: 500,
        height: 500
    });

    canvas.toBlob(function (blob) {
        const file = new File([blob], "cropped.jpg", { type: "image/jpeg" });
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);

        const fileInput = document.querySelector('input[name="image"]');
        fileInput.files = dataTransfer.files;

        // Display the cropped image as preview
        $('#item-img-output6').attr('src', URL.createObjectURL(blob));
        $('#cropImagePop6').modal('hide');  // Hide the modal after cropping
    }, 'image/jpeg');
});
