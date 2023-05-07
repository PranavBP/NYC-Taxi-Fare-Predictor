var ctx = document.getElementById('myChart').getContext('2d');

var labels = {{ labels | tojson }};
var data = {{ data | tojson }};

// Combine labels and data into a list of tuples
var labelDataTuples = labels.map((l, i) => [l, data[i]]);

// Sort the list of tuples based on the label
var sortedLabelDataTuples = labelDataTuples.sort((a, b) => a[0] - b[0]);

// Extract the sorted labels and data from the sorted list of tuples
var sortedLabels = sortedLabelDataTuples.map((t) => t[0]);
var sortedData = sortedLabelDataTuples.map((t) => t[1]);

var chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: sortedLabels,
        datasets: [{
            label: 'Hour in Day',
            data: sortedData,
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#8B008B', '#FFA07A']
        }]
    },
    options: {
        legend: { display: true },
        title: {
            display: true,
            text: 'Hourly Cab ride count distribution'
        },
        scales: {
            xAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});