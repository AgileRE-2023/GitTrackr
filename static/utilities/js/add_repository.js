document.addEventListener("DOMContentLoaded", function () {
    const dropdownButton = document.querySelector(".group");
    const dropdownMenu = document.querySelector(".absolute");

    dropdownButton.addEventListener("click", function () {
        dropdownMenu.classList.toggle("hidden");
    });
});

var containerCount = 0;
var permanentValues = [];

function clearInputValue() {
    document.getElementById('txt').value = '';
}

function getValue() {
    var input = document.getElementById('txt').value;
    var svg = document.getElementById('mySvg');
    var result = document.getElementById('result');
    result.textContent = input;

    if (input.trim() === "") {
        svg.style.display = "none";
    } else {
        svg.style.display = "block";
    }
}


document.getElementById('clickableDiv').addEventListener('click', function () {
    showPermanentValue();
});

function deletePermanentValue(valueElement, containerId) {
    valueElement.parentNode.remove();
    var index = permanentValues.indexOf(valueElement.textContent);
    if (index > -1) {
        permanentValues.splice(index, 1);
    }
    containerCount--;

    if (containerCount < 5) {
        document.getElementById('clickableDiv').addEventListener('click', showPermanentValue);
    }
}

function showPermanentValue() {
    if (containerCount < 5) {
        var result = document.getElementById('result');
        var permanentValue = document.createElement('p');
        permanentValue.textContent = result.textContent;

        containerCount++;
        var permanentValuesContainer = document.createElement('div');
        permanentValuesContainer.id = "permanentValuesContainer" + containerCount;
        permanentValuesContainer.className = "flex py-2 px-4 bg-white shadow-xl rounded-lg w-fit items-center justify-between";

        var deleteButton = document.createElement('div');
        deleteButton.innerHTML = `<svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M11.5563 1.75736L7.31371 6L11.5563 10.2426L10.1421 11.6569L5.89949 7.41421L1.65685 11.6569L0.242641 10.2426L4.48528 6L0.242641 1.75736L1.65685 0.343146L5.89949 4.58579L10.1421 0.343146L11.5563 1.75736Z" fill="black"/>
    </svg>`;
        deleteButton.className = "your-class-name";
        deleteButton.addEventListener('click', function () {
            deletePermanentValue(permanentValue, permanentValuesContainer.id);
        });

        permanentValuesContainer.style.width = "190px";
        deleteButton.style.display = "flex";
        deleteButton.style.alignItems = "start";
        deleteButton.style.justifyContent = "space-between";


        permanentValuesContainer.appendChild(permanentValue);
        permanentValuesContainer.appendChild(deleteButton);
        document.getElementById('permanentValuesContainer').appendChild(permanentValuesContainer);
        permanentValues.push(permanentValue.textContent);

        if (containerCount === 5) {
            document.getElementById('clickableDiv').removeEventListener('click', showPermanentValue);
        }
    }
    clearInputValue();

    $.ajax({
        url: '{% url "save_repository" %}',
        method: 'POST',
        data: {'repository_name': input},
        dataType: 'json',
        success: function (data) {
            updatePermanentValues(data.saved_repositories);
        },
        error: function () {
            console.log('Gagal menyimpan repository.');
        }
    });
    clearInputValue();
}

function updatePermanentValues(savedRepositories) {
    var permanentValuesContainer = $('#permanentValuesContainer');
    permanentValuesContainer.empty();

    for (const savedRepository of savedRepositories) {
        const permanentValue = $('<p>').text(savedRepository);

        const deleteButton = $('<div>').html(`<svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M11.5563 1.75736L7.31371 6L11.5563 10.2426L10.1421 11.6569L5.89949 7.41421L1.65685 11.6569L0.242641 10.2426L4.48528 6L0.242641 1.75736L1.65685 0.343146L5.89949 4.58579L10.1421 0.343146L11.5563 1.75736Z" fill="black"/>
        </svg>`);
        deleteButton.on('click', function () {
            deletePermanentValue(permanentValue, permanentValuesContainer.attr('id'));
        });

        // Adding styles for SVG
        permanentValuesContainer.css('width', '190px');
        deleteButton.css('display', 'flex');
        deleteButton.css('align-items', 'start');
        deleteButton.css('justify-content', 'space-between');

        permanentValuesContainer.append(permanentValue);
        permanentValuesContainer.append(deleteButton);
    }
}