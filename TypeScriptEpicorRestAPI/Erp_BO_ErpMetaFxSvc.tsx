import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ErpMetaFxSvc
// Description: ErpMetaFxSvc
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetApp
   Description: View JSON layout and other metadata information
   OperationID: Get_GetApp
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetApp(request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetApp" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetViews
   Description: Get all views
   OperationID: Get_GetViews
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetViews_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetViews(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetViews", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSearch
   Description: Search dialog request and other metadata information
   OperationID: Get_GetSearch
      @param request Desc: EpMetaFxSearchRequest   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetSearch(request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetSearch" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSearchForm
   Description: Check for LIKE property folder
   OperationID: Get_GetSearchForm
      @param request Desc: EpMetaFxSearchRequest   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSearchForm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetSearchForm(request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetSearchForm" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPeek
   Description: Get Peek metadata information
   OperationID: Get_GetPeek
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPeek_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetPeek(request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetPeek" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPeeks
   Description: Gets folders and sub folders from peek folder.
   OperationID: Get_GetPeeks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPeeks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetPeeks(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetPeeks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTemplateView
   Description: Gets the pre-defined templates like report/process etc
   OperationID: Get_GetTemplateView
      @param templateType Desc: EpMetaFxViewRequest   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTemplateView_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetTemplateView(templateType:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof templateType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "templateType=" + templateType
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetTemplateView" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCombosData
   Description: Gets JSON files extended properties from the comobs
   OperationID: Get_GetCombosData
      @param request Desc: EpMetaFxComboRequest   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCombosData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetCombosData(request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetCombosData" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCombos
   Description: Gets folders and sub folders names from combo shared folder
   OperationID: Get_GetCombos
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCombos_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetCombos(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetCombos", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Upgrade
   Description: Upgrades the view
   OperationID: Upgrade
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Upgrade_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Upgrade_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Upgrade(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/Upgrade", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpgradeLayer
   Description: Upgrade layer
   OperationID: UpgradeLayer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpgradeLayer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpgradeLayer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpgradeLayer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/UpgradeLayer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveApp
   Description: Saves the information.
- In case of customization it saves as draft
- In case of layers, it saves in DB as WIP
   OperationID: SaveApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveApp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveApp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/SaveApp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PublishApp
   Description: publish the information.
- In case of customization it replaces the actual file
- In case of layers, it saves in DB
   OperationID: PublishApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PublishApp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PublishApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PublishApp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/PublishApp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BulkPublishLayers
   Description: Publishes all the layers in the list. Parent layers are not published automatically.
   OperationID: BulkPublishLayers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BulkPublishLayers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BulkPublishLayers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BulkPublishLayers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/BulkPublishLayers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BulkDeleteLayers
   Description: Delete layers and base app in bulk.
   OperationID: BulkDeleteLayers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BulkDeleteLayers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BulkDeleteLayers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BulkDeleteLayers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/BulkDeleteLayers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InvalidateCache
   Description: Deletes cache folder
   OperationID: InvalidateCache
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InvalidateCache_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvalidateCache_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InvalidateCache(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/InvalidateCache", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPage
   Description: returns page to client
   OperationID: Get_GetPage
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetPage(request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetPage" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetViewTypes
   Description: returns all the folder names except common from root path(.\MetaUI\Shared\ViewTypes).
   OperationID: Get_GetViewTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetViewTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetViewTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetViewTypes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLayer
   Description: Gets the layer.
   OperationID: Get_GetLayer
      @param request Desc: Request to get layer.   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLayer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetLayer(request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetLayer" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLayers
   Description: Get the layers.
   OperationID: Get_GetLayers
      @param request Desc: Request to get layers.   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLayers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetLayers(request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetLayers" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteLayer
   Description: Deletes the layer.
   OperationID: DeleteLayer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteLayer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLayer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteLayer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/DeleteLayer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateView
   Description: Generates the view.
   OperationID: GenerateView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateView_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateView(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GenerateView", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAuditLogs
   Description: This method returns audit logs.
   OperationID: Get_GetAuditLogs
      @param request Desc: request   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAuditLogs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetAuditLogs(request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetAuditLogs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DownloadSchema
   Description: Download event schema
   OperationID: Get_DownloadSchema
      @param request Desc: DownloadSchemaRequest   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadSchema_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_DownloadSchema(request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/DownloadSchema" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEventDesigner
   Description: This method gets the event designer.
   OperationID: GetEventDesigner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEventDesigner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEventDesigner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEventDesigner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetEventDesigner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetApplicationSubTypes
   Description: Get Application Types.
   OperationID: Get_GetApplicationSubTypes
      @param applicationType Desc: applicationType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetApplicationSubTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetApplicationSubTypes(applicationType:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof applicationType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "applicationType=" + applicationType
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetApplicationSubTypes" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetApplications
   Description: Get Applications.
   OperationID: Get_GetApplications
      @param request Desc: request   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetApplications_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetApplications(request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetApplications" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewApplication
   Description: Get New Application.
   OperationID: Get_GetNewApplication
      @param request Desc: request   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewApplication_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetNewApplication(request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/GetNewApplication" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportApp
   Description: Export App
   OperationID: Get_ExportApp
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_ExportApp(viewId:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof viewId!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "viewId=" + viewId
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/ExportApp" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportApp
   Description: Import App
   OperationID: ImportApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportApp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportApp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/ImportApp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Sync
   Description: Sync
   OperationID: Sync
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Sync_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Sync_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Sync(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/Sync", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DuplicateApp
   Description: Duplicate App
   OperationID: DuplicateApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateApp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateApp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/DuplicateApp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteApp
   Description: Delete App
   OperationID: DeleteApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteApp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteApp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ErpMetaFxSvc/DeleteApp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param layersToDelete
   */  
export interface BulkDeleteLayers_input{
      /**  Layers to publish  */  
   layersToDelete:Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerForApplication[],
}

export interface BulkDeleteLayers_output{
   returnObj:Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerForApplication[],
}

   /** Required : 
      @param layersToPublish
      @param validateBeforePublish
   */  
export interface BulkPublishLayers_input{
      /**  Layers to publish  */  
   layersToPublish:Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerForApplication[],
      /**  Validate each layer before publish (not implemented currently)  */  
   validateBeforePublish:boolean,
}

export interface BulkPublishLayers_output{
   returnObj:Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerForApplication[],
}

   /** Required : 
      @param viewId
   */  
export interface DeleteApp_input{
   viewId:string,
}

export interface DeleteApp_output{
}

   /** Required : 
      @param request
   */  
export interface DeleteLayer_input{
   request:Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerRequest[],
}

export interface DeleteLayer_output{
}

   /** Required : 
      @param request
   */  
export interface DownloadSchema_input{
   request:Epicor_MetaFX_Core_Models_DownloadSchemaRequest[],
}

export interface DownloadSchema_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param request
   */  
export interface DuplicateApp_input{
   request:Epicor_MetaFX_Core_Models_Configurator_DuplicateRequest[],
}

export interface DuplicateApp_output{
}

   /** Required : 
      @param CompanyId
      @param Files
      @param ViewId
   */  
export interface Epicor_MetaFX_Core_Models_AppContent{
   ViewId:string,
   CompanyId:string,
   Files:any,      //schema had no properties on an object.
}

   /** Required : 
      @param Id
      @param SubType
      @param Type
   */  
export interface Epicor_MetaFX_Core_Models_Applications_Application{
   Id:string,
   Type:string,
   SubType:string,
   LastUpdated:string,
   IsLayerDisabled:boolean,
   SystemFlag:boolean,
   HasDraftContent:boolean,
   PublishError:string,
   PublishStatus:number,
   Layers:Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerForApplication[],
   CreatedBy:string,
   CanAccessBase:boolean,
   SecurityCode:string,
}

export interface Epicor_MetaFX_Core_Models_Applications_ApplicationRequest{
   Type:string,
   SubType:string,
   SearchText:string,
   IsPublished:boolean,
   IncludeAllLayers:boolean,
}

export interface Epicor_MetaFX_Core_Models_Applications_ApplicationSubType{
   SubType:string,
   Prefix:string,
   IsLayerDisabled:boolean,
}

export interface Epicor_MetaFX_Core_Models_BAQReport_ReportResponse{
   Id:string,
   FileName:string,
}

export interface Epicor_MetaFX_Core_Models_Configurator_ConfiguratorInfo{
   ConfigId:string,
   Approved:boolean,
   AuditDesc:string,
   Description:string,
   AprvRev:boolean,
   IsValidPwd:boolean,
   DispConfSummary:boolean,
   StatusExpr:Epicor_MetaFX_Core_Models_Configurator_StatusExpr[],
   PcPageExpr:Epicor_MetaFX_Core_Models_Configurator_PcPageExpr[],
   DynamicAttributeClassId:string,
   ConfigUDFunc:Epicor_MetaFX_Core_Models_Configurator_ConfiguratorUDFunction[],
}

export interface Epicor_MetaFX_Core_Models_Configurator_ConfiguratorUDFunction{
   PcFunctionDef:Epicor_MetaFX_Core_Models_Configurator_PcFunctionDef[],
   PcFunctionDefAttch:Epicor_MetaFX_Core_Models_Configurator_PcFunctionDefAttch[],
   PcFunctionParam:Epicor_MetaFX_Core_Models_Configurator_PcFunctionParam[],
   ExtensionTables:object
}

   /** Required : 
      @param NewViewId
      @param ViewId
   */  
export interface Epicor_MetaFX_Core_Models_Configurator_DuplicateRequest{
   ViewId:string,
   NewViewId:string,
}

export interface Epicor_MetaFX_Core_Models_Configurator_PcFunctionDef{
   Company:string,
   FunctionName:string,
   Description:string,
   ConfigID:string,
   FunctionType:string,
   Expression:string,
   ReturnType:string,
   OldFunctionName:string,
   IsSync:boolean,
   GlobalFunc:boolean,
   SysRevID:string,
   SysRowID:string,
   BagID:string,
   NoInputs:boolean,
   ScriptExpression:string,
   DispFunctionName:string,
   DispFunctionType:string,
   DispReturnType:string,
   BtnEditScript:boolean,
   BitFlag:number,
   PcStatusConfigType:string,
   PcStatusApproved:boolean,
   RowMod:string,
}

export interface Epicor_MetaFX_Core_Models_Configurator_PcFunctionDefAttch{
   Company:string,
   ConfigID:string,
   FunctionName:string,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:string,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
   RowMod:string,
}

export interface Epicor_MetaFX_Core_Models_Configurator_PcFunctionParam{
   Company:string,
   FunctionName:string,
   ParameterName:string,
   DefaultValue:string,
   Modifier:string,
   ParamType:string,
   ConfigID:string,
   ParamSeq:number,
   SysRevID:string,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Epicor_MetaFX_Core_Models_Configurator_PcPageExpr{
   TypeCode:string,
   Expression:string,
   PageName:string,
}

export interface Epicor_MetaFX_Core_Models_Configurator_StatusExpr{
   TypeCode:string,
   Expression:string,
}

   /** Required : 
      @param CompanyID
      @param ConfigId
      @param ExtCompanyID
   */  
export interface Epicor_MetaFX_Core_Models_Configurator_SyncRequest{
   ConfigId:string,
   ExtCompanyID:string,
   CompanyID:string,
}

export interface Epicor_MetaFX_Core_Models_DownloadSchemaRequest{
   EventID:string,
}

export interface Epicor_MetaFX_Core_Models_EpMetaFxCacheInvalidateRequest{
   viewId:string,
   Type:string,
   Like:string,
   LanguageId:string,
}

export interface Epicor_MetaFX_Core_Models_EpMetaFxComboRequest{
   Folder:string,
   SubFolder:string,
}

export interface Epicor_MetaFX_Core_Models_EpMetaFxPeekRequest{
   like:string,
   properties:Epicor_MetaFX_Core_Models_EpMetaFxPeekRequestProperty[],
}

export interface Epicor_MetaFX_Core_Models_EpMetaFxPeekRequestProperty{
   peekForm:string,
   deviceType:string,
   mode:string,
}

export interface Epicor_MetaFX_Core_Models_EpMetaFxRequest{
   id:string,
   properties:Epicor_MetaFX_Core_Models_EpMetaFxRequestProperty[],
}

export interface Epicor_MetaFX_Core_Models_EpMetaFxRequestProperty{
   layers:string,
   layerType:string,
   deviceType:string,
   mode:string,
   userName:string,
   pageName:string,
   company:string,
   countryGroupCode:string,
   debug:boolean,
   countryCode:string,
   includeWasm:boolean,
   applicationType:string,
   additionalContext:any,      //schema had no properties on an object.
   checkDuplicateIds:boolean,
   layerVersion:number,
   baseAppVersion:number,
}

export interface Epicor_MetaFX_Core_Models_EpMetaFxResponse_Epicor_MetaFX_Core_Models_BAQReport_ReportResponse{
   Data:Epicor_MetaFX_Core_Models_BAQReport_ReportResponse[],
   IsSuccess:boolean,
   Message:string,
   Details:Epicor_MetaFX_Core_Models_MessageDetail[],
}

export interface Epicor_MetaFX_Core_Models_EpMetaFxSaveRequestEx{
   id:string,
   commentText:string,
   deviceType:string,
   userName:string,
   viewType:string,
   layout:any,      //schema had no properties on an object.
   classicLayout:any,      //schema had no properties on an object.
   pages:any,      //schema had no properties on an object.
   rules:any,      //schema had no properties on an object.
   events:any,      //schema had no properties on an object.
   tools:any,      //schema had no properties on an object.
   dataviews:any,      //schema had no properties on an object.
   layerInfo:Epicor_MetaFX_Core_Models_Layer[],
   countryGroupCode:string,
   countryCode:string,
   serializedEvents:any,      //schema had no properties on an object.
   applicationType:string,
   subApplicationType:string,
   properties:any,      //schema had no properties on an object.
   configuratorInfo:Epicor_MetaFX_Core_Models_Configurator_ConfiguratorInfo[],
   uxAppVersion:number,
}

export interface Epicor_MetaFX_Core_Models_EpMetaFxSearchRequest{
   like:string,
   properties:Epicor_MetaFX_Core_Models_EpMetaFxSearchRequestProperty[],
}

export interface Epicor_MetaFX_Core_Models_EpMetaFxSearchRequestProperty{
   SearchForm:string,
   layers:string,
   deviceType:string,
   mode:string,
   debug:boolean,
}

export interface Epicor_MetaFX_Core_Models_EpMetaFxTemplateRequest{
   TemplateType:string,
   ViewType:string,
}

export interface Epicor_MetaFX_Core_Models_EpMetaFxUpgradeSchemaRequest{
   content:string,
}

export interface Epicor_MetaFX_Core_Models_Events_EpMetaFxEventDesigner{
   ViewId:string,
   Company:string,
   LayerName:string,
   EventId:string,
   DeviceType:string,
   Content:any,      //schema had no properties on an object.
   CGCCode:string,
}

   /** Required : 
      @param DeviceType
      @param EventId
      @param ViewId
   */  
export interface Epicor_MetaFX_Core_Models_Events_EpMetaFxEventDesignerRequest{
   ViewId:string,
   Company:string,
   Layers:string,
   EventId:string,
   DeviceType:string,
}

export interface Epicor_MetaFX_Core_Models_Layer{
   company:string,
   typeCode:string,
   layerName:string,
   layerDescription:string,
   parentLayers:string,
   wip:boolean,
   IsNew:boolean,
   CGCCode:string,
   PublishParentLayers:boolean,
}

export interface Epicor_MetaFX_Core_Models_Layers_EpMetaFXAuditLog{
   Company:string,
   TypeCode:string,
   ViewId:string,
   Name:string,
   Description:string,
   ParentLayers:string,
   CommentText:string,
   DeviceType:string,
   LastUpdated:string,
   LastUpdatedBy:string,
   Published:string,
}

export interface Epicor_MetaFX_Core_Models_Layers_EpMetaFXAuditLogRequest{
   ViewId:string,
   LayerName:string,
   ApplicationType:string,
   ApplicationSubType:string,
   Company:string,
}

export interface Epicor_MetaFX_Core_Models_Layers_EpMetaFxGetLayersRequest{
   ViewId:string,
   ViewSearchText:string,
   TypeCode:string,
   DeviceType:string,
   UserName:string,
   IncludeUnpublishedLayers:boolean,
}

   /** Required : 
      @param DeviceType
      @param TypeCode
   */  
export interface Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerForApplication{
   Id:string,
   SubType:string,
   LastUpdated:string,
   IsPublished:boolean,
   TypeCode:string,
   Company:string,
   LayerName:string,
   DeviceType:string,
   CGCCode:string,
   UpgradeStatus:number,
   UpgradeError:string,
   DeleteError:string,
   SystemFlag:boolean,
   PublishError:string,
   PublishStatus:number,
   HasDraftContent:boolean,
   LastUpdatedBy:string,
}

   /** Required : 
      @param DeviceType
      @param TypeCode
      @param UserName
      @param ViewId
   */  
export interface Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerRequest{
   ViewId:string,
   Company:string,
   TypeCode:string,
   LayerName:string,
   DeviceType:string,
   ParentLayers:string,
   UserName:string,
   PageName:string,
   CGCCode:string,
   IncludeDraftContent:boolean,
   UxAppVersion:number,
}

export interface Epicor_MetaFX_Core_Models_MessageDetail{
   Message:string,
   Type:string,
}

export interface Epicor_MetaFX_Core_Models_MetaFxUpgradeLayerRequest{
   Id:string,
   UpgradeType:number,
}

export interface Epicor_MetaFX_Core_Models_MetaUI_Strings_ApplicationString{
   id:string,
   text:string,
   layer:boolean,
   missing:boolean,
}

export interface Epicor_MetaFX_Core_Models_ViewMetadataResponse{
   AllowVersions:boolean,
   Layout:any,      //schema had no properties on an object.
   Events:any,      //schema had no properties on an object.
   ToolBar:any,      //schema had no properties on an object.
   DataViews:any,      //schema had no properties on an object.
   Rules:any,      //schema had no properties on an object.
   References:any,      //schema had no properties on an object.
   Pages:any,      //schema had no properties on an object.
   Properties:any,      //schema had no properties on an object.
   Wasm:string,
   IsLayerDisabled:boolean,
   ConfiguratorInfo:Epicor_MetaFX_Core_Models_Configurator_ConfiguratorInfo[],
   ApplicationStrings:Epicor_MetaFX_Core_Models_MetaUI_Strings_ApplicationString[],
}

export interface Erp_Services_BO_EpMetaFxGenerateViewRequest{
   Type:string,
   Id:string,
   Company:string,
   ProductId:string,
   GlbCompany:string,
   CgCCode:string,
   LayoutType:string,
}

   /** Required : 
      @param viewId
   */  
export interface ExportApp_input{
   viewId:string,
}

export interface ExportApp_output{
   returnObj:Epicor_MetaFX_Core_Models_AppContent[],
}

   /** Required : 
      @param request
   */  
export interface GenerateView_input{
   request:Erp_Services_BO_EpMetaFxGenerateViewRequest[],
}

export interface GenerateView_output{
   returnObj:Epicor_MetaFX_Core_Models_EpMetaFxResponse_Epicor_MetaFX_Core_Models_BAQReport_ReportResponse[],
}

   /** Required : 
      @param request
   */  
export interface GetApp_input{
   request:Epicor_MetaFX_Core_Models_EpMetaFxRequest[],
}

export interface GetApp_output{
      /**  View's JSON Metadata  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param applicationType
   */  
export interface GetApplicationSubTypes_input{
      /**  applicationType  */  
   applicationType:string,
}

export interface GetApplicationSubTypes_output{
   returnObj:Epicor_MetaFX_Core_Models_Applications_ApplicationSubType[],
}

   /** Required : 
      @param request
   */  
export interface GetApplications_input{
   request:Epicor_MetaFX_Core_Models_Applications_ApplicationRequest[],
}

export interface GetApplications_output{
   returnObj:Epicor_MetaFX_Core_Models_Applications_Application[],
}

   /** Required : 
      @param request
   */  
export interface GetAuditLogs_input{
   request:Epicor_MetaFX_Core_Models_Layers_EpMetaFXAuditLogRequest[],
}

export interface GetAuditLogs_output{
   returnObj:Epicor_MetaFX_Core_Models_Layers_EpMetaFXAuditLog[],
}

   /** Required : 
      @param request
   */  
export interface GetCombosData_input{
   request:Epicor_MetaFX_Core_Models_EpMetaFxComboRequest[],
}

export interface GetCombosData_output{
   returnObj:any,      //schema had no properties on an object.
}

export interface GetCombos_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param request
   */  
export interface GetEventDesigner_input{
   request:Epicor_MetaFX_Core_Models_Events_EpMetaFxEventDesignerRequest[],
}

export interface GetEventDesigner_output{
   returnObj:Epicor_MetaFX_Core_Models_Events_EpMetaFxEventDesigner[],
}

   /** Required : 
      @param request
   */  
export interface GetLayer_input{
   request:Epicor_MetaFX_Core_Models_Layers_EpMetaFxLayerRequest[],
}

export interface GetLayer_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param request
   */  
export interface GetLayers_input{
   request:Epicor_MetaFX_Core_Models_Layers_EpMetaFxGetLayersRequest[],
}

export interface GetLayers_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param request
   */  
export interface GetNewApplication_input{
   request:Epicor_MetaFX_Core_Models_Applications_Application[],
}

export interface GetNewApplication_output{
   returnObj:Epicor_MetaFX_Core_Models_ViewMetadataResponse[],
}

   /** Required : 
      @param request
   */  
export interface GetPage_input{
   request:Epicor_MetaFX_Core_Models_EpMetaFxRequest[],
}

export interface GetPage_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param request
   */  
export interface GetPeek_input{
   request:Epicor_MetaFX_Core_Models_EpMetaFxPeekRequest[],
}

export interface GetPeek_output{
   returnObj:any,      //schema had no properties on an object.
}

export interface GetPeeks_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param request
   */  
export interface GetSearchForm_input{
   request:Epicor_MetaFX_Core_Models_EpMetaFxSearchRequest[],
}

export interface GetSearchForm_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param request
   */  
export interface GetSearch_input{
   request:Epicor_MetaFX_Core_Models_EpMetaFxSearchRequest[],
}

export interface GetSearch_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param templateType
   */  
export interface GetTemplateView_input{
   templateType:Epicor_MetaFX_Core_Models_EpMetaFxTemplateRequest[],
}

export interface GetTemplateView_output{
   returnObj:any,      //schema had no properties on an object.
}

export interface GetViewTypes_output{
   returnObj:string,
}

export interface GetViews_output{
      /**  All views  */  
   returnObj:string,
}

   /** Required : 
      @param request
   */  
export interface ImportApp_input{
   request:Epicor_MetaFX_Core_Models_AppContent[],
}

export interface ImportApp_output{
}

   /** Required : 
      @param request
   */  
export interface InvalidateCache_input{
   request:Epicor_MetaFX_Core_Models_EpMetaFxCacheInvalidateRequest[],
}

export interface InvalidateCache_output{
}

   /** Required : 
      @param request
   */  
export interface PublishApp_input{
   request:Epicor_MetaFX_Core_Models_EpMetaFxSaveRequestEx[],
}

export interface PublishApp_output{
}

   /** Required : 
      @param request
   */  
export interface SaveApp_input{
   request:Epicor_MetaFX_Core_Models_EpMetaFxSaveRequestEx[],
}

export interface SaveApp_output{
}

   /** Required : 
      @param request
   */  
export interface Sync_input{
   request:Epicor_MetaFX_Core_Models_Configurator_SyncRequest[],
}

export interface Sync_output{
}

   /** Required : 
      @param request
   */  
export interface UpgradeLayer_input{
   request:Epicor_MetaFX_Core_Models_MetaFxUpgradeLayerRequest[],
}

export interface UpgradeLayer_output{
      /**  TRUE if upgrade is successful  */  
   returnObj:boolean,
}

   /** Required : 
      @param request
   */  
export interface Upgrade_input{
   request:Epicor_MetaFX_Core_Models_EpMetaFxUpgradeSchemaRequest[],
}

export interface Upgrade_output{
   returnObj:any,      //schema had no properties on an object.
}

