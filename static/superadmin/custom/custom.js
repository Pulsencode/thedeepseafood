//---Brand---//
$(document).on("click", "#brand_search", function () {
    console.log("Brand");
    brand_view("None");
});

function brand_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "brand-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#brand-table").html(data.template);
        },
    });
}

function changebrandstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "brand-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#brand-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_brand() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "brand-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#brand-table").html(data.template);
        },
    });
}
//---Category---//
$(document).on("click", "#category_search", function () {
    console.log("Category");
    category_view("None");
});

function category_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "category-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#category-table").html(data.template);
        },
    });
}

function changecategorystatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "category-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#category-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_category() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "category-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#category-table").html(data.template);
        },
    });
}

//---SubCategory---//
$(document).on("click", "#subcategory_search", function () {
    console.log("Subcategory");
    subcategory_view("None");
});

function subcategory_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "subcategory-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#sub-table").html(data.template);
        },
    });
}

function changesubcategorystatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "subcategory-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#sub-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_subcategory() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "subcategory-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#sub-table").html(data.template);
        },
    });
}
//---JobCategory---//
$(document).on("click", "#jcategory_search", function () {
    console.log("JobCategory");
    jcategory_view("None");
});

function jcategory_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "job-category-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#jcategory-table").html(data.template);
        },
    });
}

function changejcategorystatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "job-category-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#jcategory-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_jcategory() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "job-category-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#jcategory-table").html(data.template);
        },
    });
}
//---Gallery---//
$(document).on("click", "#gallery_search", function () {
    console.log("Gallery");
    gallery_view("None");
});

function gallery_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "gallery-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#gallery-table").html(data.template);
        },
    });
}

function changegallerystatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "gallery-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#gallery-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_gallery() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "gallery-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#gallery-table").html(data.template);
        },
    });
}


$(document).ready(function() {
    $(".delete-image-btn").on("click", function() {
        var imageId = $(this).data("image-id");
        var deleteUrl = "/superadmin/delete-slider/" + imageId + "/";  // Update this URL to your Django view for deleting the image
        
        // Store references to the image and delete button with unique IDs
        var imageElement = $("#slider" + imageId);
        var deleteButton = $("#btn-del" + imageId);
        console.log(imageId)
        $.ajax({
            type: "GET",
            url: deleteUrl,
            data: { csrfmiddlewaretoken: "{{ csrf_token }}" },  // Include the CSRF token
            success: function(response) {
                if (response.success) {
                    
                    // Remove the specific image and delete button associated with the clicked button
                    imageElement.remove();
                    deleteButton.remove();
                } else {
                    console.log('Error:', response.error);
                }
            }
        });
    });
});
//---News---//
$(document).on("click", "#news_search", function () {
    console.log("News");
    news_view("None");
});

function news_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "news-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#news-table").html(data.template);
        },
    });
}

function changenewsstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "news-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#news-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_news() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "news-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#news-table").html(data.template);
        },
    });
}

$(document).ready(function() {
    $(".delete-image-btn").on("click", function() {
        var imageId = $(this).data("image-id");
        var deleteUrl = "/superadmin/delete-newsslider/" + imageId + "/";  // Update this URL to your Django view for deleting the image
        
        // Store references to the image and delete button with unique IDs
        var imageElement = $("#slider" + imageId);
        var deleteButton = $("#btn-del" + imageId);
        console.log(imageId)
        $.ajax({
            type: "GET",
            url: deleteUrl,
            data: { csrfmiddlewaretoken: "{{ csrf_token }}" },  // Include the CSRF token
            success: function(response) {
                if (response.success) {
                    
                    // Remove the specific image and delete button associated with the clicked button
                    imageElement.remove();
                    deleteButton.remove();
                } else {
                    console.log('Error:', response.error);
                }
            }
        });
    });
});

//---Promotion---//
$(document).on("click", "#promotion_search", function () {
    console.log("Promotion");
    promotion_view("None");
});

function promotion_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "promotion-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#promotion-table").html(data.template);
        },
    });
}

function changepromotionstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "promotion-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#promotion-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_promotion() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "promotion-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#promotion-table").html(data.template);
        },
    });
}

$(document).ready(function() {
    $(".delete-image-btn").on("click", function() {
        var imageId = $(this).data("image-id");
        var deleteUrl = "/superadmin/delete-promotionslider/" + imageId + "/";  // Update this URL to your Django view for deleting the image
        
        // Store references to the image and delete button with unique IDs
        var imageElement = $("#slider" + imageId);
        var deleteButton = $("#btn-del" + imageId);
        console.log(imageId)
        $.ajax({
            type: "GET",
            url: deleteUrl,
            data: { csrfmiddlewaretoken: "{{ csrf_token }}" },  // Include the CSRF token
            success: function(response) {
                if (response.success) {
                    
                    // Remove the specific image and delete button associated with the clicked button
                    imageElement.remove();
                    deleteButton.remove();
                } else {
                    console.log('Error:', response.error);
                }
            }
        });
    });
});

//---Blog---//
$(document).on("click", "#blog_search", function () {
    console.log("blog");
    blog_view("None");
});

function blog_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "blog-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#blog-table").html(data.template);
        },
    });
}

function changeblogstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "blog-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#blog-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_blog() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "blog-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#blog-table").html(data.template);
        },
    });
}

$(document).ready(function() {
    $(".delete-image-btn").on("click", function() {
        var imageId = $(this).data("image-id");
        var deleteUrl = "/superadmin/delete-blogslider/" + imageId + "/";  // Update this URL to your Django view for deleting the image
        
        // Store references to the image and delete button with unique IDs
        var imageElement = $("#slider" + imageId);
        var deleteButton = $("#btn-del" + imageId);
        console.log(imageId)
        $.ajax({
            type: "GET",
            url: deleteUrl,
            data: { csrfmiddlewaretoken: "{{ csrf_token }}" },  // Include the CSRF token
            success: function(response) {
                if (response.success) {
                    
                    // Remove the specific image and delete button associated with the clicked button
                    imageElement.remove();
                    deleteButton.remove();
                } else {
                    console.log('Error:', response.error);
                }
            }
        });
    });
});


//---about us---//
$(document).on("click", "#about_search", function () {
    console.log("about");
    about_view("None");
});

function about_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "about-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#about-table").html(data.template);
        },
    });
}

function changeaboutstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "about-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#about-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_about() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "about-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#about-table").html(data.template);
        },
    });
}

//restrict character count in aboutus
$(document).ready(function() {
    $('#titleInput').on('input', function() {
        var maxLength = 40;
        if ($(this).val().length > maxLength) {
            $(this).val($(this).val().substring(0, maxLength));
        }
    });
});

//---team---//
$(document).on("click", "#team_search", function () {
    console.log("Team");
    team_view("None");
});

function team_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "team-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#team-table").html(data.template);
        },
    });
}

function changeteamstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "team-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#team-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_team() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "team-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#team-table").html(data.template);
        },
    });
}

//---certification---//
$(document).on("click", "#certification_search", function () {
    console.log("certification");
    certification_view("None");
});

function certification_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "certification-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#certification-table").html(data.template);
        },
    });
}

function changecertificationstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "certification-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#certification-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_certification() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "certification-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#certification-table").html(data.template);
        },
    });
}

//---testimonial---//
$(document).on("click", "#testimonial_search", function () {
    console.log("Team");
    testimonial_view("None");
});

function testimonial_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "testimonial-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#testimonial-table").html(data.template);
        },
    });
}

function changetestimonialstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "testimonial-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#testimonial-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_testimonial() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "testimonial-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#testimonial-table").html(data.template);
        },
    });
}
//---career---//
$(document).on("click", "#career_search", function () {
    console.log("career");
    career_view("None");
});

function career_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "career-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#career-table").html(data.template);
        },
    });
}

function changecareerstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "career-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#career-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_career() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "career-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#career-table").html(data.template);
        },
    });
}

//---history---//
$(document).on("click", "#history_search", function () {
    console.log("career");
    history_view("None");
});

function history_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "history-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#history-table").html(data.template);
        },
    });
}

function changehistorystatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "history-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#history-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_history() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "history-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#history-table").html(data.template);
        },
    });
}

$(document).ready(function() {
    $(".delete-image-btn").on("click", function() {
        var imageId = $(this).data("image-id");
        var deleteUrl = "/superadmin/delete-historyslider/" + imageId + "/";  // Update this URL to your Django view for deleting the image
        
        // Store references to the image and delete button with unique IDs
        var imageElement = $("#slider" + imageId);
        var deleteButton = $("#btn-del" + imageId);
        console.log(imageId)
        $.ajax({
            type: "GET",
            url: deleteUrl,
            data: { csrfmiddlewaretoken: "{{ csrf_token }}" },  // Include the CSRF token
            success: function(response) {
                if (response.success) {
                    
                    // Remove the specific image and delete button associated with the clicked button
                    imageElement.remove();
                    deleteButton.remove();
                } else {
                    console.log('Error:', response.error);
                }
            }
        });
    });
});

//contactus

$(document).on("click", "#contact_search", function () {
    console.log("Contactus");
    contact_view("None");
});

function contact_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "contact-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#contact-table").html(data.template);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_contact() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "contact-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#contact-table").html(data.template);
        },
    });
}

//---history---//
$(document).on("click", "#supermarket_search", function () {
    console.log("supermarket");
    supermarket_view("None");
});

function supermarket_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "supermarket-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#supermarket-table").html(data.template);
        },
    });
}

function changesuperstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "supermarket-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#supermarket-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_supermarket() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "supermarket-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#supermarket-table").html(data.template);
        },
    });
}

//enquiry

$(document).on("click", "#enquiry_search", function () {
    console.log("enquiry");
    enquiry_view("None");
});

function enquiry_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();
	var start = $("#start_date").val();
	var end = $("#end_date").val();
	// console.log('dates', start,end);
	var startDate = new Date(start);
    var endDate = new Date(end);
    var formattedSDate = formatDate(startDate);
    var formattedEDate = formatDate(endDate);
	
	function formatDate(date) {
        if (!isNaN(date.getTime())) {
            // Format the date in month/day/year format
            var month = (date.getMonth() + 1).toString().padStart(2, '0');
            var day = date.getDate().toString().padStart(2, '0');
            var year = date.getFullYear();
            return month + '/' + day + '/' + year;
        } else {
            console.error("Invalid date");
            return null;
        }
    }

    $.ajax({
        url: "enquiry-view",
        type: "GET",
        data: { search: search, page: page, sts: sts,'start':formattedSDate,'end':formattedEDate },
        success: function (data) {
            $("#enquiry-table").html(data.template);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_enquiry() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "enquiry-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#enquiry-table").html(data.template);
        },
    });
}

//export to excel
function exportEnquiry() {
    var start_date = $('#start_date').val();
    var end_date = $('#end_date').val();
    $.ajax({
        url: "export_excel",
        type: "GET",
        data: { start: start_date, end: end_date },
        success: function (data) {
            if (data.status) {
                // Process data and create Excel
                var wb = XLSX.utils.book_new();
                wb.Props = {
                    Title: "Enquiries Data",
                    Subject: "Enquiries",
                    Author: "Your Name",
                    CreatedDate: new Date()
                };
                wb.SheetNames.push("Enquiries");
                var ws_data = [];
                ws_data.push(["Product", "Name", "Location", "Email", "Mobile No", "Message", "Created"]);
                data.enquiries.forEach(function (enquiry) {
                    ws_data.push([enquiry.product, enquiry.name, enquiry.location, enquiry.email, enquiry.mobile_no, enquiry.message, enquiry.created]);
                });
                var ws = XLSX.utils.aoa_to_sheet(ws_data);
                wb.Sheets["Enquiries"] = ws;
                var wbout = XLSX.write(wb, { bookType: 'xlsx', type: 'binary' });

                function s2ab(s) {
                    var buf = new ArrayBuffer(s.length);
                    var view = new Uint8Array(buf);
                    for (var i = 0; i != s.length; ++i) view[i] = s.charCodeAt(i) & 0xFF;
                    return buf;
                }

                // Trigger file download
                saveAs(new Blob([s2ab(wbout)], { type: "application/octet-stream" }), "enquiries.xlsx");
            } else {
                console.log("Error: " + data.error);
            }
        },
        error: function(xhr, status, error) {
            console.error("Error:", error);
        }
    });
}


//---recipe---//
$(document).on("click", "#recipe_search", function () {
    console.log("recipe");
    recipe_view("None");
});

function recipe_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "recipe-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#recipe-table").html(data.template);
        },
    });
}

function changerecipestatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "recipe-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#recipe-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_recipe() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "recipe-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#recipe-table").html(data.template);
        },
    });
}

$(document).ready(function() {
    $(".delete-spec-btn").on("click", function() {
        var specIndex = $(this).data("spec-index");
        var whyNameInputId = "#why_title_" + specIndex;
        var whyDescInputId = "#why_desc_" + specIndex;

        var title = $(whyNameInputId).val();
        var amount = $(whyDescInputId).val();

        $.ajax({
            type: "GET",
            url: "/superadmin/delete-ingredient/",
            data: {
                title: title,
                amount: amount,
            },
            success: function(response) {
                if (response.success) {
                    // Successfully deleted, remove the corresponding multi-field
                    $(whyNameInputId).closest(".multi-field").remove();
                    $(this).remove(); 
                } else {
                    console.log('Error:', response.error);
                }
            }.bind(this) 
        });
    });
});


$(document).ready(function() {
    $(".delete-image-btn").on("click", function() {
        var imageId = $(this).data("image-id");
        var deleteUrl = "/superadmin/delete-recipeslider/" + imageId + "/";  // Update this URL to your Django view for deleting the image
        
        // Store references to the image and delete button with unique IDs
        var imageElement = $("#slider" + imageId);
        var deleteButton = $("#btn-del" + imageId);
        console.log(imageId)
        $.ajax({
            type: "GET",
            url: deleteUrl,
            data: { csrfmiddlewaretoken: "{{ csrf_token }}" },  // Include the CSRF token
            success: function(response) {
                if (response.success) {
                    
                    // Remove the specific image and delete button associated with the clicked button
                    imageElement.remove();
                    deleteButton.remove();
                } else {
                    console.log('Error:', response.error);
                }
            }
        });
    });
});

//application

$(document).on("click", "#application_search", function () {
    console.log("Application");
    application_view("None");
});

function application_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
	var start_date = $("#start_date").val(); // Fetch start date value
    var end_date = $("#end_date").val(); // Fetch end date value
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "application-view",
        type: "GET",
        data: { search: search,  start_date: start_date, end_date: end_date, page: page, sts: sts },
        success: function (data) {
            $("#application-table").html(data.template);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_application() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "application-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#application-table").html(data.template);
        },
    });
}



//---Product---//
$(document).on("click", "#product_search", function () {
    console.log("product");
    product_view("None");
});

function product_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "product-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#product-table").html(data.template);
        },
    });
}

function changeproductstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "product-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#product-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function changehomepagestatus(id,sts){
    var page = $("#page").val()
    console.log(id,sts)
    $.ajax({
        url:'product-view',
        type:'GET',
        data:{'page':page,'new':sts,'item_id':id},
        success: function(data){
            $("#product-table").html(data.template)
            $("#message002").show().fadeOut(1000);
        }
    })
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_product() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "product-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#product-table").html(data.template);
        },
    });
}




// deepsea product details

$(document).on("click", "#dproduct_search", function () {
    console.log("product");
    productss_view("None");
});

function productss_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "product-details-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#products-table").html(data.template);
        },
    });
}

function changeproductsstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "product-details-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#products-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}


function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_products() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "product-details-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#products-table").html(data.template);
        },
    });
}



//brand product

$(document).on("click", "#bproduct_search", function () {
    console.log("product");
    bproduct_view("None");
});

function bproduct_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "brand-product-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#bproduct-table").html(data.template);
        },
    });
}

function changebproductstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "brand-product-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#bproduct-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}


function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_bproduct() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "brand-product-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#bproduct-table").html(data.template);
        },
    });
}



function getbcategory() {
    var id = $('#prod').val();
    console.log(id, '***');
    $.ajax({
        type: 'GET',
        url: '/superadmin/brandproduct-getcategory/',
        data: {
            'id': id
        },

        success: function (data) {
            if (data.status) {
                console.log('success');
                // console.log(data);
                $('#cat').html(data.template);

            } else {
                $("#cat").html(data.template);
                // Handle errors or display a message
                console.error('Error loading category content.');
            }
        }
    });
}

// brand product details

$(document).on("click", "#bproducts_search", function () {
    console.log("product");
    bproducts_view("None");
});

function bproducts_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "brand-product-details-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#bproducts-table").html(data.template);
        },
    });
}

function changebproductsstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "brand-product-details-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#bproducts-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}


function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_bproducts() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "brand-product-details-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#bproducts-table").html(data.template);
        },
    });
}

//---Seo---//
$(document).on("click", "#seo_search", function () {
    console.log("Seo");
    seo_view("None");
});

function seo_view(data) {
    console.log(data);
    var page = "1";
    if (data != "None") {
        var page = data;
    }
    console.log('page', page);
    var search = $("#search").val();
    var sts = $("#status").val();

    $.ajax({
        url: "seo-view",
        type: "GET",
        data: { search: search, page: page, sts: sts },
        success: function (data) {
            $("#seo-table").html(data.template);
        },
    });
}

function changeseosstatus(id, sts) {
    var page = $("#page").val();
    var search = $("#search").val();
    var statusFilter = $("#status").val();
    console.log(id, sts);
    // console.log('pg', page);
    $.ajax({
        url: "seo-view",
        type: "GET",
        data: {
            page: page,
            status: sts,
            item_id: id,
            search: search,
            sts: statusFilter,
        },
        success: function (data) {
            $("#seo-table").html(data.template);
            $("#message001").show().fadeOut(1000);
        },
    });
}

function show_modal(id) {
    $("#hid").val(id);
    $("#modaldemo5").modal("show");
}

function confirm_delete_seo() {
    var page = $("#page").val();
    id = $("#hid").val();
    console.log(id);
    $.ajax({
        url: "seo-view",
        type: "GET",
        data: { page: page, delete: "1", item_id: id },
        success: function (data) {
            $("#modaldemo5").modal("hide");
            $("#seo-table").html(data.template);
        },
    });
}


// submit button restriction

document.getElementById("myform").addEventListener("submit", function(event) {
    // Disable the submit button when the form is submitted
    document.getElementById("submitButton").disabled = true;

    setTimeout(function() {
	
    document.getElementById("submitButton").disabled = false;
    }, 3000);
});




//restrict image upload

function addFileInputListener(ids) {
    ids.forEach(function(id) {
        const fileInput = document.getElementById(id);

        fileInput.addEventListener('change', function() {
            const file = fileInput.files[0];
            const allowedExtensions = /(\.jpg|\.jpeg|\.png|\.webp)$/i;

            if (!allowedExtensions.test(file.name)) {
                alert('Please select a JPEG, JPG, or PNG image file..!!');
                fileInput.value = '';
            }
        });
    });
}

addFileInputListener(['image-upload', 'image-upload1']);      