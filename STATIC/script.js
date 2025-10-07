document.getElementById('foodForm').addEventListener('submit', function(e){
    e.preventDefault();

    const age = document.getElementById('age').value;
    const diet = document.getElementById('diet').value;
    const goal = document.getElementById('goal').value;
    const cuisine = document.getElementById('cuisine').value;

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `<p>Recommendation will appear here for a ${age}-year-old following ${diet} diet, goal: ${goal}, preferring ${cuisine} cuisine.</p>`;
});
