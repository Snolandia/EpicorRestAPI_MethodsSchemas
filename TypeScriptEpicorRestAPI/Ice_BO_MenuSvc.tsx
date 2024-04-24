import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.MenuSvc
// Description: Identifies the menu items that are displayed on the main menu.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/$metadata", {
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
   Summary: Calls GetRows for the service
   Description: Get Menus items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Menus
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MenuRow
   */  
export function get_Menus(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MenuRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/Menus", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MenuRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Menus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.MenuRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.MenuRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Menus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/Menus", {
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
   Summary: Calls GetByID to retrieve the Menu item
   Description: Calls GetByID to retrieve the Menu item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Menu
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MenuID Desc: MenuID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.MenuRow
   */  
export function get_Menus_Company_MenuID(Company:string, MenuID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_MenuRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/Menus(" + Company + "," + MenuID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_MenuRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Menu for the service
   Description: Calls UpdateExt to update Menu. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Menu
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MenuID Desc: MenuID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.MenuRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Menus_Company_MenuID(Company:string, MenuID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/Menus(" + Company + "," + MenuID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete Menu item
   Description: Call UpdateExt to delete Menu item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Menu
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MenuID Desc: MenuID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Menus_Company_MenuID(Company:string, MenuID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/Menus(" + Company + "," + MenuID + ")", {
          method: 'delete',
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
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MenuListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MenuListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MenuListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseMenu:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseMenu!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMenu=" + whereClauseMenu
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetRows" + params, {
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
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(company:string, menuID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof company!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "company=" + company
   }
   if(typeof menuID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "menuID=" + menuID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetByID" + params, {
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
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetList" + params, {
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
   Summary: Invoke method GetRowsTranslated
   Description: Gets translation for each existing Row
   OperationID: GetRowsTranslated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsTranslated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsTranslated_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsTranslated(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetRowsTranslated", {
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
   Summary: Invoke method GetRowsWebAccess
   Description: Gets Rows that that are accessible from the WEB
   OperationID: GetRowsWebAccess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWebAccess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWebAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsWebAccess(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetRowsWebAccess", {
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
   Summary: Invoke method GetMenuID
   Description: Returns a DataSet given the primary key.
   OperationID: GetMenuID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMenuID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMenuID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMenuID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetMenuID", {
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
   Summary: Invoke method GetRowsWebAccessTranslated
   Description: Gets Rows that that are accessible from the WEB
   OperationID: GetRowsWebAccessTranslated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWebAccessTranslated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWebAccessTranslated_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsWebAccessTranslated(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetRowsWebAccessTranslated", {
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
   Summary: Invoke method GetRowsCRM
   Description: Gets Rows that that are accessible from the WEB
   OperationID: GetRowsCRM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCRM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCRM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCRM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetRowsCRM", {
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
   Summary: Invoke method GetRowsCRMTranslated
   Description: Gets Rows that that are accessible from the WEB
   OperationID: GetRowsCRMTranslated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCRMTranslated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCRMTranslated_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCRMTranslated(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetRowsCRMTranslated", {
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
   Summary: Invoke method CopyBeforeMenuItem
   Description: Move or Copy one menu item (source) before another (Target)
   OperationID: CopyBeforeMenuItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyBeforeMenuItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyBeforeMenuItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyBeforeMenuItem(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/CopyBeforeMenuItem", {
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
   Summary: Invoke method CopyMenuRow
   Description: Copy an existing Menu to a new menu row
   OperationID: CopyMenuRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyMenuRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyMenuRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyMenuRow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/CopyMenuRow", {
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
   Summary: Invoke method CopyToParentMenu
   Description: Move or Copy one menu item to the last menu item of the parent
   OperationID: CopyToParentMenu
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyToParentMenu_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyToParentMenu_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyToParentMenu(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/CopyToParentMenu", {
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
   Summary: Invoke method GetMenuForLicenseType
   Description: Gets the type of the menu for the license type that the client is running under.
   OperationID: GetMenuForLicenseType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMenuForLicenseType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMenuForLicenseType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMenuForLicenseType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetMenuForLicenseType", {
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
   Summary: Invoke method ValidateMenuBeforeLaunch
   Description: Validates if the UI represented by the Url can be launched by calling an ERP menu extension.
   OperationID: ValidateMenuBeforeLaunch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMenuBeforeLaunch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMenuBeforeLaunch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateMenuBeforeLaunch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/ValidateMenuBeforeLaunch", {
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
   Summary: Invoke method GetMenuAllowedForUserByView
   Description: Determines whether the user has access to a Menu based on the ViewID.
   OperationID: GetMenuAllowedForUserByView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMenuAllowedForUserByView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMenuAllowedForUserByView_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMenuAllowedForUserByView(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetMenuAllowedForUserByView", {
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
   Summary: Invoke method CheckMenuSecurityForUser
   Description: Determines if the user has access to the given MenuID or ViewID
   OperationID: CheckMenuSecurityForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckMenuSecurityForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckMenuSecurityForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckMenuSecurityForUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/CheckMenuSecurityForUser", {
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
   Summary: Invoke method GlobalRecordFound
   OperationID: GlobalRecordFound
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GlobalRecordFound_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GlobalRecordFound_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlobalRecordFound(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GlobalRecordFound", {
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
   Summary: Invoke method ProgamFoundInMenu
   OperationID: ProgamFoundInMenu
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProgamFoundInMenu_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProgamFoundInMenu_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProgamFoundInMenu(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/ProgamFoundInMenu", {
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
   Summary: Invoke method GetKineticCustomizations
   Description: Gets the kinetic customizations allowed for provided view.
   OperationID: GetKineticCustomizations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetKineticCustomizations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKineticCustomizations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetKineticCustomizations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetKineticCustomizations", {
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
   Summary: Invoke method GetKineticViews
   Description: Gets the kinetic views.
   OperationID: GetKineticViews
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKineticViews_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetKineticViews(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetKineticViews", {
          method: 'post',
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
   Summary: Invoke method GetCompaniesKineticStatus
   Description: Lists all companies that the user has access to and whether Kinetic UI is enabled
   OperationID: GetCompaniesKineticStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompaniesKineticStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCompaniesKineticStatus(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetCompaniesKineticStatus", {
          method: 'post',
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
   Summary: Invoke method GetBannerSnoozeDays
   Description: Gets the number of days the Kinetic alert to use new UI is not shown after the user "snoozes" it.
This setting is per company.
   OperationID: GetBannerSnoozeDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBannerSnoozeDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBannerSnoozeDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBannerSnoozeDays(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetBannerSnoozeDays", {
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
   Summary: Invoke method UpdateDefaultFormType
   Description: Update a menu default form type to the target type
   OperationID: UpdateDefaultFormType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDefaultFormType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDefaultFormType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateDefaultFormType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/UpdateDefaultFormType", {
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
   Summary: Invoke method EnableKineticUIOnRelatedMenus
   Description: Enable Kinetic UI on related menus
   OperationID: EnableKineticUIOnRelatedMenus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnableKineticUIOnRelatedMenus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableKineticUIOnRelatedMenus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EnableKineticUIOnRelatedMenus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/EnableKineticUIOnRelatedMenus", {
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
   Summary: Invoke method UpdateKineticBannerSnooze
   Description: Update the Kinetic Banner snooze duration
   OperationID: UpdateKineticBannerSnooze
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateKineticBannerSnooze_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateKineticBannerSnooze_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateKineticBannerSnooze(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/UpdateKineticBannerSnooze", {
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
   Summary: Invoke method EnableKineticUIForDynamicReport
   Description: Enables the Kinetic UI for a dynamic report menu item
   OperationID: EnableKineticUIForDynamicReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnableKineticUIForDynamicReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableKineticUIForDynamicReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EnableKineticUIForDynamicReport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/EnableKineticUIForDynamicReport", {
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
   Summary: Invoke method GetNewMenu
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMenu
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMenu_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMenu_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMenu(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetNewMenu", {
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
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/DeleteByID", {
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
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetBySysRowID" + params, {
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
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetBySysRowIDs" + params, {
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
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/Update", {
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
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/UpdateExt", {
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
   Summary: Invoke method GetModuleList
   Description: Create list of modules
   OperationID: GetModuleList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetModuleList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetModuleList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetModuleList", {
          method: 'post',
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
   Summary: Invoke method CGCCodeList
   Description: Build cgccode list.
   OperationID: CGCCodeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CGCCodeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CGCCodeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/CGCCodeList", {
          method: 'post',
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
   Summary: Invoke method GetRowsMenuMaint
   Description: Prepare menu row for editing
   OperationID: GetRowsMenuMaint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsMenuMaint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsMenuMaint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsMenuMaint(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetRowsMenuMaint", {
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
   Summary: Invoke method GetRowsMenuMaintCustom
   Description: Support for searching menu.
   OperationID: GetRowsMenuMaintCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsMenuMaintCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsMenuMaintCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsMenuMaintCustom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetRowsMenuMaintCustom", {
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
   Summary: Invoke method CreateNewMenu
   Description: Add a new menu with defaults
   OperationID: CreateNewMenu
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewMenu_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewMenu_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateNewMenu(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/CreateNewMenu", {
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
   Summary: Invoke method GetTopLevelMenus
   Description: Return top level menus only if a security manager
   OperationID: GetTopLevelMenus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTopLevelMenus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTopLevelMenus(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/GetTopLevelMenus", {
          method: 'post',
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
   Summary: Invoke method KineticPreviewEnabled
   Description: Return true if Kinetic preview is enabled
   OperationID: KineticPreviewEnabled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/KineticPreviewEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KineticPreviewEnabled(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/KineticPreviewEnabled", {
          method: 'post',
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
   Summary: Invoke method PreUpdate
   Description: verify/Update menu fields before calling standard update event.  In place to handle code that was in the classic UI.
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/PreUpdate", {
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
   Summary: Invoke method KineticChanged
   Description: Update fields if Kinetic flag changes.
   OperationID: KineticChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KineticChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KineticChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KineticChanged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/KineticChanged", {
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
   Summary: Invoke method KineticProgamChanged
   Description: Update fields if Kinetic flag changes.
   OperationID: KineticProgamChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KineticProgamChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KineticProgamChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KineticProgamChanged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/KineticProgamChanged", {
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
   Summary: Invoke method OptioTypeChanged
   Description: Update menu fields when field optionType is changed.
   OperationID: OptioTypeChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OptioTypeChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OptioTypeChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OptioTypeChanged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/OptioTypeChanged", {
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
   Summary: Invoke method BAQReportChanging
   Description: Validate Dynamic Report
   OperationID: BAQReportChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BAQReportChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BAQReportChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQReportChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/BAQReportChanging", {
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
   Summary: Invoke method DyanmicReportChanging
   Description: Validate Dynamic Report
   OperationID: DyanmicReportChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DyanmicReportChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DyanmicReportChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DyanmicReportChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/DyanmicReportChanging", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MenuListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_MenuListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MenuRow{
   "odatametadata":string,
   "value":Ice_Tablesets_MenuRow[],
}

export interface Ice_Tablesets_MenuListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  */  
   "MenuID":string,
      /**  Menu Description  */  
   "MenuDesc":string,
      /**  Needs manual validation because you cannot do can-find validation on the same file in the database validation.  */  
   "ParentMenuID":string,
      /**  Menu Sequence Number  */  
   "Sequence":number,
      /**   S = Sub Menu,
I = Menu Item (Program),
B = Report Builder Report Link  */  
   "OptionType":string,
      /**   F = Form
T = Tracker
M = Maintenance
P = Process
R = Report
E = Entry  */  
   "OptionSubType":string,
      /**  Either the path/program or the ID of the Custom Report Link to run.  */  
   "Program":string,
      /**  Enabled flag  */  
   "Enabled":boolean,
      /**  Security ID for the Program/SubMenu.  */  
   "SecCode":string,
      /**  If this field is YES, this menu item should not display in the Main Menu.  */  
   "DoNotDisplayInMenu":boolean,
      /**  Arguments to be passed to the program that this menu item refers to (see field "Program").  */  
   "Arguments":string,
      /**  Contains the licensing module that this menu item belongs to.  */  
   "Module":string,
      /**  Indicates a menu group that menu item belongs to  */  
   "MenuType":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  The Dashboard ID  */  
   "DashboardID":string,
      /**  Whether this menu item is available under the Express edition.  */  
   "ExpressAvailable":boolean,
      /**  CRMMenu  */  
   "CRMMenu":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  WebResourceURL  */  
   "WebResourceURL":string,
      /**  DefaultFormType  */  
   "DefaultFormType":string,
      /**  Customization  */  
   "Customization":string,
   "Extension":string,
   "ReadOnly":boolean,
   "Options":string,
   "DeveloperMode":boolean,
   "Dashboard":string,
   "AllCompanies":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_MenuRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  */  
   "MenuID":string,
      /**  Menu Description  */  
   "MenuDesc":string,
      /**  Needs manual validation because you cannot do can-find validation on the same file in the database validation.  */  
   "ParentMenuID":string,
      /**  Menu Sequence Number  */  
   "Sequence":number,
      /**   S = Sub Menu,
I = Menu Item (Program),
B = Report Builder Report Link  */  
   "OptionType":string,
      /**   F = Form
T = Tracker
M = Maintenance
P = Process
R = Report
E = Entry  */  
   "OptionSubType":string,
      /**  Either the path/program or the ID of the Custom Report Link to run.  */  
   "Program":string,
      /**  Enabled flag  */  
   "Enabled":boolean,
      /**  Security ID for the Program/SubMenu.  */  
   "SecCode":string,
      /**  If this field is YES, this menu item should not display in the Main Menu.  */  
   "DoNotDisplayInMenu":boolean,
      /**  Arguments to be passed to the program that this menu item refers to (see field "Program").  */  
   "Arguments":string,
      /**  Contains the licensing module that this menu item belongs to.  */  
   "Module":string,
      /**  Indicates a menu group that menu item belongs to  */  
   "MenuType":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  The Dashboard ID  */  
   "DashboardID":string,
      /**  Whether this menu item is available under the Express edition.  */  
   "ExpressAvailable":boolean,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  OldProgram  */  
   "OldProgram":string,
      /**  Comment  */  
   "Comment":string,
      /**  Status  */  
   "Status":string,
      /**  CRMMenu  */  
   "CRMMenu":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SaaSParam  */  
   "SaaSParam":string,
      /**  WebResourceURL  */  
   "WebResourceURL":string,
      /**  DefaultFormType  */  
   "DefaultFormType":string,
      /**  Alias  */  
   "Alias":string,
      /**  RunOnClassic  */  
   "RunOnClassic":boolean,
   "Dashboard":string,
   "DeveloperMode":boolean,
   "Extension":string,
   "Options":string,
   "ReadOnly":boolean,
      /**  Customization  */  
   "Customization":string,
   "AllCompanies":boolean,
      /**  Indicates if the navigation bar (forward/back/refresh) should be shown on the form if the Program Type is URL Form.  */  
   "ShowWebNavBar":boolean,
      /**  Description: Indicates if menu will be validated additionally by business logic before being launched. Used by Kinetic menus.  */  
   "ValidateBeforeLaunch":boolean,
   "CustomizationKinetic":string,
   "CanModify":boolean,
   "FormName":string,
   "Kinetic":boolean,
      /**  Kinetic program  */  
   "ProgramKinetic":string,
      /**  Customization Type  */  
   "CustomizationType":string,
   "Select":boolean,
   "IsDuplicate":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param reportID
   */  
export interface BAQReportChanging_input{
   reportID:string,
}

export interface BAQReportChanging_output{
}

export interface CGCCodeList_output{
   returnObj:string,
}

   /** Required : 
      @param viewId
      @param menuId
   */  
export interface CheckMenuSecurityForUser_input{
      /**  View ID to check for.  */  
   viewId:string,
      /**  Menu ID to check for.  */  
   menuId:string,
}

export interface CheckMenuSecurityForUser_output{
}

   /** Required : 
      @param sourceMenuID
      @param targetMenuID
   */  
export interface CopyBeforeMenuItem_input{
      /**  Menu ID of the source  */  
   sourceMenuID:string,
      /**  Menu ID of the target  */  
   targetMenuID:string,
}

export interface CopyBeforeMenuItem_output{
parameters : {
      /**  output parameters  */  
   newMenuID:string,
   bSuccess:boolean,
}
}

   /** Required : 
      @param ds
      @param sourceCompany
      @param sourceMenuID
      @param targetCompany
      @param targetMenuID
   */  
export interface CopyMenuRow_input{
   ds:Ice_Tablesets_MenuTableset[],
      /**  Existing Menu Company  */  
   sourceCompany:string,
      /**  Existing Menu ID of the source  */  
   sourceMenuID:string,
      /**  new menu company  */  
   targetCompany:string,
      /**  new menu ID  */  
   targetMenuID:string,
}

export interface CopyMenuRow_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_MenuTableset[],
}
}

   /** Required : 
      @param sourceMenuID
      @param parentMenuID
   */  
export interface CopyToParentMenu_input{
      /**  Menu ID of the source  */  
   sourceMenuID:string,
      /**  Menu ID of the parent  */  
   parentMenuID:string,
}

export interface CopyToParentMenu_output{
parameters : {
      /**  output parameters  */  
   newMenuID:string,
   bSuccess:boolean,
}
}

   /** Required : 
      @param ds
      @param parentCompany
      @param parrentMenuId
   */  
export interface CreateNewMenu_input{
   ds:Ice_Tablesets_MenuTableset[],
   parentCompany:string,
   parrentMenuId:string,
}

export interface CreateNewMenu_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_MenuTableset[],
}
}

   /** Required : 
      @param company
      @param menuID
   */  
export interface DeleteByID_input{
   company:string,
   menuID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param reportID
   */  
export interface DyanmicReportChanging_input{
   reportID:string,
}

export interface DyanmicReportChanging_output{
}

   /** Required : 
      @param reportId
   */  
export interface EnableKineticUIForDynamicReport_input{
      /**  The report id  */  
   reportId:string,
}

export interface EnableKineticUIForDynamicReport_output{
}

   /** Required : 
      @param company
      @param menuIDs
   */  
export interface EnableKineticUIOnRelatedMenus_input{
   company:string,
      /**  Menu IDs to search with  */  
   menuIDs:string,
}

export interface EnableKineticUIOnRelatedMenus_output{
}

   /** Required : 
      @param company
   */  
export interface GetBannerSnoozeDays_input{
      /**  the company  */  
   company:string,
}

export interface GetBannerSnoozeDays_output{
      /**  the number of days to snooze the alert.  */  
   returnObj:number,
}

   /** Required : 
      @param company
      @param menuID
   */  
export interface GetByID_input{
   company:string,
   menuID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_MenuTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_MenuTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_MenuTableset[],
}

export interface GetCompaniesKineticStatus_output{
      /**  List of company, name and Kinetic feature flag enabled  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param viewId
   */  
export interface GetKineticCustomizations_input{
      /**  The view identifier.  */  
   viewId:string,
}

export interface GetKineticCustomizations_output{
      /**  List of customizations delimited. Example: LayerName`Layer Description~LayerName2`Layer Description 2  */  
   returnObj:string,
}

export interface GetKineticViews_output{
      /**  The kinetic views available.  */  
   returnObj:string,
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Ice_Tablesets_MenuListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param viewId
   */  
export interface GetMenuAllowedForUserByView_input{
      /**  View ID to check for.  */  
   viewId:string,
}

export interface GetMenuAllowedForUserByView_output{
   returnObj:Ice_Tablesets_MenuTableset[],
}

   /** Required : 
      @param licenseType
      @param filterForWebAccess
      @param filterKineticOnly
   */  
export interface GetMenuForLicenseType_input{
      /**  Type of the license. Values: 'Default','CRM','TimeExpense'  */  
   licenseType:string,
      /**  if set to `true` filters the menu items not available in Web Access.  */  
   filterForWebAccess:boolean,
      /**  if set to `true` filters the menu items which are not Kinetic (called when in browser with no EWA)  */  
   filterKineticOnly:boolean,
}

export interface GetMenuForLicenseType_output{
   returnObj:Ice_Tablesets_MenuTableset[],
}

   /** Required : 
      @param menuID
   */  
export interface GetMenuID_input{
   menuID:string,
}

export interface GetMenuID_output{
   returnObj:Ice_Tablesets_MenuTableset[],
}

export interface GetModuleList_output{
   returnObj:string,
}

   /** Required : 
      @param ds
      @param company
   */  
export interface GetNewMenu_input{
   ds:Ice_Tablesets_MenuTableset[],
   company:string,
}

export interface GetNewMenu_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_MenuTableset[],
}
}

   /** Required : 
      @param whereClauseMenu
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCRMTranslated_input{
      /**  whereClauseSetupGrp">Where condition without the where word  */  
   whereClauseMenu:string,
      /**  # of records returned. 0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsCRMTranslated_output{
   returnObj:Ice_Tablesets_MenuTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseMenu
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCRM_input{
      /**  whereClauseSetupGrp">Where condition without the where word  */  
   whereClauseMenu:string,
      /**  # of records returned. 0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsCRM_output{
   returnObj:Ice_Tablesets_MenuTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseMenu
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsMenuMaintCustom_input{
   whereClauseMenu:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsMenuMaintCustom_output{
   returnObj:Ice_Tablesets_MenuTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseMenu
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsMenuMaint_input{
   whereClauseMenu:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsMenuMaint_output{
   returnObj:Ice_Tablesets_MenuTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseMenu
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsTranslated_input{
      /**  whereClauseSetupGrp">Where condition without the where word  */  
   whereClauseMenu:string,
      /**  # of records returned. 0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsTranslated_output{
   returnObj:Ice_Tablesets_MenuTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseMenu
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsWebAccessTranslated_input{
      /**  whereClauseSetupGrp">Where condition without the where word  */  
   whereClauseMenu:string,
      /**  # of records returned. 0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsWebAccessTranslated_output{
   returnObj:Ice_Tablesets_MenuTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseMenu
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsWebAccess_input{
      /**  whereClauseSetupGrp">Where condition without the where word  */  
   whereClauseMenu:string,
      /**  # of records returned. 0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsWebAccess_output{
   returnObj:Ice_Tablesets_MenuTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseMenu
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseMenu:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_MenuTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetTopLevelMenus_output{
   returnObj:Ice_Tablesets_MenuListTableset[],
}

   /** Required : 
      @param MenuID
   */  
export interface GlobalRecordFound_input{
   MenuID:string,
}

export interface GlobalRecordFound_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   Company:string,
   CompanyVisibility:number,
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

export interface Ice_Tablesets_MenuListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  */  
   MenuID:string,
      /**  Menu Description  */  
   MenuDesc:string,
      /**  Needs manual validation because you cannot do can-find validation on the same file in the database validation.  */  
   ParentMenuID:string,
      /**  Menu Sequence Number  */  
   Sequence:number,
      /**   S = Sub Menu,
I = Menu Item (Program),
B = Report Builder Report Link  */  
   OptionType:string,
      /**   F = Form
T = Tracker
M = Maintenance
P = Process
R = Report
E = Entry  */  
   OptionSubType:string,
      /**  Either the path/program or the ID of the Custom Report Link to run.  */  
   Program:string,
      /**  Enabled flag  */  
   Enabled:boolean,
      /**  Security ID for the Program/SubMenu.  */  
   SecCode:string,
      /**  If this field is YES, this menu item should not display in the Main Menu.  */  
   DoNotDisplayInMenu:boolean,
      /**  Arguments to be passed to the program that this menu item refers to (see field "Program").  */  
   Arguments:string,
      /**  Contains the licensing module that this menu item belongs to.  */  
   Module:string,
      /**  Indicates a menu group that menu item belongs to  */  
   MenuType:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  The Dashboard ID  */  
   DashboardID:string,
      /**  Whether this menu item is available under the Express edition.  */  
   ExpressAvailable:boolean,
      /**  CRMMenu  */  
   CRMMenu:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  WebResourceURL  */  
   WebResourceURL:string,
      /**  DefaultFormType  */  
   DefaultFormType:string,
      /**  Customization  */  
   Customization:string,
   Extension:string,
   ReadOnly:boolean,
   Options:string,
   DeveloperMode:boolean,
   Dashboard:string,
   AllCompanies:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_MenuListTableset{
   MenuList:Ice_Tablesets_MenuListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_MenuRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  */  
   MenuID:string,
      /**  Menu Description  */  
   MenuDesc:string,
      /**  Needs manual validation because you cannot do can-find validation on the same file in the database validation.  */  
   ParentMenuID:string,
      /**  Menu Sequence Number  */  
   Sequence:number,
      /**   S = Sub Menu,
I = Menu Item (Program),
B = Report Builder Report Link  */  
   OptionType:string,
      /**   F = Form
T = Tracker
M = Maintenance
P = Process
R = Report
E = Entry  */  
   OptionSubType:string,
      /**  Either the path/program or the ID of the Custom Report Link to run.  */  
   Program:string,
      /**  Enabled flag  */  
   Enabled:boolean,
      /**  Security ID for the Program/SubMenu.  */  
   SecCode:string,
      /**  If this field is YES, this menu item should not display in the Main Menu.  */  
   DoNotDisplayInMenu:boolean,
      /**  Arguments to be passed to the program that this menu item refers to (see field "Program").  */  
   Arguments:string,
      /**  Contains the licensing module that this menu item belongs to.  */  
   Module:string,
      /**  Indicates a menu group that menu item belongs to  */  
   MenuType:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  The Dashboard ID  */  
   DashboardID:string,
      /**  Whether this menu item is available under the Express edition.  */  
   ExpressAvailable:boolean,
      /**  SystemCode  */  
   SystemCode:string,
      /**  OldProgram  */  
   OldProgram:string,
      /**  Comment  */  
   Comment:string,
      /**  Status  */  
   Status:string,
      /**  CRMMenu  */  
   CRMMenu:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SaaSParam  */  
   SaaSParam:string,
      /**  WebResourceURL  */  
   WebResourceURL:string,
      /**  DefaultFormType  */  
   DefaultFormType:string,
      /**  Alias  */  
   Alias:string,
      /**  RunOnClassic  */  
   RunOnClassic:boolean,
   Dashboard:string,
   DeveloperMode:boolean,
   Extension:string,
   Options:string,
   ReadOnly:boolean,
      /**  Customization  */  
   Customization:string,
   AllCompanies:boolean,
      /**  Indicates if the navigation bar (forward/back/refresh) should be shown on the form if the Program Type is URL Form.  */  
   ShowWebNavBar:boolean,
      /**  Description: Indicates if menu will be validated additionally by business logic before being launched. Used by Kinetic menus.  */  
   ValidateBeforeLaunch:boolean,
   CustomizationKinetic:string,
   CanModify:boolean,
   FormName:string,
   Kinetic:boolean,
      /**  Kinetic program  */  
   ProgramKinetic:string,
      /**  Customization Type  */  
   CustomizationType:string,
   Select:boolean,
   IsDuplicate:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_MenuTableset{
   Menu:Ice_Tablesets_MenuRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtMenuTableset{
   Menu:Ice_Tablesets_MenuRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface KineticChanged_input{
   ds:Ice_Tablesets_MenuTableset[],
}

export interface KineticChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_MenuTableset[],
}
}

export interface KineticPreviewEnabled_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
   */  
export interface KineticProgamChanged_input{
   ds:Ice_Tablesets_MenuTableset[],
}

export interface KineticProgamChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_MenuTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OptioTypeChanged_input{
   ds:Ice_Tablesets_MenuTableset[],
}

export interface OptioTypeChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_MenuTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Ice_Tablesets_MenuTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_MenuTableset[],
}
}

   /** Required : 
      @param program
   */  
export interface ProgamFoundInMenu_input{
      /**  program to look for  */  
   program:string,
}

export interface ProgamFoundInMenu_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   menuID:string,
   menuAdded:boolean,
}
}

   /** Required : 
      @param company
      @param menuID
      @param recursive
      @param defaultFormType
   */  
export interface UpdateDefaultFormType_input{
      /**  Company to target  */  
   company:string,
      /**  Menu ID to start at  */  
   menuID:string,
      /**  Whether to recursively update child menu items  */  
   recursive:boolean,
      /**  Default form type to assign  */  
   defaultFormType:string,
}

export interface UpdateDefaultFormType_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtMenuTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtMenuTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param company
      @param days
   */  
export interface UpdateKineticBannerSnooze_input{
      /**  Company to target  */  
   company:string,
      /**  Number of days to snooze  */  
   days:number,
}

export interface UpdateKineticBannerSnooze_output{
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_MenuTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_MenuTableset[],
}
}

   /** Required : 
      @param viewId
      @param menuId
   */  
export interface ValidateMenuBeforeLaunch_input{
      /**  View identifier for the UI form  */  
   viewId:string,
      /**  Menu identifier for the UI form  */  
   menuId:string,
}

export interface ValidateMenuBeforeLaunch_output{
      /**  False if UI should not be launched.  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   errorMessage:string,
}
}

