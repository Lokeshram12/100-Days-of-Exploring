// 1. Call fetch() with the URL
fetch('https://api.sampleapis.com/coffee/iced')
// 2. Check for HTTP-level errors
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status} — ${response.statusText}`);
    }
    return response.json();           // parse JSON body
  })
// 3. Work with the parsed data
  .then(data => {
    console.log('Users:', data);
  })
// 4. Catch network or parsing errors
  .catch(err => {
    console.error('Fetch error:', err);
  });


  // for POST request

  const newUser = { name: 'Alice', email: 'alice@example.com' };

fetch('https://api.example.com/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'   // tell server it’s JSON
  },
  body: JSON.stringify(newUser)          // serialize JS → JSON
})
  .then(res => {
    if (!res.ok) throw new Error(res.statusText);
    return res.json();
  })
  .then(created => {
    console.log('Created user:', created);
  })
  .catch(err => {
    console.error('POST failed:', err);
  });
