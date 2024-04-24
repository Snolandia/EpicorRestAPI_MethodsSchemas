import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PkgControlIDGeneratorSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/$metadata", {
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
   Description: Get PkgControlIDGenerators items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlIDGenerators
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlIDGeneratorRow
   */  
export function get_PkgControlIDGenerators(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlIDGeneratorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/PkgControlIDGenerators", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlIDGeneratorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlIDGenerators
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlIDGeneratorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlIDGeneratorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PkgControlIDGenerators(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/PkgControlIDGenerators", {
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
   Summary: Calls GetByID to retrieve the PkgControlIDGenerator item
   Description: Calls GetByID to retrieve the PkgControlIDGenerator item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlIDGenerator
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlIDGeneratorRow
   */  
export function get_PkgControlIDGenerators_PkgControlIDCode(PkgControlIDCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PkgControlIDGeneratorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/PkgControlIDGenerators(" + PkgControlIDCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PkgControlIDGeneratorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PkgControlIDGenerator for the service
   Description: Calls UpdateExt to update PkgControlIDGenerator. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlIDGenerator
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlIDGeneratorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PkgControlIDGenerators_PkgControlIDCode(PkgControlIDCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/PkgControlIDGenerators(" + PkgControlIDCode + ")", {
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
   Summary: Call UpdateExt to delete PkgControlIDGenerator item
   Description: Call UpdateExt to delete PkgControlIDGenerator item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlIDGenerator
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PkgControlIDGenerators_PkgControlIDCode(PkgControlIDCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/PkgControlIDGenerators(" + PkgControlIDCode + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlIDGeneratorListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlIDGeneratorListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlIDGeneratorListRow)
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
export function get_GetRows(whereClausePkgControlIDGenerator:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePkgControlIDGenerator!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePkgControlIDGenerator=" + whereClausePkgControlIDGenerator
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(pkgControlIDCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof pkgControlIDCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pkgControlIDCode=" + pkgControlIDCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/GetList" + params, {
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
   Summary: Invoke method GetNewPkgControlIDGenerator
   Description: Create the package control ID generator dataset.
   OperationID: GetNewPkgControlIDGenerator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlIDGenerator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlIDGenerator_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPkgControlIDGenerator(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/GetNewPkgControlIDGenerator", {
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
   Summary: Invoke method GenerateButton
   Description: Generate static or dynamic PCID.
   OperationID: GenerateButton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateButton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateButton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateButton(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/GenerateButton", {
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
   Summary: Invoke method ChangePkgControlIDCode
   Description: Validates the package control ID code.
   OperationID: ChangePkgControlIDCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePkgControlIDCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePkgControlIDCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePkgControlIDCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/ChangePkgControlIDCode", {
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
   Summary: Invoke method ChangePkgControlIDType
   Description: Validates the package control ID Type.
   OperationID: ChangePkgControlIDType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePkgControlIDType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePkgControlIDType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePkgControlIDType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/ChangePkgControlIDType", {
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
   Summary: Invoke method ChangePkgCode
   Description: Validates the package code.
   OperationID: ChangePkgCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePkgCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePkgCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePkgCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/ChangePkgCode", {
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
   Summary: Invoke method ChangePartNum
   Description: Validates the part number when changed.
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/ChangePartNum", {
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
   Summary: Invoke method GetCodeDescList
   Description: Returns the code / description list of the column.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/GetCodeDescList", {
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
   Summary: Invoke method ChangeWarehouseCode
   Description: Reset the warehouse to printer to blank if the warehouse is set to blank.
   OperationID: ChangeWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeWarehouseCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/ChangeWarehouseCode", {
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
   Summary: Invoke method GetReportStyles
   Description: Gets the report style values for Package Control ID Generator
   OperationID: GetReportStyles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportStyles_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportStyles_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportStyles(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/GetReportStyles", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDGeneratorSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlIDGeneratorListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PkgControlIDGeneratorListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlIDGeneratorRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PkgControlIDGeneratorRow[],
}

export interface Erp_Tablesets_PkgControlIDGeneratorListRow{
   "NumberToGenerate":number,
   "PartDescription":string,
   "PkgCode":string,
   "PkgCodeDescription":string,
   "PkgControlIDCode":string,
   "WarehseDesc":string,
   "TypeDescription":string,
   "PrintName":string,
   "Description":string,
   "NumberOfLabelsToPrint":number,
   "PrinterID":string,
   "WarehouseCode":string,
   "CheckAllowMixedLots":boolean,
   "CheckAllowMixedParts":boolean,
   "CheckAllowMixedUOMs":boolean,
   "CheckAllowMultipleSerialNumsPerPCID":boolean,
   "GenerateStagePCIDs":boolean,
   "PartNum":string,
      /**  Package Control Type valid values are Static, Dynamic.  */  
   "PkgControlType":string,
   "PrintLabels":boolean,
   "PCIDSGenerated":string,
   "DisableScreen":boolean,
   "Plant":string,
   "SuppressPrintLabels":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PkgControlIDGeneratorRow{
      /**   This field will be like the field on the PCID Generate screen that is called from the Material Queue STK-SHP transaction.  The search button will allow searching & Selecting an Active Package Control ID Configuration having Label Print Controlled = False.
When a value is entered or selected, if the Package Code field is empty then the Package Code field should get populated with the Package Code on the selected control ID configuration  */  
   "PkgControlIDCode":string,
      /**  Package code  */  
   "PkgCode":string,
      /**  Package code description  */  
   "PkgCodeDescription":string,
      /**  Part description  */  
   "PartDescription":string,
   "WarehseDesc":string,
   "NumberToGenerate":number,
   "TypeDescription":string,
      /**  Printer name  */  
   "PrintName":string,
   "Description":string,
   "NumberOfLabelsToPrint":number,
   "PrinterID":string,
   "GenerateStagePCIDs":boolean,
   "CheckAllowMixedParts":boolean,
   "CheckAllowMixedUOMs":boolean,
   "CheckAllowMixedLots":boolean,
   "CheckAllowMultipleSerialNumsPerPCID":boolean,
   "PrintLabels":boolean,
   "PkgControlType":string,
   "PartNum":string,
      /**   pulated with all the Warehouses owned or shared with the current site.  The Search will allow searching & selecting any Warehouse owned or shared with the current site.  Users can also enter a Warehouse ID
When a Warehouse is Entered/Selected, the Printer field should be populated with the Default Printer for the Warehouse  */  
   "WarehouseCode":string,
   "HHForm":boolean,
   "PCIDSGenerated":string,
   "DisableScreen":boolean,
   "Plant":string,
      /**  Disable Warehouse in the PCID Generator screen if true as sometimes we require to pass in and force the warehouse to not be modified,  */  
   "DisableWarehouse":boolean,
   "SuppressPrintLabels":boolean,
   "DisableNumberToGenerate":boolean,
   "StyleNum":number,
   "StyleDescription":string,
   "DisableNumLblsRptStyle":boolean,
   "PkgControlOutboundContainer":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
      @param ipPartNum
      @param warehouseFrozen
   */  
export interface ChangePartNum_input{
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
      /**  The part number.  */  
   ipPartNum:string,
      /**  don't change warehouse if a warehouse is passed in from another UI  */  
   warehouseFrozen:boolean,
}

export interface ChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
}
}

   /** Required : 
      @param ds
      @param ipPkgCode
   */  
export interface ChangePkgCode_input{
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
      /**  Package code.  */  
   ipPkgCode:string,
}

export interface ChangePkgCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
}
}

   /** Required : 
      @param ds
      @param ipPkgControlIDCode
      @param warehouseFrozen
   */  
export interface ChangePkgControlIDCode_input{
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
      /**  The package control ID code.  */  
   ipPkgControlIDCode:string,
      /**  to enable change of warehouse  */  
   warehouseFrozen:boolean,
}

export interface ChangePkgControlIDCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
}
}

   /** Required : 
      @param ds
      @param pkgControlIDType
      @param warehouseFrozen
   */  
export interface ChangePkgControlIDType_input{
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
      /**  package control ID Type.  */  
   pkgControlIDType:string,
      /**  to not change warehouse on the bo side  */  
   warehouseFrozen:boolean,
}

export interface ChangePkgControlIDType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
}
}

   /** Required : 
      @param ipWarehouseCode
      @param ds
   */  
export interface ChangeWarehouseCode_input{
      /**  Warehouse Code.  */  
   ipWarehouseCode:string,
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
}

export interface ChangeWarehouseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
}
}

export interface Erp_Tablesets_PkgControlIDGeneratorListRow{
   NumberToGenerate:number,
   PartDescription:string,
   PkgCode:string,
   PkgCodeDescription:string,
   PkgControlIDCode:string,
   WarehseDesc:string,
   TypeDescription:string,
   PrintName:string,
   Description:string,
   NumberOfLabelsToPrint:number,
   PrinterID:string,
   WarehouseCode:string,
   CheckAllowMixedLots:boolean,
   CheckAllowMixedParts:boolean,
   CheckAllowMixedUOMs:boolean,
   CheckAllowMultipleSerialNumsPerPCID:boolean,
   GenerateStagePCIDs:boolean,
   PartNum:string,
      /**  Package Control Type valid values are Static, Dynamic.  */  
   PkgControlType:string,
   PrintLabels:boolean,
   PCIDSGenerated:string,
   DisableScreen:boolean,
   Plant:string,
   SuppressPrintLabels:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlIDGeneratorListTableset{
   PkgControlIDGeneratorList:Erp_Tablesets_PkgControlIDGeneratorListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PkgControlIDGeneratorRow{
      /**   This field will be like the field on the PCID Generate screen that is called from the Material Queue STK-SHP transaction.  The search button will allow searching & Selecting an Active Package Control ID Configuration having Label Print Controlled = False.
When a value is entered or selected, if the Package Code field is empty then the Package Code field should get populated with the Package Code on the selected control ID configuration  */  
   PkgControlIDCode:string,
      /**  Package code  */  
   PkgCode:string,
      /**  Package code description  */  
   PkgCodeDescription:string,
      /**  Part description  */  
   PartDescription:string,
   WarehseDesc:string,
   NumberToGenerate:number,
   TypeDescription:string,
      /**  Printer name  */  
   PrintName:string,
   Description:string,
   NumberOfLabelsToPrint:number,
   PrinterID:string,
   GenerateStagePCIDs:boolean,
   CheckAllowMixedParts:boolean,
   CheckAllowMixedUOMs:boolean,
   CheckAllowMixedLots:boolean,
   CheckAllowMultipleSerialNumsPerPCID:boolean,
   PrintLabels:boolean,
   PkgControlType:string,
   PartNum:string,
      /**   pulated with all the Warehouses owned or shared with the current site.  The Search will allow searching & selecting any Warehouse owned or shared with the current site.  Users can also enter a Warehouse ID
When a Warehouse is Entered/Selected, the Printer field should be populated with the Default Printer for the Warehouse  */  
   WarehouseCode:string,
   HHForm:boolean,
   PCIDSGenerated:string,
   DisableScreen:boolean,
   Plant:string,
      /**  Disable Warehouse in the PCID Generator screen if true as sometimes we require to pass in and force the warehouse to not be modified,  */  
   DisableWarehouse:boolean,
   SuppressPrintLabels:boolean,
   DisableNumberToGenerate:boolean,
   StyleNum:number,
   StyleDescription:string,
   DisableNumLblsRptStyle:boolean,
   PkgControlOutboundContainer:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlIDGeneratorTableset{
   PkgControlIDGenerator:Erp_Tablesets_PkgControlIDGeneratorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPkgControlIDGeneratorTableset{
   PkgControlIDGenerator:Erp_Tablesets_PkgControlIDGeneratorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param ds2
   */  
export interface GenerateButton_input{
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
      /**  Package control ID generator row.  */  
   ds2:any,      //schema had no properties on an object.
}

export interface GenerateButton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
   pcidsGeneratedMessage:string,
}
}

   /** Required : 
      @param pkgControlIDCode
   */  
export interface GetByID_input{
   pkgControlIDCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PkgControlIDGeneratorTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PkgControlIDGeneratorTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PkgControlIDGeneratorTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  The table name.  */  
   tableName:string,
      /**  The field name.  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
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
   returnObj:Erp_Tablesets_PkgControlIDGeneratorListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param isHHForm
      @param ipPkgControlType
   */  
export interface GetNewPkgControlIDGenerator_input{
      /**  Set to true if invoked from the hand held.  */  
   isHHForm:boolean,
      /**  The package control type.  */  
   ipPkgControlType:string,
}

export interface GetNewPkgControlIDGenerator_output{
   returnObj:Erp_Tablesets_PkgControlIDGeneratorTableset[],
}

   /** Required : 
      @param pkgControlType
      @param pkgControlIDCode
      @param pkgCode
   */  
export interface GetReportStyles_input{
   pkgControlType:string,
   pkgControlIDCode:string,
   pkgCode:string,
}

export interface GetReportStyles_output{
   returnObj:string,
}

   /** Required : 
      @param whereClausePkgControlIDGenerator
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePkgControlIDGenerator:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PkgControlIDGeneratorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPkgControlIDGeneratorTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPkgControlIDGeneratorTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDGeneratorTableset[],
}
}

