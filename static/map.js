document.addEventListener('DOMContentLoaded', function() {
    // Initialize the map
    const map = L.map('map').setView([0, 0], 2);
    
    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    
    // Store markers
    const markers = [];
    
    // Function to load users from API
    function loadUsers() {
        fetch('/api/users/')
            .then(response => response.json())
            .then(users => {
                // Clear existing markers
                markers.forEach(marker => map.removeLayer(marker));
                markers.length = 0;
                
                // Add markers for each user
                users.forEach(user => {
                    const marker = L.marker([user.latitude, user.longitude])
                        .addTo(map)
                        .bindPopup(
                            `<strong>${user.name}</strong><br>
                            Disability: ${user.disability_type}<br>
                            Contact: ${user.contact_info}`
                        );
                    markers.push(marker);
                });
                
                // If we have users, center the map on the first one
                if (users.length > 0) {
                    map.setView([users[0].latitude, users[0].longitude], 10);
                }
            })
            .catch(error => console.error('Error loading users:', error));
    }
    
    // Load users initially
    loadUsers();
    
    // Handle form submission
    document.getElementById('userForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form data
        const userData = {
            name: document.getElementById('name').value,
            latitude: parseFloat(document.getElementById('latitude').value),
            longitude: parseFloat(document.getElementById('longitude').value),
            disability_type: document.getElementById('disability_type').value,
            contact_info: document.getElementById('contact_info').value
        };
        
        // Submit data to API
        fetch('/api/users/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData)
        })
        .then(response => response.json())
        .then(data => {
            // Add the new user to the map
            loadUsers();
            // Reset form
            document.getElementById('userForm').reset();
            alert('User registered successfully!');
        })
        .catch(error => {
            console.error('Error registering user:', error);
            alert('Error registering user. Please try again.');
        });
    });
    
    // Add click handler to get coordinates
    map.on('click', function(e) {
        document.getElementById('latitude').value = e.latlng.lat.toFixed(6);
        document.getElementById('longitude').value = e.latlng.lng.toFixed(6);
    });
});
