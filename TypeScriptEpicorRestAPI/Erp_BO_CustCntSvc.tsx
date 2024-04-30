import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CustCntSvc
// Description: Customer Contact Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/$metadata", {
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
   Description: Get CustCnts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustCnts
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustCntRow
   */  
export function get_CustCnts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustCnts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustCntRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CustCntRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustCnts(requestBody:Erp_Tablesets_CustCntRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts", {
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
   Summary: Calls GetByID to retrieve the CustCnt item
   Description: Calls GetByID to retrieve the CustCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CustCntRow
   */  
export function get_CustCnts_Company_CustNum_ShipToNum_ConNum(Company:string, CustNum:string, ShipToNum:string, ConNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CustCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")", {
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
         resolve(data as Erp_Tablesets_CustCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CustCnt for the service
   Description: Calls UpdateExt to update CustCnt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustCntRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CustCnts_Company_CustNum_ShipToNum_ConNum(Company:string, CustNum:string, ShipToNum:string, ConNum:string, requestBody:Erp_Tablesets_CustCntRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")", {
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
   Summary: Call UpdateExt to delete CustCnt item
   Description: Call UpdateExt to delete CustCnt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CustCnts_Company_CustNum_ShipToNum_ConNum(Company:string, CustNum:string, ShipToNum:string, ConNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get CustCntAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CustCntAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustCntAttchRow
   */  
export function get_CustCnts_Company_CustNum_ShipToNum_ConNum_CustCntAttches(Company:string, CustNum:string, ShipToNum:string, ConNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")/CustCntAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CustCntAttch item
   Description: Calls GetByID to retrieve the CustCntAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustCntAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CustCntAttchRow
   */  
export function get_CustCnts_Company_CustNum_ShipToNum_ConNum_CustCntAttches_Company_CustNum_ShipToNum_ConNum_DrawingSeq(Company:string, CustNum:string, ShipToNum:string, ConNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CustCntAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")/CustCntAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_CustCntAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CustCntAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustCntAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustCntAttchRow
   */  
export function get_CustCntAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCntAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustCntAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustCntAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CustCntAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustCntAttches(requestBody:Erp_Tablesets_CustCntAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCntAttches", {
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
   Summary: Calls GetByID to retrieve the CustCntAttch item
   Description: Calls GetByID to retrieve the CustCntAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustCntAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CustCntAttchRow
   */  
export function get_CustCntAttches_Company_CustNum_ShipToNum_ConNum_DrawingSeq(Company:string, CustNum:string, ShipToNum:string, ConNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CustCntAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCntAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_CustCntAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CustCntAttch for the service
   Description: Calls UpdateExt to update CustCntAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustCntAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustCntAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CustCntAttches_Company_CustNum_ShipToNum_ConNum_DrawingSeq(Company:string, CustNum:string, ShipToNum:string, ConNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_CustCntAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCntAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete CustCntAttch item
   Description: Call UpdateExt to delete CustCntAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustCntAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param ConNum Desc: ConNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CustCntAttches_Company_CustNum_ShipToNum_ConNum_DrawingSeq(Company:string, CustNum:string, ShipToNum:string, ConNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCntAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustCntListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCustCnt:string, whereClauseCustCntAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCustCnt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCustCnt=" + whereClauseCustCnt
   }
   if(typeof whereClauseCustCntAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCustCntAttch=" + whereClauseCustCntAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/GetRows" + params, {
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
   Required: True
   Required: True   Allow empty value : True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(custNum:string, shipToNum:string, conNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
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
   if(typeof conNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "conNum=" + conNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/GetByID" + params, {
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
   Summary: Invoke method GetCustCntGlobalFields
   OperationID: GetCustCntGlobalFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCustCntGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustCntGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustCntGlobalFields(requestBody:GetCustCntGlobalFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCustCntGlobalFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/GetCustCntGlobalFields", {
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
         resolve(data as GetCustCntGlobalFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckEFFieldLength
   Description: This method checks the Customer Name and address fields to see if they conform
to the length allowed in an External Financials integration.  Will return a list of fields
longer than allowed to allow the users to change them or accept that they will be
truncated when sent to External Financials.  Needs to be run right before update.  If the user
answers no to the question then the update method should not be run.
   OperationID: CheckEFFieldLength
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckEFFieldLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEFFieldLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckEFFieldLength(requestBody:CheckEFFieldLength_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckEFFieldLength_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CheckEFFieldLength", {
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
         resolve(data as CheckEFFieldLength_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultName
   Description: This method populates the detail fields from CustCnt.Name when targetName = "Detail".
When targetField = "Name", then the CustCnt.Name is built from the detail fields.
   OperationID: DefaultName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultName(requestBody:DefaultName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/DefaultName", {
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
         resolve(data as DefaultName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGlbCustCntList
   Description: This method returns the GlbCustCnt dataset like GetList() method
GlbCustCnt.CustNum gt 0 indicates linked GlbCustCnt records
GlbCustCnt.CustNum lt = 0 indicates unlinked GlbCustCnt records
   OperationID: GetGlbCustCntList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGlbCustCntList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlbCustCntList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGlbCustCntList(requestBody:GetGlbCustCntList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGlbCustCntList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/GetGlbCustCntList", {
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
         resolve(data as GetGlbCustCntList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshGlbCustCnt
   Description: Refresh GlbCustCnt record after linking
   OperationID: RefreshGlbCustCnt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshGlbCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshGlbCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshGlbCustCnt(requestBody:RefreshGlbCustCnt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshGlbCustCnt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/RefreshGlbCustCnt", {
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
         resolve(data as RefreshGlbCustCnt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SkipGlbCustCnt
   Description: Mark unlinked GlbCustCnt records as skipped
   OperationID: SkipGlbCustCnt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SkipGlbCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SkipGlbCustCnt(requestBody:SkipGlbCustCnt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SkipGlbCustCnt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/SkipGlbCustCnt", {
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
         resolve(data as SkipGlbCustCnt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SkipSingleGlbCustCnt
   Description: Mark a specified GlbCustCnt record as skipped
   OperationID: SkipSingleGlbCustCnt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SkipSingleGlbCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipSingleGlbCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SkipSingleGlbCustCnt(requestBody:SkipSingleGlbCustCnt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SkipSingleGlbCustCnt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/SkipSingleGlbCustCnt", {
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
         resolve(data as SkipSingleGlbCustCnt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPerConData
   OperationID: GetPerConData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPerConData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPerConData(requestBody:GetPerConData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPerConData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/GetPerConData", {
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
         resolve(data as GetPerConData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCustCntForShipTos
   Description: This method returns the CustCnt table populated for specific CustNum and list of ShipToNum
   OperationID: GetCustCntForShipTos
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCustCntForShipTos_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustCntForShipTos_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustCntForShipTos(requestBody:GetCustCntForShipTos_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCustCntForShipTos_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/GetCustCntForShipTos", {
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
         resolve(data as GetCustCntForShipTos_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LinkGlbCustCntRef
   Description: Invokes LinkGlbCustCnt but returns CustCntTableset as ref
   OperationID: LinkGlbCustCntRef
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LinkGlbCustCntRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbCustCntRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LinkGlbCustCntRef(requestBody:LinkGlbCustCntRef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LinkGlbCustCntRef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/LinkGlbCustCntRef", {
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
         resolve(data as LinkGlbCustCntRef_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LinkGlbCustCnt
   Description: This method performs the actual logic behind linking a contact.  It is run after
the PreLinkGlbCustCnt method which determines the Contact to link to.
If the Contact Number is for a Contact that already exists, the GlbCustCnt information is
translated and then copied to the CustCntDataSet as an update.
If the Contact Number is for a new Contact, the GlbCustCnt information is translated and then
copied to the CustCntDataSet as an Add.  Until the update method is run on CustCnt record
the Link process is not completed.
   OperationID: LinkGlbCustCnt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LinkGlbCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LinkGlbCustCnt(requestBody:LinkGlbCustCnt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LinkGlbCustCnt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/LinkGlbCustCnt", {
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
         resolve(data as LinkGlbCustCnt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAltShipToContact
   Description: This sets the ShipTo table based on the MasterCustNum and MasterShipToNum fields.
To be used when the alternate fields change
   OperationID: OnChangeAltShipToContact
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAltShipToContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAltShipToContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAltShipToContact(requestBody:OnChangeAltShipToContact_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAltShipToContact_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/OnChangeAltShipToContact", {
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
         resolve(data as OnChangeAltShipToContact_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCustCntPerConAddress
   Description: This method updates the address fields based on the PerConAddress being changed
   OperationID: OnChangeCustCntPerConAddress
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCustCntPerConAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCustCntPerConAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCustCntPerConAddress(requestBody:OnChangeCustCntPerConAddress_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCustCntPerConAddress_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/OnChangeCustCntPerConAddress", {
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
         resolve(data as OnChangeCustCntPerConAddress_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SpecialAddressChange
   Description: This method clears or sets the Address fields based on the SpecialAddress flag.
If CustCnt.SpecialAddress is checked then the address fields are defaulted from the Customer.
   OperationID: SpecialAddressChange
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SpecialAddressChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpecialAddressChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpecialAddressChange(requestBody:SpecialAddressChange_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SpecialAddressChange_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/SpecialAddressChange", {
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
         resolve(data as SpecialAddressChange_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCustCnt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustCnt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCustCnt(requestBody:GetNewCustCnt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCustCnt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/GetNewCustCnt", {
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
         resolve(data as GetNewCustCnt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCustCntAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustCntAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCustCntAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustCntAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCustCntAttch(requestBody:GetNewCustCntAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCustCntAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/GetNewCustCntAttch", {
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
         resolve(data as GetNewCustCntAttch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CustCntAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CustCntListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CustCntRow,
}

export interface Erp_Tablesets_CustCntAttchRow{
   "Company":string,
   "CustNum":number,
   "ShipToNum":string,
   "ConNum":number,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CustCntListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Customer.CustNum value of the customer that the contact is related to.  */  
   "CustNum":number,
      /**  The ShipTo.ShipToNum of the Ship To that the customer  */  
   "ShipToNum":string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  */  
   "ConNum":number,
      /**  Full name of the contact.  */  
   "Name":string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   "Func":string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   "FaxNum":string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   "PhoneNum":string,
      /**  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  */  
   "SpecialAddress":boolean,
      /**  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  */  
   "Address1":string,
      /**  Line 2 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  */  
   "Address2":string,
      /**  Line 3 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  */  
   "Address3":string,
      /**  The city portion of the contact's mailing address. (See Address1 for additional information).  */  
   "City":string,
      /**  The state or province portion of the contact's mailing address. (See Address1 for additional information).  */  
   "State":string,
      /**  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  */  
   "Zip":string,
      /**  The Country portion of the contact's mailing address. (See Address1 for additional information).  */  
   "Country":string,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   "CorpName":string,
      /**  The contact's email address.  */  
   "EMailAddress":string,
      /**  The Country.CountryNum value of the country selected for the contact's mailing address.  */  
   "CountryNum":number,
      /**  Customer Connect password for this contact.  */  
   "SFPortalPassword":string,
      /**  Indicates if able to create Orders  */  
   "SFUser":boolean,
      /**  Indicates if "Order History" is functional  */  
   "PortalUser":boolean,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   "RoleCode":string,
      /**  The contact's cell phone number.  */  
   "CellPhoneNum":string,
      /**  The contact's pager number.  */  
   "PagerNum":string,
      /**  The contact's Home number.  */  
   "HomeNum":string,
      /**  The contact's alternate phone number.  */  
   "AltNum":string,
      /**  The contact's title.  */  
   "ContactTitle":string,
      /**  The name of the person this contact reports to.  */  
   "ReportsTo":string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   "Comment":string,
      /**  Indicates whether or not this contact should be included in marketing lists.  */  
   "NoContact":boolean,
      /**  The date that the contact was entered into the database.  */  
   "CreateDate":string,
      /**  The UserFile.DCDUserID of the user that entered the contact into the database.  */  
   "CreateDcdUserID":string,
      /**  **NOTE cannot find any code that maintains this field.  */  
   "ChangeDate":string,
      /**  **NOTE cannot find any code that maintains this field.  */  
   "ChangeDcdUserID":string,
      /**  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  */  
   "Inactive":boolean,
      /**  Contact's first name.  */  
   "FirstName":string,
      /**  Contact's middle name.  */  
   "MiddleName":string,
      /**  Contact's last name.  */  
   "LastName":string,
      /**  Contact's prefix.  */  
   "Prefix":string,
      /**  Contact's suffix.  */  
   "Suffix":string,
      /**  Contact's initials.  */  
   "Initials":string,
      /**  External ID  */  
   "ExternalID":string,
      /**  Determines whether or not this record receives global updates  */  
   "GlobalLock":boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   "ShowInputPrice":boolean,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  Pertains to Alternate Shipto. Contains the CustNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   "MasterCustNum":number,
      /**  Pertains to Alternate Shipto. Contains the ShipToNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   "MasterShipToNum":string,
      /**  Pertains to Alternate Shipto. Contains the ConNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   "MasterConNum":number,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   "SyncNameToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   "SyncAddressToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   "SyncPhoneToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   "SyncEmailToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  */  
   "SyncLinksToPerCon":boolean,
      /**  Contact's Website.  */  
   "WebSite":string,
      /**  Contact's IM.  */  
   "IM":string,
      /**  Contact's Twitter.  */  
   "Twitter":string,
      /**  Contact's LinkedIn.  */  
   "LinkedIn":string,
      /**  Contact's FaceBook.  */  
   "FaceBook":string,
      /**  User defined Link 1.  */  
   "WebLink1":string,
      /**  User defined Link 2.  */  
   "WebLink2":string,
      /**  User defined Link 3.  */  
   "WebLink3":string,
      /**  User defined Link 4.  */  
   "WebLink4":string,
      /**  User defined Link 5.  */  
   "WebLink5":string,
      /**  Indicates if the Person/Contact address should be used as the Special Quoting Address.  */  
   "PerConAddress":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "RoleDescription":string,
   "PrimaryBilling":boolean,
   "PrimaryPurchasing":boolean,
   "PrimaryShipping":boolean,
      /**  Indicates if the Contact is global (Master or Linked)  */  
   "GlbFlag":boolean,
      /**  delimited list of CustCnAttr codes  */  
   "AttrCodeList":string,
      /**  GlbCustCnt fields in a linked list to find the linking record  */  
   "GlbLink":string,
      /**  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  */  
   "ContactName":string,
   "PerConName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "MasterCustNumCustID":string,
      /**  The full name of the customer.  */  
   "MasterCustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "MasterCustNumBTName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CustCntRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Customer.CustNum value of the customer that the contact is related to.  */  
   "CustNum":number,
      /**  The ShipTo.ShipToNum of the Ship To that the customer  */  
   "ShipToNum":string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  */  
   "ConNum":number,
      /**  Full name of the contact.  */  
   "Name":string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   "Func":string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   "FaxNum":string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   "PhoneNum":string,
      /**  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  */  
   "SpecialAddress":boolean,
      /**  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  */  
   "Address1":string,
      /**  Line 2 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  */  
   "Address2":string,
      /**  Line 3 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  */  
   "Address3":string,
      /**  The city portion of the contact's mailing address. (See Address1 for additional information).  */  
   "City":string,
      /**  The state or province portion of the contact's mailing address. (See Address1 for additional information).  */  
   "State":string,
      /**  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  */  
   "Zip":string,
      /**  The Country portion of the contact's mailing address. (See Address1 for additional information).  */  
   "Country":string,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   "CorpName":string,
      /**  The contact's email address.  */  
   "EMailAddress":string,
      /**  The Country.CountryNum value of the country selected for the contact's mailing address.  */  
   "CountryNum":number,
      /**  Customer Connect password for this contact.  */  
   "SFPortalPassword":string,
      /**  Indicates if able to create Orders  */  
   "SFUser":boolean,
      /**  Indicates if "Order History" is functional  */  
   "PortalUser":boolean,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   "RoleCode":string,
      /**  The contact's cell phone number.  */  
   "CellPhoneNum":string,
      /**  The contact's pager number.  */  
   "PagerNum":string,
      /**  The contact's Home number.  */  
   "HomeNum":string,
      /**  The contact's alternate phone number.  */  
   "AltNum":string,
      /**  The contact's title.  */  
   "ContactTitle":string,
      /**  The name of the person this contact reports to.  */  
   "ReportsTo":string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   "Comment":string,
      /**  Indicates whether or not this contact should be included in marketing lists.  */  
   "NoContact":boolean,
      /**  The date that the contact was entered into the database.  */  
   "CreateDate":string,
      /**  The UserFile.DCDUserID of the user that entered the contact into the database.  */  
   "CreateDcdUserID":string,
      /**  **NOTE cannot find any code that maintains this field.  */  
   "ChangeDate":string,
      /**  **NOTE cannot find any code that maintains this field.  */  
   "ChangeDcdUserID":string,
      /**  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  */  
   "Inactive":boolean,
      /**  Contact's first name.  */  
   "FirstName":string,
      /**  Contact's middle name.  */  
   "MiddleName":string,
      /**  Contact's last name.  */  
   "LastName":string,
      /**  Contact's prefix.  */  
   "Prefix":string,
      /**  Contact's suffix.  */  
   "Suffix":string,
      /**  Contact's initials.  */  
   "Initials":string,
      /**  External ID  */  
   "ExternalID":string,
      /**  Determines whether or not this record receives global updates  */  
   "GlobalLock":boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   "ShowInputPrice":boolean,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  Pertains to Alternate Shipto. Contains the CustNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   "MasterCustNum":number,
      /**  Pertains to Alternate Shipto. Contains the ShipToNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   "MasterShipToNum":string,
      /**  Pertains to Alternate Shipto. Contains the ConNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   "MasterConNum":number,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   "SyncNameToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   "SyncAddressToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   "SyncPhoneToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   "SyncEmailToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  */  
   "SyncLinksToPerCon":boolean,
      /**  Contact's Website.  */  
   "WebSite":string,
      /**  Contact's IM.  */  
   "IM":string,
      /**  Contact's Twitter.  */  
   "Twitter":string,
      /**  Contact's LinkedIn.  */  
   "LinkedIn":string,
      /**  Contact's FaceBook.  */  
   "FaceBook":string,
      /**  User defined Link 1.  */  
   "WebLink1":string,
      /**  User defined Link 2.  */  
   "WebLink2":string,
      /**  User defined Link 3.  */  
   "WebLink3":string,
      /**  User defined Link 4.  */  
   "WebLink4":string,
      /**  User defined Link 5.  */  
   "WebLink5":string,
      /**  Indicates if the Person/Contact address should be used as the Special Quoting Address.  */  
   "PerConAddress":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  This field defines if the customer contact  is synchronized to an External CRM.  */  
   "SyncToExternalCRM":boolean,
      /**  This field holds the id of this customer in the External CRM  */  
   "ExternalCRMCustomerID":string,
      /**  This field holds the id of this customer contact in the External CRM  */  
   "ExternalCRMContactID":string,
   "RoleDescription":string,
      /**   This check box indicates that this contact is the customer's main billing contact. 
When an AR invoice is created for this customer, this contact's name will automatically appear on the invoice.  */  
   "PrimaryBilling":boolean,
      /**   This check box indicates that this contact is the customer's main purchasing contact. 
When a quote or sales order is created for this customer, this contact's name will automatically appear on the order or quote.  */  
   "PrimaryPurchasing":boolean,
      /**   This check box indicates that this contact is the customer's main shipping contact. 
When a packing slip is created for this customer, this contact's name will automatically appear on the slip.  */  
   "PrimaryShipping":boolean,
      /**  Indicates if the Contact is global (Master or Linked)  */  
   "GlbFlag":boolean,
      /**  delimited list of CustCnAttr codes  */  
   "AttrCodeList":string,
      /**  GlbCustCnt fields in a linked list to find the linking record  */  
   "GlbLink":string,
      /**  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  */  
   "ContactName":string,
   "PerConName":string,
   "BitFlag":number,
   "CustNumName":string,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "MasterCustNumBTName":string,
   "MasterCustNumName":string,
   "MasterCustNumCustID":string,
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
      @param vCustNum
      @param vShipToNum
      @param vConNum
      @param vName
      @param vAddress1
      @param vAddress2
      @param vAddress3
      @param vCity
      @param vState
      @param vCorpName
      @param vFirstName
      @param vMiddleName
      @param vLastName
      @param vInitials
   */  
export interface CheckEFFieldLength_input{
      /**  CustCnt.CustNum  */  
   vCustNum:number,
      /**  CustCnt.ShipToNum  */  
   vShipToNum:string,
      /**  CustCnt.ConNum  */  
   vConNum:number,
      /**  CustCnt.Name  */  
   vName:string,
      /**  CustCnt.Address1  */  
   vAddress1:string,
      /**  CustCnt.Address2  */  
   vAddress2:string,
      /**  CustCnt.Address3  */  
   vAddress3:string,
      /**  CustCnt.City  */  
   vCity:string,
      /**  CustCnt.State  */  
   vState:string,
      /**  CustCnt.CorpName  */  
   vCorpName:string,
      /**  CustCnt.FirstName  */  
   vFirstName:string,
      /**  CustCnt.MiddleName  */  
   vMiddleName:string,
      /**  CustCnt.LastName  */  
   vLastName:string,
      /**  CustCnt.Initials  */  
   vInitials:string,
}

export interface CheckEFFieldLength_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

   /** Required : 
      @param targetField
      @param custNum
      @param shipToNum
      @param conNum
      @param ds
   */  
export interface DefaultName_input{
      /**  Indicates which fields to populate either "Detail" or "Name"  */  
   targetField:string,
      /**  CustCnt.CustNum  */  
   custNum:number,
      /**  CustCnt.ShipToNum  */  
   shipToNum:string,
      /**  CustCnt.ConNum  */  
   conNum:number,
   ds:Erp_Tablesets_CustCntTableset[],
}

export interface DefaultName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustCntTableset,
}
}

   /** Required : 
      @param custNum
      @param shipToNum
      @param conNum
   */  
export interface DeleteByID_input{
   custNum:number,
   shipToNum:string,
   conNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CustCntAttchRow{
   Company:string,
   CustNum:number,
   ShipToNum:string,
   ConNum:number,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CustCntListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Customer.CustNum value of the customer that the contact is related to.  */  
   CustNum:number,
      /**  The ShipTo.ShipToNum of the Ship To that the customer  */  
   ShipToNum:string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  */  
   ConNum:number,
      /**  Full name of the contact.  */  
   Name:string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   Func:string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   FaxNum:string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  */  
   SpecialAddress:boolean,
      /**  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  */  
   Address1:string,
      /**  Line 2 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  */  
   Address2:string,
      /**  Line 3 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  */  
   Address3:string,
      /**  The city portion of the contact's mailing address. (See Address1 for additional information).  */  
   City:string,
      /**  The state or province portion of the contact's mailing address. (See Address1 for additional information).  */  
   State:string,
      /**  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  */  
   Zip:string,
      /**  The Country portion of the contact's mailing address. (See Address1 for additional information).  */  
   Country:string,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   CorpName:string,
      /**  The contact's email address.  */  
   EMailAddress:string,
      /**  The Country.CountryNum value of the country selected for the contact's mailing address.  */  
   CountryNum:number,
      /**  Customer Connect password for this contact.  */  
   SFPortalPassword:string,
      /**  Indicates if able to create Orders  */  
   SFUser:boolean,
      /**  Indicates if "Order History" is functional  */  
   PortalUser:boolean,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   RoleCode:string,
      /**  The contact's cell phone number.  */  
   CellPhoneNum:string,
      /**  The contact's pager number.  */  
   PagerNum:string,
      /**  The contact's Home number.  */  
   HomeNum:string,
      /**  The contact's alternate phone number.  */  
   AltNum:string,
      /**  The contact's title.  */  
   ContactTitle:string,
      /**  The name of the person this contact reports to.  */  
   ReportsTo:string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   Comment:string,
      /**  Indicates whether or not this contact should be included in marketing lists.  */  
   NoContact:boolean,
      /**  The date that the contact was entered into the database.  */  
   CreateDate:string,
      /**  The UserFile.DCDUserID of the user that entered the contact into the database.  */  
   CreateDcdUserID:string,
      /**  **NOTE cannot find any code that maintains this field.  */  
   ChangeDate:string,
      /**  **NOTE cannot find any code that maintains this field.  */  
   ChangeDcdUserID:string,
      /**  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  */  
   Inactive:boolean,
      /**  Contact's first name.  */  
   FirstName:string,
      /**  Contact's middle name.  */  
   MiddleName:string,
      /**  Contact's last name.  */  
   LastName:string,
      /**  Contact's prefix.  */  
   Prefix:string,
      /**  Contact's suffix.  */  
   Suffix:string,
      /**  Contact's initials.  */  
   Initials:string,
      /**  External ID  */  
   ExternalID:string,
      /**  Determines whether or not this record receives global updates  */  
   GlobalLock:boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   ShowInputPrice:boolean,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  Pertains to Alternate Shipto. Contains the CustNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterCustNum:number,
      /**  Pertains to Alternate Shipto. Contains the ShipToNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterShipToNum:string,
      /**  Pertains to Alternate Shipto. Contains the ConNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterConNum:number,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   SyncNameToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   SyncAddressToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   SyncPhoneToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   SyncEmailToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  */  
   SyncLinksToPerCon:boolean,
      /**  Contact's Website.  */  
   WebSite:string,
      /**  Contact's IM.  */  
   IM:string,
      /**  Contact's Twitter.  */  
   Twitter:string,
      /**  Contact's LinkedIn.  */  
   LinkedIn:string,
      /**  Contact's FaceBook.  */  
   FaceBook:string,
      /**  User defined Link 1.  */  
   WebLink1:string,
      /**  User defined Link 2.  */  
   WebLink2:string,
      /**  User defined Link 3.  */  
   WebLink3:string,
      /**  User defined Link 4.  */  
   WebLink4:string,
      /**  User defined Link 5.  */  
   WebLink5:string,
      /**  Indicates if the Person/Contact address should be used as the Special Quoting Address.  */  
   PerConAddress:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   RoleDescription:string,
   PrimaryBilling:boolean,
   PrimaryPurchasing:boolean,
   PrimaryShipping:boolean,
      /**  Indicates if the Contact is global (Master or Linked)  */  
   GlbFlag:boolean,
      /**  delimited list of CustCnAttr codes  */  
   AttrCodeList:string,
      /**  GlbCustCnt fields in a linked list to find the linking record  */  
   GlbLink:string,
      /**  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  */  
   ContactName:string,
   PerConName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   MasterCustNumCustID:string,
      /**  The full name of the customer.  */  
   MasterCustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   MasterCustNumBTName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CustCntListTableset{
   CustCntList:Erp_Tablesets_CustCntListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CustCntRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Customer.CustNum value of the customer that the contact is related to.  */  
   CustNum:number,
      /**  The ShipTo.ShipToNum of the Ship To that the customer  */  
   ShipToNum:string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  */  
   ConNum:number,
      /**  Full name of the contact.  */  
   Name:string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   Func:string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   FaxNum:string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  */  
   SpecialAddress:boolean,
      /**  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  */  
   Address1:string,
      /**  Line 2 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  */  
   Address2:string,
      /**  Line 3 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  */  
   Address3:string,
      /**  The city portion of the contact's mailing address. (See Address1 for additional information).  */  
   City:string,
      /**  The state or province portion of the contact's mailing address. (See Address1 for additional information).  */  
   State:string,
      /**  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  */  
   Zip:string,
      /**  The Country portion of the contact's mailing address. (See Address1 for additional information).  */  
   Country:string,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   CorpName:string,
      /**  The contact's email address.  */  
   EMailAddress:string,
      /**  The Country.CountryNum value of the country selected for the contact's mailing address.  */  
   CountryNum:number,
      /**  Customer Connect password for this contact.  */  
   SFPortalPassword:string,
      /**  Indicates if able to create Orders  */  
   SFUser:boolean,
      /**  Indicates if "Order History" is functional  */  
   PortalUser:boolean,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   RoleCode:string,
      /**  The contact's cell phone number.  */  
   CellPhoneNum:string,
      /**  The contact's pager number.  */  
   PagerNum:string,
      /**  The contact's Home number.  */  
   HomeNum:string,
      /**  The contact's alternate phone number.  */  
   AltNum:string,
      /**  The contact's title.  */  
   ContactTitle:string,
      /**  The name of the person this contact reports to.  */  
   ReportsTo:string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   Comment:string,
      /**  Indicates whether or not this contact should be included in marketing lists.  */  
   NoContact:boolean,
      /**  The date that the contact was entered into the database.  */  
   CreateDate:string,
      /**  The UserFile.DCDUserID of the user that entered the contact into the database.  */  
   CreateDcdUserID:string,
      /**  **NOTE cannot find any code that maintains this field.  */  
   ChangeDate:string,
      /**  **NOTE cannot find any code that maintains this field.  */  
   ChangeDcdUserID:string,
      /**  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  */  
   Inactive:boolean,
      /**  Contact's first name.  */  
   FirstName:string,
      /**  Contact's middle name.  */  
   MiddleName:string,
      /**  Contact's last name.  */  
   LastName:string,
      /**  Contact's prefix.  */  
   Prefix:string,
      /**  Contact's suffix.  */  
   Suffix:string,
      /**  Contact's initials.  */  
   Initials:string,
      /**  External ID  */  
   ExternalID:string,
      /**  Determines whether or not this record receives global updates  */  
   GlobalLock:boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   ShowInputPrice:boolean,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  Pertains to Alternate Shipto. Contains the CustNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterCustNum:number,
      /**  Pertains to Alternate Shipto. Contains the ShipToNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterShipToNum:string,
      /**  Pertains to Alternate Shipto. Contains the ConNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterConNum:number,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   SyncNameToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   SyncAddressToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   SyncPhoneToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   SyncEmailToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  */  
   SyncLinksToPerCon:boolean,
      /**  Contact's Website.  */  
   WebSite:string,
      /**  Contact's IM.  */  
   IM:string,
      /**  Contact's Twitter.  */  
   Twitter:string,
      /**  Contact's LinkedIn.  */  
   LinkedIn:string,
      /**  Contact's FaceBook.  */  
   FaceBook:string,
      /**  User defined Link 1.  */  
   WebLink1:string,
      /**  User defined Link 2.  */  
   WebLink2:string,
      /**  User defined Link 3.  */  
   WebLink3:string,
      /**  User defined Link 4.  */  
   WebLink4:string,
      /**  User defined Link 5.  */  
   WebLink5:string,
      /**  Indicates if the Person/Contact address should be used as the Special Quoting Address.  */  
   PerConAddress:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This field defines if the customer contact  is synchronized to an External CRM.  */  
   SyncToExternalCRM:boolean,
      /**  This field holds the id of this customer in the External CRM  */  
   ExternalCRMCustomerID:string,
      /**  This field holds the id of this customer contact in the External CRM  */  
   ExternalCRMContactID:string,
   RoleDescription:string,
      /**   This check box indicates that this contact is the customer's main billing contact. 
When an AR invoice is created for this customer, this contact's name will automatically appear on the invoice.  */  
   PrimaryBilling:boolean,
      /**   This check box indicates that this contact is the customer's main purchasing contact. 
When a quote or sales order is created for this customer, this contact's name will automatically appear on the order or quote.  */  
   PrimaryPurchasing:boolean,
      /**   This check box indicates that this contact is the customer's main shipping contact. 
When a packing slip is created for this customer, this contact's name will automatically appear on the slip.  */  
   PrimaryShipping:boolean,
      /**  Indicates if the Contact is global (Master or Linked)  */  
   GlbFlag:boolean,
      /**  delimited list of CustCnAttr codes  */  
   AttrCodeList:string,
      /**  GlbCustCnt fields in a linked list to find the linking record  */  
   GlbLink:string,
      /**  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  */  
   ContactName:string,
   PerConName:string,
   BitFlag:number,
   CustNumName:string,
   CustNumBTName:string,
   CustNumCustID:string,
   MasterCustNumBTName:string,
   MasterCustNumName:string,
   MasterCustNumCustID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CustCntTableset{
   CustCnt:Erp_Tablesets_CustCntRow[],
   CustCntAttch:Erp_Tablesets_CustCntAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlbCustCntRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique internal number assigned to the customer for which the contact is related to.  */  
   CustNum:number,
      /**  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  */  
   ShipToNum:string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  */  
   ConNum:number,
      /**  Name of contact.  */  
   Name:string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   Func:string,
      /**  Specific Fax telephone number for the contact. Optional field.  When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   FaxNum:string,
      /**  Specific Business telephone number for the contact. Optional field.  When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  */  
   SpecialAddress:boolean,
      /**  Contacts mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  */  
   Address1:string,
      /**  see Address1.  */  
   Address2:string,
      /**  See Address 1  */  
   Address3:string,
      /**  see address1  */  
   City:string,
      /**  Special State ID. ( See Address1 )  Can be blank.  */  
   State:string,
      /**  Special Zip (see Address1 )  */  
   Zip:string,
      /**  Special Country is used as part of the mailing address. It can be left blank. ( See Address1 )  */  
   Country:string,
      /**  Contacts mailing address company name if different than that of the customer.  */  
   CorpName:string,
      /**  Email address of contact person.  */  
   EMailAddress:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Password for SF/Portal, should not be easily editable from the Manufacturing System.  */  
   SFPortalPassword:string,
      /**  Indicates if able to create Orders  */  
   SFUser:boolean,
      /**  Indicates if "Order History" is functional  */  
   PortalUser:boolean,
      /**  Code that identifies the role of this person. Link to the RoleCD table.  */  
   RoleCode:string,
      /**  The contacts Cell phone number.  */  
   CellPhoneNum:string,
      /**  The contacts Pager number.  */  
   PagerNum:string,
      /**  The contacts Home number.  */  
   HomeNum:string,
      /**  The contacts Alternate number.  */  
   AltNum:string,
      /**  The Contacts Title  */  
   ContactTitle:string,
      /**  The name if the person this contact reports to.  */  
   ReportsTo:string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   Comment:string,
      /**  Indicates that this contact is not included in marketing lists  */  
   NoContact:boolean,
      /**  The date the task was created.  */  
   CreateDate:string,
      /**  The UserID that created the task  */  
   CreateDcdUserID:string,
      /**  The date the task was last changed.  */  
   ChangeDate:string,
      /**  The UserID that last changed the task  */  
   ChangeDcdUserID:string,
      /**  This contact does not get used on new LOQs  */  
   Inactive:boolean,
      /**  First Name  */  
   FirstName:string,
      /**  Middle Name  */  
   MiddleName:string,
      /**  Last Name  */  
   LastName:string,
      /**  Prefix  */  
   Prefix:string,
      /**  Suffix  */  
   Suffix:string,
      /**  Initials  */  
   Initials:string,
      /**  External ID  */  
   ExternalID:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the owner company  */  
   GlbCustNum:number,
      /**  Owner Company Identifier.  */  
   GlbCompany:string,
      /**  Global ShipToNumber.  This is the number in the parent company  */  
   GlbShipToNum:string,
      /**  This is the Contact Number of the parent company  */  
   GlbConNum:number,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   OldCompany:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  */  
   OldCustNum:number,
      /**  Original ShipToNumber.  This is the number in the original owner's parent company - NOT CURRENTLY IN USE  */  
   OldShipToNum:string,
      /**  This is the Contact Number of the original parent company - CURRENTLY NOT IN USE  */  
   OldConNum:number,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   ShowInputPrice:boolean,
      /**  Indicates if the user chose to skip this record when linking global customer contacts.  The user can come back at a later time and choose to link a skipped customer contact if they need to.  */  
   Skipped:boolean,
   ChangedBy:string,
   ChangeTime:number,
   MasterConNum:number,
   MasterCustNum:number,
   MasterShipToNum:string,
   FaceBook:string,
   IM:string,
   LinkedIn:string,
   PerConID:number,
   SyncAddressToPerCon:boolean,
   SyncEmailToPerCon:boolean,
   SyncLinksToPerCon:boolean,
   SyncNameToPerCon:boolean,
   SyncPhoneToPerCon:boolean,
   Twitter:string,
   WebLink1:string,
   WebLink2:string,
   WebLink3:string,
   WebLink4:string,
   WebLink5:string,
   WebSite:string,
   PerConAddress:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SyncToExternalCRM  */  
   SyncToExternalCRM:boolean,
      /**  ExternalCRMCustomerID  */  
   ExternalCRMCustomerID:string,
      /**  ExternalCRMContactID  */  
   ExternalCRMContactID:string,
      /**  Local Contact Number to Link to  */  
   LinkConNum:number,
   RoleDescription:string,
      /**  Indicates if the record is linked  */  
   IsLinked:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCustCntTableset{
   GlbCustCnt:Erp_Tablesets_GlbCustCntRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCustCntTableset{
   CustCnt:Erp_Tablesets_CustCntRow[],
   CustCntAttch:Erp_Tablesets_CustCntAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param custNum
      @param shipToNum
      @param conNum
   */  
export interface GetByID_input{
   custNum:number,
   shipToNum:string,
   conNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CustCntTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CustCntTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CustCntTableset[],
}

   /** Required : 
      @param company
      @param custNum
      @param shipToNumList
   */  
export interface GetCustCntForShipTos_input{
      /**  Company to return records for  */  
   company:string,
      /**  Customer Number to return records for  */  
   custNum:number,
      /**  List of ShipToNum's to return records for  */  
   shipToNumList:string,
}

export interface GetCustCntForShipTos_output{
   returnObj:Erp_Tablesets_CustCntTableset[],
}

   /** Required : 
      @param CustNum
      @param ShiptoNum
      @param ConNum
   */  
export interface GetCustCntGlobalFields_input{
   CustNum:number,
   ShiptoNum:string,
   ConNum:number,
}

export interface GetCustCntGlobalFields_output{
   returnObj:string,
}

   /** Required : 
      @param inCompany
      @param inGlbCompany
      @param inGlbCustNum
      @param pageSize
      @param absolutePage
   */  
export interface GetGlbCustCntList_input{
      /**  Company to return records for  */  
   inCompany:string,
      /**  Global Company to return records for  */  
   inGlbCompany:string,
      /**  Global Customer to return records for  */  
   inGlbCustNum:number,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetGlbCustCntList_output{
   returnObj:Erp_Tablesets_GlbCustCntTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
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
   returnObj:Erp_Tablesets_CustCntListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param custNum
      @param shipToNum
      @param conNum
   */  
export interface GetNewCustCntAttch_input{
   ds:Erp_Tablesets_CustCntTableset[],
   custNum:number,
   shipToNum:string,
   conNum:number,
}

export interface GetNewCustCntAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustCntTableset,
}
}

   /** Required : 
      @param ds
      @param custNum
      @param shipToNum
   */  
export interface GetNewCustCnt_input{
   ds:Erp_Tablesets_CustCntTableset[],
   custNum:number,
   shipToNum:string,
}

export interface GetNewCustCnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustCntTableset,
}
}

   /** Required : 
      @param PerConID
      @param ds
   */  
export interface GetPerConData_input{
   PerConID:number,
   ds:Erp_Tablesets_CustCntTableset[],
}

export interface GetPerConData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustCntTableset,
}
}

   /** Required : 
      @param whereClauseCustCnt
      @param whereClauseCustCntAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCustCnt:string,
   whereClauseCustCntAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CustCntTableset[],
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
      @param glbCompany
      @param glbCustNum
      @param glbShipToNum
      @param glbConNum
      @param ds
      @param dsCustCnt
   */  
export interface LinkGlbCustCntRef_input{
   glbCompany:string,
   glbCustNum:number,
   glbShipToNum:string,
   glbConNum:number,
   ds:Erp_Tablesets_GlbCustCntTableset[],
   dsCustCnt:Erp_Tablesets_CustCntTableset[],
}

export interface LinkGlbCustCntRef_output{
parameters : {
      /**  output parameters  */  
   dsCustCnt:Erp_Tablesets_CustCntTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbCustNum
      @param glbShipToNum
      @param glbConNum
      @param ds
   */  
export interface LinkGlbCustCnt_input{
      /**  Global Company field on the GlbCustCnt record to link  */  
   glbCompany:string,
      /**  Global CustNum field on the GlbCustCnt record to link  */  
   glbCustNum:number,
      /**  Global ShipToNum field on the GlbCustCnt record to link  */  
   glbShipToNum:string,
      /**  Global ConNum field on the GlbCustCnt record to link  */  
   glbConNum:number,
   ds:Erp_Tablesets_GlbCustCntTableset[],
}

export interface LinkGlbCustCnt_output{
   returnObj:Erp_Tablesets_CustCntTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCustCntTableset,
}
}

   /** Required : 
      @param iProposedMasterCustID
      @param iProposedMasterShipToNum
      @param iProposedMasterConNum
      @param ds
   */  
export interface OnChangeAltShipToContact_input{
      /**  The proposed CustID value  */  
   iProposedMasterCustID:string,
      /**  The proposed ShipTo Num value  */  
   iProposedMasterShipToNum:string,
      /**  The proposed Contact number value  */  
   iProposedMasterConNum:number,
   ds:Erp_Tablesets_CustCntTableset[],
}

export interface OnChangeAltShipToContact_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustCntTableset,
}
}

   /** Required : 
      @param conNum
      @param proposedPerConAddress
      @param ds
   */  
export interface OnChangeCustCntPerConAddress_input{
   conNum:number,
   proposedPerConAddress:boolean,
   ds:Erp_Tablesets_CustCntTableset[],
}

export interface OnChangeCustCntPerConAddress_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustCntTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbCustNum
      @param glbShipToNum
      @param glbConNum
      @param ds
   */  
export interface RefreshGlbCustCnt_input{
      /**  Global Company  */  
   glbCompany:string,
      /**  Global Customer Number  */  
   glbCustNum:number,
      /**  Global Ship To Number  */  
   glbShipToNum:string,
      /**  Global Contact Number  */  
   glbConNum:number,
   ds:Erp_Tablesets_GlbCustCntTableset[],
}

export interface RefreshGlbCustCnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCustCntTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbCustNum
      @param glbShipToNum
      @param ds
   */  
export interface SkipGlbCustCnt_input{
      /**  Global Company  */  
   glbCompany:string,
      /**  Global Customer Number  */  
   glbCustNum:number,
      /**  Global Ship To Number  */  
   glbShipToNum:string,
   ds:Erp_Tablesets_GlbCustCntTableset[],
}

export interface SkipGlbCustCnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCustCntTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbCustNum
      @param glbShipToNum
      @param glbConNum
      @param ds
   */  
export interface SkipSingleGlbCustCnt_input{
      /**  Global Company  */  
   glbCompany:string,
      /**  Global Customer Number  */  
   glbCustNum:number,
      /**  Global Ship To Number  */  
   glbShipToNum:string,
      /**  Global Contact Number  */  
   glbConNum:number,
   ds:Erp_Tablesets_GlbCustCntTableset[],
}

export interface SkipSingleGlbCustCnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCustCntTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface SpecialAddressChange_input{
   ds:Erp_Tablesets_CustCntTableset[],
}

export interface SpecialAddressChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustCntTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCustCntTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCustCntTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CustCntTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustCntTableset,
}
}

