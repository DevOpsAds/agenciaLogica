
    document.addEventListener("DOMContentLoaded", function () {
        // Event listener para expandir/colapsar seções de categoria
        var categoryHeaders = document.querySelectorAll(".category-header");
        categoryHeaders.forEach(function (header) {
            header.addEventListener("click", function () {
                this.classList.toggle("active");
                var categoryContent = this.nextElementSibling;
                if (categoryContent.style.maxHeight) {
                    categoryContent.style.maxHeight = null;
                } else {
                    categoryContent.style.maxHeight = categoryContent.scrollHeight + "px";
                }
            });
        });

        // Event listener para expandir/colapsar serviços
        var serviceHeaders = document.querySelectorAll(".service-header");
        serviceHeaders.forEach(function (header) {
            header.addEventListener("click", function () {
                this.classList.toggle("active");
                var serviceContent = this.nextElementSibling;
                if (serviceContent.style.maxHeight) {
                    serviceContent.style.maxHeight = null;
                } else {
                    serviceContent.style.maxHeight = serviceContent.scrollHeight + "px";
                }
            });
        });
    });

