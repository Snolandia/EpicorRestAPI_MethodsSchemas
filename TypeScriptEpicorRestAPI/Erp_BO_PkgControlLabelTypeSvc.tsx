import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PkgControlLabelTypeSvc
// Description: 
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get PkgControlLabelTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlLabelTypes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlLabelTypeRow
   */  
export function get_PkgControlLabelTypes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/PkgControlLabelTypes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlLabelTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlLabelTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PkgControlLabelTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PkgControlLabelTypes(requestBody:Erp_Tablesets_PkgControlLabelTypeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/PkgControlLabelTypes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PkgControlLabelType item
   Description: Calls GetByID to retrieve the PkgControlLabelType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlLabelType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param LabelType Desc: LabelType   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PkgControlLabelTypeRow
   */  
export function get_PkgControlLabelTypes_Company_Plant_LabelType_PartNum_CustNum_ShipToNum_PkgCode_PkgControlIDCode(Company:string, Plant:string, LabelType:string, PartNum:string, CustNum:string, ShipToNum:string, PkgCode:string, PkgControlIDCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PkgControlLabelTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/PkgControlLabelTypes(" + Company + "," + Plant + "," + LabelType + "," + PartNum + "," + CustNum + "," + ShipToNum + "," + PkgCode + "," + PkgControlIDCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PkgControlLabelTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PkgControlLabelType for the service
   Description: Calls UpdateExt to update PkgControlLabelType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlLabelType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param LabelType Desc: LabelType   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlLabelTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PkgControlLabelTypes_Company_Plant_LabelType_PartNum_CustNum_ShipToNum_PkgCode_PkgControlIDCode(Company:string, Plant:string, LabelType:string, PartNum:string, CustNum:string, ShipToNum:string, PkgCode:string, PkgControlIDCode:string, requestBody:Erp_Tablesets_PkgControlLabelTypeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/PkgControlLabelTypes(" + Company + "," + Plant + "," + LabelType + "," + PartNum + "," + CustNum + "," + ShipToNum + "," + PkgCode + "," + PkgControlIDCode + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete PkgControlLabelType item
   Description: Call UpdateExt to delete PkgControlLabelType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlLabelType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param LabelType Desc: LabelType   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param PkgControlIDCode Desc: PkgControlIDCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PkgControlLabelTypes_Company_Plant_LabelType_PartNum_CustNum_ShipToNum_PkgCode_PkgControlIDCode(Company:string, Plant:string, LabelType:string, PartNum:string, CustNum:string, ShipToNum:string, PkgCode:string, PkgControlIDCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/PkgControlLabelTypes(" + Company + "," + Plant + "," + LabelType + "," + PartNum + "," + CustNum + "," + ShipToNum + "," + PkgCode + "," + PkgControlIDCode + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlLabelTypeListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelTypeListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelTypeListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePkgControlLabelType:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePkgControlLabelType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePkgControlLabelType=" + whereClausePkgControlLabelType
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

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRows_output)
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
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(plant:string, labelType:string, partNum:string, custNum:string, shipToNum:string, pkgCode:string, pkgControlIDCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof plant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plant=" + plant
   }
   if(typeof labelType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "labelType=" + labelType
   }
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof custNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "custNum=" + custNum
   }
   if(typeof shipToNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "shipToNum=" + shipToNum
   }
   if(typeof pkgCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pkgCode=" + pkgCode
   }
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

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PopulateLabelType
   Description: Parameters:  none
   OperationID: PopulateLabelType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PopulateLabelType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PopulateLabelType(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PopulateLabelType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/PopulateLabelType", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PopulateLabelType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCustomer
   OperationID: ValidateCustomer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCustomer(requestBody:ValidateCustomer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateCustomer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ValidateCustomer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateCustomer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateShipTo
   OperationID: ValidateShipTo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateShipTo(requestBody:ValidateShipTo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateShipTo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ValidateShipTo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateShipTo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePartNum
   OperationID: ValidatePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePartNum(requestBody:ValidatePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ValidatePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidatePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePkgCode
   OperationID: ValidatePkgCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePkgCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePkgCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePkgCode(requestBody:ValidatePkgCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePkgCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ValidatePkgCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidatePkgCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePackageControlIDCode
   OperationID: ValidatePackageControlIDCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePackageControlIDCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePackageControlIDCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePackageControlIDCode(requestBody:ValidatePackageControlIDCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePackageControlIDCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ValidatePackageControlIDCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidatePackageControlIDCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateReportID
   OperationID: ValidateReportID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateReportID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateReportID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateReportID(requestBody:ValidateReportID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateReportID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ValidateReportID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateReportID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangedCustID
   OperationID: ChangedCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangedCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedCustID(requestBody:ChangedCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangedCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ChangedCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangedCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangedLabelType
   Description: Called when the LabelType is changed
   OperationID: ChangedLabelType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangedLabelType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedLabelType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedLabelType(requestBody:ChangedLabelType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangedLabelType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ChangedLabelType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangedLabelType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangedShipToNum
   OperationID: ChangedShipToNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangedShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedShipToNum(requestBody:ChangedShipToNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangedShipToNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ChangedShipToNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangedShipToNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangedPartNum
   OperationID: ChangedPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangedPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedPartNum(requestBody:ChangedPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangedPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ChangedPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangedPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangedReportID
   OperationID: ChangedReportID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangedReportID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedReportID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedReportID(requestBody:ChangedReportID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangedReportID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ChangedReportID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangedReportID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangedStyleNum
   OperationID: ChangedStyleNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangedStyleNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedStyleNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedStyleNum(requestBody:ChangedStyleNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangedStyleNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ChangedStyleNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangedStyleNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangedPkgCode
   OperationID: ChangedPkgCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangedPkgCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedPkgCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedPkgCode(requestBody:ChangedPkgCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangedPkgCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ChangedPkgCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangedPkgCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangedPkgControlIDCode
   OperationID: ChangedPkgControlIDCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangedPkgControlIDCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedPkgControlIDCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedPkgControlIDCode(requestBody:ChangedPkgControlIDCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangedPkgControlIDCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/ChangedPkgControlIDCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangedPkgControlIDCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyLabelTypeBySysRowID
   Description: Returns a copy of the current record
   OperationID: CopyLabelTypeBySysRowID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyLabelTypeBySysRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyLabelTypeBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyLabelTypeBySysRowID(requestBody:CopyLabelTypeBySysRowID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyLabelTypeBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/CopyLabelTypeBySysRowID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CopyLabelTypeBySysRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyLabelType
   Description: KInetic Returns a copy of the current record
   OperationID: CopyLabelType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyLabelType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyLabelType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyLabelType(requestBody:CopyLabelType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyLabelType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/CopyLabelType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CopyLabelType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPkgControlLabelType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControlLabelType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlLabelType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlLabelType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPkgControlLabelType(requestBody:GetNewPkgControlLabelType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPkgControlLabelType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/GetNewPkgControlLabelType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPkgControlLabelType_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowIDs_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Update_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelTypeListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PkgControlLabelTypeListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelTypeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PkgControlLabelTypeRow,
}

export interface Erp_Tablesets_PkgControlLabelTypeListRow{
      /**  Company  */  
   "Company":string,
      /**  Site ID  */  
   "Plant":string,
      /**  Available values are INTERNAL, GENERAL, STATIC, INDIVIDUAL, MASTER, MIXEDMASTER  */  
   "LabelType":string,
      /**  Any valid part for the site selected. This field is optional  */  
   "PartNum":string,
      /**  Any valid customer. This field is optional  */  
   "CustNum":number,
      /**  Any valid ship to for the customer selected. This field is optional.  */  
   "ShipToNum":string,
      /**  Any valid selection from Packing table. This field is optional  */  
   "PkgCode":string,
      /**  Required field. The values comes from PkgControl.PkgControlIDCode field  */  
   "PkgControlIDCode":string,
      /**  Checkbox. The default should be False  */  
   "IsPartDefault":boolean,
      /**  Number Of Labels To Print. Required field, value must be greater than 0  */  
   "NumLabelsToPrint":number,
      /**  Inactive flag  */  
   "Inactive":boolean,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Report ID  */  
   "ReportID":string,
      /**  Report Style Number  */  
   "StyleNum":number,
   "Name":string,
   "CustID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PkgControlLabelTypeRow{
      /**  Company  */  
   "Company":string,
      /**  Site ID  */  
   "Plant":string,
      /**  Available values are INTERNAL, GENERAL, STATIC, INDIVIDUAL, MASTER, MIXEDMASTER  */  
   "LabelType":string,
      /**  Any valid part for the site selected. This field is optional  */  
   "PartNum":string,
      /**  Any valid customer. This field is optional  */  
   "CustNum":number,
      /**  Any valid ship to for the customer selected. This field is optional.  */  
   "ShipToNum":string,
      /**  Any valid selection from Packing table. This field is optional  */  
   "PkgCode":string,
      /**  Required field. The values comes from PkgControl.PkgControlIDCode field  */  
   "PkgControlIDCode":string,
      /**  Checkbox. The default should be False  */  
   "IsPartDefault":boolean,
      /**  Number Of Labels To Print. Required field, value must be greater than 0  */  
   "NumLabelsToPrint":number,
      /**  Inactive flag  */  
   "Inactive":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Report ID  */  
   "ReportID":string,
      /**  Report Style Number  */  
   "StyleNum":number,
      /**  If checked = true during the print routine the system will prompt the user with a dialogue box in which they will be able to pick a different Report Style. This dialogue box should be the standard dialogue we use for the STD application and HH. If this new checkbox is False then the system will use the data it has to print the label.  It will be up to the program calling the routine to notify the user the report was sent.  */  
   "PromptForReportStyle":boolean,
      /**  For Mixed Masters this is the number of distinct Part Qty’s that can be added to a single label  */  
   "MaxPartQtyPerLabel":number,
      /**  Report Description  */  
   "RptDescription":string,
      /**  Location of the Bartender Label file  */  
   "PrintProgram":string,
      /**  Active flag  */  
   "Active":boolean,
   "StyleList":string,
   "StyleDescription":string,
   "BitFlag":number,
   "CustomerBTName":string,
   "CustomerName":string,
   "CustomerCustID":string,
   "PackingDescription":string,
   "PartPartDescription":string,
   "PartPricePerCode":string,
   "PartTrackSerialNum":boolean,
   "PartSellingFactor":number,
   "PartIUM":string,
   "PartSalesUM":string,
   "PartTrackDimension":boolean,
   "PartTrackLots":boolean,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
   */  
export interface ChangedCustID_input{
   ds:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

export interface ChangedCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlLabelTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedLabelType_input{
   ds:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

export interface ChangedLabelType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlLabelTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedPartNum_input{
   ds:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

export interface ChangedPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlLabelTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedPkgCode_input{
   ds:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

export interface ChangedPkgCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlLabelTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedPkgControlIDCode_input{
   ds:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

export interface ChangedPkgControlIDCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlLabelTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedReportID_input{
   ds:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

export interface ChangedReportID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlLabelTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedShipToNum_input{
   ds:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

export interface ChangedShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlLabelTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedStyleNum_input{
   ds:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

export interface ChangedStyleNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlLabelTypeTableset,
}
}

   /** Required : 
      @param originalSysRowID
      @param ds
   */  
export interface CopyLabelTypeBySysRowID_input{
   originalSysRowID:string,
   ds:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

export interface CopyLabelTypeBySysRowID_output{
   returnObj:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

   /** Required : 
      @param originalSysRowID
      @param ds
   */  
export interface CopyLabelType_input{
   originalSysRowID:string,
   ds:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

export interface CopyLabelType_output{
   returnObj:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

   /** Required : 
      @param plant
      @param labelType
      @param partNum
      @param custNum
      @param shipToNum
      @param pkgCode
      @param pkgControlIDCode
   */  
export interface DeleteByID_input{
   plant:string,
   labelType:string,
   partNum:string,
   custNum:number,
   shipToNum:string,
   pkgCode:string,
   pkgControlIDCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PkgControlLabelTypeListRow{
      /**  Company  */  
   Company:string,
      /**  Site ID  */  
   Plant:string,
      /**  Available values are INTERNAL, GENERAL, STATIC, INDIVIDUAL, MASTER, MIXEDMASTER  */  
   LabelType:string,
      /**  Any valid part for the site selected. This field is optional  */  
   PartNum:string,
      /**  Any valid customer. This field is optional  */  
   CustNum:number,
      /**  Any valid ship to for the customer selected. This field is optional.  */  
   ShipToNum:string,
      /**  Any valid selection from Packing table. This field is optional  */  
   PkgCode:string,
      /**  Required field. The values comes from PkgControl.PkgControlIDCode field  */  
   PkgControlIDCode:string,
      /**  Checkbox. The default should be False  */  
   IsPartDefault:boolean,
      /**  Number Of Labels To Print. Required field, value must be greater than 0  */  
   NumLabelsToPrint:number,
      /**  Inactive flag  */  
   Inactive:boolean,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Report ID  */  
   ReportID:string,
      /**  Report Style Number  */  
   StyleNum:number,
   Name:string,
   CustID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlLabelTypeListTableset{
   PkgControlLabelTypeList:Erp_Tablesets_PkgControlLabelTypeListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PkgControlLabelTypeRow{
      /**  Company  */  
   Company:string,
      /**  Site ID  */  
   Plant:string,
      /**  Available values are INTERNAL, GENERAL, STATIC, INDIVIDUAL, MASTER, MIXEDMASTER  */  
   LabelType:string,
      /**  Any valid part for the site selected. This field is optional  */  
   PartNum:string,
      /**  Any valid customer. This field is optional  */  
   CustNum:number,
      /**  Any valid ship to for the customer selected. This field is optional.  */  
   ShipToNum:string,
      /**  Any valid selection from Packing table. This field is optional  */  
   PkgCode:string,
      /**  Required field. The values comes from PkgControl.PkgControlIDCode field  */  
   PkgControlIDCode:string,
      /**  Checkbox. The default should be False  */  
   IsPartDefault:boolean,
      /**  Number Of Labels To Print. Required field, value must be greater than 0  */  
   NumLabelsToPrint:number,
      /**  Inactive flag  */  
   Inactive:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Report ID  */  
   ReportID:string,
      /**  Report Style Number  */  
   StyleNum:number,
      /**  If checked = true during the print routine the system will prompt the user with a dialogue box in which they will be able to pick a different Report Style. This dialogue box should be the standard dialogue we use for the STD application and HH. If this new checkbox is False then the system will use the data it has to print the label.  It will be up to the program calling the routine to notify the user the report was sent.  */  
   PromptForReportStyle:boolean,
      /**  For Mixed Masters this is the number of distinct Part Qty’s that can be added to a single label  */  
   MaxPartQtyPerLabel:number,
      /**  Report Description  */  
   RptDescription:string,
      /**  Location of the Bartender Label file  */  
   PrintProgram:string,
      /**  Active flag  */  
   Active:boolean,
   StyleList:string,
   StyleDescription:string,
   BitFlag:number,
   CustomerBTName:string,
   CustomerName:string,
   CustomerCustID:string,
   PackingDescription:string,
   PartPartDescription:string,
   PartPricePerCode:string,
   PartTrackSerialNum:boolean,
   PartSellingFactor:number,
   PartIUM:string,
   PartSalesUM:string,
   PartTrackDimension:boolean,
   PartTrackLots:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlLabelTypeTableset{
   PkgControlLabelType:Erp_Tablesets_PkgControlLabelTypeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPkgControlLabelTypeTableset{
   PkgControlLabelType:Erp_Tablesets_PkgControlLabelTypeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param plant
      @param labelType
      @param partNum
      @param custNum
      @param shipToNum
      @param pkgCode
      @param pkgControlIDCode
   */  
export interface GetByID_input{
   plant:string,
   labelType:string,
   partNum:string,
   custNum:number,
   shipToNum:string,
   pkgCode:string,
   pkgControlIDCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PkgControlLabelTypeTableset[],
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
   returnObj:Erp_Tablesets_PkgControlLabelTypeListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
      @param labelType
      @param partNum
      @param custNum
      @param shipToNum
      @param pkgCode
   */  
export interface GetNewPkgControlLabelType_input{
   ds:Erp_Tablesets_PkgControlLabelTypeTableset[],
   plant:string,
   labelType:string,
   partNum:string,
   custNum:number,
   shipToNum:string,
   pkgCode:string,
}

export interface GetNewPkgControlLabelType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlLabelTypeTableset,
}
}

   /** Required : 
      @param whereClausePkgControlLabelType
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePkgControlLabelType:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PkgControlLabelTypeTableset[],
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

export interface PopulateLabelType_output{
parameters : {
      /**  output parameters  */  
   valueList:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPkgControlLabelTypeTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPkgControlLabelTypeTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PkgControlLabelTypeTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlLabelTypeTableset,
}
}

   /** Required : 
      @param proposedCustID
   */  
export interface ValidateCustomer_input{
   proposedCustID:string,
}

export interface ValidateCustomer_output{
   returnObj:number,
}

   /** Required : 
      @param proposedPkgControlType
      @param proposedPkgControlIDCode
   */  
export interface ValidatePackageControlIDCode_input{
   proposedPkgControlType:string,
   proposedPkgControlIDCode:string,
}

export interface ValidatePackageControlIDCode_output{
   returnObj:string,
}

   /** Required : 
      @param proposedPartNum
   */  
export interface ValidatePartNum_input{
   proposedPartNum:string,
}

export interface ValidatePartNum_output{
   returnObj:string,
}

   /** Required : 
      @param proposedPkgCode
      @param partNumber
   */  
export interface ValidatePkgCode_input{
   proposedPkgCode:string,
   partNumber:string,
}

export interface ValidatePkgCode_output{
   returnObj:string,
}

   /** Required : 
      @param proposedReportId
   */  
export interface ValidateReportID_input{
   proposedReportId:string,
}

export interface ValidateReportID_output{
}

   /** Required : 
      @param custNum
      @param proposedShipTo
   */  
export interface ValidateShipTo_input{
   custNum:number,
   proposedShipTo:string,
}

export interface ValidateShipTo_output{
   returnObj:string,
}

