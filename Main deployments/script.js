document.getElementById('search-btn').addEventListener('click', async function () {
    const url = document.getElementById('youtube-url').value;
    const videoId = getYouTubeVideoID(url);
    const API_KEY = "AIzaSyCO9VG4-8i5TGZr6VuROa4pRbFgeHX1BNI";

    if (!videoId) {
        alert("❌ Invalid YouTube URL!");
        return;
    }

    // Show Loader
    document.getElementById("loading-section").style.display = "block";
    document.getElementById("result-section").style.display = "none";
    document.getElementById("video-details-section").style.display = "none";

    try {
        const response = await fetch(`https://www.googleapis.com/youtube/v3/videos?part=statistics,snippet&id=${videoId}&key=${API_KEY}`);
        const data = await response.json();

        if (!data.items || data.items.length === 0) {
            alert("❌ Video Not Found!");
            document.getElementById("loading-section").style.display = "none";
            return;
        }

        const video = data.items[0];

        // Fill Video Details
        document.getElementById('views-count').textContent = video.statistics.viewCount;
        document.getElementById('likes-count').textContent = video.statistics.likeCount;
        document.getElementById('comments-count').textContent = video.statistics.commentCount;
        document.getElementById('video-title').textContent = video.snippet.title;
        document.getElementById('thumbnail').src = video.snippet.thumbnails.high.url;
        document.getElementById('video-summary').textContent = video.snippet.description;

        // Update Sentiment Breakdown
        updateSentimentBreakdown({ positive: 60, negative: 25, neutral: 15 });

        // Show Result Section
        document.getElementById("loading-section").style.display = "none";
        document.getElementById("result-section").style.display = "flex";
        document.getElementById("video-details-section").style.display = "flex";

    } catch (error) {
        alert("❌ Error Fetching Data!");
        console.error(error);
        document.getElementById("loading-section").style.display = "none";
    }
});

// Function to Extract Video ID from URL
function getYouTubeVideoID(url) {
    const match = url.match(/(?:youtu\.be\/|youtube\.com\/(?:.*v=|embed\/|v\/|shorts\/))([^?&]+)/);
    return match ? match[1] : null;
}

// Function to Update Sentiment Breakdown
function updateSentimentBreakdown(sentiments) {
    document.getElementById("positive-count").textContent = sentiments.positive + "%";
    document.getElementById("negative-count").textContent = sentiments.negative + "%";
    document.getElementById("neutral-count").textContent = sentiments.neutral + "%";
}

// Show Graph Function
document.getElementById("graph-btn").addEventListener("click", function () {
    document.querySelector(".graph-section").style.display = "block";
    const ctx = document.getElementById("sentimentBarChart").getContext("2d");

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Positive", "Negative", "Neutral"],
            datasets: [{
                label: "Sentiment Analysis",
                data: [60, 25, 15],
                backgroundColor: ["#4CAF50", "#F44336", "#FFC107"]
            }]
        }
    });
});
