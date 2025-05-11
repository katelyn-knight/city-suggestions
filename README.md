# City Autocomplete API

This project provides an API endpoint for autocomplete suggestions of large cities based on user input. It leverages a database of cities to quickly provide suggestions as the user types.

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone
    ```
2. Activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ``` 

3. Run the Flask application:
    ```bash
    flask run
    ```

## API Endpoint

The API provides a single endpoint for retrieving autocomplete suggestions:

### Endpoint

```
GET /suggestions?q={user_input}&latitude={latitude}&longitude={longitude}
```

### Parameters

- `q` (required): User input for which autocomplete suggestions are requested.
- `latitude` (optional): Latitude of the desired location.
- `longitude` (optional): Longitude of the desired location.

### Response

The response is a JSON object containing a list of suggestions. Each suggestion includes the city name, latitude, longitude, and a score indicating its relevance.

Example response:
```json
{
    "suggestions": [
       {
          "latitude": 42.98339, 
          "longitude": -81.23304, 
          "name": "London, 08, CA", 
          "score": 1.0
       },
       {
          "latitude": 42.46676, 
          "longitude": -70.94949, 
          "name": "Lynn, MA, US",
          "score": 0.9736842105263158
       },
        ...
    ]
}
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes to the branch (`git push origin feature/new-feature`).
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README.md file further to include more detailed instructions, explanations, or additional sections as needed for your project.
