<template>
  <div class="container">
    <div class="header-section">
      <h1>Users</h1>
      <router-link to="/products" class="btn-nav">Product Analytics</router-link>
    </div>
    <div v-if="analytics" class="analytics-grid">
      <div class="stat-card">
        <h3>User Distribution by State</h3>
        <div class="data-list">
          <div v-for="(count, state) in analytics.by_state" :key="state" class="stat-row">
            <span>{{ state }}</span>
            <span>{{ count }}</span>
          </div>
        </div>
      </div>

      <div class="stat-card">
        <h3>User Distribution by University</h3>
        <div class="data-list">
          <div v-for="(count, uni) in analytics.by_university" :key="uni" class="stat-row">
            <span>{{ uni }}</span>
            <span class="count-badge">{{ count }}</span>
          </div>
        </div>
      </div>
    </div>
    <input
      v-model="searchQuery"
      placeholder="Filter by name, age, gender, role or state..."
      class="filter-input"
    />
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>User Image</th>
            <th @click="sort('name')" class="sortable">Name ↕</th>
            <th @click="sort('age')" class="sortable">Age ↕</th>
            <th @click="sort('gender')" class="sortable">Gender ↕</th>
            <th @click="sort('role')" class="sortable">Role ↕</th>
            <th @click="sort('state')" class="sortable">State ↕</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in filteredAndSortedUsers" :key="user.name">
            <td><img :src="user.image" class="user-img" alt="profile" /></td>
            <td style="font-weight: 600">{{ user.name }}</td>
            <td>{{ user.age }}</td>
            <td>{{ user.gender }}</td>
            <td>{{ user.role }}</td>
            <td>{{ user.state }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import axios from "axios";

const users = ref([]);
const analytics = ref(null);
const searchQuery = ref("");
const sortKey = ref("name");

onMounted(async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/users");
    users.value = response.data.users;
    analytics.value = response.data.analytics;
  } catch (error) {
    console.error("Erro ao carregar utilizadores:", error);
  }
});

const sort = (key) => {
  sortKey.value = key;
};

const roleHierarchy = {
  admin: 1,
  moderator: 2,
  user: 3,
};

const filteredAndSortedUsers = computed(() => {
  const search = searchQuery.value.toLowerCase();

  let result = users.value.filter((user) => {
    const userGender = user.gender.toLowerCase();

    const matchesGender =
      search === "male" || search === "female"
        ? userGender === search
        : userGender.includes(search);

    return (
      String(user.name).toLowerCase().includes(search) ||
      String(user.age).includes(search) ||
      String(user.role).toLowerCase().includes(search) ||
      String(user.state).toLowerCase().includes(search) ||
      matchesGender
    );
  });

  return result.sort((a, b) => {
    if (sortKey.value === "role") {
      return roleHierarchy[a.role] - roleHierarchy[b.role];
    }
    if (a[sortKey.value] < b[sortKey.value]) return -1;
    if (a[sortKey.value] > b[sortKey.value]) return 1;
    return 0;
  });
});
</script>
