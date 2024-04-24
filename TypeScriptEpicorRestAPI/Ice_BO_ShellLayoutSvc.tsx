import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.ShellLayoutSvc
// Description: Service for managing IceShell layouts
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/$metadata", {
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
   Description: Get ShellLayouts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShellLayouts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ShellLayoutRow
   */  
export function get_ShellLayouts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ShellLayoutRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/ShellLayouts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ShellLayoutRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShellLayouts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ShellLayoutRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ShellLayoutRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShellLayouts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/ShellLayouts", {
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
   Summary: Calls GetByID to retrieve the ShellLayout item
   Description: Calls GetByID to retrieve the ShellLayout item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShellLayout
      @param TenantID Desc: TenantID   Required: True   Allow empty value : True
      @param HomePageType Desc: HomePageType   Required: True   Allow empty value : True
      @param SubType Desc: SubType   Required: True   Allow empty value : True
      @param LayoutID Desc: LayoutID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ShellLayoutRow
   */  
export function get_ShellLayouts_TenantID_HomePageType_SubType_LayoutID(TenantID:string, HomePageType:string, SubType:string, LayoutID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ShellLayoutRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/ShellLayouts(" + TenantID + "," + HomePageType + "," + SubType + "," + LayoutID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ShellLayoutRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShellLayout for the service
   Description: Calls UpdateExt to update ShellLayout. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShellLayout
      @param TenantID Desc: TenantID   Required: True   Allow empty value : True
      @param HomePageType Desc: HomePageType   Required: True   Allow empty value : True
      @param SubType Desc: SubType   Required: True   Allow empty value : True
      @param LayoutID Desc: LayoutID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ShellLayoutRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShellLayouts_TenantID_HomePageType_SubType_LayoutID(TenantID:string, HomePageType:string, SubType:string, LayoutID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/ShellLayouts(" + TenantID + "," + HomePageType + "," + SubType + "," + LayoutID + ")", {
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
   Summary: Call UpdateExt to delete ShellLayout item
   Description: Call UpdateExt to delete ShellLayout item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShellLayout
      @param TenantID Desc: TenantID   Required: True   Allow empty value : True
      @param HomePageType Desc: HomePageType   Required: True   Allow empty value : True
      @param SubType Desc: SubType   Required: True   Allow empty value : True
      @param LayoutID Desc: LayoutID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShellLayouts_TenantID_HomePageType_SubType_LayoutID(TenantID:string, HomePageType:string, SubType:string, LayoutID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/ShellLayouts(" + TenantID + "," + HomePageType + "," + SubType + "," + LayoutID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ShellLayoutListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ShellLayoutListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ShellLayoutListRow)
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
export function get_GetRows(whereClauseShellLayout:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseShellLayout!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShellLayout=" + whereClauseShellLayout
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(tenantID:string, homePageType:string, subType:string, layoutID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof tenantID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tenantID=" + tenantID
   }
   if(typeof homePageType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "homePageType=" + homePageType
   }
   if(typeof subType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "subType=" + subType
   }
   if(typeof layoutID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "layoutID=" + layoutID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetList" + params, {
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
   Summary: Invoke method GetDefaultLayout
   Description: Get Layout for user
   OperationID: GetDefaultLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultLayout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetDefaultLayout", {
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
   Summary: Invoke method ResetToDefaultLayout
   Description: Resets to default layout.
   OperationID: ResetToDefaultLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetToDefaultLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetToDefaultLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetToDefaultLayout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/ResetToDefaultLayout", {
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
   Summary: Invoke method SetAsSystemDefaultLayout
   Description: Sets the specified published layout as the system default layout for the homepage type.
   OperationID: SetAsSystemDefaultLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetAsSystemDefaultLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAsSystemDefaultLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetAsSystemDefaultLayout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/SetAsSystemDefaultLayout", {
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
   Summary: Invoke method IsLayoutPublished
   Description: Checks if layout is published.
   OperationID: IsLayoutPublished
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsLayoutPublished_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsLayoutPublished_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsLayoutPublished(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/IsLayoutPublished", {
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
   Summary: Invoke method GetPublishedShellLayouts
   Description: Gets the published layouts.
   OperationID: GetPublishedShellLayouts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPublishedShellLayouts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPublishedShellLayouts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPublishedShellLayouts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetPublishedShellLayouts", {
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
   Summary: Invoke method CheckIfUserHasAccessToLayout
   Description: Checks if user has access to layout.
   OperationID: CheckIfUserHasAccessToLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIfUserHasAccessToLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfUserHasAccessToLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIfUserHasAccessToLayout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/CheckIfUserHasAccessToLayout", {
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
   Summary: Invoke method UpdateSecurityCodeForPublishedLayout
   Description: Updates the security code for published layout.
   OperationID: UpdateSecurityCodeForPublishedLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSecurityCodeForPublishedLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSecurityCodeForPublishedLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateSecurityCodeForPublishedLayout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/UpdateSecurityCodeForPublishedLayout", {
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
   Summary: Invoke method PublishLayout
   Description: Publishes the layout from the ShellLayoutPersonal into the ShellLayout table.
   OperationID: PublishLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PublishLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PublishLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PublishLayout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/PublishLayout", {
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
   Summary: Invoke method UnpublishLayout
   Description: Unpublishes the layout if it is un-used.
   OperationID: UnpublishLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnpublishLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnpublishLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnpublishLayout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/UnpublishLayout", {
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
   Summary: Invoke method SelectPublishedLayoutForUser
   Description: Selects the published layout for user.
   OperationID: SelectPublishedLayoutForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectPublishedLayoutForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectPublishedLayoutForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectPublishedLayoutForUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/SelectPublishedLayoutForUser", {
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
   Summary: Invoke method SaveShellLayoutAsPersonal
   Description: Saves the published layout as personal.
   OperationID: SaveShellLayoutAsPersonal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveShellLayoutAsPersonal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveShellLayoutAsPersonal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveShellLayoutAsPersonal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/SaveShellLayoutAsPersonal", {
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
   Summary: Invoke method IsCurrentPersonalLayoutReadonly
   Description: Determines whether the user's layout is non-editable (published or system layout).
   OperationID: IsCurrentPersonalLayoutReadonly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsCurrentPersonalLayoutReadonly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsCurrentPersonalLayoutReadonly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsCurrentPersonalLayoutReadonly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/IsCurrentPersonalLayoutReadonly", {
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
   Summary: Invoke method GetCurrentCompanySiteLogo
   Description: Gets the current company site logo.
   OperationID: GetCurrentCompanySiteLogo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentCompanySiteLogo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrentCompanySiteLogo(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetCurrentCompanySiteLogo", {
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
   Summary: Invoke method ExportShellLayout
   Description: Exports the shell layout.
   OperationID: ExportShellLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportShellLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportShellLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportShellLayout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/ExportShellLayout", {
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
   Summary: Invoke method ImportShellLayout
   Description: Imports the shell layout.
   OperationID: ImportShellLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportShellLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportShellLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportShellLayout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/ImportShellLayout", {
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
   Summary: Invoke method GetPersonalShellLayoutForUser
   Description: Gets the personal shell layout for user.
   OperationID: GetPersonalShellLayoutForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPersonalShellLayoutForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPersonalShellLayoutForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPersonalShellLayoutForUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetPersonalShellLayoutForUser", {
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
   Summary: Invoke method GetHomePageForUser
   Description: Gets the home page for user.
   OperationID: GetHomePageForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHomePageForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHomePageForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHomePageForUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetHomePageForUser", {
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
   Summary: Invoke method UpdateHomePageForUser
   Description: Updates the home page for user.
   OperationID: UpdateHomePageForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateHomePageForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateHomePageForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateHomePageForUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/UpdateHomePageForUser", {
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
   Summary: Invoke method GetUserOptionsForUser
   Description: Gets the user options for user.
   OperationID: GetUserOptionsForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUserOptionsForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserOptionsForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUserOptionsForUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetUserOptionsForUser", {
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
   Summary: Invoke method UpdateUserOptionsForUser
   Description: Updates the user options for user.
   OperationID: UpdateUserOptionsForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateUserOptionsForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateUserOptionsForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateUserOptionsForUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/UpdateUserOptionsForUser", {
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
   Summary: Invoke method GetImageForTile
   Description: Gets the image for tile.
   OperationID: GetImageForTile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetImageForTile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetImageForTile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetImageForTile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetImageForTile", {
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
   Summary: Invoke method SaveImageForTile
   Description: Saves the image for tile.
   OperationID: SaveImageForTile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveImageForTile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveImageForTile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveImageForTile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/SaveImageForTile", {
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
   Summary: Invoke method GetDataDiscoveryUrl
   Description: Gets the data discovery URL from the system configuration.
   OperationID: GetDataDiscoveryUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataDiscoveryUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataDiscoveryUrl(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetDataDiscoveryUrl", {
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
   Summary: Invoke method SaveDataDiscoveryUrl
   Description: Saves the data discovery URL to the system configuration.
   OperationID: SaveDataDiscoveryUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveDataDiscoveryUrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveDataDiscoveryUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveDataDiscoveryUrl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/SaveDataDiscoveryUrl", {
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
   Summary: Invoke method GetNewShellLayout
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShellLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShellLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShellLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShellLayout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetNewShellLayout", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ShellLayoutListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ShellLayoutListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ShellLayoutRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ShellLayoutRow[],
}

export interface Ice_Tablesets_ShellLayoutListRow{
      /**  TenantID  */  
   "TenantID":string,
      /**  LayoutID  */  
   "LayoutID":string,
      /**  AuthorID  */  
   "AuthorID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SecCode  */  
   "SecCode":string,
      /**  Published  */  
   "Published":boolean,
      /**  HomePageType  */  
   "HomePageType":string,
      /**  SubType  */  
   "SubType":string,
      /**  LayoutDescription  */  
   "LayoutDescription":string,
      /**  IsHomeDefault  */  
   "IsHomeDefault":boolean,
      /**  Version of the release this layout was exported from.  */  
   "Version":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ShellLayoutRow{
      /**  TenantID  */  
   "TenantID":string,
      /**  LayoutID  */  
   "LayoutID":string,
      /**  AuthorID  */  
   "AuthorID":string,
      /**  DateModified  */  
   "DateModified":string,
      /**  ShellHomePage  */  
   "ShellHomePage":string,
      /**  ShellUserOptions  */  
   "ShellUserOptions":string,
      /**  FavoriteItems  */  
   "FavoriteItems":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SecCode  */  
   "SecCode":string,
      /**  Published  */  
   "Published":boolean,
      /**  HomePageType  */  
   "HomePageType":string,
      /**  SubType  */  
   "SubType":string,
      /**  LayoutDescription  */  
   "LayoutDescription":string,
      /**  IsHomeDefault  */  
   "IsHomeDefault":boolean,
      /**  Version of the release this layout was exported from.  */  
   "Version":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param layoutId
      @param userId
      @param homePageType
      @param subType
   */  
export interface CheckIfUserHasAccessToLayout_input{
      /**  The layout identifier.  */  
   layoutId:string,
      /**  The user identifier.  */  
   userId:string,
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
}

export interface CheckIfUserHasAccessToLayout_output{
   returnObj:boolean,
}

   /** Required : 
      @param tenantID
      @param homePageType
      @param subType
      @param layoutID
   */  
export interface DeleteByID_input{
   tenantID:string,
   homePageType:string,
   subType:string,
   layoutID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param homePageType
      @param subType
      @param layoutId
   */  
export interface ExportShellLayout_input{
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
      /**  The layout identifier.  */  
   layoutId:string,
}

export interface ExportShellLayout_output{
      /**  Serialized ShellLayoutDataSet.  */  
   returnObj:string,
}

   /** Required : 
      @param tenantID
      @param homePageType
      @param subType
      @param layoutID
   */  
export interface GetByID_input{
   tenantID:string,
   homePageType:string,
   subType:string,
   layoutID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_ShellLayoutTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_ShellLayoutTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_ShellLayoutTableset[],
}

export interface GetCurrentCompanySiteLogo_output{
      /**  Default logo for current Company or Site, if defined.  */  
   returnObj:string,
}

export interface GetDataDiscoveryUrl_output{
   returnObj:string,
}

   /** Required : 
      @param homePageType
      @param subType
   */  
export interface GetDefaultLayout_input{
      /**  Type of the home page (ERP, CRM, MES).  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
}

export interface GetDefaultLayout_output{
   returnObj:Ice_Tablesets_ShellLayoutTableset[],
}

   /** Required : 
      @param homePageType
      @param subType
      @param layoutId
   */  
export interface GetHomePageForUser_input{
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
      /**  The layout identifier.  */  
   layoutId:string,
}

export interface GetHomePageForUser_output{
   returnObj:Ice_Tablesets_HomePageTableset[],
parameters : {
      /**  output parameters  */  
   warningLayoutNoAccess:string,
}
}

   /** Required : 
      @param imageId
   */  
export interface GetImageForTile_input{
      /**  The image identifier.  */  
   imageId:string,
}

export interface GetImageForTile_output{
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
   returnObj:Ice_Tablesets_ShellLayoutListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param tenantID
      @param homePageType
      @param subType
   */  
export interface GetNewShellLayout_input{
   ds:Ice_Tablesets_ShellLayoutTableset[],
   tenantID:string,
   homePageType:string,
   subType:string,
}

export interface GetNewShellLayout_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ShellLayoutTableset[],
}
}

   /** Required : 
      @param homePageType
      @param subType
      @param layoutId
      @param homePageData
      @param userOptionsData
      @param favoritesData
   */  
export interface GetPersonalShellLayoutForUser_input{
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
      /**  The layout identifier.  */  
   layoutId:string,
   homePageData:Ice_Tablesets_HomePageTableset[],
   userOptionsData:Ice_Tablesets_UserOptionsTableset[],
   favoritesData:Ice_Tablesets_FavoriteTableset[],
}

export interface GetPersonalShellLayoutForUser_output{
parameters : {
      /**  output parameters  */  
   homePageData:Ice_Tablesets_HomePageTableset[],
   userOptionsData:Ice_Tablesets_UserOptionsTableset[],
   favoritesData:Ice_Tablesets_FavoriteTableset[],
   warningNoAccess:string,
}
}

   /** Required : 
      @param homePageType
      @param subType
      @param includeSystemLayouts
   */  
export interface GetPublishedShellLayouts_input{
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
      /**  if set to `true` [include system layouts].  */  
   includeSystemLayouts:boolean,
}

export interface GetPublishedShellLayouts_output{
   returnObj:Ice_Tablesets_ShellLayoutListTableset[],
}

   /** Required : 
      @param whereClauseShellLayout
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseShellLayout:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_ShellLayoutTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param homePageType
      @param subType
      @param layoutId
   */  
export interface GetUserOptionsForUser_input{
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
      /**  The layout identifier. Pass empty string for 'modern' subtype.  */  
   layoutId:string,
}

export interface GetUserOptionsForUser_output{
   returnObj:Ice_Tablesets_UserOptionsTableset[],
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

export interface Ice_Tablesets_FavFolderRow{
   UserID:string,
   FolderSeq:number,
   Description:string,
   YPos:number,
   AutoLoadContents:boolean,
   AutoLoadSessionChange:boolean,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_FavItemsRow{
   UserID:string,
   FolderSeq:number,
   ItemSeq:number,
   ItemType:string,
   ItemName:string,
   Description:string,
   MenuName:string,
   YPos:number,
   AppServerURL:string,
   CompanyID:string,
   PlantID:string,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   FolderSeqDescription:string,
   RowMod:string,
}

export interface Ice_Tablesets_FavoriteTableset{
   FavFolder:Ice_Tablesets_FavFolderRow[],
   FavItems:Ice_Tablesets_FavItemsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_HomePageTableset{
   HomeTileGroup:Ice_Tablesets_HomeTileGroupRow[],
   HomeTile:Ice_Tablesets_HomeTileRow[],
   LayoutInfo:Ice_Tablesets_LayoutInfoRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_HomeTileGroupRow{
   GroupID:number,
      /**  Title of the group of tiles.  */  
   Title:string,
      /**  If this is the default Favorites group.  */  
   IsFaveDefault:boolean,
      /**  Sequence of this group on the home page.  */  
   Sequence:number,
      /**  Stores tile settings as required by the web home page in a Json format.  */  
   WebProperties:string,
      /**  The type of group.  */  
   Type:string,
      /**  Marks the tile group to be retained when no longer the active tab.  */  
   Retain:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_HomeTileRow{
      /**  Tile identifier  */  
   TileID:number,
      /**  Group that this tile belongs to.  */  
   GroupID:number,
      /**   Type of tile:                 
Baq = "B";
Favorite = "V";
General = "G";
Link = "K";
Social = "S";
DataDiscovery = "Y";
Metric = "M";

to be removed "soon".
List = "L";
Custom = "T";

UnknownA = "A";
UnknownD = "D";
UnknownF = "F";
UnknownU = "U";  */  
   Type:string,
      /**  URL or file paths for the tile.  */  
   Path:string,
      /**   Type of link on tile.         
File = "P";
Form = "F";
NoAction = "N";
Url = "U";  */  
   LinkType:string,
      /**   Display type for tile:        
Default = "D";
Image = "I";
Url = "U";  */  
   DisplayType:string,
   DisplayPath:string,
      /**   Possible values:              
File = "P";
Form = "F";
NoAction = "N";
Url = "U";  */  
   LineLinkType:string,
      /**  URL/path for the BAQ tiles.  */  
   LinePath:string,
      /**  BAQ identifier if tile displays a BAQ.  */  
   BaqId:string,
      /**  Color  */  
   Color:string,
      /**  Tile title  */  
   Title:string,
      /**  Default width of the tile  */  
   DefaultWidth:number,
      /**  Default height of the tile.  */  
   DefaultHeight:number,
      /**  Maximum width of the tile.  */  
   MaxWidth:number,
      /**  Maximum height of the tile.  */  
   MaxHeight:number,
      /**  Identifier to the image displayed for the baq.  */  
   ListImage:string,
      /**  Folder sequence for the favorite folder this tile represents.  */  
   FavoriteFolderSeq:number,
      /**  If tile is in expanded state.  */  
   ExpandedFlag:boolean,
      /**  List of Baq columns to display.  */  
   BaqColumnList:string,
      /**  Sequence of the tile.  */  
   Sequence:number,
      /**  Menu id that the tile represents.  */  
   RelatedMenuId:string,
      /**  Interval between refresh of tile data.  */  
   RefreshInterval:number,
      /**  Company if the user made the tile company-specific.  */  
   Company:string,
      /**  Appserver Url if tile is company specific.  */  
   Appserver:string,
      /**  BaqContextColumn  */  
   BaqContextColumn:string,
      /**  Site if tile is company/site specific.  */  
   Plant:string,
      /**   Aggregation function to perform on the BAQ results. 
SUM, AVG,COUNT,COUNT_STAR,MIN,MAX  */  
   MetricAggregate:string,
      /**  Prefix for Metric tile.  */  
   MetricTextPrefix:string,
      /**  Suffix for text displayed in Metric tile.  */  
   MetricTextSuffix:string,
      /**  Image identifier for the metric tile.  */  
   MetricImage:string,
      /**  Font size for Metric tile.  */  
   MetricTextFontSize:number,
      /**  SysRowID into FileStore for the image used by the tile.  */  
   ImageRowID:string,
      /**  Contains the image contents of the ImageRowID image.  */  
   ImageBlob:string,
      /**  FileName from Ice.FileStore - only used during import and export.  */  
   ImageFilename:string,
      /**  Stores tile settings as required by the web home page in a Json format.  */  
   WebProperties:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_LayoutInfoRow{
      /**  Published layout that this layout is connected to.  */  
   BaseLayoutID:string,
      /**  Indicates if this is a system default layout.  */  
   IsDefaultLayout:boolean,
      /**  LayoutID from Ice.ShellLayoutPersonal  */  
   LayoutID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ShellLayoutListRow{
      /**  TenantID  */  
   TenantID:string,
      /**  LayoutID  */  
   LayoutID:string,
      /**  AuthorID  */  
   AuthorID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SecCode  */  
   SecCode:string,
      /**  Published  */  
   Published:boolean,
      /**  HomePageType  */  
   HomePageType:string,
      /**  SubType  */  
   SubType:string,
      /**  LayoutDescription  */  
   LayoutDescription:string,
      /**  IsHomeDefault  */  
   IsHomeDefault:boolean,
      /**  Version of the release this layout was exported from.  */  
   Version:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ShellLayoutListTableset{
   ShellLayoutList:Ice_Tablesets_ShellLayoutListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ShellLayoutRow{
      /**  TenantID  */  
   TenantID:string,
      /**  LayoutID  */  
   LayoutID:string,
      /**  AuthorID  */  
   AuthorID:string,
      /**  DateModified  */  
   DateModified:string,
      /**  ShellHomePage  */  
   ShellHomePage:string,
      /**  ShellUserOptions  */  
   ShellUserOptions:string,
      /**  FavoriteItems  */  
   FavoriteItems:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SecCode  */  
   SecCode:string,
      /**  Published  */  
   Published:boolean,
      /**  HomePageType  */  
   HomePageType:string,
      /**  SubType  */  
   SubType:string,
      /**  LayoutDescription  */  
   LayoutDescription:string,
      /**  IsHomeDefault  */  
   IsHomeDefault:boolean,
      /**  Version of the release this layout was exported from.  */  
   Version:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ShellLayoutTableset{
   ShellLayout:Ice_Tablesets_ShellLayoutRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtShellLayoutTableset{
   ShellLayout:Ice_Tablesets_ShellLayoutRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UserOptionsRow{
      /**  Tile depth for home page.  */  
   HomePageTileDepth:number,
      /**  Menu that the user was on in the last session.  */  
   LastMenuFolderOpened:string,
      /**  Last menu view (zoom or tree) that user had.  */  
   LastViewDisplayed:string,
      /**  View within the contents panel for the menu (icons or list)  */  
   ContentsView:string,
      /**  Palette picked by the user.  */  
   Palette:string,
      /**  Edd theme picked by the user - Light/Dark.  */  
   EddTheme:string,
      /**  Color  */  
   Color1:string,
      /**  Color  */  
   Color2:string,
      /**  Color  */  
   Color3:string,
      /**  Color  */  
   Color4:string,
      /**  Color  */  
   Color5:string,
      /**  Background color selection  */  
   Background1:string,
      /**  Background color selection  */  
   Background2:string,
      /**  Background color selection  */  
   Background3:string,
      /**  Background color selection  */  
   Background4:string,
   ColorBars:string,
   ShowSplashText:boolean,
   ShowSplashAnimation:boolean,
   SplashText1:string,
   SplashText2:string,
   SplashText3:string,
   SplashText4:string,
   SplashText5:string,
   SplashText6:string,
   MenuTreeZoomLevel:number,
   SearchProviders:string,
      /**  Launch classic menu after log in.  */  
   LaunchClassicMenu:boolean,
      /**  Show animation when form is being launched.  */  
   ShowLoadingFormAnnimation:boolean,
      /**  Last size of the home page.  */  
   HomePageSize:string,
      /**  HomePageLocation  */  
   HomePageLocation:string,
      /**  MainFontColor  */  
   MainFontColor:string,
   ShowMenuAnimation:boolean,
      /**  File path to the logo displayed on home page.  */  
   AppLogoFile:string,
   DefaultFontFamily:string,
   DefaultFontWeight:string,
   DefaultFontSize:number,
      /**  Company  */  
   CompanyID:string,
      /**  Colors picked by the user stored as a json.  */  
   ColorsStorage:string,
      /**  SysRowID for the image row in Ice.FileStore.  */  
   AppLogoRowID:string,
      /**  Contains the image contents of theAppLogoRowID image.  */  
   AppLogoBlob:string,
      /**  FileName from Ice.FileStore. Only used during Import/Export.  */  
   AppLogoFilename:string,
      /**  Stores tile settings as required by the web home page in a Json format.  */  
   WebProperties:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UserOptionsTableset{
   UserOptions:Ice_Tablesets_UserOptionsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param layoutToImport
      @param homePageType
      @param subType
      @param layoutId
      @param replaceFavorites
      @param importedHomepageData
      @param importedUseroptionsData
      @param importedFavoritesData
   */  
export interface ImportShellLayout_input{
      /**  The layout to import.  */  
   layoutToImport:string,
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
      /**  The layout identifier into which the new layout should be imported.  */  
   layoutId:string,
      /**  if set to `true` replaces the current user's favorites with the ones from the imported layout.  */  
   replaceFavorites:boolean,
   importedHomepageData:Ice_Tablesets_HomePageTableset[],
   importedUseroptionsData:Ice_Tablesets_UserOptionsTableset[],
   importedFavoritesData:Ice_Tablesets_FavoriteTableset[],
}

export interface ImportShellLayout_output{
parameters : {
      /**  output parameters  */  
   importedHomepageData:Ice_Tablesets_HomePageTableset[],
   importedUseroptionsData:Ice_Tablesets_UserOptionsTableset[],
   importedFavoritesData:Ice_Tablesets_FavoriteTableset[],
}
}

   /** Required : 
      @param homePageType
      @param subType
      @param layoutId
   */  
export interface IsCurrentPersonalLayoutReadonly_input{
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
      /**  The layout identifier.  */  
   layoutId:string,
}

export interface IsCurrentPersonalLayoutReadonly_output{
      /**  `true` if user's layout is a published or system layout, otherwise, `false`.  */  
   returnObj:boolean,
}

   /** Required : 
      @param layoutId
      @param homePageType
      @param subType
   */  
export interface IsLayoutPublished_input{
      /**  The layout identifier.  */  
   layoutId:string,
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
}

export interface IsLayoutPublished_output{
      /**  `true` if layout is published; otherwise, `false`.  */  
   returnObj:boolean,
}

   /** Required : 
      @param personalLayoutId
      @param publishedLayoutId
      @param securityCode
      @param homePageType
      @param subType
   */  
export interface PublishLayout_input{
      /**  The personal layout identifier to publish.  */  
   personalLayoutId:string,
      /**  The layout identifier for the published layout.  */  
   publishedLayoutId:string,
      /**  The security code.  */  
   securityCode:string,
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
}

export interface PublishLayout_output{
}

   /** Required : 
      @param homePageType
      @param subType
      @param layoutId
   */  
export interface ResetToDefaultLayout_input{
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
      /**  The layout identifier.  */  
   layoutId:string,
}

export interface ResetToDefaultLayout_output{
   returnObj:Ice_Tablesets_ShellLayoutTableset[],
}

   /** Required : 
      @param url
   */  
export interface SaveDataDiscoveryUrl_input{
      /**  The URL.  */  
   url:string,
}

export interface SaveDataDiscoveryUrl_output{
}

   /** Required : 
      @param fileName
      @param imageBlob
   */  
export interface SaveImageForTile_input{
      /**  Name of the file.  */  
   fileName:string,
      /**  The image BLOB.  */  
   imageBlob:string,
}

export interface SaveImageForTile_output{
   returnObj:string,
}

   /** Required : 
      @param homePageType
      @param subType
      @param layoutId
   */  
export interface SaveShellLayoutAsPersonal_input{
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
      /**  The layout identifier. Pass in empty string for modern.  */  
   layoutId:string,
}

export interface SaveShellLayoutAsPersonal_output{
}

   /** Required : 
      @param publishedLayoutId
      @param homePageType
      @param subType
      @param replaceFavorites
   */  
export interface SelectPublishedLayoutForUser_input{
      /**  The published layout identifier.  */  
   publishedLayoutId:string,
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
      /**  if set to `true` replaces the favorites for the current user.  */  
   replaceFavorites:boolean,
}

export interface SelectPublishedLayoutForUser_output{
   returnObj:Ice_Tablesets_ShellLayoutTableset[],
}

   /** Required : 
      @param publishedLayout
      @param homePageType
      @param subType
   */  
export interface SetAsSystemDefaultLayout_input{
      /**  The layout identifier. Send in null if IsHomeDefault should be reset.  */  
   publishedLayout:string,
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
}

export interface SetAsSystemDefaultLayout_output{
}

   /** Required : 
      @param publishedLayoutId
      @param homePageType
      @param subType
   */  
export interface UnpublishLayout_input{
      /**  The published layout identifier.  */  
   publishedLayoutId:string,
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
}

export interface UnpublishLayout_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtShellLayoutTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtShellLayoutTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param homePageType
      @param subType
      @param layoutId
      @param homePageData
   */  
export interface UpdateHomePageForUser_input{
      /**  Type of the home page.  */  
   homePageType:string,
      /**  Type of the sub.  */  
   subType:string,
      /**  The layout identifier. Empty string for 'modern'. 'Default' or user defined layout identifier in kinetic.  */  
   layoutId:string,
   homePageData:Ice_Tablesets_HomePageTableset[],
}

export interface UpdateHomePageForUser_output{
}

   /** Required : 
      @param publishedLayoutId
      @param newSecurityCode
      @param homePageType
      @param subType
   */  
export interface UpdateSecurityCodeForPublishedLayout_input{
      /**  The published layout identifier.  */  
   publishedLayoutId:string,
      /**  The new security code.  */  
   newSecurityCode:string,
      /**  Type of the home page.  */  
   homePageType:string,
      /**  The client side implementation, 'modern' or 'kinetic'.  */  
   subType:string,
}

export interface UpdateSecurityCodeForPublishedLayout_output{
}

   /** Required : 
      @param homePageType
      @param subType
      @param layoutId
      @param userOptionsData
   */  
export interface UpdateUserOptionsForUser_input{
      /**  Type of the home page.  */  
   homePageType:string,
      /**  Type of the sub.  */  
   subType:string,
      /**  The layout identifier. Pass empty string for 'modern' subtype.  */  
   layoutId:string,
   userOptionsData:Ice_Tablesets_UserOptionsTableset[],
}

export interface UpdateUserOptionsForUser_output{
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_ShellLayoutTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ShellLayoutTableset[],
}
}

