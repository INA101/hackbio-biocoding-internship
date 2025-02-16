def hamming_distance(str1, str2):
    """Calculates Hamming distance between two strings."""

    # Make both strings the same length by padding with spaces
    max_length = max(len(str1), len(str2))
    str1 = str1.ljust(max_length)  # Pad with spaces
    str2 = str2.ljust(max_length)

    # Count number of differing characters
    distance = sum(1 for a, b in zip(str1, str2) if a != b)

    return distance


# my usernames
slack_username = "Noel"
twitter_handle = "_notnoel"

distance = hamming_distance(slack_username, twitter_handle)
print("Hamming Distance:", distance)
