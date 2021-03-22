import Vue from "vue"; // 설치했던 fontawesome-svg-core와 vue-fontawesome 
import { library } from "@fortawesome/fontawesome-svg-core"; 
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome"; // 설치했던 아이콘파일에서 해당 아이콘만 불러옵니다. 

import { faFeatherAlt, faPaw, faHome } from "@fortawesome/free-solid-svg-icons"; 
 
library.add(faFeatherAlt, faPaw, faHome); // fontawesome아이콘을 Vue탬플릿에 사용할 수 있게 등록해 줍니다. 

Vue.component("font-awesome-icon", FontAwesomeIcon);
