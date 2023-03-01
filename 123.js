import React, { useState } from "react";

const App = () => {
  const [categories, setCategories] = useState([
    {
      id: 1,
      name: "Category 1",
      products: [
        { id: 1, name: "Product 1", likes: 0 },
        { id: 2, name: "Product 2", likes: 0 },
        { id: 3, name: "Product 3", likes: 0 },
        { id: 4, name: "Product 4", likes: 0 },
        { id: 5, name: "Product 5", likes: 0 },
      ],
    },
    {
      id: 2,
      name: "Category 2",
      products: [
        { id: 6, name: "Product 6", likes: 0 },
        { id: 7, name: "Product 7", likes: 0 },
        { id: 8, name: "Product 8", likes: 0 },
        { id: 9, name: "Product 9", likes: 0 },
        { id: 10, name: "Product 10", likes: 0 },
      ],
    },
    {
      id: 3,
      name: "Category 3",
      products: [
        { id: 11, name: "Product 11", likes: 0 },
        { id: 12, name: "Product 12", likes: 0 },
        { id: 13, name: "Product 13", likes: 0 },
        { id: 14, name: "Product 14", likes: 0 },
        { id: 15, name: "Product 15", likes: 0 },
      ],
    },
    {
      id: 4,
      name: "Category 4",
      products: [
        { id: 16, name: "Product 16", likes: 0 },
        { id: 17, name: "Product 17", likes: 0 },
        { id: 18, name: "Product 18", likes: 0 },
        { id: 19, name: "Product 19", likes: 0 },
        { id: 20, name: "Product 20", likes: 0 },
      ],
    },
  ]);

  const [selectedCategoryId, setSelectedCategoryId] = useState(null);

  const handleCategorySelect = (categoryId) => {
    setSelectedCategoryId(categoryId);
  };

  const handleProductLike = (productId) => {
    const updatedCategories = categories.map((category) => {
      const updatedProducts = category.products.map((product) => {
        if (product.id === productId) {
          return {
            ...product,
            likes: product.likes + 1,
          };
        }
        return product;
      });
      return { ...category, products: updatedProducts };
    });
    setCategories(updatedCategories);
  };

  const handleProductRemove = (productId) => {
    const updatedCategories = categories.map((category) => {
      const updatedProducts = category.products.filter(
        (product) => product.id !== productId
      );
      return { ...category, products: updatedProducts };
    });
    setCategories(updatedCategories);
  };

  return (
    <div>
      <h1>Categories</h1>
      <ul>
        {categories.map((category) => (
          <li key={category.id}>
            <button onClick={() => handleCategorySelect(category.id)}>
              {category.name}
            </button>
            {selectedCategoryId === category.id && (
              <ul>
                {category.products.map((product) => (
                  <ProductItem
                    key={product.id}
                    product={product}
                    onLike={handleProductLike}
                    onRemove={handleProductRemove}
                  />
                ))}
              </ul>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

const ProductList = ({ products, onLike, onRemove }) => {
  return (
    <ul>
      {products.map((product) => (
        <ProductItem
          key={product.id}
          product={product}
          onLike={onLike}
          onRemove={onRemove}
        />
      ))}
    </ul>
  );
};

const ProductItem = ({ product, onLike, onRemove }) => {
  const handleLikeClick = () => {
    onLike(product.id);
  };

  const handleRemoveClick = () => {
    onRemove(product.id);
  };

  return (
    <li>
      <span>{product.name}</span>
      <button onClick={handleLikeClick}>{`${product.likes} Likes`}</button>
      <button onClick={handleRemoveClick}>Remove</button>
    </li>
  );
};
