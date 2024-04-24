import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.NARelationshipSvc
// Description: National Account Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/$metadata", {
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
   Description: Get NARelationships items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NARelationships
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RlsHeadRow
   */  
export function get_NARelationships(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NARelationships
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RlsHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RlsHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NARelationships(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships", {
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
   Summary: Calls GetByID to retrieve the NARelationship item
   Description: Calls GetByID to retrieve the NARelationship item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NARelationship
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RlsHeadRow
   */  
export function get_NARelationships_Company_RlsClassCode_TopCustNum_CustNum(Company:string, RlsClassCode:string, TopCustNum:string, CustNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RlsHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RlsHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update NARelationship for the service
   Description: Calls UpdateExt to update NARelationship. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NARelationship
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RlsHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_NARelationships_Company_RlsClassCode_TopCustNum_CustNum(Company:string, RlsClassCode:string, TopCustNum:string, CustNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + ")", {
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
   Summary: Call UpdateExt to delete NARelationship item
   Description: Call UpdateExt to delete NARelationship item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NARelationship
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_NARelationships_Company_RlsClassCode_TopCustNum_CustNum(Company:string, RlsClassCode:string, TopCustNum:string, CustNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get RlsParents items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RlsParents1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RlsParentRow
   */  
export function get_NARelationships_Company_RlsClassCode_TopCustNum_CustNum_RlsParents(Company:string, RlsClassCode:string, TopCustNum:string, CustNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsParentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + ")/RlsParents", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsParentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RlsParent item
   Description: Calls GetByID to retrieve the RlsParent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RlsParent1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param ParentCustNum Desc: ParentCustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RlsParentRow
   */  
export function get_NARelationships_Company_RlsClassCode_TopCustNum_CustNum_RlsParents_Company_RlsClassCode_TopCustNum_CustNum_ParentCustNum(Company:string, RlsClassCode:string, TopCustNum:string, CustNum:string, ParentCustNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RlsParentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + ")/RlsParents(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + "," + ParentCustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RlsParentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RlsParents items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RlsParents
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RlsParentRow
   */  
export function get_RlsParents(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsParentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/RlsParents", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsParentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RlsParents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RlsParentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RlsParentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RlsParents(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/RlsParents", {
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
   Summary: Calls GetByID to retrieve the RlsParent item
   Description: Calls GetByID to retrieve the RlsParent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RlsParent
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param ParentCustNum Desc: ParentCustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RlsParentRow
   */  
export function get_RlsParents_Company_RlsClassCode_TopCustNum_CustNum_ParentCustNum(Company:string, RlsClassCode:string, TopCustNum:string, CustNum:string, ParentCustNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RlsParentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/RlsParents(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + "," + ParentCustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RlsParentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RlsParent for the service
   Description: Calls UpdateExt to update RlsParent. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RlsParent
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param ParentCustNum Desc: ParentCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RlsParentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RlsParents_Company_RlsClassCode_TopCustNum_CustNum_ParentCustNum(Company:string, RlsClassCode:string, TopCustNum:string, CustNum:string, ParentCustNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/RlsParents(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + "," + ParentCustNum + ")", {
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
   Summary: Call UpdateExt to delete RlsParent item
   Description: Call UpdateExt to delete RlsParent item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RlsParent
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param ParentCustNum Desc: ParentCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RlsParents_Company_RlsClassCode_TopCustNum_CustNum_ParentCustNum(Company:string, RlsClassCode:string, TopCustNum:string, CustNum:string, ParentCustNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/RlsParents(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + "," + ParentCustNum + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get CreditPoolHeads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CreditPoolHeads
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditPoolHeadRow
   */  
export function get_CreditPoolHeads(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditPoolHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditPoolHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CreditPoolHeads
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CreditPoolHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CreditPoolHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreditPoolHeads(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads", {
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
   Summary: Calls GetByID to retrieve the CreditPoolHead item
   Description: Calls GetByID to retrieve the CreditPoolHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditPoolHead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CrdPoolCode Desc: CrdPoolCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditPoolHeadRow
   */  
export function get_CreditPoolHeads_Company_RlsClassCode_TopCustNum_CrdPoolCode(Company:string, RlsClassCode:string, TopCustNum:string, CrdPoolCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CreditPoolHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CreditPoolHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CreditPoolHead for the service
   Description: Calls UpdateExt to update CreditPoolHead. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CreditPoolHead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CrdPoolCode Desc: CrdPoolCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CreditPoolHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CreditPoolHeads_Company_RlsClassCode_TopCustNum_CrdPoolCode(Company:string, RlsClassCode:string, TopCustNum:string, CrdPoolCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + ")", {
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
   Summary: Call UpdateExt to delete CreditPoolHead item
   Description: Call UpdateExt to delete CreditPoolHead item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CreditPoolHead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CrdPoolCode Desc: CrdPoolCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CreditPoolHeads_Company_RlsClassCode_TopCustNum_CrdPoolCode(Company:string, RlsClassCode:string, TopCustNum:string, CrdPoolCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get CreditPoolDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CreditPoolDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CrdPoolCode Desc: CrdPoolCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditPoolDtlRow
   */  
export function get_CreditPoolHeads_Company_RlsClassCode_TopCustNum_CrdPoolCode_CreditPoolDtls(Company:string, RlsClassCode:string, TopCustNum:string, CrdPoolCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditPoolDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + ")/CreditPoolDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditPoolDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CreditPoolDtl item
   Description: Calls GetByID to retrieve the CreditPoolDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditPoolDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CrdPoolCode Desc: CrdPoolCode   Required: True   Allow empty value : True
      @param ShareCustNum Desc: ShareCustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditPoolDtlRow
   */  
export function get_CreditPoolHeads_Company_RlsClassCode_TopCustNum_CrdPoolCode_CreditPoolDtls_Company_RlsClassCode_TopCustNum_CrdPoolCode_ShareCustNum(Company:string, RlsClassCode:string, TopCustNum:string, CrdPoolCode:string, ShareCustNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CreditPoolDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + ")/CreditPoolDtls(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + "," + ShareCustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CreditPoolDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CreditPoolDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CreditPoolDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditPoolDtlRow
   */  
export function get_CreditPoolDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditPoolDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditPoolDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CreditPoolDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CreditPoolDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CreditPoolDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreditPoolDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolDtls", {
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
   Summary: Calls GetByID to retrieve the CreditPoolDtl item
   Description: Calls GetByID to retrieve the CreditPoolDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditPoolDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CrdPoolCode Desc: CrdPoolCode   Required: True   Allow empty value : True
      @param ShareCustNum Desc: ShareCustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditPoolDtlRow
   */  
export function get_CreditPoolDtls_Company_RlsClassCode_TopCustNum_CrdPoolCode_ShareCustNum(Company:string, RlsClassCode:string, TopCustNum:string, CrdPoolCode:string, ShareCustNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CreditPoolDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolDtls(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + "," + ShareCustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CreditPoolDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CreditPoolDtl for the service
   Description: Calls UpdateExt to update CreditPoolDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CreditPoolDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CrdPoolCode Desc: CrdPoolCode   Required: True   Allow empty value : True
      @param ShareCustNum Desc: ShareCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CreditPoolDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CreditPoolDtls_Company_RlsClassCode_TopCustNum_CrdPoolCode_ShareCustNum(Company:string, RlsClassCode:string, TopCustNum:string, CrdPoolCode:string, ShareCustNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolDtls(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + "," + ShareCustNum + ")", {
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
   Summary: Call UpdateExt to delete CreditPoolDtl item
   Description: Call UpdateExt to delete CreditPoolDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CreditPoolDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RlsClassCode Desc: RlsClassCode   Required: True   Allow empty value : True
      @param TopCustNum Desc: TopCustNum   Required: True
      @param CrdPoolCode Desc: CrdPoolCode   Required: True   Allow empty value : True
      @param ShareCustNum Desc: ShareCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CreditPoolDtls_Company_RlsClassCode_TopCustNum_CrdPoolCode_ShareCustNum(Company:string, RlsClassCode:string, TopCustNum:string, CrdPoolCode:string, ShareCustNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolDtls(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + "," + ShareCustNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RlsHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsHeadListRow)
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseRlsHead:string, whereClauseRlsParent:string, whereClauseCreditPoolHead:string, whereClauseCreditPoolDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRlsHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRlsHead=" + whereClauseRlsHead
   }
   if(typeof whereClauseRlsParent!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRlsParent=" + whereClauseRlsParent
   }
   if(typeof whereClauseCreditPoolHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCreditPoolHead=" + whereClauseCreditPoolHead
   }
   if(typeof whereClauseCreditPoolDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCreditPoolDtl=" + whereClauseCreditPoolDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/GetRows" + params, {
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(rlsClassCode:string, topCustNum:string, custNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof rlsClassCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rlsClassCode=" + rlsClassCode
   }
   if(typeof topCustNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "topCustNum=" + topCustNum
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/GetList" + params, {
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
   Summary: Invoke method AddChildCustomer
   Description: Add Child to the Customer for both tiered and non tiered classes
   OperationID: AddChildCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddChildCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddChildCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddChildCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/AddChildCustomer", {
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
   Summary: Invoke method CustListPayFor
   Description: Gets list CustNum of customers which can be payed by Customer ipPayerCustNum
   OperationID: CustListPayFor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustListPayFor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustListPayFor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustListPayFor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CustListPayFor", {
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
   Summary: Invoke method GetNAData
   Description: Get National Accout dataset by RlsClass and any Customer from Relationship (TODO-rename parameters TopCust with Cust)
   OperationID: GetNAData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNAData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNAData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNAData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/GetNAData", {
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
   Summary: Invoke method MoveChildCustomer
   Description: MoveChildCustomer
   OperationID: MoveChildCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveChildCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveChildCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveChildCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/MoveChildCustomer", {
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
   Summary: Invoke method OnChangeCustID
   Description: Check Cust Id, get Name, Num
   OperationID: OnChangeCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/OnChangeCustID", {
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
   Summary: Invoke method OnChangeGlobalNAGroup
   Description: Check all customers if they are Global if the flag was set
   OperationID: OnChangeGlobalNAGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeGlobalNAGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeGlobalNAGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeGlobalNAGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/OnChangeGlobalNAGroup", {
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
   Summary: Invoke method OnChangeParentCustID
   Description: Check Parent Cust Id for non tiered Relationship
   OperationID: OnChangeParentCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeParentCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeParentCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeParentCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/OnChangeParentCustID", {
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
   Summary: Invoke method OnChangeRlsClassCode
   Description: Check Rls Class Code
   OperationID: OnChangeRlsClassCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRlsClassCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRlsClassCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRlsClassCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/OnChangeRlsClassCode", {
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
   Summary: Invoke method SetGlobalCustomer
   Description: Purpose: Set Glabal customer
   OperationID: SetGlobalCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetGlobalCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetGlobalCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetGlobalCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/SetGlobalCustomer", {
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
   Summary: Invoke method SetGlobalNACustomers
   Description: Purpose: Set Global flag to all customers in National Account
   OperationID: SetGlobalNACustomers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetGlobalNACustomers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetGlobalNACustomers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetGlobalNACustomers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/SetGlobalNACustomers", {
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
   Summary: Invoke method GetNewRlsHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRlsHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRlsHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRlsHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRlsHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/GetNewRlsHead", {
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
   Summary: Invoke method GetNewRlsParent
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRlsParent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRlsParent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRlsParent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRlsParent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/GetNewRlsParent", {
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
   Summary: Invoke method GetNewCreditPoolHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCreditPoolHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCreditPoolHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCreditPoolHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCreditPoolHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/GetNewCreditPoolHead", {
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
   Summary: Invoke method GetNewCreditPoolDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCreditPoolDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCreditPoolDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCreditPoolDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCreditPoolDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/GetNewCreditPoolDtl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditPoolDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CreditPoolDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditPoolHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CreditPoolHeadRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RlsHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RlsHeadRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsParentRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RlsParentRow[],
}

export interface Erp_Tablesets_CreditPoolDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for the Relationship Class  */  
   "RlsClassCode":string,
      /**  A  unique code of Customer on the Top  */  
   "TopCustNum":number,
      /**  unique identifier for the credit pool  */  
   "CrdPoolCode":string,
      /**  Customer from NA which has access to credit pool  */  
   "ShareCustNum":number,
      /**  The Maximum percentage of the credit pool amount that the customer could use  */  
   "PrcShare":number,
      /**  Credit used by this customer in base currency  */  
   "CreditUsed":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "ShareCustomerName":string,
   "ShareCustomerBTName":string,
   "ShareCustomerCustID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CreditPoolHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for the Relationship Class  */  
   "RlsClassCode":string,
      /**  A  unique code of Customer on the Top  */  
   "TopCustNum":number,
      /**  unique identifier for the credit pool  */  
   "CrdPoolCode":string,
      /**  Credit amount that could be used by the customers with access to the credit pool - in base currency  */  
   "PoolAmount":number,
      /**  Available Credit amount that could be used by the customers with access to the credit pool - in base currency  */  
   "AmtAvailable":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RlsHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for the Relationship Class  */  
   "RlsClassCode":string,
      /**  A  unique code of Customer on the Top  */  
   "TopCustNum":number,
      /**  A  unique code of the current Customer  */  
   "CustNum":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Customer ID of the current customer (link)  */  
   "CustomerCustID":string,
      /**  RlsClass is Tiered (link)  */  
   "RlsClassTiered":boolean,
      /**  Cust Id of Top Customer (link)  */  
   "TopCustomerCustID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RlsHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for the Relationship Class  */  
   "RlsClassCode":string,
      /**  A  unique code of Customer on the Top  */  
   "TopCustNum":number,
      /**  A  unique code of the current Customer  */  
   "CustNum":number,
      /**  key unique for whole UnTiered Group  */  
   "UnTieredGroup":number,
      /**  Level number for tiered Relationship  */  
   "TierLevelNum":number,
      /**  Determines whether or not National Account is shared between more than one company.  */  
   "GlobalNA":boolean,
      /**  shows if Credit Data or Credit Relationship has been updated, it is used for recalculation process  */  
   "IsCreditUpdated":boolean,
      /**  Starting AR Total when Customer was added to the National Account (in Customer Global Currency)  */  
   "DocStartARTotal":number,
      /**  Starting SO Total when Customer was added to the National Account (in Customer Global Currency)  */  
   "DocStartSOTotal":number,
      /**  Starting PI Total when Customer was added to the National Account (in Customer Global Currency)  */  
   "DocStartPITotal":number,
      /**  Starting AR Total when Customer was added to the National Account (in Base Currency)  */  
   "StartARTotal":number,
      /**  Starting AR Total when Customer was added to the National Account (in Base Currency)  */  
   "StartSOTotal":number,
      /**  Starting AR Total when Customer was added to the National Account (in Base Currency)  */  
   "StartPITotal":number,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when System when customer was added to National Account  */  
   "SysTime":number,
      /**  current number of the Sequence NACreditDocSeq when custromer was added to NA  */  
   "Seq":number,
      /**  Stores the keys (CustNum) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   "Lineage":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "dspTierLabel":string,
      /**  String level (for tiered Class), empty for non tiered  */  
   "dspTierLevel":string,
   "NewChildCustID":string,
      /**  New Customer Name added as child for tiered relationship  */  
   "NewChildCustName":string,
      /**  New Customer ID added as child for tiered relationship or parent for non tiered relationship  */  
   "NewCustID":string,
      /**  New Customer Name added as parent for non tiered relationship  */  
   "NewCustName":string,
      /**  reference to Parent Customer Used for tiered Relationship  */  
   "ParentCustNum":number,
      /**  Parent Cust ID for tiered Class  */  
   "ParentCustID":string,
      /**  Top Customer is Global  */  
   "TopCustomerIsGlobal":boolean,
      /**  link to RlsGroup  */  
   "GlobalNAGroup":boolean,
      /**  link to RlsGroup  */  
   "IsCreditUpdatedGroup":boolean,
      /**  Selected Customer ID - for tiered classes only  */  
   "SelectedCustID":string,
      /**  Selected Customer Name - for tiered classes only  */  
   "SelectedCustName":string,
   "BitFlag":number,
   "CustomerName":string,
   "CustomerBTName":string,
   "CustomerCustID":string,
   "RlsClassTiered":boolean,
   "RlsClassDescription":string,
   "TopCustomerName":string,
   "TopCustomerBTName":string,
   "TopCustomerCustID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RlsParentRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for the Relationship Class  */  
   "RlsClassCode":string,
      /**  A  unique code of Customer on the Top  */  
   "TopCustNum":number,
      /**  A  unique code of the current Customer  */  
   "CustNum":number,
      /**  Code of the Parent for current Customer  */  
   "ParentCustNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "ParentCustomerName":string,
   "ParentCustomerCustID":string,
   "ParentCustomerBTName":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
      @param ipRlsClassCode
      @param ipTopCustNum
      @param ipCustNum
      @param ipChildCustID
   */  
export interface AddChildCustomer_input{
   ds:Erp_Tablesets_NARelationshipTableset[],
      /**  RlsClass.RlsClassCode  */  
   ipRlsClassCode:string,
      /**  Top Cust Num  */  
   ipTopCustNum:number,
      /**  Parent Cust Num  */  
   ipCustNum:number,
      /**  Child CustID  */  
   ipChildCustID:string,
}

export interface AddChildCustomer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NARelationshipTableset[],
   errorMsg:string,
}
}

   /** Required : 
      @param ipPayerCustNum
   */  
export interface CustListPayFor_input{
      /**  Payer Cust Num  */  
   ipPayerCustNum:number,
}

export interface CustListPayFor_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   listPayFor:string,
}
}

   /** Required : 
      @param rlsClassCode
      @param topCustNum
      @param custNum
   */  
export interface DeleteByID_input{
   rlsClassCode:string,
   topCustNum:number,
   custNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CreditPoolDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for the Relationship Class  */  
   RlsClassCode:string,
      /**  A  unique code of Customer on the Top  */  
   TopCustNum:number,
      /**  unique identifier for the credit pool  */  
   CrdPoolCode:string,
      /**  Customer from NA which has access to credit pool  */  
   ShareCustNum:number,
      /**  The Maximum percentage of the credit pool amount that the customer could use  */  
   PrcShare:number,
      /**  Credit used by this customer in base currency  */  
   CreditUsed:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   ShareCustomerName:string,
   ShareCustomerBTName:string,
   ShareCustomerCustID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CreditPoolHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for the Relationship Class  */  
   RlsClassCode:string,
      /**  A  unique code of Customer on the Top  */  
   TopCustNum:number,
      /**  unique identifier for the credit pool  */  
   CrdPoolCode:string,
      /**  Credit amount that could be used by the customers with access to the credit pool - in base currency  */  
   PoolAmount:number,
      /**  Available Credit amount that could be used by the customers with access to the credit pool - in base currency  */  
   AmtAvailable:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_NARelationshipListTableset{
   RlsHeadList:Erp_Tablesets_RlsHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_NARelationshipTableset{
   RlsHead:Erp_Tablesets_RlsHeadRow[],
   RlsParent:Erp_Tablesets_RlsParentRow[],
   CreditPoolHead:Erp_Tablesets_CreditPoolHeadRow[],
   CreditPoolDtl:Erp_Tablesets_CreditPoolDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RlsHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for the Relationship Class  */  
   RlsClassCode:string,
      /**  A  unique code of Customer on the Top  */  
   TopCustNum:number,
      /**  A  unique code of the current Customer  */  
   CustNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Customer ID of the current customer (link)  */  
   CustomerCustID:string,
      /**  RlsClass is Tiered (link)  */  
   RlsClassTiered:boolean,
      /**  Cust Id of Top Customer (link)  */  
   TopCustomerCustID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RlsHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for the Relationship Class  */  
   RlsClassCode:string,
      /**  A  unique code of Customer on the Top  */  
   TopCustNum:number,
      /**  A  unique code of the current Customer  */  
   CustNum:number,
      /**  key unique for whole UnTiered Group  */  
   UnTieredGroup:number,
      /**  Level number for tiered Relationship  */  
   TierLevelNum:number,
      /**  Determines whether or not National Account is shared between more than one company.  */  
   GlobalNA:boolean,
      /**  shows if Credit Data or Credit Relationship has been updated, it is used for recalculation process  */  
   IsCreditUpdated:boolean,
      /**  Starting AR Total when Customer was added to the National Account (in Customer Global Currency)  */  
   DocStartARTotal:number,
      /**  Starting SO Total when Customer was added to the National Account (in Customer Global Currency)  */  
   DocStartSOTotal:number,
      /**  Starting PI Total when Customer was added to the National Account (in Customer Global Currency)  */  
   DocStartPITotal:number,
      /**  Starting AR Total when Customer was added to the National Account (in Base Currency)  */  
   StartARTotal:number,
      /**  Starting AR Total when Customer was added to the National Account (in Base Currency)  */  
   StartSOTotal:number,
      /**  Starting AR Total when Customer was added to the National Account (in Base Currency)  */  
   StartPITotal:number,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when System when customer was added to National Account  */  
   SysTime:number,
      /**  current number of the Sequence NACreditDocSeq when custromer was added to NA  */  
   Seq:number,
      /**  Stores the keys (CustNum) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   Lineage:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   dspTierLabel:string,
      /**  String level (for tiered Class), empty for non tiered  */  
   dspTierLevel:string,
   NewChildCustID:string,
      /**  New Customer Name added as child for tiered relationship  */  
   NewChildCustName:string,
      /**  New Customer ID added as child for tiered relationship or parent for non tiered relationship  */  
   NewCustID:string,
      /**  New Customer Name added as parent for non tiered relationship  */  
   NewCustName:string,
      /**  reference to Parent Customer Used for tiered Relationship  */  
   ParentCustNum:number,
      /**  Parent Cust ID for tiered Class  */  
   ParentCustID:string,
      /**  Top Customer is Global  */  
   TopCustomerIsGlobal:boolean,
      /**  link to RlsGroup  */  
   GlobalNAGroup:boolean,
      /**  link to RlsGroup  */  
   IsCreditUpdatedGroup:boolean,
      /**  Selected Customer ID - for tiered classes only  */  
   SelectedCustID:string,
      /**  Selected Customer Name - for tiered classes only  */  
   SelectedCustName:string,
   BitFlag:number,
   CustomerName:string,
   CustomerBTName:string,
   CustomerCustID:string,
   RlsClassTiered:boolean,
   RlsClassDescription:string,
   TopCustomerName:string,
   TopCustomerBTName:string,
   TopCustomerCustID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RlsParentRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for the Relationship Class  */  
   RlsClassCode:string,
      /**  A  unique code of Customer on the Top  */  
   TopCustNum:number,
      /**  A  unique code of the current Customer  */  
   CustNum:number,
      /**  Code of the Parent for current Customer  */  
   ParentCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   ParentCustomerName:string,
   ParentCustomerCustID:string,
   ParentCustomerBTName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtNARelationshipTableset{
   RlsHead:Erp_Tablesets_RlsHeadRow[],
   RlsParent:Erp_Tablesets_RlsParentRow[],
   CreditPoolHead:Erp_Tablesets_CreditPoolHeadRow[],
   CreditPoolDtl:Erp_Tablesets_CreditPoolDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param rlsClassCode
      @param topCustNum
      @param custNum
   */  
export interface GetByID_input{
   rlsClassCode:string,
   topCustNum:number,
   custNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_NARelationshipTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_NARelationshipTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_NARelationshipTableset[],
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
   returnObj:Erp_Tablesets_NARelationshipListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipRlsClassCode
      @param ipTopCustID
      @param ipNewNA
   */  
export interface GetNAData_input{
      /**  RlsClass.RlsClassCode  */  
   ipRlsClassCode:string,
      /**  Customer CustID  */  
   ipTopCustID:string,
      /**  Is it a new record  */  
   ipNewNA:boolean,
}

export interface GetNAData_output{
   returnObj:Erp_Tablesets_NARelationshipTableset[],
parameters : {
      /**  output parameters  */  
   pTopCustNum:number,
   errorMsg:string,
}
}

   /** Required : 
      @param ds
      @param rlsClassCode
      @param topCustNum
      @param crdPoolCode
   */  
export interface GetNewCreditPoolDtl_input{
   ds:Erp_Tablesets_NARelationshipTableset[],
   rlsClassCode:string,
   topCustNum:number,
   crdPoolCode:string,
}

export interface GetNewCreditPoolDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NARelationshipTableset[],
}
}

   /** Required : 
      @param ds
      @param rlsClassCode
      @param topCustNum
   */  
export interface GetNewCreditPoolHead_input{
   ds:Erp_Tablesets_NARelationshipTableset[],
   rlsClassCode:string,
   topCustNum:number,
}

export interface GetNewCreditPoolHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NARelationshipTableset[],
}
}

   /** Required : 
      @param ds
      @param rlsClassCode
      @param topCustNum
   */  
export interface GetNewRlsHead_input{
   ds:Erp_Tablesets_NARelationshipTableset[],
   rlsClassCode:string,
   topCustNum:number,
}

export interface GetNewRlsHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NARelationshipTableset[],
}
}

   /** Required : 
      @param ds
      @param rlsClassCode
      @param topCustNum
      @param custNum
   */  
export interface GetNewRlsParent_input{
   ds:Erp_Tablesets_NARelationshipTableset[],
   rlsClassCode:string,
   topCustNum:number,
   custNum:number,
}

export interface GetNewRlsParent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NARelationshipTableset[],
}
}

   /** Required : 
      @param whereClauseRlsHead
      @param whereClauseRlsParent
      @param whereClauseCreditPoolHead
      @param whereClauseCreditPoolDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRlsHead:string,
   whereClauseRlsParent:string,
   whereClauseCreditPoolHead:string,
   whereClauseCreditPoolDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_NARelationshipTableset[],
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
      @param ipRlsClassCode
      @param ipTopCustNum
      @param ipCustNum
      @param ipTargetCustNum
   */  
export interface MoveChildCustomer_input{
   ds:Erp_Tablesets_NARelationshipTableset[],
      /**  RlsClass.RlsClassCode  */  
   ipRlsClassCode:string,
      /**  Customer CustID  */  
   ipTopCustNum:number,
      /**  Customer CustID  */  
   ipCustNum:number,
      /**  Customer CustID  */  
   ipTargetCustNum:number,
}

export interface MoveChildCustomer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NARelationshipTableset[],
   errorMsg:string,
}
}

   /** Required : 
      @param ipCustID
   */  
export interface OnChangeCustID_input{
      /**  Customer ID  */  
   ipCustID:string,
}

export interface OnChangeCustID_output{
parameters : {
      /**  output parameters  */  
   pCustName:string,
}
}

   /** Required : 
      @param ds
      @param ipRlsGlobal
   */  
export interface OnChangeGlobalNAGroup_input{
   ds:Erp_Tablesets_NARelationshipTableset[],
      /**  Global flag  */  
   ipRlsGlobal:boolean,
}

export interface OnChangeGlobalNAGroup_output{
parameters : {
      /**  output parameters  */  
   isSetGlobal:boolean,
}
}

   /** Required : 
      @param ds
      @param ipParentCustID
   */  
export interface OnChangeParentCustID_input{
   ds:Erp_Tablesets_NARelationshipTableset[],
      /**  Parent CustID  */  
   ipParentCustID:string,
}

export interface OnChangeParentCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NARelationshipTableset[],
}
}

   /** Required : 
      @param ipRlsClassCode
   */  
export interface OnChangeRlsClassCode_input{
      /**  Relationship Class Code  */  
   ipRlsClassCode:string,
}

export interface OnChangeRlsClassCode_output{
parameters : {
      /**  output parameters  */  
   errorMsg:string,
}
}

   /** Required : 
      @param ipCustID
   */  
export interface SetGlobalCustomer_input{
   ipCustID:string,
}

export interface SetGlobalCustomer_output{
}

   /** Required : 
      @param ds
   */  
export interface SetGlobalNACustomers_input{
   ds:Erp_Tablesets_NARelationshipTableset[],
}

export interface SetGlobalNACustomers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NARelationshipTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtNARelationshipTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtNARelationshipTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_NARelationshipTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NARelationshipTableset[],
}
}

