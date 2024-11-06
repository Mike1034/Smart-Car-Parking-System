document.addEventListener('DOMContentLoaded', function() {
    const resultsDiv = document.getElementById('results');
    const carResults = [
        { car_count: 5, free_space: 8 },
        { car_count: 6, free_space: 7 },
        { car_count: 7, free_space: 6 }
    ];

    carResults.forEach(result => {
        const resultDiv = document.createElement('div');
        resultDiv.classList.add('result');
        resultDiv.innerHTML = `
            <p>CARCOUNTER: ${result.car_count}</p>
            <p>FREESPACE: ${result.free_space}</p>
        `;
        resultsDiv.appendChild(resultDiv);
    });
});
