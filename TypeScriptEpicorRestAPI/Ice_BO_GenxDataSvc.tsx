import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.GenxDataSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/$metadata", {
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
   Description: Get GenXDatas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GenXDatas
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.XXXDefRow
   */  
export function get_GenXDatas(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XXXDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GenXDatas", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XXXDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GenXDatas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.XXXDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.XXXDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenXDatas(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GenXDatas", {
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
   Summary: Calls GetByID to retrieve the GenXData item
   Description: Calls GetByID to retrieve the GenXData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GenXData
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.XXXDefRow
   */  
export function get_GenXDatas_Company_ProductID_TypeCode_CGCCode_Key1_Key2_Key3(Company:string, ProductID:string, TypeCode:string, CGCCode:string, Key1:string, Key2:string, Key3:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_XXXDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GenXDatas(" + Company + "," + ProductID + "," + TypeCode + "," + CGCCode + "," + Key1 + "," + Key2 + "," + Key3 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_XXXDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GenXData for the service
   Description: Calls UpdateExt to update GenXData. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GenXData
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.XXXDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GenXDatas_Company_ProductID_TypeCode_CGCCode_Key1_Key2_Key3(Company:string, ProductID:string, TypeCode:string, CGCCode:string, Key1:string, Key2:string, Key3:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GenXDatas(" + Company + "," + ProductID + "," + TypeCode + "," + CGCCode + "," + Key1 + "," + Key2 + "," + Key3 + ")", {
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
   Summary: Call UpdateExt to delete GenXData item
   Description: Call UpdateExt to delete GenXData item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GenXData
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GenXDatas_Company_ProductID_TypeCode_CGCCode_Key1_Key2_Key3(Company:string, ProductID:string, TypeCode:string, CGCCode:string, Key1:string, Key2:string, Key3:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GenXDatas(" + Company + "," + ProductID + "," + TypeCode + "," + CGCCode + "," + Key1 + "," + Key2 + "," + Key3 + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.XXXDefListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XXXDefListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XXXDefListRow)
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
export function get_GetRows(whereClauseXXXDef:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseXXXDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseXXXDef=" + whereClauseXXXDef
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(company:string, productID:string, typeCode:string, cgCCode:string, key1:string, key2:string, key3:string, epicorHeaders?:Headers){
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
   if(typeof productID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "productID=" + productID
   }
   if(typeof typeCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "typeCode=" + typeCode
   }
   if(typeof cgCCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "cgCCode=" + cgCCode
   }
   if(typeof key1!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key1=" + key1
   }
   if(typeof key2!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key2=" + key2
   }
   if(typeof key3!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key3=" + key3
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GetList" + params, {
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
   Summary: Invoke method SearchCustomizations
   Description: Search customizations.
   OperationID: SearchCustomizations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SearchCustomizations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SearchCustomizations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SearchCustomizations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/SearchCustomizations", {
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
   Summary: Invoke method GetCustomizationList
   Description: Find customizations
   OperationID: GetCustomizationList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomizationList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomizationList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustomizationList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GetCustomizationList", {
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
   Summary: Invoke method CreateKineticCustomization
   Description: return delimited list of select kinetic customizations
   OperationID: CreateKineticCustomization
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateKineticCustomization_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateKineticCustomization_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateKineticCustomization(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/CreateKineticCustomization", {
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
   Summary: Invoke method GetVersion
   Description: This method will require the primary unique index fields
locate the XXXDef record and return the "version" field value.
   OperationID: GetVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVersion(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GetVersion", {
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
   Summary: Invoke method GetOrAdd
   Description: This method will require the primary unique index fields
locate the XXXDef record and return the "version" field value.
   OperationID: GetOrAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrAdd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GetOrAdd", {
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
   Summary: Invoke method GetByIDEx
   Description: This method returns a dataset representing a XXXDEF with a blank CompanyID
   OperationID: GetByIDEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDEx(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GetByIDEx", {
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
   Summary: Invoke method StoreData
   Description: This methods should be ran instead of the base Update method.
This method will require the dataset to come in, next it will delete all XXXChunk
records associated with each ttXXXDef in the dataset while also deleting
the XXXDef records in the database.  Next the ttXXXDef table will be the driving force behind
the creation of new XXXDef and XXXChunk records in the database.
The values for the fields in these records will come from what is in the dataset.
This 'StoreData' process is basically a complete 'overlay' of the Generic Large Data data.
   OperationID: StoreData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StoreData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StoreData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StoreData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/StoreData", {
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
   Summary: Invoke method VerifyClientShare
   Description: Verify Client share
   OperationID: VerifyClientShare
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyClientShare_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyClientShare_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifyClientShare(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/VerifyClientShare", {
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
   Summary: Invoke method XXXDefExist
   Description: This method will return if an existing xxxdef record exists based on the primary keys.
   OperationID: XXXDefExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/XXXDefExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/XXXDefExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_XXXDefExist(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/XXXDefExist", {
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
   Summary: Invoke method CheckIfRecordExists
   Description: Checks if the record exists in the db.
   OperationID: CheckIfRecordExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIfRecordExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfRecordExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIfRecordExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/CheckIfRecordExists", {
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
   Summary: Invoke method ImportCustomization
   Description: Imports customization.
   OperationID: ImportCustomization
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportCustomization_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportCustomization_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportCustomization(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/ImportCustomization", {
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
   Summary: Invoke method GetNewXXXDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewXXXDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewXXXDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewXXXDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewXXXDef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GetNewXXXDef", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.GenxDataSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XXXDefListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_XXXDefListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XXXDefRow{
   "odatametadata":string,
   "value":Ice_Tablesets_XXXDefRow[],
}

export interface Ice_Tablesets_XXXDefListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Valid values:  BE - Base Extention, EX - Express, ST - Standard, EP - Enterprise  */  
   "ProductID":string,
      /**  Ex: Customization, Personalization  */  
   "TypeCode":string,
      /**   Generic key component field.
Ex: Customization Name if TypeCode =  "Customization" 
FormName if TypeCode = "Personalization"  */  
   "Key1":string,
      /**   Generic key component field.
Ex: FormName Name if TypeCode =  "Customization" 
UserID if TypeCode = "Personalization"  */  
   "Key2":string,
      /**   Generic key component field.
Ex: if TypeCode =  "Customization"  this may contain "WIP" or blanks.  */  
   "Key3":string,
      /**  Description  */  
   "Description":string,
      /**  Date Last Updated  */  
   "LastUpdated":string,
      /**  Last Updated By  */  
   "LastUpdatedBy":string,
      /**  Version  */  
   "Version":string,
      /**  Database Version  */  
   "DataBaseVersion":number,
      /**  SysCharacter01  */  
   "SysCharacter01":string,
      /**  SysCharacter02  */  
   "SysCharacter02":string,
      /**  SysCharacter03  */  
   "SysCharacter03":string,
      /**  SysCharacter04  */  
   "SysCharacter04":string,
      /**  SysCharacter05  */  
   "SysCharacter05":string,
      /**  SysNumber01  */  
   "SysNumber01":number,
      /**  SysNumber02  */  
   "SysNumber02":number,
      /**  SysNumber03  */  
   "SysNumber03":number,
      /**  SysNumber04  */  
   "SysNumber04":number,
      /**  SysNumber05  */  
   "SysNumber05":number,
      /**  SysDate01  */  
   "SysDate01":string,
      /**  SysDate02  */  
   "SysDate02":string,
      /**  SysDate03  */  
   "SysDate03":string,
      /**  SysDate04  */  
   "SysDate04":string,
      /**  SysDate05  */  
   "SysDate05":string,
      /**  SysCheckBox01  */  
   "SysCheckBox01":boolean,
      /**  SysCheckBox02  */  
   "SysCheckBox02":boolean,
      /**  SysCheckBox03  */  
   "SysCheckBox03":boolean,
      /**  SysCheckBox04  */  
   "SysCheckBox04":boolean,
      /**  SysCheckBox05  */  
   "SysCheckBox05":boolean,
      /**  Contains comments about the GenX.  */  
   "CommentText":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SysCheckBox06  */  
   "SysCheckBox06":boolean,
      /**  SysCheckBox07  */  
   "SysCheckBox07":boolean,
      /**  OnMenu  */  
   "OnMenu":boolean,
      /**  Duplicate  */  
   "Duplicate":boolean,
      /**  Cosmetic  */  
   "Cosmetic":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_XXXDefRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Valid values:  BE - Base Extention, EX - Express, ST - Standard, EP - Enterprise  */  
   "ProductID":string,
      /**  Ex: Customization, Personalization  */  
   "TypeCode":string,
      /**   Generic key component field.
Ex: Customization Name if TypeCode =  "Customization" 
FormName if TypeCode = "Personalization"  */  
   "Key1":string,
      /**   Generic key component field.
Ex: FormName Name if TypeCode =  "Customization" 
UserID if TypeCode = "Personalization"  */  
   "Key2":string,
      /**   Generic key component field.
Ex: if TypeCode =  "Customization"  this may contain "WIP" or blanks.  */  
   "Key3":string,
      /**  Description  */  
   "Description":string,
      /**  Date Last Updated  */  
   "LastUpdated":string,
      /**  Last Updated By  */  
   "LastUpdatedBy":string,
      /**  Version  */  
   "Version":string,
      /**  Database Version  */  
   "DataBaseVersion":number,
      /**  SysCharacter01  */  
   "SysCharacter01":string,
      /**  SysCharacter02  */  
   "SysCharacter02":string,
      /**  SysCharacter03  */  
   "SysCharacter03":string,
      /**  SysCharacter04  */  
   "SysCharacter04":string,
      /**  SysCharacter05  */  
   "SysCharacter05":string,
      /**  SysNumber01  */  
   "SysNumber01":number,
      /**  SysNumber02  */  
   "SysNumber02":number,
      /**  SysNumber03  */  
   "SysNumber03":number,
      /**  SysNumber04  */  
   "SysNumber04":number,
      /**  SysNumber05  */  
   "SysNumber05":number,
      /**  SysDate01  */  
   "SysDate01":string,
      /**  SysDate02  */  
   "SysDate02":string,
      /**  SysDate03  */  
   "SysDate03":string,
      /**  SysDate04  */  
   "SysDate04":string,
      /**  SysDate05  */  
   "SysDate05":string,
      /**  SysCheckBox01  */  
   "SysCheckBox01":boolean,
      /**  SysCheckBox02  */  
   "SysCheckBox02":boolean,
      /**  SysCheckBox03  */  
   "SysCheckBox03":boolean,
      /**  SysCheckBox04  */  
   "SysCheckBox04":boolean,
      /**  SysCheckBox05  */  
   "SysCheckBox05":boolean,
      /**  Contains comments about the GenX.  */  
   "CommentText":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SysCheckBox06  */  
   "SysCheckBox06":boolean,
      /**  SysCheckBox07  */  
   "SysCheckBox07":boolean,
      /**  OnMenu  */  
   "OnMenu":boolean,
      /**  Duplicate  */  
   "Duplicate":boolean,
      /**  Cosmetic  */  
   "Cosmetic":boolean,
      /**  Content  */  
   "Content":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param importFileXml
      @param allCompanies
      @param newName
   */  
export interface CheckIfRecordExists_input{
      /**  Import file XML.  */  
   importFileXml:string,
      /**  Is all companies.  */  
   allCompanies:boolean,
      /**  New file name.  */  
   newName:string,
}

export interface CheckIfRecordExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
   */  
export interface CreateKineticCustomization_input{
   ds:Ice_Tablesets_CustomizationListTableset[],
}

export interface CreateKineticCustomization_output{
   returnObj:string,
}

   /** Required : 
      @param company
      @param productID
      @param typeCode
      @param cgCCode
      @param key1
      @param key2
      @param key3
   */  
export interface DeleteByID_input{
   company:string,
   productID:string,
   typeCode:string,
   cgCCode:string,
   key1:string,
   key2:string,
   key3:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ipProductID
      @param ipTypeCode
      @param ipCGCCode
      @param ipKey1
      @param ipKey2
      @param ipKey3
   */  
export interface GetByIDEx_input{
      /**  The company id.  */  
   ipProductID:string,
      /**  The type code.  */  
   ipTypeCode:string,
      /**  The CSF Code.  */  
   ipCGCCode:string,
      /**  The Key1.  */  
   ipKey1:string,
      /**  The Key2.  */  
   ipKey2:string,
      /**  The Key3.  */  
   ipKey3:string,
}

export interface GetByIDEx_output{
   returnObj:Ice_Tablesets_GenXDataTableset[],
}

   /** Required : 
      @param company
      @param productID
      @param typeCode
      @param cgCCode
      @param key1
      @param key2
      @param key3
   */  
export interface GetByID_input{
   company:string,
   productID:string,
   typeCode:string,
   cgCCode:string,
   key1:string,
   key2:string,
   key3:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_GenXDataTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_GenXDataTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_GenXDataTableset[],
}

   /** Required : 
      @param company
      @param allCompanies
      @param menuType
      @param program
      @param report
   */  
export interface GetCustomizationList_input{
   company:string,
   allCompanies:boolean,
   menuType:string,
   program:string,
   report:string,
}

export interface GetCustomizationList_output{
   returnObj:Ice_Tablesets_CustomizationListTableset[],
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
   returnObj:Ice_Tablesets_XXXDefListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param company
      @param productID
      @param typeCode
      @param cgCCode
      @param key1
      @param key2
   */  
export interface GetNewXXXDef_input{
   ds:Ice_Tablesets_GenXDataTableset[],
   company:string,
   productID:string,
   typeCode:string,
   cgCCode:string,
   key1:string,
   key2:string,
}

export interface GetNewXXXDef_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_GenXDataTableset[],
}
}

   /** Required : 
      @param company
      @param productID
      @param typeCode
      @param cgCCode
      @param key1
      @param key2
      @param key3
   */  
export interface GetOrAdd_input{
      /**  The company id value to return version for.  */  
   company:string,
      /**  The product id value to return version for.  */  
   productID:string,
      /**  The type code value to return version for.  */  
   typeCode:string,
      /**  The CSF Code.  */  
   cgCCode:string,
      /**  The key1 value to return version for.  */  
   key1:string,
      /**  The key2 value to return version for.  */  
   key2:string,
      /**  The key3 value to return version for.  */  
   key3:string,
}

export interface GetOrAdd_output{
   returnObj:Ice_Tablesets_GenXDataTableset[],
parameters : {
      /**  output parameters  */  
   newRecord:boolean,
}
}

   /** Required : 
      @param whereClauseXXXDef
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseXXXDef:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_GenXDataTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipCompanyID
      @param ipProductID
      @param ipTypeCode
      @param ipCGCCode
      @param ipKey1
      @param ipKey2
      @param ipKey3
   */  
export interface GetVersion_input{
      /**  The company id value to return version for.  */  
   ipCompanyID:string,
      /**  The product id value to return version for.  */  
   ipProductID:string,
      /**  The type code value to return version for.  */  
   ipTypeCode:string,
      /**  The CSF Code.  */  
   ipCGCCode:string,
      /**  The key1 value to return version for.  */  
   ipKey1:string,
      /**  The key2 value to return version for.  */  
   ipKey2:string,
      /**  The key3 value to return version for.  */  
   ipKey3:string,
}

export interface GetVersion_output{
parameters : {
      /**  output parameters  */  
   opVersion:string,
   opRecordExists:boolean,
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

export interface Ice_Tablesets_CustomizationListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Valid values:  BE - Base Extention, EX - Express, ST - Standard, EP - Enterprise  */  
   ProductID:string,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**   Generic key component field.
Ex: Customization Name if TypeCode =  "Customization" 
FormName if TypeCode = "Personalization"  */  
   Key1:string,
      /**   Generic key component field.
Ex: FormName Name if TypeCode =  "Customization" 
UserID if TypeCode = "Personalization"  */  
   Key2:string,
      /**   Generic key component field.
Ex: if TypeCode =  "Customization"  this may contain "WIP" or blanks.  */  
   Key3:string,
      /**  Description  */  
   Description:string,
      /**  SysCharacter01  */  
   SysCharacter01:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Order:number,
   Select:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_CustomizationListTableset{
   CustomizationList:Ice_Tablesets_CustomizationListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_GenXDataTableset{
   XXXDef:Ice_Tablesets_XXXDefRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtGenXDataTableset{
   XXXDef:Ice_Tablesets_XXXDefRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_XXXDefListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Valid values:  BE - Base Extention, EX - Express, ST - Standard, EP - Enterprise  */  
   ProductID:string,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**   Generic key component field.
Ex: Customization Name if TypeCode =  "Customization" 
FormName if TypeCode = "Personalization"  */  
   Key1:string,
      /**   Generic key component field.
Ex: FormName Name if TypeCode =  "Customization" 
UserID if TypeCode = "Personalization"  */  
   Key2:string,
      /**   Generic key component field.
Ex: if TypeCode =  "Customization"  this may contain "WIP" or blanks.  */  
   Key3:string,
      /**  Description  */  
   Description:string,
      /**  Date Last Updated  */  
   LastUpdated:string,
      /**  Last Updated By  */  
   LastUpdatedBy:string,
      /**  Version  */  
   Version:string,
      /**  Database Version  */  
   DataBaseVersion:number,
      /**  SysCharacter01  */  
   SysCharacter01:string,
      /**  SysCharacter02  */  
   SysCharacter02:string,
      /**  SysCharacter03  */  
   SysCharacter03:string,
      /**  SysCharacter04  */  
   SysCharacter04:string,
      /**  SysCharacter05  */  
   SysCharacter05:string,
      /**  SysNumber01  */  
   SysNumber01:number,
      /**  SysNumber02  */  
   SysNumber02:number,
      /**  SysNumber03  */  
   SysNumber03:number,
      /**  SysNumber04  */  
   SysNumber04:number,
      /**  SysNumber05  */  
   SysNumber05:number,
      /**  SysDate01  */  
   SysDate01:string,
      /**  SysDate02  */  
   SysDate02:string,
      /**  SysDate03  */  
   SysDate03:string,
      /**  SysDate04  */  
   SysDate04:string,
      /**  SysDate05  */  
   SysDate05:string,
      /**  SysCheckBox01  */  
   SysCheckBox01:boolean,
      /**  SysCheckBox02  */  
   SysCheckBox02:boolean,
      /**  SysCheckBox03  */  
   SysCheckBox03:boolean,
      /**  SysCheckBox04  */  
   SysCheckBox04:boolean,
      /**  SysCheckBox05  */  
   SysCheckBox05:boolean,
      /**  Contains comments about the GenX.  */  
   CommentText:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SysCheckBox06  */  
   SysCheckBox06:boolean,
      /**  SysCheckBox07  */  
   SysCheckBox07:boolean,
      /**  OnMenu  */  
   OnMenu:boolean,
      /**  Duplicate  */  
   Duplicate:boolean,
      /**  Cosmetic  */  
   Cosmetic:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_XXXDefListTableset{
   XXXDefList:Ice_Tablesets_XXXDefListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_XXXDefRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Valid values:  BE - Base Extention, EX - Express, ST - Standard, EP - Enterprise  */  
   ProductID:string,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**   Generic key component field.
Ex: Customization Name if TypeCode =  "Customization" 
FormName if TypeCode = "Personalization"  */  
   Key1:string,
      /**   Generic key component field.
Ex: FormName Name if TypeCode =  "Customization" 
UserID if TypeCode = "Personalization"  */  
   Key2:string,
      /**   Generic key component field.
Ex: if TypeCode =  "Customization"  this may contain "WIP" or blanks.  */  
   Key3:string,
      /**  Description  */  
   Description:string,
      /**  Date Last Updated  */  
   LastUpdated:string,
      /**  Last Updated By  */  
   LastUpdatedBy:string,
      /**  Version  */  
   Version:string,
      /**  Database Version  */  
   DataBaseVersion:number,
      /**  SysCharacter01  */  
   SysCharacter01:string,
      /**  SysCharacter02  */  
   SysCharacter02:string,
      /**  SysCharacter03  */  
   SysCharacter03:string,
      /**  SysCharacter04  */  
   SysCharacter04:string,
      /**  SysCharacter05  */  
   SysCharacter05:string,
      /**  SysNumber01  */  
   SysNumber01:number,
      /**  SysNumber02  */  
   SysNumber02:number,
      /**  SysNumber03  */  
   SysNumber03:number,
      /**  SysNumber04  */  
   SysNumber04:number,
      /**  SysNumber05  */  
   SysNumber05:number,
      /**  SysDate01  */  
   SysDate01:string,
      /**  SysDate02  */  
   SysDate02:string,
      /**  SysDate03  */  
   SysDate03:string,
      /**  SysDate04  */  
   SysDate04:string,
      /**  SysDate05  */  
   SysDate05:string,
      /**  SysCheckBox01  */  
   SysCheckBox01:boolean,
      /**  SysCheckBox02  */  
   SysCheckBox02:boolean,
      /**  SysCheckBox03  */  
   SysCheckBox03:boolean,
      /**  SysCheckBox04  */  
   SysCheckBox04:boolean,
      /**  SysCheckBox05  */  
   SysCheckBox05:boolean,
      /**  Contains comments about the GenX.  */  
   CommentText:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SysCheckBox06  */  
   SysCheckBox06:boolean,
      /**  SysCheckBox07  */  
   SysCheckBox07:boolean,
      /**  OnMenu  */  
   OnMenu:boolean,
      /**  Duplicate  */  
   Duplicate:boolean,
      /**  Cosmetic  */  
   Cosmetic:boolean,
      /**  Content  */  
   Content:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param importFileXml
      @param allCompanies
      @param newName
   */  
export interface ImportCustomization_input{
      /**  Import file XML.  */  
   importFileXml:string,
      /**  Is all companies.  */  
   allCompanies:boolean,
      /**  New file name.  */  
   newName:string,
}

export interface ImportCustomization_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   outputMessage:string,
}
}

   /** Required : 
      @param whereClause
   */  
export interface SearchCustomizations_input{
      /**  where clause.  */  
   whereClause:string,
}

export interface SearchCustomizations_output{
   returnObj:Ice_Tablesets_CustomizationListTableset[],
}

   /** Required : 
      @param dsGenXData
   */  
export interface StoreData_input{
   dsGenXData:Ice_Tablesets_GenXDataTableset[],
}

export interface StoreData_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtGenXDataTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtGenXDataTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_GenXDataTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_GenXDataTableset[],
}
}

   /** Required : 
      @param clientDir
   */  
export interface VerifyClientShare_input{
   clientDir:string,
}

export interface VerifyClientShare_output{
}

   /** Required : 
      @param company
      @param productID
      @param typeCode
      @param cgCCode
      @param key1
      @param key2
      @param key3
   */  
export interface XXXDefExist_input{
      /**  The company id value to return version for.  */  
   company:string,
      /**  The product id value to return version for.  */  
   productID:string,
      /**  The type code value to return version for.  */  
   typeCode:string,
      /**  The CSF Code.  */  
   cgCCode:string,
      /**  The key1 value to return version for.  */  
   key1:string,
      /**  The key2 value to return version for.  */  
   key2:string,
      /**  The key3 value to return version for.  */  
   key3:string,
}

export interface XXXDefExist_output{
   returnObj:boolean,
}

