<template>
  <div class="container">
    <div class="header-section">
      <h1>Product Analyticss</h1>
      <router-link to="/" class="btn-nav">Users</router-link>
    </div>

    <div v-if="!analytics">Loading...</div>

    <div v-else>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 40px">
        <div class="card" style="border: 1px solid #eee; padding: 20px; border-radius: 8px">
          <h3>Top Brands (Reviews)</h3>
          <ul style="list-style: none; padding: 0">
            <li
              v-for="(data, brand) in analytics.top_brands"
              :key="brand"
              style="margin-bottom: 8px; border-bottom: 1px solid #f9f9f9"
            >
              <strong>{{ brand }}:</strong> {{ (data.total_rating / data.count).toFixed(2) }}
            </li>
          </ul>
        </div>
        <div class="card" style="border: 1px solid #eee; padding: 20px; border-radius: 8px">
          <h3>Price Range</h3>
          <ul style="list-style: none; padding: 0">
            <li
              v-for="(range, cat) in analytics.price_ranges"
              :key="cat"
              style="margin-bottom: 8px; border-bottom: 1px solid #f9f9f9"
            >
              <span style="text-transform: capitalize">{{ cat }}:</span>
              <strong>${{ range }}</strong>
            </li>
          </ul>
        </div>
      </div>
      <div style="margin-bottom: 40px; padding: 20px; background: #f1f5f9; border-radius: 8px">
        <h3>Stock Available by Category</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 15px">
          <div
            v-for="(stock, cat) in analytics.categories_stock"
            :key="cat"
            style="background: white; padding: 10px 15px; border-radius: 20px; font-size: 0.9rem"
          >
            <strong style="text-transform: capitalize">{{ cat }}:</strong> {{ stock }} un.
          </div>
        </div>
      </div>
      <h3>Stock</h3>
      <table>
        <thead>
          <tr>
            <th>Product</th>
            <th>Category</th>
            <th>Stock Available</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="p in analytics.all_products" :key="p.name">
            <td>{{ p.name }}</td>
            <td style="text-transform: capitalize">{{ p.category }}</td>
            <td>{{ p.stock }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const analytics = ref(null);

onMounted(async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/products/analytics");
    analytics.value = response.data;
    console.log("Dados recebidos:", response.data);
  } catch (error) {
    console.error("Erro ao procurar produtos:", error);
  }
});
</script>
