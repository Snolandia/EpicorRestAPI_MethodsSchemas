import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ContactSvc
// Description: The contact service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/$metadata", {
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
   Summary: Calls GetByID to retrieve the Contact item
   Description: Calls GetByID to retrieve the Contact item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Contact
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContactName Desc: ContactName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContactRow
   */  
export function get_Contacts_Company_ContactName(Company:string, ContactName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContactRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/Contacts(" + Company + "," + ContactName + ")", {
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
         resolve(data as Erp_Tablesets_ContactRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ContactCustomer item
   Description: Calls GetByID to retrieve the ContactCustomer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContactCustomer1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContactName Desc: ContactName   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContactCustomerRow
   */  
export function get_Contacts_Company_ContactName_ContactCustomers_Company_CustNum(Company:string, ContactName:string, CustNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContactCustomerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/Contacts(" + Company + "," + ContactName + ")/ContactCustomers(" + Company + "," + CustNum + ")", {
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
         resolve(data as Erp_Tablesets_ContactCustomerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ContactCustomer item
   Description: Calls GetByID to retrieve the ContactCustomer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContactCustomer
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContactCustomerRow
   */  
export function get_ContactCustomers_Company_CustNum(Company:string, CustNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContactCustomerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/ContactCustomers(" + Company + "," + CustNum + ")", {
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
         resolve(data as Erp_Tablesets_ContactCustomerRow)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")/CustCntAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + DrawingSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/CustCntAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + DrawingSeq + ")", {
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
   Summary: Calls GetByID to retrieve the ShipTo item
   Description: Calls GetByID to retrieve the ShipTo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipTo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ShipToRow
   */  
export function get_ShipToes_Company_CustNum_ShipToNum(Company:string, CustNum:string, ShipToNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipToRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")", {
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
         resolve(data as Erp_Tablesets_ShipToRow)
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContactListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContactListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContactListRow)
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
   Summary: Invoke method GetByID
   Description: Get customers, ship to's and contacts by Contact Name.
   OperationID: Get_GetByID
      @param ContactName Desc: The Contact Name   Required: True   Allow empty value : True
      @param CustNumList Desc: Delimited list of customer numbers selected   Required: True   Allow empty value : True
      @param inCustNum Desc: Specific Customer number.  Used for context menu   Required: True
      @param inShipToNum Desc: Specific ShipTo Number.  Used for context menu   Required: True   Allow empty value : True
      @param inConNum Desc: Specific Contact Number.  Used for context menu   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(ContactName:string, CustNumList:string, inCustNum:string, inShipToNum:string, inConNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ContactName!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ContactName=" + ContactName
   }
   if(typeof CustNumList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "CustNumList=" + CustNumList
   }
   if(typeof inCustNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "inCustNum=" + inCustNum
   }
   if(typeof inShipToNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "inShipToNum=" + inShipToNum
   }
   if(typeof inConNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "inConNum=" + inConNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/GetByID" + params, {
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
   Description: List of contacts.
   OperationID: Get_GetList
      @param whereClause Desc: Where condition   Required: True   Allow empty value : True
      @param pageSize Desc: # of records returned.  0 means all   Required: True
   Required: True
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/GetList" + params, {
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
   Summary: Invoke method CondenseContactList
   Description: Condenses the list of contacts.
   OperationID: CondenseContactList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CondenseContactList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CondenseContactList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CondenseContactList(requestBody:CondenseContactList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CondenseContactList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/CondenseContactList", {
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
         resolve(data as CondenseContactList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListCustom
   Description: List of contacts.
   OperationID: GetListCustom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCustom(requestBody:GetListCustom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListCustom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/GetListCustom", {
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
         resolve(data as GetListCustom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCustCntAttch
   Description: Empty method so the adapter will add the attachment logic for CustCnt.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/GetNewCustCntAttch", {
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
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:GetCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/GetCodeDescList", {
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
         resolve(data as GetCodeDescList_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContactListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContactListRow,
}

export interface Erp_Tablesets_ContactCustomerRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustID":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   "CustNum":number,
      /**  The full name of the customer.  */  
   "Name":string,
      /**  The first line of the customer's main address.  */  
   "Address1":string,
      /**  The second line of the customer's main address.  */  
   "Address2":string,
      /**  The third line of the customer's main address.  */  
   "Address3":string,
      /**  The city portion of the customer's main address.  */  
   "City":string,
      /**  The state or province portion of the customer's main address.  */  
   "State":string,
      /**  The zip or postal code portion of the customer's main address.  */  
   "Zip":string,
      /**  The country of the main customer address.  */  
   "Country":string,
      /**  Optional field used to record the customer's State Tax Identification number, which is displayed on Sales Acknowledgments.  */  
   "ResaleID":string,
      /**  The SalesRep.SalesRepCode of the default salesperson for the customer. This field is used to supply defaults to Order Entry and Invoice entry for invoices that do not reference a sales orders.  */  
   "SalesRepCode":string,
      /**  The SalesTer.TerritoryID value of the territory assigned to the customer.  */  
   "TerritoryID":string,
      /**  Contains the key of the default ship to for the customer. A blank value indicates that the name and address in the Customer file is considered the default ship to. This field is updated when the user marks the check box in ship to maintenance indicating that the ship to is to be designated as the default. This default will be used in areas such as Sales Order entry.  */  
   "ShipToNum":string,
      /**   The Terms.TermsCode value of the default sales terms associated with the customer. A default may be supplied by XaSyst.TermsCode if not blank. The terms will default into quotes and orders for this customer.
For invoices not related to a sales order, these terms will also default into the invoice.  */  
   "TermsCode":string,
      /**  Contains the ShipVia.ShipViaCode value of the default ShipVia for the customer.  */  
   "ShipViaCode":string,
      /**  Controls whether or not this customer's statement will print when   printing of customer statements.  */  
   "PrintStatements":boolean,
      /**  Only customers that are PrintLabels = Yes will be selected for printing of mailing labels.  */  
   "PrintLabels":boolean,
      /**   Allows the user to establish whether or not a specific customer requires Sales Order Acknowledgements.  This does not force or limit the printing of sales acknowledgments directly from within Order Entry.  Order entry displays this setting to the user so that they know if they should print the acknowledgment.
For batch mode printing, (where ranges of sales orders are selected...future release) this setting will be used to exclude orders from printing.  */  
   "PrintAck":boolean,
      /**  Controls whether or not the customer will be included in the finance charge calculation process.  */  
   "FinCharges":boolean,
      /**  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  */  
   "CreditHold":boolean,
      /**  Contains the CustGrup.GroupCode value of the customer group that the customer has been assigned to. This field is used by the application for sorting or filtering on reports and can also be associated with price lists.  */  
   "GroupCode":string,
      /**  An optional field used to establish a default purchasing discount percentage for any order placed by customer. This value is supplied to order entry as a default for line item discount percent.  */  
   "DiscountPercent":number,
      /**  Contains the CustCnt.ConNum value of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Order Entry and Quoting.  */  
   "PrimPCon":number,
      /**  The same as the PrimPCon except that this is the Primary Billing Contact and this is used as a default in invoice entry.  */  
   "PrimBCon":number,
      /**  Same as PrimPCon except that this the Primary Shipping Contact and is used as a default in Packing Slip entry.  */  
   "PrimSCon":number,
      /**   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   "Comment":string,
      /**  The date when the customer was established as a customer. Use the system date as a default when creating new customers.  */  
   "EstDate":string,
      /**  The Fax Number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  */  
   "FaxNum":string,
      /**  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  */  
   "PhoneNum":string,
      /**  Indicates the reason why the customer is normally exempt from sales tax. Used as a default in invoice entry.  If field is non-blank it is considered exempt.  */  
   "TaxExempt":string,
      /**  The QMarkup.MarkupID value of the quote markup table which will be used to provide default markup percents in quote entry for this customer. If left blank the quote module will use the default quote markup table for the customer. (See EQSyst.MarkupID).  */  
   "MarkUpID":string,
      /**   Represents the day of the week or month that this customer is invoiced on. The possible choices are determined by the Customer.Bill-Frequency field value.

When the Bill-Frequency is "W" (Weeky):
The valid values are 0-7 where 0=All Days,1=Sun,2=Mon,...,7=Sat.  

ll-frequency is 'M' (Monthly) this field contains the 1st -> 31st as possible choices to represent the day of the month to bill on.  */  
   "BillDay":number,
      /**  Determines whether or not packing slips for the same Sales Order and Fiscal Period will combined into a single invoice or not. If the packing slips are for different sales orders for the customer or fall in different fiscal periods, seperate invoices will be created even when this field is set to Yes.  */  
   "OneInvPerPS":boolean,
      /**  Contains the default FOB.FOB value of the FOB policy for this  customers orders.  Default used in sales order entry for this customer.  */  
   "DefaultFOB":string,
      /**  Determines whether or not Open Sales Orders are to be included in the credit limit checking process for the customer. This checkbox will also include open service contracts.  */  
   "CreditIncludeOrders":boolean,
      /**  Date on which the next credit review should be conducted for the customer.  */  
   "CreditReviewDate":string,
      /**  Date on which the customer was last placed on credit hold. This field is maintained by the system.  */  
   "CreditHoldDate":string,
      /**  Indicates how the customer was placed on credit hold.  Valid values are "MANUAL", "INVOICES", "ORDERS","CONTRACTS".  "MANUAL" means that the user placed the customer on hold.  INVOICES means that the customer’s open A/R balance exceeded the credit limit.  ORDERS means that the sum of the open A/R and the open orders exceeded the credit limit. This field is maintained by the system.  */  
   "CreditHoldSource":string,
      /**  The UserFile.DCDUSERID value of the user that last cleared the customer’s credit hold. This field is maintained by the system.  */  
   "CreditClearUserID":string,
      /**  The date that the user last cleared the customer’s credit hold. This field is maintained by the system.  */  
   "CreditClearDate":string,
      /**  The time that the user last cleared the customer’s credit hold in HH:MM:SS format. This field is maintained by the system.  */  
   "CreditClearTime":string,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   "EDICode":string,
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Character05":string,
   "Character06":string,
   "Character07":string,
   "Character08":string,
   "Character09":string,
   "Character10":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
      /**  Contains the Currency.CurrencyCode value of the customer's base currency.  */  
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "Date04":string,
   "Date05":string,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
   "CheckBox05":boolean,
      /**  Contains the Currency.CurrencyCode value of the customer's base currency.  */  
   "CurrencyCode":string,
      /**  Contains the Country.CountryNum value of the country the customer is located in.  */  
   "CountryNum":number,
      /**  Contains the LangName.LangNameID value of the customer's language. This controls which language will be selected when extracting part descriptions from PartLangDesc table and report labels for customer related forms such as orders, packing slips and invoices.  */  
   "LangNameID":string,
      /**  Area/City code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set to yes.  */  
   "BorderCrossing":string,
      /**  Optional custom address format used to format the customer's main address.  */  
   "FormatStr":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "BTName":string,
      /**  The first line of the customer's Bill To address.  */  
   "BTAddress1":string,
      /**  The second line of the customer's Bill To address.  */  
   "BTAddress2":string,
      /**  The second line of the customer's Bill To address.  */  
   "BTAddress3":string,
      /**  The city portion of the customer's Bill To address.  */  
   "BTCity":string,
      /**  The state or province portion of the customer's Bill To address.  */  
   "BTState":string,
      /**  The zip or postal code portion of the customer's Bill To address.  */  
   "BTZip":string,
      /**  The Country.Countrynum value of the Country portion of the customer's Bill To address.  */  
   "BTCountryNum":number,
      /**  Contains the Country.Description value of the Country portion of the customer's Bill To address.  */  
   "BTCountry":string,
      /**  The phone number related to the customer's Bill To Address.  */  
   "BTPhoneNum":string,
      /**  The fax number of the customer's Bill To address.  */  
   "BTFaxNum":string,
      /**  Optional custom address format used to format the customer's Bill To address.  */  
   "BTFormatStr":string,
      /**  The Customer.CustNum value of the customer's parent company.  */  
   "ParentCustNum":number,
      /**  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  */  
   "TaxRegionCode":string,
      /**  Determines whether or not this customer is an inter-company customer.  */  
   "ICCust":boolean,
      /**  The day of the month that service contracts for the customer marked for recurring invoicing are billed on.  If the invoice group's invoice date is greater than or equal to this date then the invoice will be generated.  */  
   "ContBillDay":number,
      /**  Default email address for the customer.  */  
   "EMailAddress":string,
      /**  Determines whether or not the customer will accept partial shipments at the line or order level. This functionality is only available with the Advanced Material Management module.  */  
   "ShippingQualifier":string,
      /**  Contains the AllocPri.PriorityCode value of the priority that this customer's orders receive. This functionality is only available with the Advanced Material Management module.  */  
   "AllocPriorityCode":string,
      /**  Used with Global alerts  */  
   "LinkPortNum":number,
      /**  Indicates if this customer will be able to access Customer Connect.  Only Customers with this equal to YES will be synchronized between the Manufacturing System DB and Customer Connect DB.  */  
   "WebCustomer":boolean,
      /**  Used to define the type of the customer record.  */  
   "CustomerType":string,
      /**  Indicates whether or not this customer will be included in marketing lists.  */  
   "NoContact":boolean,
      /**  Determines whether or not the customer's territory can be changed by system processes that could potentially change the territory from its current value.  */  
   "TerritoryLock":boolean,
      /**  The Customer's website URL.  */  
   "CustURL":string,
      /**  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  */  
   "PendingTerritoryID":string,
   "ExtID":string,
      /**  Determines whether or not shipments to this customer for different sales orders within the same fiscal period wil be consolidated into one invoice. (See Customer.OneInvPerPS - for the shipments from the same sales order are handled).  */  
   "ConsolidateSO":boolean,
      /**  Used in conjunction with the Customer.BillDay field to determine on what days the customer can be invoiced on. See Customer.BillDay description for additional information.  */  
   "Bill_Frequency":string,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   "CreditIncludePI":boolean,
      /**  Determines whether or not this customer is shared between more than one company.  */  
   "GlobalCust":boolean,
      /**  Indicates if this customer participates in the Inter-Company Trading.  */  
   "ICTrader":boolean,
      /**  Establishes the tax authority for this customer.  */  
   "TaxAuthorityCode":string,
      /**  Determines whether or not an external delivery note is required for the customer.  This field is available only when ExtCompany.SendShip is set to Yes.  This will provide the default for the ShipHead record.  */  
   "ExternalDeliveryNote":boolean,
      /**  Determines whether or not Open Orders are to be included in the global credit limit checking process. This checkbox will also include open service contracts.  */  
   "GlobalCredIncOrd":boolean,
      /**  Indicates whether or not Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking process.  */  
   "GlobalCredIncPI":boolean,
      /**  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  */  
   "GlobalCurrencyCode":string,
   "ExternalID":string,
      /**  Determines whether or not the customer has been placed into a "Global Credit Hold" status.  Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  */  
   "GlobalCreditHold":string,
      /**  Determines whether or not this customer record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  Determines whether or not the system should check existing orders for this customer to insure that the same PO number is not used twice by the customer.  */  
   "CheckDuplicatePO":boolean,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit.  A credit limit of zero is considered as having unlimited credit.  */  
   "CreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  */  
   "CustPILimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit Limit.  A credit limit of zero is considered as having unlimited credit.  */  
   "GlobalCreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  */  
   "GlobalPILimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  */  
   "DocGlobalCreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  */  
   "DocGlobalPILimit":number,
      /**  Indicates whether RFQ Attachments are allowed for this Customer  */  
   "RfqAttachAllow":boolean,
      /**   The discount qualifier is primarily used when applying order value based discounts to the customer's sales orders.  The value of this field affects the discount percent given to the customer.  Here's the rule:  
"MIN" = means that the default order discount percent is the minimum discount the customer could get as compared to the order value based discount.
"MAX" = means that the default order discount percent is the maximum discount the customer could get as compared to the order value based d  */  
   "DiscountQualifier":string,
   "Number11":number,
   "Number12":number,
   "Number13":number,
   "Number14":number,
   "Number15":number,
   "Number16":number,
   "Number17":number,
   "Number18":number,
   "Number19":number,
   "Number20":number,
   "Date06":string,
   "Date07":string,
   "Date08":string,
   "Date09":string,
   "Date10":string,
   "Date11":string,
   "Date12":string,
   "Date13":string,
   "Date14":string,
   "Date15":string,
   "Date16":string,
   "Date17":string,
   "Date18":string,
   "Date19":string,
   "Date20":string,
   "CheckBox06":boolean,
   "CheckBox07":boolean,
   "CheckBox08":boolean,
   "CheckBox09":boolean,
   "CheckBox10":boolean,
   "CheckBox11":boolean,
   "CheckBox12":boolean,
   "CheckBox13":boolean,
   "CheckBox14":boolean,
   "CheckBox15":boolean,
   "CheckBox16":boolean,
   "CheckBox17":boolean,
   "CheckBox18":boolean,
   "CheckBox19":boolean,
   "CheckBox20":boolean,
   "ShortChar01":string,
   "ShortChar02":string,
   "ShortChar03":string,
   "ShortChar04":string,
   "ShortChar05":string,
   "ShortChar06":string,
   "ShortChar07":string,
   "ShortChar08":string,
   "ShortChar09":string,
   "ShortChar10":string,
      /**  Specifies the current customer can be an alternate bill to customer.  */  
   "AllowAltBillTo":boolean,
      /**  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  */  
   "DemandDeliveryDays":number,
      /**   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  */  
   "DemandDateType":string,
      /**  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  */  
   "DemandAddLeadTime":number,
      /**  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandAddAction":string,
      /**  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  */  
   "DemandChangeLeadTime":number,
      /**  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandChangeAction":string,
      /**  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  */  
   "DemandCancelLeadTime":number,
      /**  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandCancelAction":string,
      /**  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  */  
   "DemandNewLineLeadTime":number,
      /**  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandNewLineAction":string,
      /**  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  */  
   "DemandQtyChangeLeadTime":number,
      /**  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandQtyChangeAction":string,
      /**  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  */  
   "DemandChangeDateLeadTime":number,
      /**  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandChangeDateAction":string,
      /**  The trading partner name.  */  
   "TradingPartnerName":string,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Verbal Confirmation required  */  
   "VerbalConf":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Periodicity Code.  Must be a valid code in the Periodicity table.  */  
   "PeriodicityCode":number,
      /**  Is a Service Saturday delivery acceptable  */  
   "ServSatDelivery":boolean,
      /**  Is a Service Saturday pickup available  */  
   "ServSatPickup":boolean,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Auto POD flag  */  
   "ServPOD":boolean,
      /**  AOD  */  
   "ServAOD":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Override Carrier Defaults.  If not checked then the plant values will be used  */  
   "OverrideCarrier":boolean,
      /**  Override Service Options.  If not checked then the Plant values will be used  */  
   "OverrideService":boolean,
      /**  Used to calculate on-time delivery performance rating  */  
   "EarlyBuffer":number,
      /**  Used to calculate on-time delivery performance rating  */  
   "LateBuffer":number,
      /**  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  */  
   "DemandUnitPriceDiff":boolean,
      /**  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  */  
   "DemandUnitPriceDiffAction":string,
      /**  A flag that indicates whether this address should be validated by the tax service.  */  
   "ExcFromVal":boolean,
      /**  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  */  
   "AddressVal":boolean,
      /**  This is the Vendor ID to be used when generating a Rebate for the customer  */  
   "RebateVendorNum":number,
      /**  Indicates if the rebate should be a Check or a Credit Memo  */  
   "RebateForm":string,
      /**  Indicates if the order should default as a credit card order.  Can be overriden at the order level.  */  
   "CreditCardOrder":boolean,
      /**  Check for the part in the Part master.  */  
   "DemandCheckForPart":boolean,
      /**  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  */  
   "DemandCheckForPartAction":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Unique Identifier for the Finance Charges  */  
   "ChargeCode":string,
      /**  The contact's name.  */  
   "ContactName":string,
   "AllocationDescription":string,
      /**  Label that displays as the suffix behind the amount printed on checks  */  
   "CurrencyCurrDesc":string,
      /**  The label that displays as the suffix behind the amount printed on checks.  */  
   "CurrencyCurrName":string,
      /**  The special character used for this currency. This character displays on reports and programs near the currency amounts.  */  
   "CurrencyCurrSymbol":string,
   "CurrencyDocumentDesc":string,
   "CustGrupGroupDesc":string,
      /**  Service Home Delivery Type Code Description.  */  
   "DeliveryTypeDescription":string,
   "FOBDescription":string,
   "GlobalCurrencyCurrDesc":string,
      /**  The label that displays as the suffix behind the amount printed on checks.  */  
   "GlobalCurrencyCurrName":string,
      /**  The symbol of the global currency linked to this currency record.  */  
   "GlobalCurrencyCurrSymbol":string,
   "GlobalCurrencyDocumentDesc":string,
   "LanguageDescription":string,
   "MarkUpDescription":string,
   "SalesRepName":string,
   "ShipViaDescription":string,
   "ShipViaWebDesc":string,
   "TATaxAuthorityDescription":string,
   "TaxRegionDescription":string,
   "TermsDescription":string,
   "TerritoryTerritoryDesc":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ContactListRow{
   "Company":string,
   "FirstName":string,
   "LastName":string,
   "ContactName":string,
   "CustNum":number,
   "CustID":string,
   "CustomerName":string,
      /**  A list of customer numbers that were selected for the contact name.  Delimited with ~.  */  
   "CustNumList":string,
   "ConNum":number,
   "ShipToNum":string,
   "CustNumCustID":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ContactRow{
      /**  The name of the current company.  */  
   "Company":string,
      /**  The contact's full first name. This first name will default from the Contact Details sheet, but you can edit it within this field as well.  */  
   "FirstName":string,
      /**  The contact's full last name. This last name will default from the Contact Details sheet, but you can edit it within this field as well.  */  
   "LastName":string,
      /**  The contact’s name.  */  
   "ContactName":string,
      /**  The number of a Customer.  */  
   "CustNum":number,
      /**  The unique identifier for a customer record. On certain reports or windows where space is limited, you may see only the ID.  */  
   "CustID":string,
      /**  The full name for customer.  */  
   "CustomerName":string,
      /**  Delimited list of Customer CustNum.  */  
   "CustNumList":string,
      /**  Delimited list of Customer CustNum and Name (for Kinetic)  */  
   "CustomerList":string,
      /**  Delimited list of shipto CustNum and Name (for Kinetic)  */  
   "ShipToList":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
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

export interface Erp_Tablesets_ShipToRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   "CustNum":number,
      /**  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  */  
   "ShipToNum":string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  */  
   "Name":string,
      /**  The first line of the ShipTo address.  */  
   "Address1":string,
      /**  The second line of the ShipTo address.  */  
   "Address2":string,
      /**  The third line of the ShipTo address.  */  
   "Address3":string,
      /**  The city portion of the ShipTo address.  */  
   "City":string,
      /**  The state or province portion of the ShipTo address.  */  
   "State":string,
      /**  The zip or postal code portion of the ShipTo address.  */  
   "ZIP":string,
      /**  The country portion of the ShipTo address.  */  
   "Country":string,
      /**  The State Tax Identification Number. Used in Order Entry and prints on Sales Acknowledgements.  */  
   "ResaleID":string,
      /**  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  */  
   "SalesRepCode":string,
      /**  The SalesTer.TerritoryID value of the territory the customer is assigned to.  */  
   "TerritoryID":string,
      /**  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  */  
   "ShipViaCode":string,
      /**  The CustCnt.ConNum of the default shipping contact for the ShipTo location. The primary shipping contact is used as a default in the shipping process.  */  
   "PrimSCon":number,
      /**  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   "FaxNum":string,
      /**  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   "PhoneNum":string,
      /**  Determines whether or not the ShipTo location is normally exempt from sales tax. Used as a default in invoice entry.  If the field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  */  
   "TaxExempt":string,
      /**  A mutually agreed upon value that links a customer's EDI shipto record (an N1 / ST) to the Manufacturing System DB ShipTo record.  */  
   "EDIShipNum":string,
      /**  The Country.CountryNum value of the country selected in the ShipTo.Country field.  */  
   "CountryNum":number,
      /**  The LangName.LangNameID value of the default Language assigned to the ShipTo location. This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   "LangNameID":string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Customer table. This field is only visible if ISSyst.EnableHarbour is set.  */  
   "BorderCrossing":string,
      /**  Optional custom address format for the ShipTo location.  */  
   "FormatStr":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  */  
   "TaxRegionCode":string,
      /**  The email address of the ShipTo location.  */  
   "EMailAddress":string,
      /**   Determines how the ShipTo location should be assigned to a territory. There are 3 methods for Territory assignment in Ship-to:

Sync - Keep the ShipTo territory synchronized with the territory on the
       main customer record. (ShipTo.TerritoryID = Customer.TerritoryID)
Syst - Let the system (Get Territory) determine the territory to assign         to the ShipTo based on territory boundaries.
Lock - Check this method after assigning the territory manually to 
       prevent the system from attempting to reassign the territory.  */  
   "TerritorySelect":string,
      /**  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  */  
   "PendingTerritoryID":string,
      /**  Determines whether or not the ShipTo record was created by an EDI transaction.  */  
   "CreatedByEDI":boolean,
      /**  Unique identifier of the ShipTo from an external General Ledger interface such as the EuroFinancial integration.  */  
   "ExternalID":string,
      /**  The TaxAuthorityCd.TaxAuthorityCode value of the Tax Authority assigned to this ShipTo location.  */  
   "TaxAuthorityCode":string,
      /**  Disable this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   "EDICode":string,
      /**  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  */  
   "DemandDeliveryDays":number,
      /**   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  */  
   "DemandDateType":string,
      /**  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  */  
   "DemandAddLeadTime":number,
      /**  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandAddAction":string,
      /**  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  */  
   "DemandChangeLeadTime":number,
      /**  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandChangeAction":string,
      /**  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  */  
   "DemandCancelLeadTime":number,
      /**  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandCancelAction":string,
      /**  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  */  
   "DemandNewLineLeadTime":number,
      /**  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandNewLineAction":string,
      /**  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  */  
   "DemandQtyChangeLeadTime":number,
      /**  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandQtyChangeAction":string,
      /**  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  */  
   "DemandChangeDateLeadTime":number,
      /**  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   "DemandChangeDateAction":string,
      /**  The trading partner name.  */  
   "TradingPartnerName":string,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Periodicity Code.  Must be a valid code in the Periodicity table.  */  
   "PeriodicityCode":number,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  International Shipping - HazardousShipment  */  
   "HazardousShipment":boolean,
      /**  Override Carrier Defaults.  If not checked then the customer values will be used if overriden else the Site values  */  
   "OverrideCarrier":boolean,
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  Override Service Options.  If not checked then the customer values will be used if overriden else the Site values  */  
   "OverrideService":boolean,
      /**  Indicates if the demand fields from the customer should be used.  */  
   "DemandUseCustomerValues":boolean,
      /**  Tax Payer Registration Reason Code  */  
   "TaxRegReason":string,
      /**  Used to calculate on-time delivery performance rating  */  
   "EarlyBuffer":number,
      /**  Organization Registration Code  */  
   "OrgRegCode":string,
      /**  Used to calculate on-time delivery performance rating  */  
   "LateBuffer":number,
      /**  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  */  
   "DemandUnitPriceDiff":boolean,
      /**  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  */  
   "DemandUnitPriceDiffAction":string,
      /**  A flag that indicates whether this address should be validated by the tax service.  */  
   "ExcFromVal":boolean,
      /**  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  */  
   "AddressVal":boolean,
      /**  Check for the part in the Part master.  */  
   "DemandCheckForPart":boolean,
      /**  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  */  
   "DemandCheckForPartAction":string,
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   "FFAddress1":string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   "FFAddress2":string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   "FFCity":string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   "FFState":string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   "FFZip":string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   "FFCountry":string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   "FFContact":string,
      /**  International Shipping. Frieght Forwarder company name  */  
   "FFCompName":string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   "FFPhoneNum":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Individual Pack IDs  */  
   "IndividualPackIDs":boolean,
      /**  Freight Forwarder Third address line  */  
   "FFCountryNum":number,
      /**  Additional Handling flag  */  
   "NonStdPkg":boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Non Standard Packaging  */  
   "AddlHdlgFlag":boolean,
      /**  UPS Quantum View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View From Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Freight Forwarder Country portion of the address  */  
   "FFAddress3":string,
      /**  Used to determine if an address changed because of the tax integration.  If true, the tax integration changed the address.  */  
   "ETCAddrChg":boolean,
      /**  Indicates if this is a alternate ShipTo. An alternate is a Shipto that is valid for this customer, but is defined/maintained by the "master" customer. See ShipTo.MasterCustNum/MasterShiptoNum.  */  
   "IsAlternate":boolean,
      /**  Pertains to Alternate Shipto (IsAlternate). Contains the CustNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   "MasterCustNum":number,
      /**  Pertains to Alternate Shipto (IsAlternate). Contains the ShipToNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   "MasterShipToNum":string,
      /**  Check for Revision  */  
   "DemandCheckForRev":boolean,
      /**  Check for Revision Action  */  
   "DemandCheckForRevAction":string,
      /**  Flag for checking partial Shipment for Demand Entry.  */  
   "DemandCheckPartialShip":boolean,
      /**  Check Partial Shipments Action: B =Stop  and W = Warning  */  
   "DemandCheckShipAction":string,
      /**  Define if at the moment of processing a demand the process should also close those rejected schedules that remain at demand entry  */  
   "DemandCloseRejSkd":boolean,
      /**  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  */  
   "DemandPricing":string,
      /**  Defines the tolerance for price difference validations  */  
   "PriceTolerance":number,
      /**  If this flags is turned on then Demand CTP will automatically be executed as a part of the demand to order process.  */  
   "CheckDateCapPromise":boolean,
      /**  Confirm or not the Capable to Promise jobs from Demand Entry  */  
   "CheckConfirmCapPromise":boolean,
      /**  If checked, Updates the date in Demand Entry  */  
   "CheckUpdateCapPromise":boolean,
      /**  This field will define the dates that will be validated as a part of the demand to order process. The valid values for this combo will be:  Need By (N), Ship By (S) and Both (B)  */  
   "DemandCapPromiseDate":string,
      /**  The value on this field will define the action to be taken when validating CTP. The valid values for this combo box will be: Warning (W) and Stop (S)  */  
   "DemandCapPromiseAction":string,
      /**   This field will define the dates that will be updated as a part of the demand to order process. The valid options will be:
Need By (N), Ship By (S) and Both  (B) NOTE .-In all the cases above the update of date will only be done if the CTP dates are beyond the dates on the file.  */  
   "DemandCapPromiseUpdate":string,
      /**  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  */  
   "OTSmartString":boolean,
      /**  Full Legal name  */  
   "LegalName":string,
      /**  If true then demand will be rejected when one or more demand lines are not configured properly. Applies only to Configurable parts.  */  
   "DemandCheckConfig":boolean,
      /**  Indicates the action to be taken if configuration values have not been entered for one or more demand lines.  */  
   "DemandCheckCfgAction":string,
      /**  WIWebShipTo  */  
   "WIWebShipTo":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGApartment  */  
   "AGApartment":string,
      /**  AGExtraStreetNumber  */  
   "AGExtraStreetNumber":string,
      /**  AGFloor  */  
   "AGFloor":string,
      /**  AGGrossIncomeTaxID  */  
   "AGGrossIncomeTaxID":string,
      /**  AGLocationCode  */  
   "AGLocationCode":string,
      /**  AGNeighborhood  */  
   "AGNeighborhood":string,
      /**  AGProvinceCode  */  
   "AGProvinceCode":string,
      /**  AGStreet  */  
   "AGStreet":string,
      /**  AGStreetNumber  */  
   "AGStreetNumber":string,
      /**  EntityUseCode  */  
   "EntityUseCode":string,
      /**  Check if the part is a run out part.  */  
   "DemandCheckForRunOutPart":boolean,
      /**  Indicates what type of action to take if the Check for Run Out Part option is selected and the part is marked as a run out part.  Options are B (reject the change) or W (warning - alert that the part is marked as run out but allow the record to be accepted).  */  
   "DemandCheckForRunOutPartAction":string,
      /**  INExciseRegNumber  */  
   "INExciseRegNumber":string,
      /**  INVATNumber  */  
   "INVATNumber":string,
      /**  INSTRegistration  */  
   "INSTRegistration":string,
      /**  MXCURP  */  
   "MXCURP":string,
      /**  MXMunicipio  */  
   "MXMunicipio":string,
      /**  MXFederalID  */  
   "MXFederalID":string,
      /**  INTaxRegistrationID  */  
   "INTaxRegistrationID":string,
      /**  Geographical Location Code  */  
   "PEUBIGEOCode":string,
      /**  EORI Number  */  
   "EORINumber":string,
      /**  Tax ID Validation Status: Not Validated – 0, Valid – 1, Invalid – 2.  */  
   "TaxValidationStatus":number,
      /**  Tax Validation Date  */  
   "TaxValidationDate":string,
      /**  HMRCTaxValidationLog  */  
   "HMRCTaxValidationLog":string,
      /**  Indicates if the record is inactive.  */  
   "Inactive":boolean,
      /**  FSMRegionCode  */  
   "FSMRegionCode":string,
      /**  FSMArea  */  
   "FSMArea":string,
      /**  List of fields which are referenced by COA segments.  */  
   "COASegReferences":string,
      /**  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  */  
   "ContactName":string,
      /**  Display Format String  */  
   "DspFormatStr":string,
      /**  Indicates if ShipTo is Global (Master or Linked)  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany, GlbCustNum and GlbShipto that is linking to this shipto  */  
   "GlbLink":string,
      /**  Indicates Integration with financial package (like EuroFin)  */  
   "IntegrationFlag":boolean,
      /**  Flag used for integrations whether to run the on change country logic.  */  
   "IntRunChangeCountry":boolean,
   "PeriodicityDesc":string,
      /**  List of available Periodicity values  */  
   "PeriodicityList":string,
      /**  Used to indicate if primary shipto.  Updates Customer.ShipToNum field  */  
   "PrimaryShipTo":boolean,
      /**  Sales Tax ID  */  
   "SalesTaxID":string,
      /**  Service Tax ID  */  
   "ServiceTaxID":string,
   "TerritorySelectDescription":string,
      /**  Use this field to display/update; replaces TerritorySelect  */  
   "TerrSelectFlag":string,
      /**  Address in formatted delimited list  */  
   "AddrList":string,
   "LanguageDescription":string,
   "BitFlag":number,
   "AGLocationDescription":string,
   "AGProvinceDescription":string,
   "CountryISOCode":string,
   "CountryEUMember":boolean,
   "CustNumName":string,
   "CustNumCustID":string,
   "CustNumBTName":string,
   "DeliveryTypeDescription":string,
   "MasterCustIDBTName":string,
   "MasterCustIDCustID":string,
   "MasterCustIDName":string,
   "SalesRepName":string,
   "ShipViaWebDesc":string,
   "ShipViaDescription":string,
   "TATaxAuthorityDescription":string,
   "TaxRegionDescription":string,
   "TerritoryTerritoryDesc":string,
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
export interface CondenseContactList_input{
   ds:Erp_Tablesets_ContactListTableset[],
}

export interface CondenseContactList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContactListTableset,
}
}

export interface Erp_Tablesets_ContactCustomerRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustID:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  The full name of the customer.  */  
   Name:string,
      /**  The first line of the customer's main address.  */  
   Address1:string,
      /**  The second line of the customer's main address.  */  
   Address2:string,
      /**  The third line of the customer's main address.  */  
   Address3:string,
      /**  The city portion of the customer's main address.  */  
   City:string,
      /**  The state or province portion of the customer's main address.  */  
   State:string,
      /**  The zip or postal code portion of the customer's main address.  */  
   Zip:string,
      /**  The country of the main customer address.  */  
   Country:string,
      /**  Optional field used to record the customer's State Tax Identification number, which is displayed on Sales Acknowledgments.  */  
   ResaleID:string,
      /**  The SalesRep.SalesRepCode of the default salesperson for the customer. This field is used to supply defaults to Order Entry and Invoice entry for invoices that do not reference a sales orders.  */  
   SalesRepCode:string,
      /**  The SalesTer.TerritoryID value of the territory assigned to the customer.  */  
   TerritoryID:string,
      /**  Contains the key of the default ship to for the customer. A blank value indicates that the name and address in the Customer file is considered the default ship to. This field is updated when the user marks the check box in ship to maintenance indicating that the ship to is to be designated as the default. This default will be used in areas such as Sales Order entry.  */  
   ShipToNum:string,
      /**   The Terms.TermsCode value of the default sales terms associated with the customer. A default may be supplied by XaSyst.TermsCode if not blank. The terms will default into quotes and orders for this customer.
For invoices not related to a sales order, these terms will also default into the invoice.  */  
   TermsCode:string,
      /**  Contains the ShipVia.ShipViaCode value of the default ShipVia for the customer.  */  
   ShipViaCode:string,
      /**  Controls whether or not this customer's statement will print when   printing of customer statements.  */  
   PrintStatements:boolean,
      /**  Only customers that are PrintLabels = Yes will be selected for printing of mailing labels.  */  
   PrintLabels:boolean,
      /**   Allows the user to establish whether or not a specific customer requires Sales Order Acknowledgements.  This does not force or limit the printing of sales acknowledgments directly from within Order Entry.  Order entry displays this setting to the user so that they know if they should print the acknowledgment.
For batch mode printing, (where ranges of sales orders are selected...future release) this setting will be used to exclude orders from printing.  */  
   PrintAck:boolean,
      /**  Controls whether or not the customer will be included in the finance charge calculation process.  */  
   FinCharges:boolean,
      /**  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  */  
   CreditHold:boolean,
      /**  Contains the CustGrup.GroupCode value of the customer group that the customer has been assigned to. This field is used by the application for sorting or filtering on reports and can also be associated with price lists.  */  
   GroupCode:string,
      /**  An optional field used to establish a default purchasing discount percentage for any order placed by customer. This value is supplied to order entry as a default for line item discount percent.  */  
   DiscountPercent:number,
      /**  Contains the CustCnt.ConNum value of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Order Entry and Quoting.  */  
   PrimPCon:number,
      /**  The same as the PrimPCon except that this is the Primary Billing Contact and this is used as a default in invoice entry.  */  
   PrimBCon:number,
      /**  Same as PrimPCon except that this the Primary Shipping Contact and is used as a default in Packing Slip entry.  */  
   PrimSCon:number,
      /**   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   Comment:string,
      /**  The date when the customer was established as a customer. Use the system date as a default when creating new customers.  */  
   EstDate:string,
      /**  The Fax Number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  */  
   FaxNum:string,
      /**  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**  Indicates the reason why the customer is normally exempt from sales tax. Used as a default in invoice entry.  If field is non-blank it is considered exempt.  */  
   TaxExempt:string,
      /**  The QMarkup.MarkupID value of the quote markup table which will be used to provide default markup percents in quote entry for this customer. If left blank the quote module will use the default quote markup table for the customer. (See EQSyst.MarkupID).  */  
   MarkUpID:string,
      /**   Represents the day of the week or month that this customer is invoiced on. The possible choices are determined by the Customer.Bill-Frequency field value.

When the Bill-Frequency is "W" (Weeky):
The valid values are 0-7 where 0=All Days,1=Sun,2=Mon,...,7=Sat.  

ll-frequency is 'M' (Monthly) this field contains the 1st -> 31st as possible choices to represent the day of the month to bill on.  */  
   BillDay:number,
      /**  Determines whether or not packing slips for the same Sales Order and Fiscal Period will combined into a single invoice or not. If the packing slips are for different sales orders for the customer or fall in different fiscal periods, seperate invoices will be created even when this field is set to Yes.  */  
   OneInvPerPS:boolean,
      /**  Contains the default FOB.FOB value of the FOB policy for this  customers orders.  Default used in sales order entry for this customer.  */  
   DefaultFOB:string,
      /**  Determines whether or not Open Sales Orders are to be included in the credit limit checking process for the customer. This checkbox will also include open service contracts.  */  
   CreditIncludeOrders:boolean,
      /**  Date on which the next credit review should be conducted for the customer.  */  
   CreditReviewDate:string,
      /**  Date on which the customer was last placed on credit hold. This field is maintained by the system.  */  
   CreditHoldDate:string,
      /**  Indicates how the customer was placed on credit hold.  Valid values are "MANUAL", "INVOICES", "ORDERS","CONTRACTS".  "MANUAL" means that the user placed the customer on hold.  INVOICES means that the customer’s open A/R balance exceeded the credit limit.  ORDERS means that the sum of the open A/R and the open orders exceeded the credit limit. This field is maintained by the system.  */  
   CreditHoldSource:string,
      /**  The UserFile.DCDUSERID value of the user that last cleared the customer’s credit hold. This field is maintained by the system.  */  
   CreditClearUserID:string,
      /**  The date that the user last cleared the customer’s credit hold. This field is maintained by the system.  */  
   CreditClearDate:string,
      /**  The time that the user last cleared the customer’s credit hold in HH:MM:SS format. This field is maintained by the system.  */  
   CreditClearTime:string,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   EDICode:string,
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
      /**  Contains the Currency.CurrencyCode value of the customer's base currency.  */  
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
      /**  Contains the Currency.CurrencyCode value of the customer's base currency.  */  
   CurrencyCode:string,
      /**  Contains the Country.CountryNum value of the country the customer is located in.  */  
   CountryNum:number,
      /**  Contains the LangName.LangNameID value of the customer's language. This controls which language will be selected when extracting part descriptions from PartLangDesc table and report labels for customer related forms such as orders, packing slips and invoices.  */  
   LangNameID:string,
      /**  Area/City code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set to yes.  */  
   BorderCrossing:string,
      /**  Optional custom address format used to format the customer's main address.  */  
   FormatStr:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   BTName:string,
      /**  The first line of the customer's Bill To address.  */  
   BTAddress1:string,
      /**  The second line of the customer's Bill To address.  */  
   BTAddress2:string,
      /**  The second line of the customer's Bill To address.  */  
   BTAddress3:string,
      /**  The city portion of the customer's Bill To address.  */  
   BTCity:string,
      /**  The state or province portion of the customer's Bill To address.  */  
   BTState:string,
      /**  The zip or postal code portion of the customer's Bill To address.  */  
   BTZip:string,
      /**  The Country.Countrynum value of the Country portion of the customer's Bill To address.  */  
   BTCountryNum:number,
      /**  Contains the Country.Description value of the Country portion of the customer's Bill To address.  */  
   BTCountry:string,
      /**  The phone number related to the customer's Bill To Address.  */  
   BTPhoneNum:string,
      /**  The fax number of the customer's Bill To address.  */  
   BTFaxNum:string,
      /**  Optional custom address format used to format the customer's Bill To address.  */  
   BTFormatStr:string,
      /**  The Customer.CustNum value of the customer's parent company.  */  
   ParentCustNum:number,
      /**  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  */  
   TaxRegionCode:string,
      /**  Determines whether or not this customer is an inter-company customer.  */  
   ICCust:boolean,
      /**  The day of the month that service contracts for the customer marked for recurring invoicing are billed on.  If the invoice group's invoice date is greater than or equal to this date then the invoice will be generated.  */  
   ContBillDay:number,
      /**  Default email address for the customer.  */  
   EMailAddress:string,
      /**  Determines whether or not the customer will accept partial shipments at the line or order level. This functionality is only available with the Advanced Material Management module.  */  
   ShippingQualifier:string,
      /**  Contains the AllocPri.PriorityCode value of the priority that this customer's orders receive. This functionality is only available with the Advanced Material Management module.  */  
   AllocPriorityCode:string,
      /**  Used with Global alerts  */  
   LinkPortNum:number,
      /**  Indicates if this customer will be able to access Customer Connect.  Only Customers with this equal to YES will be synchronized between the Manufacturing System DB and Customer Connect DB.  */  
   WebCustomer:boolean,
      /**  Used to define the type of the customer record.  */  
   CustomerType:string,
      /**  Indicates whether or not this customer will be included in marketing lists.  */  
   NoContact:boolean,
      /**  Determines whether or not the customer's territory can be changed by system processes that could potentially change the territory from its current value.  */  
   TerritoryLock:boolean,
      /**  The Customer's website URL.  */  
   CustURL:string,
      /**  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  */  
   PendingTerritoryID:string,
   ExtID:string,
      /**  Determines whether or not shipments to this customer for different sales orders within the same fiscal period wil be consolidated into one invoice. (See Customer.OneInvPerPS - for the shipments from the same sales order are handled).  */  
   ConsolidateSO:boolean,
      /**  Used in conjunction with the Customer.BillDay field to determine on what days the customer can be invoiced on. See Customer.BillDay description for additional information.  */  
   Bill_Frequency:string,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   CreditIncludePI:boolean,
      /**  Determines whether or not this customer is shared between more than one company.  */  
   GlobalCust:boolean,
      /**  Indicates if this customer participates in the Inter-Company Trading.  */  
   ICTrader:boolean,
      /**  Establishes the tax authority for this customer.  */  
   TaxAuthorityCode:string,
      /**  Determines whether or not an external delivery note is required for the customer.  This field is available only when ExtCompany.SendShip is set to Yes.  This will provide the default for the ShipHead record.  */  
   ExternalDeliveryNote:boolean,
      /**  Determines whether or not Open Orders are to be included in the global credit limit checking process. This checkbox will also include open service contracts.  */  
   GlobalCredIncOrd:boolean,
      /**  Indicates whether or not Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking process.  */  
   GlobalCredIncPI:boolean,
      /**  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  */  
   GlobalCurrencyCode:string,
   ExternalID:string,
      /**  Determines whether or not the customer has been placed into a "Global Credit Hold" status.  Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  */  
   GlobalCreditHold:string,
      /**  Determines whether or not this customer record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Determines whether or not the system should check existing orders for this customer to insure that the same PO number is not used twice by the customer.  */  
   CheckDuplicatePO:boolean,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit.  A credit limit of zero is considered as having unlimited credit.  */  
   CreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  */  
   CustPILimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit Limit.  A credit limit of zero is considered as having unlimited credit.  */  
   GlobalCreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  */  
   GlobalPILimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  */  
   DocGlobalCreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  */  
   DocGlobalPILimit:number,
      /**  Indicates whether RFQ Attachments are allowed for this Customer  */  
   RfqAttachAllow:boolean,
      /**   The discount qualifier is primarily used when applying order value based discounts to the customer's sales orders.  The value of this field affects the discount percent given to the customer.  Here's the rule:  
"MIN" = means that the default order discount percent is the minimum discount the customer could get as compared to the order value based discount.
"MAX" = means that the default order discount percent is the maximum discount the customer could get as compared to the order value based d  */  
   DiscountQualifier:string,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
      /**  Specifies the current customer can be an alternate bill to customer.  */  
   AllowAltBillTo:boolean,
      /**  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  */  
   DemandDeliveryDays:number,
      /**   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  */  
   DemandDateType:string,
      /**  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  */  
   DemandAddLeadTime:number,
      /**  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandAddAction:string,
      /**  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  */  
   DemandChangeLeadTime:number,
      /**  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandChangeAction:string,
      /**  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  */  
   DemandCancelLeadTime:number,
      /**  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandCancelAction:string,
      /**  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  */  
   DemandNewLineLeadTime:number,
      /**  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandNewLineAction:string,
      /**  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  */  
   DemandQtyChangeLeadTime:number,
      /**  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandQtyChangeAction:string,
      /**  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  */  
   DemandChangeDateLeadTime:number,
      /**  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandChangeDateAction:string,
      /**  The trading partner name.  */  
   TradingPartnerName:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Verbal Confirmation required  */  
   VerbalConf:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Periodicity Code.  Must be a valid code in the Periodicity table.  */  
   PeriodicityCode:number,
      /**  Is a Service Saturday delivery acceptable  */  
   ServSatDelivery:boolean,
      /**  Is a Service Saturday pickup available  */  
   ServSatPickup:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Auto POD flag  */  
   ServPOD:boolean,
      /**  AOD  */  
   ServAOD:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Override Carrier Defaults.  If not checked then the plant values will be used  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the Plant values will be used  */  
   OverrideService:boolean,
      /**  Used to calculate on-time delivery performance rating  */  
   EarlyBuffer:number,
      /**  Used to calculate on-time delivery performance rating  */  
   LateBuffer:number,
      /**  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  */  
   DemandUnitPriceDiff:boolean,
      /**  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  */  
   DemandUnitPriceDiffAction:string,
      /**  A flag that indicates whether this address should be validated by the tax service.  */  
   ExcFromVal:boolean,
      /**  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  */  
   AddressVal:boolean,
      /**  This is the Vendor ID to be used when generating a Rebate for the customer  */  
   RebateVendorNum:number,
      /**  Indicates if the rebate should be a Check or a Credit Memo  */  
   RebateForm:string,
      /**  Indicates if the order should default as a credit card order.  Can be overriden at the order level.  */  
   CreditCardOrder:boolean,
      /**  Check for the part in the Part master.  */  
   DemandCheckForPart:boolean,
      /**  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  */  
   DemandCheckForPartAction:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Unique Identifier for the Finance Charges  */  
   ChargeCode:string,
      /**  The contact's name.  */  
   ContactName:string,
   AllocationDescription:string,
      /**  Label that displays as the suffix behind the amount printed on checks  */  
   CurrencyCurrDesc:string,
      /**  The label that displays as the suffix behind the amount printed on checks.  */  
   CurrencyCurrName:string,
      /**  The special character used for this currency. This character displays on reports and programs near the currency amounts.  */  
   CurrencyCurrSymbol:string,
   CurrencyDocumentDesc:string,
   CustGrupGroupDesc:string,
      /**  Service Home Delivery Type Code Description.  */  
   DeliveryTypeDescription:string,
   FOBDescription:string,
   GlobalCurrencyCurrDesc:string,
      /**  The label that displays as the suffix behind the amount printed on checks.  */  
   GlobalCurrencyCurrName:string,
      /**  The symbol of the global currency linked to this currency record.  */  
   GlobalCurrencyCurrSymbol:string,
   GlobalCurrencyDocumentDesc:string,
   LanguageDescription:string,
   MarkUpDescription:string,
   SalesRepName:string,
   ShipViaDescription:string,
   ShipViaWebDesc:string,
   TATaxAuthorityDescription:string,
   TaxRegionDescription:string,
   TermsDescription:string,
   TerritoryTerritoryDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContactListRow{
   Company:string,
   FirstName:string,
   LastName:string,
   ContactName:string,
   CustNum:number,
   CustID:string,
   CustomerName:string,
      /**  A list of customer numbers that were selected for the contact name.  Delimited with ~.  */  
   CustNumList:string,
   ConNum:number,
   ShipToNum:string,
   CustNumCustID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContactListTableset{
   ContactList:Erp_Tablesets_ContactListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ContactRow{
      /**  The name of the current company.  */  
   Company:string,
      /**  The contact's full first name. This first name will default from the Contact Details sheet, but you can edit it within this field as well.  */  
   FirstName:string,
      /**  The contact's full last name. This last name will default from the Contact Details sheet, but you can edit it within this field as well.  */  
   LastName:string,
      /**  The contact’s name.  */  
   ContactName:string,
      /**  The number of a Customer.  */  
   CustNum:number,
      /**  The unique identifier for a customer record. On certain reports or windows where space is limited, you may see only the ID.  */  
   CustID:string,
      /**  The full name for customer.  */  
   CustomerName:string,
      /**  Delimited list of Customer CustNum.  */  
   CustNumList:string,
      /**  Delimited list of Customer CustNum and Name (for Kinetic)  */  
   CustomerList:string,
      /**  Delimited list of shipto CustNum and Name (for Kinetic)  */  
   ShipToList:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContactTableset{
   Contact:Erp_Tablesets_ContactRow[],
   ContactCustomer:Erp_Tablesets_ContactCustomerRow[],
   CustCnt:Erp_Tablesets_CustCntRow[],
   CustCntAttch:Erp_Tablesets_CustCntAttchRow[],
   ShipTo:Erp_Tablesets_ShipToRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

export interface Erp_Tablesets_ShipToRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  */  
   ShipToNum:string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  */  
   Name:string,
      /**  The first line of the ShipTo address.  */  
   Address1:string,
      /**  The second line of the ShipTo address.  */  
   Address2:string,
      /**  The third line of the ShipTo address.  */  
   Address3:string,
      /**  The city portion of the ShipTo address.  */  
   City:string,
      /**  The state or province portion of the ShipTo address.  */  
   State:string,
      /**  The zip or postal code portion of the ShipTo address.  */  
   ZIP:string,
      /**  The country portion of the ShipTo address.  */  
   Country:string,
      /**  The State Tax Identification Number. Used in Order Entry and prints on Sales Acknowledgements.  */  
   ResaleID:string,
      /**  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  */  
   SalesRepCode:string,
      /**  The SalesTer.TerritoryID value of the territory the customer is assigned to.  */  
   TerritoryID:string,
      /**  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  */  
   ShipViaCode:string,
      /**  The CustCnt.ConNum of the default shipping contact for the ShipTo location. The primary shipping contact is used as a default in the shipping process.  */  
   PrimSCon:number,
      /**  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   FaxNum:string,
      /**  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**  Determines whether or not the ShipTo location is normally exempt from sales tax. Used as a default in invoice entry.  If the field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  */  
   TaxExempt:string,
      /**  A mutually agreed upon value that links a customer's EDI shipto record (an N1 / ST) to the Manufacturing System DB ShipTo record.  */  
   EDIShipNum:string,
      /**  The Country.CountryNum value of the country selected in the ShipTo.Country field.  */  
   CountryNum:number,
      /**  The LangName.LangNameID value of the default Language assigned to the ShipTo location. This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   LangNameID:string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Customer table. This field is only visible if ISSyst.EnableHarbour is set.  */  
   BorderCrossing:string,
      /**  Optional custom address format for the ShipTo location.  */  
   FormatStr:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  */  
   TaxRegionCode:string,
      /**  The email address of the ShipTo location.  */  
   EMailAddress:string,
      /**   Determines how the ShipTo location should be assigned to a territory. There are 3 methods for Territory assignment in Ship-to:

Sync - Keep the ShipTo territory synchronized with the territory on the
       main customer record. (ShipTo.TerritoryID = Customer.TerritoryID)
Syst - Let the system (Get Territory) determine the territory to assign         to the ShipTo based on territory boundaries.
Lock - Check this method after assigning the territory manually to 
       prevent the system from attempting to reassign the territory.  */  
   TerritorySelect:string,
      /**  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  */  
   PendingTerritoryID:string,
      /**  Determines whether or not the ShipTo record was created by an EDI transaction.  */  
   CreatedByEDI:boolean,
      /**  Unique identifier of the ShipTo from an external General Ledger interface such as the EuroFinancial integration.  */  
   ExternalID:string,
      /**  The TaxAuthorityCd.TaxAuthorityCode value of the Tax Authority assigned to this ShipTo location.  */  
   TaxAuthorityCode:string,
      /**  Disable this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   EDICode:string,
      /**  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  */  
   DemandDeliveryDays:number,
      /**   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  */  
   DemandDateType:string,
      /**  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  */  
   DemandAddLeadTime:number,
      /**  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandAddAction:string,
      /**  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  */  
   DemandChangeLeadTime:number,
      /**  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandChangeAction:string,
      /**  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  */  
   DemandCancelLeadTime:number,
      /**  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandCancelAction:string,
      /**  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  */  
   DemandNewLineLeadTime:number,
      /**  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandNewLineAction:string,
      /**  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  */  
   DemandQtyChangeLeadTime:number,
      /**  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandQtyChangeAction:string,
      /**  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  */  
   DemandChangeDateLeadTime:number,
      /**  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  */  
   DemandChangeDateAction:string,
      /**  The trading partner name.  */  
   TradingPartnerName:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Periodicity Code.  Must be a valid code in the Periodicity table.  */  
   PeriodicityCode:number,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  International Shipping - HazardousShipment  */  
   HazardousShipment:boolean,
      /**  Override Carrier Defaults.  If not checked then the customer values will be used if overriden else the Site values  */  
   OverrideCarrier:boolean,
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  Override Service Options.  If not checked then the customer values will be used if overriden else the Site values  */  
   OverrideService:boolean,
      /**  Indicates if the demand fields from the customer should be used.  */  
   DemandUseCustomerValues:boolean,
      /**  Tax Payer Registration Reason Code  */  
   TaxRegReason:string,
      /**  Used to calculate on-time delivery performance rating  */  
   EarlyBuffer:number,
      /**  Organization Registration Code  */  
   OrgRegCode:string,
      /**  Used to calculate on-time delivery performance rating  */  
   LateBuffer:number,
      /**  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  */  
   DemandUnitPriceDiff:boolean,
      /**  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  */  
   DemandUnitPriceDiffAction:string,
      /**  A flag that indicates whether this address should be validated by the tax service.  */  
   ExcFromVal:boolean,
      /**  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  */  
   AddressVal:boolean,
      /**  Check for the part in the Part master.  */  
   DemandCheckForPart:boolean,
      /**  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  */  
   DemandCheckForPartAction:string,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   FFAddress1:string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   FFAddress2:string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   FFCity:string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   FFState:string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   FFZip:string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   FFCountry:string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   FFContact:string,
      /**  International Shipping. Frieght Forwarder company name  */  
   FFCompName:string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   FFPhoneNum:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Individual Pack IDs  */  
   IndividualPackIDs:boolean,
      /**  Freight Forwarder Third address line  */  
   FFCountryNum:number,
      /**  Additional Handling flag  */  
   NonStdPkg:boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Non Standard Packaging  */  
   AddlHdlgFlag:boolean,
      /**  UPS Quantum View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View From Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Freight Forwarder Country portion of the address  */  
   FFAddress3:string,
      /**  Used to determine if an address changed because of the tax integration.  If true, the tax integration changed the address.  */  
   ETCAddrChg:boolean,
      /**  Indicates if this is a alternate ShipTo. An alternate is a Shipto that is valid for this customer, but is defined/maintained by the "master" customer. See ShipTo.MasterCustNum/MasterShiptoNum.  */  
   IsAlternate:boolean,
      /**  Pertains to Alternate Shipto (IsAlternate). Contains the CustNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterCustNum:number,
      /**  Pertains to Alternate Shipto (IsAlternate). Contains the ShipToNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterShipToNum:string,
      /**  Check for Revision  */  
   DemandCheckForRev:boolean,
      /**  Check for Revision Action  */  
   DemandCheckForRevAction:string,
      /**  Flag for checking partial Shipment for Demand Entry.  */  
   DemandCheckPartialShip:boolean,
      /**  Check Partial Shipments Action: B =Stop  and W = Warning  */  
   DemandCheckShipAction:string,
      /**  Define if at the moment of processing a demand the process should also close those rejected schedules that remain at demand entry  */  
   DemandCloseRejSkd:boolean,
      /**  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  */  
   DemandPricing:string,
      /**  Defines the tolerance for price difference validations  */  
   PriceTolerance:number,
      /**  If this flags is turned on then Demand CTP will automatically be executed as a part of the demand to order process.  */  
   CheckDateCapPromise:boolean,
      /**  Confirm or not the Capable to Promise jobs from Demand Entry  */  
   CheckConfirmCapPromise:boolean,
      /**  If checked, Updates the date in Demand Entry  */  
   CheckUpdateCapPromise:boolean,
      /**  This field will define the dates that will be validated as a part of the demand to order process. The valid values for this combo will be:  Need By (N), Ship By (S) and Both (B)  */  
   DemandCapPromiseDate:string,
      /**  The value on this field will define the action to be taken when validating CTP. The valid values for this combo box will be: Warning (W) and Stop (S)  */  
   DemandCapPromiseAction:string,
      /**   This field will define the dates that will be updated as a part of the demand to order process. The valid options will be:
Need By (N), Ship By (S) and Both  (B) NOTE .-In all the cases above the update of date will only be done if the CTP dates are beyond the dates on the file.  */  
   DemandCapPromiseUpdate:string,
      /**  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  */  
   OTSmartString:boolean,
      /**  Full Legal name  */  
   LegalName:string,
      /**  If true then demand will be rejected when one or more demand lines are not configured properly. Applies only to Configurable parts.  */  
   DemandCheckConfig:boolean,
      /**  Indicates the action to be taken if configuration values have not been entered for one or more demand lines.  */  
   DemandCheckCfgAction:string,
      /**  WIWebShipTo  */  
   WIWebShipTo:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGApartment  */  
   AGApartment:string,
      /**  AGExtraStreetNumber  */  
   AGExtraStreetNumber:string,
      /**  AGFloor  */  
   AGFloor:string,
      /**  AGGrossIncomeTaxID  */  
   AGGrossIncomeTaxID:string,
      /**  AGLocationCode  */  
   AGLocationCode:string,
      /**  AGNeighborhood  */  
   AGNeighborhood:string,
      /**  AGProvinceCode  */  
   AGProvinceCode:string,
      /**  AGStreet  */  
   AGStreet:string,
      /**  AGStreetNumber  */  
   AGStreetNumber:string,
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  Check if the part is a run out part.  */  
   DemandCheckForRunOutPart:boolean,
      /**  Indicates what type of action to take if the Check for Run Out Part option is selected and the part is marked as a run out part.  Options are B (reject the change) or W (warning - alert that the part is marked as run out but allow the record to be accepted).  */  
   DemandCheckForRunOutPartAction:string,
      /**  INExciseRegNumber  */  
   INExciseRegNumber:string,
      /**  INVATNumber  */  
   INVATNumber:string,
      /**  INSTRegistration  */  
   INSTRegistration:string,
      /**  MXCURP  */  
   MXCURP:string,
      /**  MXMunicipio  */  
   MXMunicipio:string,
      /**  MXFederalID  */  
   MXFederalID:string,
      /**  INTaxRegistrationID  */  
   INTaxRegistrationID:string,
      /**  Geographical Location Code  */  
   PEUBIGEOCode:string,
      /**  EORI Number  */  
   EORINumber:string,
      /**  Tax ID Validation Status: Not Validated – 0, Valid – 1, Invalid – 2.  */  
   TaxValidationStatus:number,
      /**  Tax Validation Date  */  
   TaxValidationDate:string,
      /**  HMRCTaxValidationLog  */  
   HMRCTaxValidationLog:string,
      /**  Indicates if the record is inactive.  */  
   Inactive:boolean,
      /**  FSMRegionCode  */  
   FSMRegionCode:string,
      /**  FSMArea  */  
   FSMArea:string,
      /**  List of fields which are referenced by COA segments.  */  
   COASegReferences:string,
      /**  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  */  
   ContactName:string,
      /**  Display Format String  */  
   DspFormatStr:string,
      /**  Indicates if ShipTo is Global (Master or Linked)  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany, GlbCustNum and GlbShipto that is linking to this shipto  */  
   GlbLink:string,
      /**  Indicates Integration with financial package (like EuroFin)  */  
   IntegrationFlag:boolean,
      /**  Flag used for integrations whether to run the on change country logic.  */  
   IntRunChangeCountry:boolean,
   PeriodicityDesc:string,
      /**  List of available Periodicity values  */  
   PeriodicityList:string,
      /**  Used to indicate if primary shipto.  Updates Customer.ShipToNum field  */  
   PrimaryShipTo:boolean,
      /**  Sales Tax ID  */  
   SalesTaxID:string,
      /**  Service Tax ID  */  
   ServiceTaxID:string,
   TerritorySelectDescription:string,
      /**  Use this field to display/update; replaces TerritorySelect  */  
   TerrSelectFlag:string,
      /**  Address in formatted delimited list  */  
   AddrList:string,
   LanguageDescription:string,
   BitFlag:number,
   AGLocationDescription:string,
   AGProvinceDescription:string,
   CountryISOCode:string,
   CountryEUMember:boolean,
   CustNumName:string,
   CustNumCustID:string,
   CustNumBTName:string,
   DeliveryTypeDescription:string,
   MasterCustIDBTName:string,
   MasterCustIDCustID:string,
   MasterCustIDName:string,
   SalesRepName:string,
   ShipViaWebDesc:string,
   ShipViaDescription:string,
   TATaxAuthorityDescription:string,
   TaxRegionDescription:string,
   TerritoryTerritoryDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ContactName
      @param CustNumList
      @param inCustNum
      @param inShipToNum
      @param inConNum
   */  
export interface GetByID_input{
      /**  The Contact Name  */  
   ContactName:string,
      /**  Delimited list of customer numbers selected  */  
   CustNumList:string,
      /**  Specific Customer number.  Used for context menu  */  
   inCustNum:number,
      /**  Specific ShipTo Number.  Used for context menu  */  
   inShipToNum:string,
      /**  Specific Contact Number.  Used for context menu  */  
   inConNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ContactTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param whereClause
      @param shipToWhereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListCustom_input{
      /**  Where condition  */  
   whereClause:string,
      /**  ShipTo Where condition  */  
   shipToWhereClause:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetListCustom_output{
   returnObj:Erp_Tablesets_ContactListTableset[],
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
      /**  Where condition  */  
   whereClause:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_ContactListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param CustNum
      @param ShipToNum
      @param ConNum
   */  
export interface GetNewCustCntAttch_input{
      /**  The Customer Number  */  
   CustNum:number,
      /**  The ShipTo Number  */  
   ShipToNum:string,
      /**  The Contact Number  */  
   ConNum:number,
}

export interface GetNewCustCntAttch_output{
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

