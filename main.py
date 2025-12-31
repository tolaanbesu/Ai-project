import numpy as np

def pca(X, k):
    mean = np.mean(X, axis=0)
    X_centered = X - mean

    cov_matrix = np.cov(X_centered, rowvar=False)

    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    W = eigenvectors[:, :k]

    X_reduced = np.dot(X_centered, W)

    return X_reduced, eigenvalues[:k]


if __name__ == "__main__":

    while True:
        print("\n=== PCA MENU ===")
        print("1. Compute PCA")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "2":
            print("Exiting program...")
            break

        elif choice == "1":
            try:
                # Input number of samples
                n_samples = int(input("Enter number of samples (rows): "))
                if n_samples <= 0:
                    raise ValueError("Number of samples must be positive.")

                # Input number of features
                n_features = int(input("Enter number of features (columns): "))
                if n_features <= 0:
                    raise ValueError("Number of features must be positive.")

                print("\nEnter the data row by row (space-separated):")

                data = []
                for i in range(n_samples):
                    row_input = input(f"Row {i+1}: ").split()

                    if len(row_input) != n_features:
                        raise ValueError(
                            f"Row {i+1} must contain exactly {n_features} values."
                        )

                    row = list(map(float, row_input))
                    data.append(row)

                X = np.array(data)

                # Input no of principal components
                k = int(input("\nEnter number of principal components (k): "))
                if k <= 0 or k > n_features:
                    raise ValueError(
                        "k must be greater than 0 and less than or equal to number of features."
                    )

                # Run PCA
                X_reduced, eigenvalues = pca(X, k)

                # Output
                print("\nOriginal shape:", X.shape)
                print("Reduced shape:", X_reduced.shape)
                print("Top eigenvalue(s):", eigenvalues)
                print("Reduced data:")
                print(X_reduced)

            except ValueError as ve:
                print("\nInput Error:", ve)

            except Exception as e:
                print("\nUnexpected Error:", e)

        else:
            print("\nInvalid choice! Please enter 1 or 2.")
















