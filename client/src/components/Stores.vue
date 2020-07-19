  <!-- eslint-disable-next-line vue/max-attributes-per-line -->
<script>
import axios from 'axios';
import debounce from 'lodash';
import BACKEND_URL from '../constants';

export default {
  name: 'autocomplete',

  data() {
    return {
      results: [],
      search: '',
      isLoading: false,
      offset: 0,
      fullyLoaded: false,
    };
  },

  methods: {
    onChange() {
      this.fullyLoaded = false;
      debounce(this.fetchAutocompleteResults(), 100);
    },
    fetchAutocompleteResults() {
      // Let's warn the parent that a change was made
      if (this.search.length >= 2) {
        this.$emit('input', this.search);
        this.isLoading = true;
        const path = `${BACKEND_URL}/stores?query=${this.search}&limit=3`;
        axios.get(path)
          .then((res) => {
            this.results = res.data;
            this.isLoading = false;
            this.offset = res.data.length;
            // eslint-disable-next-line
            console.log(this.results);
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      }
    },
    fetchFurtherResults() {
      if (this.fullyLoaded || this.search.length < 2) {
        return;
      }
      this.$emit('input', this.search);
      const path = `${BACKEND_URL}/stores?query=${this.search}&offset=${this.offset}`;
      axios.get(path)
        .then((res) => {
          // eslint-disable-next-line
          this.results.push.apply(this.results, res.data);
          // eslint-disable-next-line
          console.log(this.results);
          this.fullyLoaded = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    onEnter() {
      this.fetchFurtherResults();
    },
    handleScroll(evt) {
      this.fetchFurtherResults();
    },
  },
  watch: {
    items(val, oldValue) {
      // actually compare them
      if (val.length !== oldValue.length) {
        this.results = val;
        this.isLoading = false;
      }
    },
  },
  mounted() {
    document.addEventListener('click', this.handleClickOutside);
    window.addEventListener('scroll', this.handleScroll);
  },
  destroyed() {
    document.removeEventListener('click', this.handleClickOutside);
    window.removeEventListener('scroll', this.handleScroll);
  },
};
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="query">Stores Query:</div>
      <div class="autocomplete">
        <input
          type="text"
          @input="onChange"
          v-model="search"
          @keydown.down="onArrowDown"
          @keydown.up="onArrowUp"
          @keydown.enter="onEnter"
          class="input-box"
        />
        <button id="search-button" v-on:click="fetchFurtherResults">
          <svg id="search-icon" class="search-icon" viewBox="0 0 24 24">
            <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
            <path d="M0 0h24v24H0z" fill="none"/>
          </svg>
        </button>
        <ul id="autocomplete-results" v-show="search.length>=2" class="autocomplete-results list-group">
          <li v-if="results.length!==0">
            <div class="li-item">Name</div>
            <div class="li-item">Postcode</div>
          </li>
          <li class="loading" v-if="isLoading">Loading results...</li>
          <li class="loading" v-if="results.length===0">No results available</li>
          <li
            v-else
            v-for="(result, i) in results"
            :key="i"
            class="autocomplete-result list-group-item"
          >
            <div class="li-item list-group-item">{{result.name}}</div>
            <div class="li-item list-group-item">{{result.postcode}}</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style>
.autocomplete {
  position: relative;
  width: 480px;
}

.query {
  width: 100%;
  margin: 10px;
  font-weight: 700;
}

.autocomplete-results {
  padding: 10px;
  margin: 0;
  border: 1px solid #eeeeee;
  overflow: auto;
  width: 100%;
}

.autocomplete-result {
  list-style: none;
  text-align: left;
  padding: 4px 2px;
  cursor: pointer;
}

.input-box {
  width: 420px;
}

#search-button {
  width: 40px;
  height: 30px;
  margin-left: 16px;
}

#search-button svg {
  width: 25px;
  height: 25px;
}

.li-item{
  width: 160px;
  margin-right: 10px;
  float: left;
  text-align: center;
  border: none;
}
</style>
