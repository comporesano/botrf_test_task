import { defineStore } from "pinia";

interface User {
    birth_date: string;
    first_name: string;
    last_name: string;
    username: string;
  }

export const useUserManagerStore = defineStore('userManager', {
  state: () => ({
    currentUser: {} as User,
  }),
  actions: {
    setCurrentUser(user: User) {
      this.currentUser = user;
    },
    
    clearCurrentUser() {
      this.currentUser = {} as User;
    },

    updateUserProperty(propertyName: keyof User, newValue: User[keyof User]) {
      if (propertyName in this.currentUser) {
        this.currentUser[propertyName] = newValue;
      }
    }
  }
});
