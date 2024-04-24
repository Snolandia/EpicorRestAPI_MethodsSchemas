import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.DemandEntrySvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/$metadata", {
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
   Description: Get DemandEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandHeadRow
   */  
export function get_DemandEntries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandEntries(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries", {
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
   Summary: Calls GetByID to retrieve the DemandEntry item
   Description: Calls GetByID to retrieve the DemandEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandHeadRow
   */  
export function get_DemandEntries_Company_DemandContractNum_DemandHeadSeq(Company:string, DemandContractNum:string, DemandHeadSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemandHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandEntry for the service
   Description: Calls UpdateExt to update DemandEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandEntries_Company_DemandContractNum_DemandHeadSeq(Company:string, DemandContractNum:string, DemandHeadSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")", {
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
   Summary: Call UpdateExt to delete DemandEntry item
   Description: Call UpdateExt to delete DemandEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandEntries_Company_DemandContractNum_DemandHeadSeq(Company:string, DemandContractNum:string, DemandHeadSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")", {
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
   Description: Get DemandDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandDetails1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandDetailRow
   */  
export function get_DemandEntries_Company_DemandContractNum_DemandHeadSeq_DemandDetails(Company:string, DemandContractNum:string, DemandHeadSeq:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandDetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DemandDetail item
   Description: Calls GetByID to retrieve the DemandDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandDetail1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandDetailRow
   */  
export function get_DemandEntries_Company_DemandContractNum_DemandHeadSeq_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemandDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DemandMiscChgDHs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandMiscChgDHs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgDHRow
   */  
export function get_DemandEntries_Company_DemandContractNum_DemandHeadSeq_DemandMiscChgDHs(Company:string, DemandContractNum:string, DemandHeadSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgDHRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandMiscChgDHs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgDHRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DemandMiscChgDH item
   Description: Calls GetByID to retrieve the DemandMiscChgDH item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChgDH1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandMiscChgDHRow
   */  
export function get_DemandEntries_Company_DemandContractNum_DemandHeadSeq_DemandMiscChgDHs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandMiscChgDHRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandEntries(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandMiscChgDHs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemandMiscChgDHRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DemandDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandDetails
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandDetailRow
   */  
export function get_DemandDetails(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails", {
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
   Summary: Calls GetByID to retrieve the DemandDetail item
   Description: Calls GetByID to retrieve the DemandDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandDetailRow
   */  
export function get_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemandDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandDetail for the service
   Description: Calls UpdateExt to update DemandDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")", {
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
   Summary: Call UpdateExt to delete DemandDetail item
   Description: Call UpdateExt to delete DemandDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")", {
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
   Description: Get DemandMiscChgs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandMiscChgs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgRow
   */  
export function get_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandMiscChgs(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandMiscChgs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DemandMiscChg item
   Description: Calls GetByID to retrieve the DemandMiscChg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChg1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandMiscChgRow
   */  
export function get_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandMiscChgs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandMiscChgRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandMiscChgs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemandMiscChgRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DemandSchedules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandSchedules1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandScheduleRow
   */  
export function get_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandSchedules(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandScheduleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandSchedules", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandScheduleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DemandSchedule item
   Description: Calls GetByID to retrieve the DemandSchedule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandSchedule1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param DemandScheduleSeq Desc: DemandScheduleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandScheduleRow
   */  
export function get_DemandDetails_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandSchedules_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, DemandScheduleSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandScheduleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandDetails(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandSchedules(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemandScheduleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DemandMiscChgs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandMiscChgs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgRow
   */  
export function get_DemandMiscChgs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandMiscChgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandMiscChgs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgs", {
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
   Summary: Calls GetByID to retrieve the DemandMiscChg item
   Description: Calls GetByID to retrieve the DemandMiscChg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandMiscChgRow
   */  
export function get_DemandMiscChgs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandMiscChgRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemandMiscChgRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandMiscChg for the service
   Description: Calls UpdateExt to update DemandMiscChg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandMiscChg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandMiscChgs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete DemandMiscChg item
   Description: Call UpdateExt to delete DemandMiscChg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandMiscChg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandMiscChgs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
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
   Description: Get DemandSchedules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandSchedules
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandScheduleRow
   */  
export function get_DemandSchedules(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandScheduleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandSchedules", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandScheduleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandSchedules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandScheduleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandScheduleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandSchedules(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandSchedules", {
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
   Summary: Calls GetByID to retrieve the DemandSchedule item
   Description: Calls GetByID to retrieve the DemandSchedule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandSchedule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param DemandScheduleSeq Desc: DemandScheduleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandScheduleRow
   */  
export function get_DemandSchedules_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, DemandScheduleSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandScheduleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandSchedules(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemandScheduleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandSchedule for the service
   Description: Calls UpdateExt to update DemandSchedule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandSchedule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param DemandScheduleSeq Desc: DemandScheduleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandScheduleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandSchedules_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, DemandScheduleSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandSchedules(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")", {
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
   Summary: Call UpdateExt to delete DemandSchedule item
   Description: Call UpdateExt to delete DemandSchedule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandSchedule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param DemandScheduleSeq Desc: DemandScheduleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandSchedules_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, DemandScheduleSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandSchedules(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")", {
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
   Description: Get DemandMiscChgDHs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandMiscChgDHs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgDHRow
   */  
export function get_DemandMiscChgDHs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgDHRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgDHs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgDHRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandMiscChgDHs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgDHRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgDHRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandMiscChgDHs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgDHs", {
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
   Summary: Calls GetByID to retrieve the DemandMiscChgDH item
   Description: Calls GetByID to retrieve the DemandMiscChgDH item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChgDH
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandMiscChgDHRow
   */  
export function get_DemandMiscChgDHs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandMiscChgDHRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgDHs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DemandMiscChgDHRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandMiscChgDH for the service
   Description: Calls UpdateExt to update DemandMiscChgDH. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandMiscChgDH
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgDHRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandMiscChgDHs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgDHs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete DemandMiscChgDH item
   Description: Call UpdateExt to delete DemandMiscChgDH item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandMiscChgDH
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandMiscChgDHs_Company_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DemandMiscChgDHs(" + Company + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseDemandHead:string, whereClauseDemandDetail:string, whereClauseDemandMiscChg:string, whereClauseDemandSchedule:string, whereClauseDemandMiscChgDH:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDemandHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemandHead=" + whereClauseDemandHead
   }
   if(typeof whereClauseDemandDetail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemandDetail=" + whereClauseDemandDetail
   }
   if(typeof whereClauseDemandMiscChg!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemandMiscChg=" + whereClauseDemandMiscChg
   }
   if(typeof whereClauseDemandSchedule!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemandSchedule=" + whereClauseDemandSchedule
   }
   if(typeof whereClauseDemandMiscChgDH!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemandMiscChgDH=" + whereClauseDemandMiscChgDH
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetRows" + params, {
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(demandContractNum:string, demandHeadSeq:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof demandContractNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "demandContractNum=" + demandContractNum
   }
   if(typeof demandHeadSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "demandHeadSeq=" + demandHeadSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetList" + params, {
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
   Summary: Invoke method GetBasePartAndConfigType
   Description: Retrieve the based configured part and config type
   OperationID: GetBasePartAndConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartAndConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartAndConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBasePartAndConfigType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetBasePartAndConfigType", {
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
   Summary: Invoke method GetBasePartForConfig
   Description: This method will retrieve the base configured part number to be passed
to configuration entry
   OperationID: GetBasePartForConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartForConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartForConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBasePartForConfig(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetBasePartForConfig", {
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
   Summary: Invoke method BuildDisplayAddress
   Description: Format a list of addresses into a display string.
   OperationID: BuildDisplayAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildDisplayAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildDisplayAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildDisplayAddress(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/BuildDisplayAddress", {
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
   Summary: Invoke method GetCreateCycleListValues
   Description: Public method to return the list values of getCreateCycleList
   OperationID: GetCreateCycleListValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCreateCycleListValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCreateCycleListValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCreateCycleListValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetCreateCycleListValues", {
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
   Summary: Invoke method ChangeCreateNewOrder
   Description: Update Demand Header information when the Bill To.
   OperationID: ChangeCreateNewOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCreateNewOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCreateNewOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCreateNewOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeCreateNewOrder", {
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
   Summary: Invoke method ChangeDemandDetailCustomerPrice
   Description: Update UnitPrice Based on Customer Price.
   OperationID: ChangeDemandDetailCustomerPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailCustomerPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailCustomerPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandDetailCustomerPrice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandDetailCustomerPrice", {
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
   Summary: Invoke method ChangeDemandDetailDemandContractLine
   Description: Update Demand Detail information when the Demand Contract Line is changed.
   OperationID: ChangeDemandDetailDemandContractLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailDemandContractLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailDemandContractLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandDetailDemandContractLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandDetailDemandContractLine", {
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
   Summary: Invoke method ChangeDemandDetailInternalPrice
   Description: Update UnitPrice Based on Internal Price.
   OperationID: ChangeDemandDetailInternalPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailInternalPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailInternalPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandDetailInternalPrice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandDetailInternalPrice", {
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
   Summary: Invoke method ChangeDemandDetailMktgCamp
   Description: Update MktgCampaign on the DmdCntDtl.
   OperationID: ChangeDemandDetailMktgCamp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailMktgCamp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailMktgCamp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandDetailMktgCamp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandDetailMktgCamp", {
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
   Summary: Invoke method ChangeDemandDetailPartNum
   Description: Update partnum on the DmdCntDtl.
   OperationID: ChangeDemandDetailPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandDetailPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandDetailPartNum", {
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
   Summary: Invoke method ChangeDemandDetailRevisionNum
   Description: Update Demand Detail information when the Part Revision Number is changed.
   OperationID: ChangeDemandDetailRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandDetailRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandDetailRevisionNum", {
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
   Summary: Invoke method ChangeDemandDetailUnitPrice
   Description: Update UnitPrice Base.
   OperationID: ChangeDemandDetailUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandDetailUnitPrice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandDetailUnitPrice", {
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
   Summary: Invoke method ChangeDemandDetailUOM
   Description: Update Demand Detail information when the SalesUM changes.
   OperationID: ChangeDemandDetailUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandDetailUOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandDetailUOM", {
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
   Summary: Invoke method ChangeDemandHeadBTCustID
   Description: Update Demand Header information when the Bill To.
   OperationID: ChangeDemandHeadBTCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadBTCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadBTCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadBTCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandHeadBTCustID", {
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
   Summary: Invoke method ChangeDemandHeadCancelPO
   Description: Update Demand Header information when the Cancel PO flag changes.
   OperationID: ChangeDemandHeadCancelPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadCancelPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadCancelPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadCancelPO(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandHeadCancelPO", {
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
   Summary: Invoke method ChangeDemandHeadDemandContract
   Description: Update Demand Header information when the Demand Contract is changed.
   OperationID: ChangeDemandHeadDemandContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadDemandContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadDemandContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadDemandContract(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandHeadDemandContract", {
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
   Summary: Invoke method ChangeDemandHeadDemandContractNum
   Description: Update Demand Header information when the Demand Contract is changed.
   OperationID: ChangeDemandHeadDemandContractNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadDemandContractNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadDemandContractNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadDemandContractNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandHeadDemandContractNum", {
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
   Summary: Invoke method ChangeDemandHeadERSOrder
   Description: Update Demand Header information when the ERS Order changes.
   OperationID: ChangeDemandHeadERSOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadERSOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadERSOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadERSOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandHeadERSOrder", {
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
   Summary: Invoke method ChangeDemandHeadShipToCustID
   Description: Method to call when changing the ShipTo Customer ID on the DemandHead record.
Validates the ShipTo Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeDemandHeadShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadShipToCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandHeadShipToCustID", {
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
   Summary: Invoke method ChangeDemandHeadShipToNum
   Description: Update Demand Header information when the Ship To Num changes.
   OperationID: ChangeDemandHeadShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadShipToNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandHeadShipToNum", {
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
   Summary: Invoke method ChangeDemandHeadUseOTS
   Description: Method to call when changing the UseOTS field the DemandHead record.
Refreshes the address list and contact info
   OperationID: ChangeDemandHeadUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadUseOTS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandHeadUseOTS", {
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
   Summary: Invoke method ChangeDemandScheduleCreateShipToNum
   Description: Update DemandScheduleCreate information with values from the Ship To when the Ship To is changed.
   OperationID: ChangeDemandScheduleCreateShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleCreateShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleCreateShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleCreateShipToNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandScheduleCreateShipToNum", {
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
   Summary: Invoke method ChangeDemandScheduleMarkForNum
   Description: Update DemandSchedule information with values from the Mark For when the Mark For is changed.
   OperationID: ChangeDemandScheduleMarkForNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleMarkForNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleMarkForNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleMarkForNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandScheduleMarkForNum", {
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
   Summary: Invoke method ChangeDemandScheduleMFCustID
   Description: Method to call when changing the Mark For Customer ID on the DemandSchedule record.
Validates the Mark For Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeDemandScheduleMFCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleMFCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleMFCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleMFCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandScheduleMFCustID", {
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
   Summary: Invoke method ChangeDemandScheduleNeedByDate
   Description: Calculate the DemandSchedule Ship Date when the NeedByDate is changed.
   OperationID: ChangeDemandScheduleNeedByDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleNeedByDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleNeedByDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleNeedByDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandScheduleNeedByDate", {
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
   Summary: Invoke method ChangeDemandScheduleDeliveryDays
   Description: Calculate the DemandSchedule ShipDate or NeedBy Date when the DeliveryDays are changed.
   OperationID: ChangeDemandScheduleDeliveryDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleDeliveryDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleDeliveryDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleDeliveryDays(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandScheduleDeliveryDays", {
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
   Summary: Invoke method ChangeDemandScheduleOTSDetails
   Description: Method to call when changing the OTS fields the DemandSchedule record.
Refreshes the address list and contact info
   OperationID: ChangeDemandScheduleOTSDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleOTSDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleOTSDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleOTSDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandScheduleOTSDetails", {
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
   Summary: Invoke method ChangeDemandSchedulePlant
   Description: Update DemandSchedule information with values from the Plant when the Plant is changed.
   OperationID: ChangeDemandSchedulePlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandSchedulePlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandSchedulePlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandSchedulePlant(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandSchedulePlant", {
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
   Summary: Invoke method ChangeDemandScheduleReqDate
   Description: Calculate the DemandSchedule NeedByDate when the Ship Date (ReqDate) is changed.
   OperationID: ChangeDemandScheduleReqDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleReqDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleReqDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleReqDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandScheduleReqDate", {
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
   Summary: Invoke method ChangeDemandScheduleSellingReqQty
   Description: Update Demand Schedule information when the Selling Req Qty is changed.
   OperationID: ChangeDemandScheduleSellingReqQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleSellingReqQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleSellingReqQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleSellingReqQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandScheduleSellingReqQty", {
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
   Summary: Invoke method ChangeDemandScheduleShipToCustID
   Description: Method to call when changing the ShipTo Customer ID on the DemandSchedule record.
Validates the ShipTo Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeDemandScheduleShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleShipToCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandScheduleShipToCustID", {
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
   Summary: Invoke method ChangeDemandScheduleShipToNum
   Description: Update DemandSchedule information with values from the Ship To when the Ship To is changed.
   OperationID: ChangeDemandScheduleShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleShipToNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandScheduleShipToNum", {
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
   Summary: Invoke method ChangeDemandScheduleUseOTMF
   Description: Method to call when changing the UseOTMF field the DemandSchedule record.
Refreshes the address list and contact info
   OperationID: ChangeDemandScheduleUseOTMF
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleUseOTMF_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleUseOTMF_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleUseOTMF(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandScheduleUseOTMF", {
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
   Summary: Invoke method ChangeDemandScheduleUseOTS
   Description: Method to call when changing the UseOTS field the DemandSchedule record.
Refreshes the address list and contact info
   OperationID: ChangeDemandScheduleUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleUseOTS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeDemandScheduleUseOTS", {
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
   Summary: Invoke method ChangeMiscAmount
   Description: Update Order Miscellaneous information when the amount changes.
   OperationID: ChangeMiscAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMiscAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMiscAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeMiscAmount", {
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
   Summary: Invoke method ChangeMiscCode
   Description: This method returns default information for the MiscChrg.  Method must use
parameters instead of the dataset due to the problem with changing the primary key field.
Also allows DemandMiscChgDH and DemandMiscChg to use the same code
   OperationID: ChangeMiscCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMiscCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMiscCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeMiscCode", {
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
   Summary: Invoke method ChangeMiscPercent
   Description: Update Order Miscellaneous information when the percentage was changed.
   OperationID: ChangeMiscPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMiscPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMiscPercent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ChangeMiscPercent", {
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
   Summary: Invoke method CheckPartRevisionChange
   Description: The method is to be run on leave of the PartNum and Revision fields
before the ChangePart, ChangeRevision, or Update methods are run.
When run before CreateOrderFromQuote, the Part Number expected is the part number
from the quote.
This returns all the questions that need to be asked before a part can be changed.
   OperationID: CheckPartRevisionChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPartRevisionChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartRevisionChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPartRevisionChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/CheckPartRevisionChange", {
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
   Summary: Invoke method CloseAllSchedules
   Description: Close All Schedules.
   OperationID: CloseAllSchedules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseAllSchedules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseAllSchedules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseAllSchedules(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/CloseAllSchedules", {
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
   Summary: Invoke method CloseDemandDetail
   Description: Closes the Demand detail and sub-table (DemandSchedule).
   OperationID: CloseDemandDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseDemandDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseDemandDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseDemandDetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/CloseDemandDetail", {
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
   Summary: Invoke method CloseDemandHead
   Description: Closes the Demand Header and sub-tables (DemandDetail and DemandSchedule).
   OperationID: CloseDemandHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseDemandHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseDemandHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseDemandHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/CloseDemandHead", {
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
   Summary: Invoke method CloseDemandSchedule
   Description: Closes the Demand Schedule record.
   OperationID: CloseDemandSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseDemandSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseDemandSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseDemandSchedule(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/CloseDemandSchedule", {
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
   Summary: Invoke method CreateDemandDetailFromContractLines
   Description: Create DemandDetail records from the contract lines selected.  This method
will create a DemandDetail record for each contract line where SelectedForDemand
is true.  After this method is run the GetRows or GetByID method should be called
so the dataset has the new DemandDetail records.
   OperationID: CreateDemandDetailFromContractLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateDemandDetailFromContractLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateDemandDetailFromContractLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateDemandDetailFromContractLines(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/CreateDemandDetailFromContractLines", {
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
   Summary: Invoke method DeleteScheduleByScheduleNumberKeepHeader
   Description: Delete Schedule by number, but return the existing header, details, and schedule rows
   OperationID: DeleteScheduleByScheduleNumberKeepHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteScheduleByScheduleNumberKeepHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteScheduleByScheduleNumberKeepHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteScheduleByScheduleNumberKeepHeader(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DeleteScheduleByScheduleNumberKeepHeader", {
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
   Summary: Invoke method DeleteScheduleByScheduleNumber
   Description: Deletes DemandSchedule records by Schedule Number.  All DemandSchedule records
where the Schedule Number equals the number passed in will be deleted.
cReturnMessage will return a message of how many records were deleted.
   OperationID: DeleteScheduleByScheduleNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteScheduleByScheduleNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteScheduleByScheduleNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteScheduleByScheduleNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DeleteScheduleByScheduleNumber", {
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
   Summary: Invoke method EDIHeaderValidate
   Description: Calls the method Process Demand To create a Sales Order.
   OperationID: EDIHeaderValidate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EDIHeaderValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EDIHeaderValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EDIHeaderValidate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/EDIHeaderValidate", {
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
   Summary: Invoke method GetDemandContractDtl
   Description: Get Demand Contract Detail lines for Create Demand Detail from Demand Contract
lines functionality.  The contract lines returned can be selected by the user
to indicate what contract lines to create Demand Detail records from.
   OperationID: GetDemandContractDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDemandContractDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDemandContractDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDemandContractDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetDemandContractDtl", {
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
   Summary: Invoke method GetDemandDtlReview
   Description: Creates records in the DemandReview DataSet so the user can review the impact
of the demand schedule prior to accepting or rejecting it.
   OperationID: GetDemandDtlReview
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDemandDtlReview_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDemandDtlReview_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDemandDtlReview(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetDemandDtlReview", {
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
   Summary: Invoke method GetDemandMatching
   Description: Creates records in the DemandMatching DataSet so the user can manually match
DemandSchedule records to existing OrderRel records.
   OperationID: GetDemandMatching
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDemandMatching_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDemandMatching_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDemandMatching(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetDemandMatching", {
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
   Summary: Invoke method GetDemandScheduleCreate
   Description: Creates a record in the DemandScheduleCreate datatable to store the parameters
needed to mass-build DemandSchedule records for a DemandDetail line.
   OperationID: GetDemandScheduleCreate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDemandScheduleCreate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDemandScheduleCreate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDemandScheduleCreate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetDemandScheduleCreate", {
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
   Summary: Invoke method GetListCustom
   Description: Custom Search
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCustom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetListCustom", {
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
   Summary: Invoke method GetListCustomWithPaging
   Description: Custom Search that handles server paging
   OperationID: Get_GetListCustomWithPaging
      @param whereClause Desc: The search criteria   Required: True   Allow empty value : True
      @param pageSize Desc: Size of a page   Required: True
      @param absolutePage Desc: The absolute page   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustomWithPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetListCustomWithPaging(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetListCustomWithPaging" + params, {
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
   Summary: Invoke method GetPriceDiscrepancy
   Description: Check if the difference between the InternalPrice and EDIUnitPrice (Customer Price) is less than the value defined in
the PriceTolerance field of the ShipTo or Customer tables.
   OperationID: GetPriceDiscrepancy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPriceDiscrepancy_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceDiscrepancy_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPriceDiscrepancy(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetPriceDiscrepancy", {
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
   Summary: Invoke method MassCreateDemandSchedule
   Description: Creates DemandSchedule records based on user criteria entered in the
DemandScheduleCreate datatable. At the end refresh the
DemandHead/DemandDetail/DemandSchedule for a specific Demand
Contract Line to avoid perform a GetByID that consumes a lot of time.
   OperationID: MassCreateDemandSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassCreateDemandSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassCreateDemandSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassCreateDemandSchedule(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/MassCreateDemandSchedule", {
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
   Summary: Invoke method OpenDemandDetail
   Description: Opens the Demand detail.
   OperationID: OpenDemandDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenDemandDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenDemandDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpenDemandDetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/OpenDemandDetail", {
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
   Summary: Invoke method OpenDemandHeadKeepDemandDetail
   Description: Opens the Demand Header and keeps the existing Details and Schedules.
   OperationID: OpenDemandHeadKeepDemandDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenDemandHeadKeepDemandDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenDemandHeadKeepDemandDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpenDemandHeadKeepDemandDetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/OpenDemandHeadKeepDemandDetail", {
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
   Summary: Invoke method OpenDemandHead
   Description: Opens the Demand Header.
   OperationID: OpenDemandHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenDemandHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenDemandHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpenDemandHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/OpenDemandHead", {
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
   Summary: Invoke method OpenDemandSchedule
   Description: Opens the Demand Schedule record.
   OperationID: OpenDemandSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenDemandSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenDemandSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpenDemandSchedule(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/OpenDemandSchedule", {
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
   Summary: Invoke method ProcessDemand
   Description: Process the demand.  This will accept or reject DemandHead, DemandDetail, and
DemandSchedule records and create/update Forecasts or Orders.
cReturnMessage contains an informational message that lets the user know the process
has completed and if any errors were written to the DemandLog table.
   OperationID: ProcessDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessDemand(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ProcessDemand", {
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
   Summary: Invoke method ProcessMatching
   Description: Updates the Order fields in DemandSchedule with the values from DemandScheduleToMatch.
   OperationID: ProcessMatching
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessMatching_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessMatching_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessMatching(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ProcessMatching", {
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
   Summary: Invoke method RejectDemandDetail
   Description: Rejects the Demand detail and sub-table (DemandSchedule).
   OperationID: RejectDemandDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RejectDemandDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RejectDemandDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RejectDemandDetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/RejectDemandDetail", {
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
   Summary: Invoke method RejectDemandHead
   Description: Rejects the Demand Header and sub-tables (DemandDetail and DemandSchedule).
   OperationID: RejectDemandHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RejectDemandHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RejectDemandHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RejectDemandHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/RejectDemandHead", {
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
   Summary: Invoke method RejectDemandScheduleKeepSchedules
   Description: Reject a Demand Schedule but return previously existing schedules
   OperationID: RejectDemandScheduleKeepSchedules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RejectDemandScheduleKeepSchedules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RejectDemandScheduleKeepSchedules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RejectDemandScheduleKeepSchedules(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/RejectDemandScheduleKeepSchedules", {
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
   Summary: Invoke method RejectDemandSchedule
   Description: Rejects the Demand Schedule record.
   OperationID: RejectDemandSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RejectDemandSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RejectDemandSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RejectDemandSchedule(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/RejectDemandSchedule", {
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
   Summary: Invoke method SetReadyToProcess
   Description: Set the Ready to Process flag on the Demand Header.
This was created mainly for web services.
   OperationID: SetReadyToProcess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetReadyToProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetReadyToProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetReadyToProcess(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/SetReadyToProcess", {
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
   Summary: Invoke method UnlockDemand
   Description: Provide a way to unlock a demand entry for cases when ESC fails.
   OperationID: UnlockDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlockDemand(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/UnlockDemand", {
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
   Summary: Invoke method UnrejectDemandDetail
   Description: Unrejects the Demand detail.
   OperationID: UnrejectDemandDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnrejectDemandDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnrejectDemandDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnrejectDemandDetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/UnrejectDemandDetail", {
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
   Summary: Invoke method UnrejectDemandHead
   Description: UnReject the Demand Header.
   OperationID: UnrejectDemandHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnrejectDemandHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnrejectDemandHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnrejectDemandHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/UnrejectDemandHead", {
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
   Summary: Invoke method UnrejectDemandScheduleKeepSchedules
   Description: Unreject a Demand Schedule but return the other existing schedules.
   OperationID: UnrejectDemandScheduleKeepSchedules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnrejectDemandScheduleKeepSchedules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnrejectDemandScheduleKeepSchedules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnrejectDemandScheduleKeepSchedules(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/UnrejectDemandScheduleKeepSchedules", {
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
   Summary: Invoke method UnrejectDemandSchedule
   Description: Unrejects the Demand Schedule record.
   OperationID: UnrejectDemandSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnrejectDemandSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnrejectDemandSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnrejectDemandSchedule(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/UnrejectDemandSchedule", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetCodeDescList", {
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
   Summary: Invoke method PartValidation
   OperationID: PartValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartValidation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/PartValidation", {
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
   Summary: Invoke method ConfigurationChangePart
   Description: Update Order details information when the Part Number is changed by Configuration Part Creation.
   OperationID: ConfigurationChangePart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfigurationChangePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfigurationChangePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfigurationChangePart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ConfigurationChangePart", {
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
   Summary: Invoke method ConfigurationRefreshQty
   Description: Update PriceList Qty breaks and set new unit price on those
when the Part Number is changed by Document Rule.
   OperationID: ConfigurationRefreshQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfigurationRefreshQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfigurationRefreshQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfigurationRefreshQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ConfigurationRefreshQty", {
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
   Summary: Invoke method ValidateOTSTaxID
   Description: One Time Ship To Tax Id validation
   OperationID: ValidateOTSTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOTSTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTSTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateOTSTaxID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/ValidateOTSTaxID", {
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
   Summary: Invoke method GetDemandHeadData
   Description: this method returns DemandHead Records with search criteria for DemandEntry LandingPage
   OperationID: GetDemandHeadData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDemandHeadData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDemandHeadData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDemandHeadData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetDemandHeadData", {
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
   Summary: Invoke method GetNewDemandHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDemandHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetNewDemandHead", {
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
   Summary: Invoke method GetNewDemandDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDemandDetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetNewDemandDetail", {
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
   Summary: Invoke method GetNewDemandMiscChg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandMiscChg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandMiscChg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandMiscChg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDemandMiscChg(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetNewDemandMiscChg", {
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
   Summary: Invoke method GetNewDemandSchedule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDemandSchedule(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetNewDemandSchedule", {
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
   Summary: Invoke method GetNewDemandMiscChgDH
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandMiscChgDH
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandMiscChgDH_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandMiscChgDH_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDemandMiscChgDH(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetNewDemandMiscChgDH", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandEntrySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandDetailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandDetailRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandHeadRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgDHRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandMiscChgDHRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandMiscChgRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandScheduleRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandScheduleRow[],
}

export interface Erp_Tablesets_DemandDetailRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The demand contract this demand is for.  */  
   "DemandContractNum":number,
      /**  The sequence from the DemandHead record this DemandDetail is related to.  */  
   "DemandHeadSeq":number,
      /**  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  */  
   "DemandDtlSeq":number,
      /**  The contract line this demand line is for.  */  
   "DemandContractLine":number,
      /**  Determines whether or not this line is being run in a test mode.  */  
   "TestRecord":boolean,
      /**  Contains the Order Number that ties this detail record back to an OrderDtl record.  */  
   "OrderNum":number,
      /**  The OrderDtl record this demand detail is linked to.  */  
   "OrderLine":number,
      /**  The date before which the order cannot be shipped.  */  
   "DoNotShipBeforeDate":string,
      /**  The date after which the order cannot be shipped.  */  
   "DoNotShipAfterDate":string,
      /**  The reference from the incoming demand source.  Can be used to locate other sales order detail records that have been created by this demand.  */  
   "DemandReference":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   "IUM":string,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "SalesUM":string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  */  
   "DiscountPercent":number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "UnitPrice":number,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  */  
   "ProjectID":string,
      /**  This is the Price Group ID used to price the order line with.  */  
   "PriceGroupCode":string,
      /**  Quote number to which the line item detail record is associated with. This is part of the foreign key to QuoteHed file.  */  
   "QuoteNum":number,
      /**  Quote Line number to which this line was related. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  */  
   "QuoteLine":number,
      /**  The PO Type.  This is set by Service Connect when the record is created.  Reference only.  */  
   "POType":string,
      /**   The type of acknowledgement that is expected by the trading partner.  Values are:
OutSOAck - Outgoing Acknowledgement
OutChgRsp - Outgoing Response to Change
OutStatus - Outgoing Order Status  */  
   "AcknowledgementType":string,
      /**  The schedule type from the trading partner.  Reference only.  */  
   "ScheduleType":string,
      /**  Contains the Customer number that the demand is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   "PONum":string,
      /**  Indicates if the DemandDetail has been rejected by the user.  */  
   "RejectedByUser":boolean,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  */  
   "PartNum":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Use standard Epicor Price matrix/logic  */  
   "UsePriceList":boolean,
      /**  Indicates if this record has been written to an OrderDtl.  */  
   "Posted":boolean,
      /**  Indicates if the DemandDetail has been rejected by the system.  */  
   "RejectedBySystem":boolean,
      /**  Indicates if the system rejection should be overridden so the record can be accepted.  */  
   "OverrideSystemReject":boolean,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Indicates if the DemandDetail record is in a "open or closed" status.  */  
   "OpenLine":boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   "POLine":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter01":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter02":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter03":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter04":string,
      /**  For Epicor Development Use Only  */  
   "DemandNumber01":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber02":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber03":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber04":number,
      /**  For Epicor Development Use Only  */  
   "DemandDate01":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate02":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate03":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate04":string,
      /**  For Epicor Development Use Only  */  
   "DemandLogical01":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical02":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical03":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical04":boolean,
      /**  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  */  
   "DeleteCurrentReleases":boolean,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand entry if the CRM module is installed.  */  
   "MktgCampaignID":string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand entry if the CRM module is installed.  */  
   "MktgEvntSeq":number,
      /**  Cross Reference Part Num. Only used for audit purposes for EDI.  */  
   "XRefPartNum":string,
      /**   Cross Reference Part Type. Only used for audit purposes for EDI.

I=Internal Cross Reference / C = Customer Part  */  
   "XRefPartType":string,
      /**  Customer Number XRefPartNum is related to if it is a customer part. Only used for audit purposes for EDI.  */  
   "XRefCustNum":number,
      /**  Optional field that contains the  part revision.  */  
   "RevisionNum":string,
      /**  Optional field that contains the customers revision.  */  
   "XRevisionNum":string,
      /**  The Incoming EDI Unit Price.  */  
   "EDIUnitPrice":number,
      /**  The total quantity that has been received according to the training partner data  */  
   "CumulativeQty":number,
      /**  The date when the trading partner calculated the cumulative quantity field  */  
   "CumulativeDate":string,
      /**  A qty that will create a new reconciliation adjustment.  */  
   "StartCumQty":number,
      /**  The date since the trading partner has been accumulating the quantities.  */  
   "StartCumDate":string,
      /**  The pack id of the last trading partner information received by the trading partner.  */  
   "LastShipmentID":number,
      /**  The quantity received in the last shipment according to the trading partner information  */  
   "LastShipmentQty":number,
      /**  The date when of the last shipment according to the trading partner information  */  
   "LastShipmentDate":string,
      /**  The current schedule number of the file where the cumulative info was received  */  
   "ScheduleNumber":string,
      /**  Last Master Pack ID  */  
   "LastMasterPack":number,
      /**  Contains the internal system unit price in a foreign currency  */  
   "DocUnitPrice":number,
      /**  Contains the Customer Price in a foreign currency  */  
   "DocEDIUnitPrice":number,
      /**  This is the Internal Price assigned by the system calculated from the part sales price or a price list. It will be used when the Demand Contract is using Internal Pricing.  */  
   "InternalPrice":number,
      /**  The doc currency value of the internal price  */  
   "DocInternalPrice":number,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   "BasePartNum":string,
      /**  The date when the configuration was completed for the assembly.  */  
   "LastConfigDate":string,
      /**  The system time when the configuration was completed for the assembly.  */  
   "LastConfigTime":number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   "LastConfigUserID":string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   "ConfigUnitPrice":number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   "ConfigBaseUnitPrice":number,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   "BaseRevisionNum":string,
      /**  Trading Partner Quote Number. This is not an internal quote number, it is the quote sent by the trading partner.  */  
   "TPQuoteNum":number,
      /**  Trading Partner Quote Line Number. This is not related to an internal quote, it is sent by the trading partner.  */  
   "TPQuoteLine":number,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   "Rpt1UnitPrice":number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   "Rpt2UnitPrice":number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   "Rpt3UnitPrice":number,
      /**  Same as Internal Price except that this field contains the Internal Price in a report currency  */  
   "Rpt1InternalPrice":number,
      /**  Same as Internal Price except that this field contains the Internal Price in a report currency  */  
   "Rpt2InternalPrice":number,
      /**  Same as Internal Price except that this field contains the Internal Price in a report currency  */  
   "Rpt3InternalPrice":number,
      /**  Same as EDI Unit price except that this field contains the EDI unit price in a report currency  */  
   "Rpt1EDIUnitPrice":number,
      /**  Same as EDI Unit price except that this field contains the EDI unit price in a report currency  */  
   "Rpt2EDIUnitPrice":number,
      /**  Same as EDI Unit price except that this field contains the EDI unit price in a report currency  */  
   "Rpt3EDIUnitPrice":number,
      /**  Indicates if current line is blocked for processing.  */  
   "BlockProcLine":boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   "POLineRef":string,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  This is field is similar to DemandContract. The field CUMMSetting helps to choose how the DemandReconciliation will open.  */  
   "CUMMSetting":string,
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
      /**  Indicates if the Create Demand Schedule option is available.  */  
   "EnableCreateSchedule":boolean,
   "EnableDeleteReleases":boolean,
      /**  Indicates if the Delete Schedule by Schedule Number option is available.  */  
   "EnableDeleteSchedule":boolean,
      /**  Indicates if the Log action item is available.  */  
   "EnableLog":boolean,
      /**  This field is true is Demand Detail is posted or has link with SO.  */  
   "EnableOnlyPart":boolean,
   "EnableOverrideReject":boolean,
      /**  Indicates if the Reject option is available.  */  
   "EnableReject":boolean,
      /**  Indicates if the Review and Matching options are available.  */  
   "EnableRevMatch":boolean,
   "EnableUnreject":boolean,
      /**  True when the XRefPartNum has multiple references.  */  
   "MultipleXRef":boolean,
      /**  True when exists a Price Discrepancy beetwen UnitPrice and EDIUnitPrice  */  
   "PriceDiscrepancy":boolean,
      /**  Indicates if this record is in read-only mode.  */  
   "ReadOnly":boolean,
   "Configured":string,
   "BitFlag":number,
   "CustomerBTName":string,
   "CustomerName":string,
   "CustomerCustID":string,
   "DemandContractDtlSalesUM":string,
   "DemandContractHdrCUMMSetting":string,
   "DemandContractHdrDemandContract":string,
   "MktgCampaignIDCampDescription":string,
   "MktgEvntEvntDescription":string,
   "PlantName":string,
   "PriceGroupDescription":string,
   "ProjectDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DemandHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The demand contract this demand is for.  */  
   "DemandContractNum":number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   "DemandHeadSeq":number,
      /**  The OrderHed record this demand is linked to.  */  
   "OrderNum":number,
      /**  Contains the Customer number that the demand is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  This is a mandatory field used to enter the customers Purchase Order Number.  */  
   "PONum":string,
      /**  The date before which the order cannot be shipped.  */  
   "DoNotShipBeforeDate":string,
      /**  The date after which the order cannot be shipped.  */  
   "DoNotShipAfterDate":string,
      /**  The date after which the sales order should be canceled.  */  
   "CancelAfterDate":string,
      /**  An optional field that describes the FOB policy.  */  
   "FOB":string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   "ShipViaCode":string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  */  
   "TermsCode":string,
      /**  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  */  
   "AllocPriorityCode":string,
      /**  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  */  
   "ReservePriorityCode":string,
      /**  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  */  
   "ShipOrderComplete":boolean,
      /**  Contains comments about the overall order. These will be printed on the Sales Acknowledgements.  */  
   "OrderComment":string,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   "InvoiceComment":string,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   "AutoOrderBasedDisc":boolean,
      /**  Determines whether or not this line is being run in a test mode.  */  
   "TestRecord":boolean,
      /**  The PO Type.  This is set by Service Connect when the record is created.  Reference only.  */  
   "POType":string,
      /**   The type of acknowledgement that is expected by the trading partner.  Values are:
OutSOAck - Outgoing Acknowledgement
OutChgRsp - Outgoing Response to Change
OutStatus - Outgoing Order Status  */  
   "AcknowledgementType":string,
      /**   The type of action to take for this demand.  Values are:
ALW - Always accept the demand automatically
ANE - Accpet the demand automatically if no errors
ASD - Always stop at demand.  User will accept demands manually.  */  
   "AcceptType":string,
      /**  An internal identifier to group demand schedules together.  This will be changed every time a demand is received via EDI or changed manually.  This number will carry over to the DemandSchedule table.  This number can be manually entered, generated by the system, or come from EDI.  */  
   "ScheduleNumber":string,
      /**  Holds the value of the last sequence used for ScheduleNumber.  When generating ScheduleNumbers, this field is incremented by 1 and is used to populate ScheduleNumber.  */  
   "ScheduleNumberSeq":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   "LockRate":boolean,
      /**  Indicates if this demand has been accepted or not.  */  
   "Accepted":boolean,
      /**  Indicates if the DemandHead has been rejected by the user.  */  
   "RejectedByUser":boolean,
      /**  Indicates if this demand is in an "open" status.  A demand is closed when the the Demand Contract is closed.  It can also be set if it is tied to an OrderHed and the OrderHed record is closed.  */  
   "OpenDemand":boolean,
      /**  Indicates if this record and it's children (DemandDetail and DemandSchedule) have been written to the Forecast table or Order tables.  This can be toggled back on by the system as new demand schedules are created.  */  
   "Posted":boolean,
      /**  Indicates if the DemandDetail has been rejected by the system.  */  
   "RejectedBySystem":boolean,
      /**  Indicates if the system rejection should be overridden so the record can be accepted.  */  
   "OverrideSystemReject":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter01":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter02":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter03":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter04":string,
      /**  For Epicor Development Use Only  */  
   "DemandNumber01":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber02":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber03":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber04":number,
      /**  For Epicor Development Use Only  */  
   "DemandDate01":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate02":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate03":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate04":string,
      /**  For Epicor Development Use Only  */  
   "DemandLogical01":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical02":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical03":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical04":boolean,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  Order created from EDI.  */  
   "EDIOrder":boolean,
      /**  Indicates the demand has been selected for processing.  The value will be set back to false when processing has been done.  */  
   "SelectedForProcessing":boolean,
      /**  Do Not Process  */  
   "SCProcessing":boolean,
      /**  Indicates which customer ship to is to be used as the default for the Demand records. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new demands.  */  
   "ShipToNum":string,
      /**  Flag at the Header Level that indicate that the demand can be process.  */  
   "ReadyToProcess":boolean,
      /**  If turned on, this flag will rest the accumulative quantities stored in Epicor applications  */  
   "ResetCums":boolean,
      /**  It will be used to identify POs that will generate an invoice at the shipment.  If the order is created manually the default for this order will be taken from the customer master file. If the order is created via EDI, the default will be taken from the value in the inbound file.  */  
   "ERSOrder":boolean,
      /**  It will be displayed when the user ask to cancel the whole order. There is a field in the inbound EDI message to ask for this.  */  
   "CancelPO":boolean,
      /**  new orders will be created when it is set to true  */  
   "CreateNewOrder":boolean,
      /**  Sales Order linked to this Demand  */  
   "LinkedOrders":string,
      /**  EDI Transaction Control Number  */  
   "TCtrlNum":string,
      /**  EDI Batch Control Number  */  
   "BatchNum":string,
      /**  Quote Number to which this record is related.  */  
   "QuoteNum":number,
      /**  Date in which the related demand was last processed.  */  
   "DemandProcessDate":string,
      /**  System Time when demand was last processed.  */  
   "DemandProcessTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping Country Number  */  
   "OTSCountryNum":number,
      /**  OTS Tax Liability Code (Header)  */  
   "OTSTaxRegionCode":string,
      /**  Indicates if the One Time Shipto information is to be used.  */  
   "UseOTS":boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Holds a string with the customer address  */  
   "CustAddrList":string,
      /**  Indicates if this record is in read-only mode.  */  
   "ReadOnly":boolean,
   "BTCustID":string,
   "BillToCustomerName":string,
   "BTAddressList":string,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   "AvailBTCustList":string,
      /**  Indicates if the Get Contract Lines option is available.  */  
   "EnableGetLines":boolean,
      /**  Indicates if the Reject option is available  */  
   "EnableReject":boolean,
      /**  Indicates if the Process action item is available.  */  
   "EnableProcess":boolean,
   "DemandContract":string,
   "EnableUnreject":boolean,
   "EnableLog":boolean,
   "DemandSchedAvail":boolean,
      /**  Indicates if the recently created order should be placed on hold. Defaults from Contract.  */  
   "OrderHoldForReview":boolean,
      /**  Ship To Address List.  */  
   "ShipToAddressList":string,
      /**  This Field is used to be related to the CustomerName Field on the Table CustomerDocs for EDI.  */  
   "EDITran_Type":string,
      /**  Used to pass the value of Customer.AllowOTS to the client so that it can easily be used in Row Rules.  */  
   "OTSAllowed":boolean,
   "ShipToCustID":string,
      /**  The value of the Customer.AllowShipTo3 of the Cusomer by the DemandHead. If this is false then the DemandHead.ShipToCustNum is  disabled  */  
   "CustNumAllowShipTo3":boolean,
      /**  Support for OTSCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTSCountryNum will be populated based on it  */  
   "EDI_OTSCountry":string,
      /**  It will be displayed when the value of the ERS flag at the demand entry is different from the value in the customer master file.  */  
   "ERSOverride":boolean,
      /**  Description of the currency  */  
   "CurrencyCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyDocumentDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCurrName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  The unique identifier of the demand contract.  This must be unique for a customer.  */  
   "DemandContractHdrDemandContract":string,
      /**  Full description of the FOB Code.  */  
   "FOBDescription":string,
      /**  Country name  */  
   "OTSCountryDescription":string,
      /**  Full description for the Tax Region.  */  
   "OTSTaxRegionCodeDescription":string,
      /**  Description of the reservation priority. Example "High".  */  
   "ReservePriDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  Full description of the terms which prints on sales orders and invoices.  */  
   "TermsDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DemandHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The demand contract this demand is for.  */  
   "DemandContractNum":number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   "DemandHeadSeq":number,
      /**  The OrderHed record this demand is linked to.  */  
   "OrderNum":number,
      /**  Contains the Customer number that the demand is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  This is a mandatory field used to enter the customers Purchase Order Number.  */  
   "PONum":string,
      /**  The date before which the order cannot be shipped.  */  
   "DoNotShipBeforeDate":string,
      /**  The date after which the order cannot be shipped.  */  
   "DoNotShipAfterDate":string,
      /**  The date after which the sales order should be canceled.  */  
   "CancelAfterDate":string,
      /**  An optional field that describes the FOB policy.  */  
   "FOB":string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   "ShipViaCode":string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  */  
   "TermsCode":string,
      /**  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  */  
   "AllocPriorityCode":string,
      /**  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  */  
   "ReservePriorityCode":string,
      /**  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  */  
   "ShipOrderComplete":boolean,
      /**  Contains comments about the overall order. These will be printed on the Sales Acknowledgements.  */  
   "OrderComment":string,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   "InvoiceComment":string,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   "AutoOrderBasedDisc":boolean,
      /**  Determines whether or not this line is being run in a test mode.  */  
   "TestRecord":boolean,
      /**  The PO Type.  This is set by Service Connect when the record is created.  Reference only.  */  
   "POType":string,
      /**   The type of acknowledgement that is expected by the trading partner.  Values are:
OutSOAck - Outgoing Acknowledgement
OutChgRsp - Outgoing Response to Change
OutStatus - Outgoing Order Status  */  
   "AcknowledgementType":string,
      /**   The type of action to take for this demand.  Values are:
ALW - Always accept the demand automatically
ANE - Accpet the demand automatically if no errors
ASD - Always stop at demand.  User will accept demands manually.  */  
   "AcceptType":string,
      /**  An internal identifier to group demand schedules together.  This will be changed every time a demand is received via EDI or changed manually.  This number will carry over to the DemandSchedule table.  This number can be manually entered, generated by the system, or come from EDI.  */  
   "ScheduleNumber":string,
      /**  Holds the value of the last sequence used for ScheduleNumber.  When generating ScheduleNumbers, this field is incremented by 1 and is used to populate ScheduleNumber.  */  
   "ScheduleNumberSeq":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   "LockRate":boolean,
      /**  Indicates if this demand has been accepted or not.  */  
   "Accepted":boolean,
      /**  Indicates if the DemandHead has been rejected by the user.  */  
   "RejectedByUser":boolean,
      /**  Indicates if this demand is in an "open" status.  A demand is closed when the the Demand Contract is closed.  It can also be set if it is tied to an OrderHed and the OrderHed record is closed.  */  
   "OpenDemand":boolean,
      /**  Indicates if this record and it's children (DemandDetail and DemandSchedule) have been written to the Forecast table or Order tables.  This can be toggled back on by the system as new demand schedules are created.  */  
   "Posted":boolean,
      /**  Indicates if the DemandDetail has been rejected by the system.  */  
   "RejectedBySystem":boolean,
      /**  Indicates if the system rejection should be overridden so the record can be accepted.  */  
   "OverrideSystemReject":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter01":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter02":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter03":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter04":string,
      /**  For Epicor Development Use Only  */  
   "DemandNumber01":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber02":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber03":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber04":number,
      /**  For Epicor Development Use Only  */  
   "DemandDate01":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate02":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate03":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate04":string,
      /**  For Epicor Development Use Only  */  
   "DemandLogical01":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical02":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical03":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical04":boolean,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  Order created from EDI.  */  
   "EDIOrder":boolean,
      /**  Indicates the demand has been selected for processing.  The value will be set back to false when processing has been done.  */  
   "SelectedForProcessing":boolean,
      /**  Do Not Process  */  
   "SCProcessing":boolean,
      /**  Indicates which customer ship to is to be used as the default for the Demand records. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new demands.  */  
   "ShipToNum":string,
      /**  Flag at the Header Level that indicate that the demand can be process.  */  
   "ReadyToProcess":boolean,
      /**  If turned on, this flag will rest the accumulative quantities stored in Epicor applications  */  
   "ResetCums":boolean,
      /**  It will be used to identify POs that will generate an invoice at the shipment.  If the order is created manually the default for this order will be taken from the customer master file. If the order is created via EDI, the default will be taken from the value in the inbound file.  */  
   "ERSOrder":boolean,
      /**  It will be displayed when the user ask to cancel the whole order. There is a field in the inbound EDI message to ask for this.  */  
   "CancelPO":boolean,
      /**  new orders will be created when it is set to true  */  
   "CreateNewOrder":boolean,
      /**  Sales Order linked to this Demand  */  
   "LinkedOrders":string,
      /**  EDI Transaction Control Number  */  
   "TCtrlNum":string,
      /**  EDI Batch Control Number  */  
   "BatchNum":string,
      /**  Quote Number to which this record is related.  */  
   "QuoteNum":number,
      /**  Date in which the related demand was last processed.  */  
   "DemandProcessDate":string,
      /**  System Time when demand was last processed.  */  
   "DemandProcessTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  UserChar1  */  
   "UserChar1":string,
      /**  UserChar2  */  
   "UserChar2":string,
      /**  UserChar3  */  
   "UserChar3":string,
      /**  UserChar4  */  
   "UserChar4":string,
      /**  UserDate1  */  
   "UserDate1":string,
      /**  UserDate2  */  
   "UserDate2":string,
      /**  UserDate3  */  
   "UserDate3":string,
      /**  UserDate4  */  
   "UserDate4":string,
      /**  UserDecimal1  */  
   "UserDecimal1":number,
      /**  UserDecimal2  */  
   "UserDecimal2":number,
      /**  UserInteger1  */  
   "UserInteger1":number,
      /**  UserInteger2  */  
   "UserInteger2":number,
      /**  Ship the good by this time  */  
   "ShipByTime":number,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping Country Number  */  
   "OTSCountryNum":number,
      /**  OTS Tax Liability Code (Header)  */  
   "OTSTaxRegionCode":string,
      /**  True if Customer or ShipTo record was created using the  OTS info.  */  
   "OTSCustSaved":boolean,
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   "OTSSaveAs":string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   "OTSSaveCustID":string,
      /**  OTSSaved  */  
   "OTSSaved":boolean,
      /**  OTS ShipToNum  */  
   "OTSShipToNum":string,
      /**  Indicates if the One Time Shipto information is to be used.  */  
   "UseOTS":boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
   "BaseCurrencyCode":string,
   "CurrencySwitch":boolean,
      /**  Indicates if the Process action item is available.  */  
   "EnableProcess":boolean,
      /**  Indicates if the Reject option is available  */  
   "EnableReject":boolean,
   "EnableUnreject":boolean,
      /**  It will be displayed when the value of the ERS flag at the demand entry is different from the value in the customer master file.  */  
   "ERSOverride":boolean,
   "OpenContract":boolean,
      /**  Indicates if the recently created order should be placed on hold. Defaults from Contract.  */  
   "OrderHoldForReview":boolean,
      /**  Used to pass the value of Customer.AllowOTS to the client so that it can easily be used in Row Rules.  */  
   "OTSAllowed":boolean,
      /**  OTS Country Description  */  
   "OTSCountryDescription":string,
      /**  OTS Tax Region Description  */  
   "OTSTaxRegionCodeDescription":string,
      /**  Indicates if this record is in read-only mode.  */  
   "ReadOnly":boolean,
      /**  Ship To Address List.  */  
   "ShipToAddressList":string,
   "ShipToCustID":string,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   "AvailBTCustList":string,
   "BillToCustomerName":string,
   "BTAddressList":string,
   "BTCustID":string,
      /**  Holds a string with the customer address  */  
   "CustAddrList":string,
      /**  The value of the Customer.AllowShipTo3 of the Cusomer by the DemandHead. If this is false then the DemandHead.ShipToCustNum is  disabled  */  
   "CustNumAllowShipTo3":boolean,
   "DemandContract":string,
   "DemandSchedAvail":boolean,
      /**  Support for OTSCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTSCountryNum will be populated based on it  */  
   "EDI_OTSCountry":string,
      /**  This Field is used to be related to the CustomerName Field on the Table CustomerDocs for EDI.  */  
   "EDITran_Type":string,
      /**  Indicates if the Get Contract Lines option is available.  */  
   "EnableGetLines":boolean,
   "EnableLog":boolean,
   "BitFlag":number,
   "BTCustNumInactive":boolean,
   "CurrencyCurrSymbol":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrName":string,
   "CurrencyDocumentDesc":string,
   "CustomerInactive":boolean,
   "CustomerCustID":string,
   "CustomerName":string,
   "CustomerBTName":string,
   "DemandContractHdrDemandContract":string,
   "FOBDescription":string,
   "OTSCountryISOCode":string,
   "OTSCountryEUMember":boolean,
   "OTSCountryDescription_":string,
   "ReservePriDescription":string,
   "ShipToCustNumInactive":boolean,
   "ShipToNumInactive":boolean,
   "ShipViaCodeWebDesc":string,
   "ShipViaCodeDescription":string,
   "TermsDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DemandMiscChgDHRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The demand contract this demand misc charge is for.  */  
   "DemandContractNum":number,
      /**  The DemandHead this charge is for.  */  
   "DemandHeadSeq":number,
      /**  Demand Detail sequence that this miscellaneous record is related to. If related to the DemandHead then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when miscellaneous maintenance was requested.  */  
   "DemandDtlSeq":number,
      /**  This along with Company, DemandHeadSeq and DemandDetailSeq make up the unique keys for this record.  */  
   "SeqNum":number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   "MiscCode":string,
      /**  Description of the miscellaneous charge. The default is provided by MiscChrg.Description, but it's overridable by the user. This can't be blank.  */  
   "Description":string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   "MiscAmt":number,
      /**  The amount of the Miscellaneous Charge/Credit(display value). Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   "DocMiscAmt":number,
      /**  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  */  
   "FreqCode":string,
      /**  An internally used flag which indicates that this record was created from a Quote via the "Get Quote" function. "Q" = related to the QuoteQty record, "L" = related to the overall QuoteDtl record. This flag is used so that the OrderMsc file can be refreshed from the QuoteMsc when Quantity or Quote/Line # changes occur. The logic is that if a change in order quantity of a order line that is linked to a quote causes a different price break to be selected then all the existing all OrderMsc records where Quoting = "Q" are deleted and then re-pulled in based on the new qty. If the Quote # or QuoteLine are changed then all OrderMsc records where Quoting is either a "Q" or "L" are deleted then re-pulled in from the newly referenced quote.  */  
   "Quoting":string,
      /**  Reporting currency value of this field  */  
   "Rpt1MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3MiscAmt":number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   "Percentage":number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   "Type":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Indicates if this record is in read-only mode.  */  
   "ReadOnly":boolean,
   "CurrencySwitch":boolean,
   "BitFlag":number,
   "MiscCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DemandMiscChgRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The demand contract this demand misc charge is for.  */  
   "DemandContractNum":number,
      /**  The DemandHead this charge is for.  */  
   "DemandHeadSeq":number,
      /**  Demand Detail sequence that this miscellaneous record is related to. If related to the DemandHead then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when miscellaneous maintenance was requested.  */  
   "DemandDtlSeq":number,
      /**  This along with Company, DemandHeadSeq and DemandDetailSeq make up the unique keys for this record.  */  
   "SeqNum":number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   "MiscCode":string,
      /**  Description of the miscellaneous charge. The default is provided by MiscChrg.Description, but it's overridable by the user. This can't be blank.  */  
   "Description":string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   "MiscAmt":number,
      /**  The amount of the Miscellaneous Charge/Credit(display value). Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   "DocMiscAmt":number,
      /**  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  */  
   "FreqCode":string,
      /**  An internally used flag which indicates that this record was created from a Quote via the "Get Quote" function. "Q" = related to the QuoteQty record, "L" = related to the overall QuoteDtl record. This flag is used so that the OrderMsc file can be refreshed from the QuoteMsc when Quantity or Quote/Line # changes occur. The logic is that if a change in order quantity of a order line that is linked to a quote causes a different price break to be selected then all the existing all OrderMsc records where Quoting = "Q" are deleted and then re-pulled in based on the new qty. If the Quote # or QuoteLine are changed then all OrderMsc records where Quoting is either a "Q" or "L" are deleted then re-pulled in from the newly referenced quote.  */  
   "Quoting":string,
      /**  Reporting currency value of this field  */  
   "Rpt1MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3MiscAmt":number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   "Percentage":number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   "Type":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Indicates if this record is in read-only mode.  */  
   "ReadOnly":boolean,
   "CurrencySwitch":boolean,
   "BitFlag":number,
   "MiscCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DemandScheduleRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The demand contract this demand schedule is for.  */  
   "DemandContractNum":number,
      /**  The sequence from the DemandHead record this DemandSchedule is related to.  */  
   "DemandHeadSeq":number,
      /**  The sequence from the DemandDetail record this DemandSchedule is related to.  */  
   "DemandDtlSeq":number,
      /**  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDetailSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandSchedulel record for the DemandDetail and the adding 1 to it.  */  
   "DemandScheduleSeq":number,
      /**  All invoices belong to a group until the group is closed. The GroupID is assigned by the user.  */  
   "GroupID":string,
      /**  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   "OurReqQty":number,
      /**  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   "ShipToNum":string,
      /**  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  */  
   "ShipViaCode":string,
      /**  Quantity ,using Selling U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   "SellingReqQty":number,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  */  
   "ReqDate":string,
      /**  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  */  
   "NeedByDate":string,
      /**  The Mark For to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file.  */  
   "MarkForNum":string,
      /**  The delivery days required for the shipment to reach its destination.  Defaults from Customer.DemandDeliveryDays or ShipTo.DemandDeliveryDays.  */  
   "DeliveryDays":number,
      /**  An internal identifier to group demand schedules together.  This will be changed every time a demand is received via EDI or changed manually.  This number will carry over to the DemandSchedule table.  This number can be manually entered, generated by the system, or come from EDI.  */  
   "ScheduleNumber":string,
      /**   The type of demand this line represents.  Values are:
InForecast - Incoming Forecast (Forecasts)
InUnfirm - Incoming Unfirm Releases (Unfirm OrderRel)
InShSched - Incoming Shipping Schedule (Firm OrderRel)  */  
   "DemandType":string,
      /**  Sales order number of the OrderRel record this DemandSchedule is linked to.  */  
   "OrderNum":number,
      /**  Sales order Line number of the OrderRel record this DemandSchedule is linked to.  */  
   "OrderLine":number,
      /**  Sales order release number of the OrderRel record this DemandSchedule is linked to.  */  
   "OrderRelNum":number,
      /**  Indicates if the DemandSchedule has been rejected by the user.  */  
   "RejectedByUser":boolean,
      /**  RAN Number.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  */  
   "RAN":string,
      /**  Demand Reference.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  */  
   "DemandReference":string,
      /**  Indicates if this record has been written to an OrderDtl.  */  
   "Posted":boolean,
      /**  Indicates if the DemandDetail has been rejected by the system.  */  
   "RejectedBySystem":boolean,
      /**  Indicates if the system rejection should be overridden so the record can be accepted.  */  
   "OverrideSystemReject":boolean,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Indicates if this schedule is open.  */  
   "OpenSchedule":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter01":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter02":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter03":string,
      /**  For Epicor Development Use Only  */  
   "DemandCharacter04":string,
      /**  For Epicor Development Use Only  */  
   "DemandNumber01":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber02":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber03":number,
      /**  For Epicor Development Use Only  */  
   "DemandNumber04":number,
      /**  For Epicor Development Use Only  */  
   "DemandDate01":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate02":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate03":string,
      /**  For Epicor Development Use Only  */  
   "DemandDate04":string,
      /**  For Epicor Development Use Only  */  
   "DemandLogical01":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical02":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical03":boolean,
      /**  For Epicor Development Use Only  */  
   "DemandLogical04":boolean,
      /**  The document that initiated the demand.  Will be blank when the demand is manually entered.  */  
   "DocumentName":string,
      /**  Date until this forecast is considered effective. for information purposes only. for future use.  */  
   "ForecastEndDate":string,
      /**  The dockingstation of the shipto address.  For future use.  */  
   "DockingStation":string,
      /**  The location within the customer shipto address.  For future use.  */  
   "Location":string,
      /**  The code of the transport routing/time. For future use.  */  
   "TransportID":string,
      /**  Ship the good by this time.  */  
   "ShipbyTime":number,
      /**  Indicates that the One Time ShipTO information defined for this release should be used.  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping Country Number  */  
   "OTSCountryNum":number,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a store description.
Will be printed on the packing slip  */  
   "SubShipTo":string,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a routing description.
Will be printed on the packing slip  */  
   "ShipRouting":string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  Last update to the demand schedule record  */  
   "CreateDate":string,
      /**  Bookdate of the related bookrel by the sales order releases on the demand schedule  */  
   "ProcessDate":string,
      /**  Booktime of the related bookrel by the sales order releases on the demand schedule  */  
   "ProcessTime":number,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   "MFCustNum":number,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   "UseOTMF":boolean,
      /**  One Time Mark For Name of the ShipTo.  */  
   "OTMFName":string,
      /**  One Time Mark For first line of the ShipTo address.  */  
   "OTMFAddress1":string,
      /**  One Time Mark For second line of the ShipTo address.  */  
   "OTMFAddress2":string,
      /**  One Time Mark For third line of the ShipTo address.  */  
   "OTMFAddress3":string,
      /**  City portion of the One Time Mark For address.  */  
   "OTMFCity":string,
      /**  The state or province portion of the One Time Mark For address.  */  
   "OTMFState":string,
      /**  The zip or postal code portion of the One Time Mark For address.  */  
   "OTMFZIP":string,
      /**  One Time Mark For Contact Name  */  
   "OTMFContact":string,
      /**  Fax number for the One Time Mark For.  */  
   "OTMFFaxNum":string,
      /**  Phone number for the One Time Mark For  */  
   "OTMFPhoneNum":string,
      /**  Country number for the One Time Mark For  */  
   "OTMFCountryNum":number,
      /**  Quote Number to which this record is related.  */  
   "QuoteNum":number,
      /**  Quote Line Number to which this record is related.  */  
   "QuoteLine":number,
      /**  The release number to which this schedule is related.  */  
   "QuoteRelNum":number,
      /**  Date customer needs the item to be delivered and calculated by CTP  */  
   "CTPNeedByDate":string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date and calculated by CTP.  */  
   "CTPShipDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  OTSCustSaved  */  
   "OTSCustSaved":boolean,
      /**  OTSSaveAs  */  
   "OTSSaveAs":string,
      /**  OTSSaveCustID  */  
   "OTSSaveCustID":string,
      /**  OTSSaved  */  
   "OTSSaved":boolean,
      /**  OTSShipToNum  */  
   "OTSShipToNum":string,
      /**  The value will be set to true  if a manual CTP calculation was confirmed for this demand schedule. It will prevent auto CTP calculation for this demand schedule during process demand.  */  
   "CTPManualConfirm":boolean,
      /**  The value will be set to the calculated CapPromiseDtl  JobNum (Source)  if a manual CTP calculation was confirmed for this demand schedule.  */  
   "CTPSource":string,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
      /**  The value of the Customer.AllowShipTo3 of the Cusomer by the DemandHead. If this is false then the DemandSchedule.ShipToCustNum is  disabled  */  
   "CustNumAllowShipTo3":boolean,
   "DemandContractLine":number,
      /**  Support for OTMFCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTMFCountryNum will be populated based on it  */  
   "EDI_OTMFCountry":string,
      /**  Support for OTSCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTSCountryNum will be populated based on it  */  
   "EDI_OTSCountry":string,
      /**  Indicates if the Log action item is available.  */  
   "EnableLog":boolean,
      /**  Indicates if the OverrideSystemReject option is available or not.  */  
   "EnableOverrideReject":boolean,
      /**  Indicates if the user Reject option is available.  */  
   "EnableReject":boolean,
   "EnableUnreject":boolean,
   "IUM":string,
      /**  Contains the Mark For Address  */  
   "MarkForAddrList":string,
   "MFCustID":string,
      /**  Used to pass the value of Customer.AllowOTS to the client so that it can easily be used in Row Rules.  */  
   "OTSAllowed":boolean,
   "PartNum":string,
   "PONum":string,
      /**  Indicates if this record is in read-only mode.  */  
   "ReadOnly":boolean,
   "SalesUM":string,
      /**  Contains the Ship To Address  */  
   "ShipToAddrList":string,
   "ShipToCustID":string,
   "BitFlag":number,
   "DemandContractHdrDemandContract":string,
   "DmdMassGrpCreatedBy":string,
   "MarkForNumInactive":boolean,
   "OTMFCountryDescription":string,
   "OTSCountryISOCode":string,
   "OTSCountryDescription":string,
   "OTSCountryEUMember":boolean,
   "OTSTaxRegionCodeDescription":string,
   "ShipToNumInactive":boolean,
   "ShipViaWebDesc":string,
   "ShipViaDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param addressList
   */  
export interface BuildDisplayAddress_input{
   addressList:string,
}

export interface BuildDisplayAddress_output{
   returnObj:string,
}

   /** Required : 
      @param ipCreateNewSO
      @param ds
   */  
export interface ChangeCreateNewOrder_input{
      /**  Boolean value to enable/disable CreateNewOrder flag  */  
   ipCreateNewSO:boolean,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeCreateNewOrder_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param iCustomerPrice
      @param ds
   */  
export interface ChangeDemandDetailCustomerPrice_input{
      /**  The Customer Price  */  
   iCustomerPrice:number,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandDetailCustomerPrice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param proposedDemandContractLine
      @param ds
   */  
export interface ChangeDemandDetailDemandContractLine_input{
      /**  The proposed Demand Contract Line  */  
   proposedDemandContractLine:number,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandDetailDemandContractLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param iInternalPrice
      @param ds
   */  
export interface ChangeDemandDetailInternalPrice_input{
      /**  The Internal Price  */  
   iInternalPrice:number,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandDetailInternalPrice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param iMktgCampaignID
      @param ds
   */  
export interface ChangeDemandDetailMktgCamp_input{
      /**  The Marketing Campaign ID  */  
   iMktgCampaignID:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandDetailMktgCamp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param iPartNum
      @param ds
      @param sysRowID
      @param rowType
   */  
export interface ChangeDemandDetailPartNum_input{
      /**  The part  */  
   iPartNum:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   sysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface ChangeDemandDetailPartNum_output{
parameters : {
      /**  output parameters  */  
   iPartNum:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDemandDetailRevisionNum_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandDetailRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDemandDetailUOM_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandDetailUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param iUnitPrice
      @param ds
   */  
export interface ChangeDemandDetailUnitPrice_input{
      /**  The Unit Price  */  
   iUnitPrice:number,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandDetailUnitPrice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param proposedBTCustID
      @param ds
   */  
export interface ChangeDemandHeadBTCustID_input{
      /**  The proposed Bill To Cust ID  */  
   proposedBTCustID:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandHeadBTCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ipCancelPO
      @param ds
   */  
export interface ChangeDemandHeadCancelPO_input{
      /**  Boolean value to enable/disable Cancel PO flag  */  
   ipCancelPO:boolean,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandHeadCancelPO_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param proposedDemandContractNum
      @param ds
   */  
export interface ChangeDemandHeadDemandContractNum_input{
      /**  The proposed Demand Contract Number  */  
   proposedDemandContractNum:number,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandHeadDemandContractNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param proposedDemandContract
      @param ds
   */  
export interface ChangeDemandHeadDemandContract_input{
      /**  The proposed Demand Contract  */  
   proposedDemandContract:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandHeadDemandContract_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param proposedERSOrder
      @param ds
   */  
export interface ChangeDemandHeadERSOrder_input{
      /**  The proposed ERS Order  */  
   proposedERSOrder:boolean,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandHeadERSOrder_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ipShipToCustID
      @param ds
   */  
export interface ChangeDemandHeadShipToCustID_input{
      /**  The proposed ShipTo Customer ID  */  
   ipShipToCustID:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandHeadShipToCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param proposedShipToNum
      @param ds
   */  
export interface ChangeDemandHeadShipToNum_input{
      /**  The proposed Ship To Num  */  
   proposedShipToNum:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandHeadShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDemandHeadUseOTS_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandHeadUseOTS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param proposedShipToNum
      @param ds
   */  
export interface ChangeDemandScheduleCreateShipToNum_input{
      /**  The Proposed ShipToNum  */  
   proposedShipToNum:string,
   ds:Erp_Tablesets_DemandScheduleCreateTableset[],
}

export interface ChangeDemandScheduleCreateShipToNum_output{
parameters : {
      /**  output parameters  */  
   cCreateCycleList:string,
   ds:Erp_Tablesets_DemandScheduleCreateTableset[],
}
}

   /** Required : 
      @param newDeliveryDays
      @param ds
   */  
export interface ChangeDemandScheduleDeliveryDays_input{
      /**  The new DeliveryDays  */  
   newDeliveryDays:number,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandScheduleDeliveryDays_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ipMFCustID
      @param ds
   */  
export interface ChangeDemandScheduleMFCustID_input{
      /**  The proposed Mark For Customer ID  */  
   ipMFCustID:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandScheduleMFCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param proposedMarkForNum
      @param ds
   */  
export interface ChangeDemandScheduleMarkForNum_input{
      /**  The Proposed ShipToNum  */  
   proposedMarkForNum:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandScheduleMarkForNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param proposedNeedByDate
      @param ds
   */  
export interface ChangeDemandScheduleNeedByDate_input{
      /**  The Proposed NeedByDate  */  
   proposedNeedByDate:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandScheduleNeedByDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDemandScheduleOTSDetails_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandScheduleOTSDetails_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param proposedPlant
      @param ds
   */  
export interface ChangeDemandSchedulePlant_input{
      /**  The Proposed Plant  */  
   proposedPlant:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandSchedulePlant_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param proposedReqDate
      @param ds
   */  
export interface ChangeDemandScheduleReqDate_input{
      /**  The Proposed ReqDate  */  
   proposedReqDate:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandScheduleReqDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param proposedSellingReqQty
      @param ds
   */  
export interface ChangeDemandScheduleSellingReqQty_input{
      /**  The proposed Selling Req Quantity  */  
   proposedSellingReqQty:number,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandScheduleSellingReqQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ipShipToCustID
      @param ds
   */  
export interface ChangeDemandScheduleShipToCustID_input{
      /**  The proposed ShipTo Customer ID  */  
   ipShipToCustID:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandScheduleShipToCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param proposedShipToNum
      @param ds
   */  
export interface ChangeDemandScheduleShipToNum_input{
      /**  The Proposed ShipToNum  */  
   proposedShipToNum:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandScheduleShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDemandScheduleUseOTMF_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandScheduleUseOTMF_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDemandScheduleUseOTS_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeDemandScheduleUseOTS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param tableName
      @param ds
   */  
export interface ChangeMiscAmount_input{
      /**  name of table being passed in  */  
   tableName:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeMiscAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param tableName
      @param ds
   */  
export interface ChangeMiscCode_input{
      /**  name of table being passed in  */  
   tableName:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeMiscCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param tableName
      @param ds
   */  
export interface ChangeMiscPercent_input{
      /**  name of table being passed in  */  
   tableName:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface ChangeMiscPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CheckPartRevisionChange_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface CheckPartRevisionChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
   cConfigPartMessage:string,
}
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
   */  
export interface CloseAllSchedules_input{
      /**  The Demand Detail Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Detail Header Sequence number  */  
   iDemandHeadSeq:number,
}

export interface CloseAllSchedules_output{
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
   */  
export interface CloseDemandDetail_input{
      /**  The Demand Detail Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Detail Header Sequence number  */  
   iDemandHeadSeq:number,
      /**  The Demand Detail Detail Sequence number  */  
   iDemandDtlSeq:number,
}

export interface CloseDemandDetail_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
   */  
export interface CloseDemandHead_input{
      /**  The Demand Header Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Header Sequence number  */  
   iDemandHeadSeq:number,
}

export interface CloseDemandHead_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
      @param iDemandScheduleSeq
   */  
export interface CloseDemandSchedule_input{
      /**  The Demand Schedule Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Schedule Header Sequence number  */  
   iDemandHeadSeq:number,
      /**  The Demand Schedule Detail Sequence number  */  
   iDemandDtlSeq:number,
      /**  The Demand Schedule Sequence number  */  
   iDemandScheduleSeq:number,
}

export interface CloseDemandSchedule_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param demandDtlSysRowID
   */  
export interface ConfigurationChangePart_input{
      /**  DemandDtl SysRowID  */  
   demandDtlSysRowID:string,
}

export interface ConfigurationChangePart_output{
}

   /** Required : 
      @param demandDetailSysRowID
   */  
export interface ConfigurationRefreshQty_input{
      /**  Demand Details SysRowID  */  
   demandDetailSysRowID:string,
}

export interface ConfigurationRefreshQty_output{
}

   /** Required : 
      @param ds
      @param iDemandContractNum
      @param iDemandHeadSeq
   */  
export interface CreateDemandDetailFromContractLines_input{
   ds:Erp_Tablesets_DemandContractDtlTableset[],
      /**  The Demand Header Contract Number  */  
   iDemandContractNum:number,
      /**  The Demand Header Sequence  */  
   iDemandHeadSeq:number,
}

export interface CreateDemandDetailFromContractLines_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractDtlTableset[],
}
}

   /** Required : 
      @param demandContractNum
      @param demandHeadSeq
   */  
export interface DeleteByID_input{
   demandContractNum:number,
   demandHeadSeq:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param cScheduleNumber
      @param ds
   */  
export interface DeleteScheduleByScheduleNumberKeepHeader_input{
      /**  The Demand Detail Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Detail Header Sequence number  */  
   iDemandHeadSeq:number,
      /**  Tje Schedule Number to delete  */  
   cScheduleNumber:string,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface DeleteScheduleByScheduleNumberKeepHeader_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
   cReturnMessage:string,
}
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param cScheduleNumber
   */  
export interface DeleteScheduleByScheduleNumber_input{
      /**  The Demand Detail Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Detail Header Sequence number  */  
   iDemandHeadSeq:number,
      /**  The Schedule Number to delete  */  
   cScheduleNumber:string,
}

export interface DeleteScheduleByScheduleNumber_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
parameters : {
      /**  output parameters  */  
   cReturnMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface EDIHeaderValidate_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface EDIHeaderValidate_output{
parameters : {
      /**  output parameters  */  
   cReturnMessage:string,
   dprocess:boolean,
   matchDemand:boolean,
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

export interface Erp_Tablesets_DemandContractDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  */  
   DemandContractNum:number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  */  
   DemandContractLine:number,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  */  
   PartNum:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  */  
   TestRecord:boolean,
      /**  The total selling quantity expected to be ordered for this line over the life of the contract.  */  
   SellingTotalContractQty:number,
      /**  The total quantity expected to be ordered for this line over the life of the contract.  */  
   TotalContractQty:number,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   UnitPrice:number,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  */  
   ProjectID:string,
      /**  This is the Price Group ID used to price the order line with.  */  
   PriceGroupCode:string,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Comments about the demand detail line.  */  
   DetailComments:string,
      /**  Use standard Epicor Price matrix/logic  */  
   UsePriceList:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   TotalInvoiceAmt:number,
      /**  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   TotalOrderAmt:number,
      /**  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  */  
   TotalOrderedQty:number,
      /**  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  */  
   TotalShippedQty:number,
      /**  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  */  
   TotalInvoicedQty:number,
      /**  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  */  
   DeleteCurrentReleases:boolean,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  */  
   MktgCampaignID:string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  */  
   MktgEvntSeq:number,
      /**  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  */  
   MinCallOffQty:number,
      /**  Optional field that contains the  part revision.  */  
   RevisionNum:string,
      /**  Optional field that contains the customers revision.  */  
   XRevisionNum:string,
      /**  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  */  
   DemandPricing:string,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   DocUnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt1UnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt2UnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt3UnitPrice:number,
      /**  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  */  
   OTSmartString:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   DocTotalInvoiceAmt:number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt1TotalInvoiceAmt:number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt2TotalInvoiceAmt:number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt3TotalInvoiceAmt:number,
      /**  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   DocTotalOrderAmt:number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt1TotalOrderAmt:number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt2TotalOrderAmt:number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt3TotalOrderAmt:number,
      /**  Defines the tolerance for price difference validations.  */  
   PriceTolerance:number,
      /**  Defines the tolerance for price difference validations in document currency.  */  
   DocPriceTolerance:number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   Rpt1PriceTolerance:number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   Rpt2PriceTolerance:number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   Rpt3PriceTolerance:number,
      /**  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  */  
   SelectedForDemand:boolean,
   BitFlag:number,
   DemandCntHdrDemandContract:string,
   PlantName:string,
   ProjectIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandContractDtlTableset{
   DemandContractDtl:Erp_Tablesets_DemandContractDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DemandDetailRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
      /**  The sequence from the DemandHead record this DemandDetail is related to.  */  
   DemandHeadSeq:number,
      /**  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  */  
   DemandDtlSeq:number,
      /**  The contract line this demand line is for.  */  
   DemandContractLine:number,
      /**  Determines whether or not this line is being run in a test mode.  */  
   TestRecord:boolean,
      /**  Contains the Order Number that ties this detail record back to an OrderDtl record.  */  
   OrderNum:number,
      /**  The OrderDtl record this demand detail is linked to.  */  
   OrderLine:number,
      /**  The date before which the order cannot be shipped.  */  
   DoNotShipBeforeDate:string,
      /**  The date after which the order cannot be shipped.  */  
   DoNotShipAfterDate:string,
      /**  The reference from the incoming demand source.  Can be used to locate other sales order detail records that have been created by this demand.  */  
   DemandReference:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SalesUM:string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   UnitPrice:number,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  */  
   ProjectID:string,
      /**  This is the Price Group ID used to price the order line with.  */  
   PriceGroupCode:string,
      /**  Quote number to which the line item detail record is associated with. This is part of the foreign key to QuoteHed file.  */  
   QuoteNum:number,
      /**  Quote Line number to which this line was related. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  */  
   QuoteLine:number,
      /**  The PO Type.  This is set by Service Connect when the record is created.  Reference only.  */  
   POType:string,
      /**   The type of acknowledgement that is expected by the trading partner.  Values are:
OutSOAck - Outgoing Acknowledgement
OutChgRsp - Outgoing Response to Change
OutStatus - Outgoing Order Status  */  
   AcknowledgementType:string,
      /**  The schedule type from the trading partner.  Reference only.  */  
   ScheduleType:string,
      /**  Contains the Customer number that the demand is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   PONum:string,
      /**  Indicates if the DemandDetail has been rejected by the user.  */  
   RejectedByUser:boolean,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  */  
   PartNum:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Use standard Epicor Price matrix/logic  */  
   UsePriceList:boolean,
      /**  Indicates if this record has been written to an OrderDtl.  */  
   Posted:boolean,
      /**  Indicates if the DemandDetail has been rejected by the system.  */  
   RejectedBySystem:boolean,
      /**  Indicates if the system rejection should be overridden so the record can be accepted.  */  
   OverrideSystemReject:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Indicates if the DemandDetail record is in a "open or closed" status.  */  
   OpenLine:boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLine:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter01:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter02:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter03:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter04:string,
      /**  For Epicor Development Use Only  */  
   DemandNumber01:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber02:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber03:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber04:number,
      /**  For Epicor Development Use Only  */  
   DemandDate01:string,
      /**  For Epicor Development Use Only  */  
   DemandDate02:string,
      /**  For Epicor Development Use Only  */  
   DemandDate03:string,
      /**  For Epicor Development Use Only  */  
   DemandDate04:string,
      /**  For Epicor Development Use Only  */  
   DemandLogical01:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical02:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical03:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical04:boolean,
      /**  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  */  
   DeleteCurrentReleases:boolean,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand entry if the CRM module is installed.  */  
   MktgCampaignID:string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand entry if the CRM module is installed.  */  
   MktgEvntSeq:number,
      /**  Cross Reference Part Num. Only used for audit purposes for EDI.  */  
   XRefPartNum:string,
      /**   Cross Reference Part Type. Only used for audit purposes for EDI.

I=Internal Cross Reference / C = Customer Part  */  
   XRefPartType:string,
      /**  Customer Number XRefPartNum is related to if it is a customer part. Only used for audit purposes for EDI.  */  
   XRefCustNum:number,
      /**  Optional field that contains the  part revision.  */  
   RevisionNum:string,
      /**  Optional field that contains the customers revision.  */  
   XRevisionNum:string,
      /**  The Incoming EDI Unit Price.  */  
   EDIUnitPrice:number,
      /**  The total quantity that has been received according to the training partner data  */  
   CumulativeQty:number,
      /**  The date when the trading partner calculated the cumulative quantity field  */  
   CumulativeDate:string,
      /**  A qty that will create a new reconciliation adjustment.  */  
   StartCumQty:number,
      /**  The date since the trading partner has been accumulating the quantities.  */  
   StartCumDate:string,
      /**  The pack id of the last trading partner information received by the trading partner.  */  
   LastShipmentID:number,
      /**  The quantity received in the last shipment according to the trading partner information  */  
   LastShipmentQty:number,
      /**  The date when of the last shipment according to the trading partner information  */  
   LastShipmentDate:string,
      /**  The current schedule number of the file where the cumulative info was received  */  
   ScheduleNumber:string,
      /**  Last Master Pack ID  */  
   LastMasterPack:number,
      /**  Contains the internal system unit price in a foreign currency  */  
   DocUnitPrice:number,
      /**  Contains the Customer Price in a foreign currency  */  
   DocEDIUnitPrice:number,
      /**  This is the Internal Price assigned by the system calculated from the part sales price or a price list. It will be used when the Demand Contract is using Internal Pricing.  */  
   InternalPrice:number,
      /**  The doc currency value of the internal price  */  
   DocInternalPrice:number,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   ConfigUnitPrice:number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   ConfigBaseUnitPrice:number,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  Trading Partner Quote Number. This is not an internal quote number, it is the quote sent by the trading partner.  */  
   TPQuoteNum:number,
      /**  Trading Partner Quote Line Number. This is not related to an internal quote, it is sent by the trading partner.  */  
   TPQuoteLine:number,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt1UnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt2UnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt3UnitPrice:number,
      /**  Same as Internal Price except that this field contains the Internal Price in a report currency  */  
   Rpt1InternalPrice:number,
      /**  Same as Internal Price except that this field contains the Internal Price in a report currency  */  
   Rpt2InternalPrice:number,
      /**  Same as Internal Price except that this field contains the Internal Price in a report currency  */  
   Rpt3InternalPrice:number,
      /**  Same as EDI Unit price except that this field contains the EDI unit price in a report currency  */  
   Rpt1EDIUnitPrice:number,
      /**  Same as EDI Unit price except that this field contains the EDI unit price in a report currency  */  
   Rpt2EDIUnitPrice:number,
      /**  Same as EDI Unit price except that this field contains the EDI unit price in a report currency  */  
   Rpt3EDIUnitPrice:number,
      /**  Indicates if current line is blocked for processing.  */  
   BlockProcLine:boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLineRef:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  This is field is similar to DemandContract. The field CUMMSetting helps to choose how the DemandReconciliation will open.  */  
   CUMMSetting:string,
   CurrencyCode:string,
   CurrencySwitch:boolean,
      /**  Indicates if the Create Demand Schedule option is available.  */  
   EnableCreateSchedule:boolean,
   EnableDeleteReleases:boolean,
      /**  Indicates if the Delete Schedule by Schedule Number option is available.  */  
   EnableDeleteSchedule:boolean,
      /**  Indicates if the Log action item is available.  */  
   EnableLog:boolean,
      /**  This field is true is Demand Detail is posted or has link with SO.  */  
   EnableOnlyPart:boolean,
   EnableOverrideReject:boolean,
      /**  Indicates if the Reject option is available.  */  
   EnableReject:boolean,
      /**  Indicates if the Review and Matching options are available.  */  
   EnableRevMatch:boolean,
   EnableUnreject:boolean,
      /**  True when the XRefPartNum has multiple references.  */  
   MultipleXRef:boolean,
      /**  True when exists a Price Discrepancy beetwen UnitPrice and EDIUnitPrice  */  
   PriceDiscrepancy:boolean,
      /**  Indicates if this record is in read-only mode.  */  
   ReadOnly:boolean,
   Configured:string,
   BitFlag:number,
   CustomerBTName:string,
   CustomerName:string,
   CustomerCustID:string,
   DemandContractDtlSalesUM:string,
   DemandContractHdrCUMMSetting:string,
   DemandContractHdrDemandContract:string,
   MktgCampaignIDCampDescription:string,
   MktgEvntEvntDescription:string,
   PlantName:string,
   PriceGroupDescription:string,
   ProjectDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandDtlMatchingRow{
   Company:string,
   DemandContractNum:number,
   DemandHeadSeq:number,
   DemandDtlSeq:number,
   OrderNum:number,
   OrderLine:number,
   PartNum:string,
   XPartNum:string,
   LineDesc:string,
   CustID:string,
   CustName:string,
   DemandContract:string,
   UnitPrice:number,
      /**  Indicates if the user chose to reject this record.  */  
   Rejected:boolean,
   DeleteCurrentReleases:boolean,
   IncludePOForReconcile:boolean,
   PONum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandDtlReviewRow{
   Company:string,
   DemandContractNum:number,
   DemandHeadSeq:number,
   DemandDtlSeq:number,
   DemandContract:string,
   CustID:string,
   CustName:string,
   LineDesc:string,
   PartNum:string,
   XPartNum:string,
   OrderNum:number,
   OrderLine:number,
   MDPV:number,
   AvailableQty:number,
   OnHandQty:number,
   TotalQtyDifference:number,
   TotalCostQtyDifference:number,
   IncludePOForReconcile:boolean,
   PONum:string,
      /**  Unit of Measure,  The Part Stocking UOM, if not valid part then DemandDtl.SalesUM  */  
   ReviewUOM:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandEntryTableset{
   DemandHead:Erp_Tablesets_DemandHeadRow[],
   DemandDetail:Erp_Tablesets_DemandDetailRow[],
   DemandMiscChg:Erp_Tablesets_DemandMiscChgRow[],
   DemandSchedule:Erp_Tablesets_DemandScheduleRow[],
   DemandMiscChgDH:Erp_Tablesets_DemandMiscChgDHRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DemandHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   DemandHeadSeq:number,
      /**  The OrderHed record this demand is linked to.  */  
   OrderNum:number,
      /**  Contains the Customer number that the demand is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  This is a mandatory field used to enter the customers Purchase Order Number.  */  
   PONum:string,
      /**  The date before which the order cannot be shipped.  */  
   DoNotShipBeforeDate:string,
      /**  The date after which the order cannot be shipped.  */  
   DoNotShipAfterDate:string,
      /**  The date after which the sales order should be canceled.  */  
   CancelAfterDate:string,
      /**  An optional field that describes the FOB policy.  */  
   FOB:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  */  
   TermsCode:string,
      /**  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  */  
   AllocPriorityCode:string,
      /**  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  */  
   ReservePriorityCode:string,
      /**  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  */  
   ShipOrderComplete:boolean,
      /**  Contains comments about the overall order. These will be printed on the Sales Acknowledgements.  */  
   OrderComment:string,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   AutoOrderBasedDisc:boolean,
      /**  Determines whether or not this line is being run in a test mode.  */  
   TestRecord:boolean,
      /**  The PO Type.  This is set by Service Connect when the record is created.  Reference only.  */  
   POType:string,
      /**   The type of acknowledgement that is expected by the trading partner.  Values are:
OutSOAck - Outgoing Acknowledgement
OutChgRsp - Outgoing Response to Change
OutStatus - Outgoing Order Status  */  
   AcknowledgementType:string,
      /**   The type of action to take for this demand.  Values are:
ALW - Always accept the demand automatically
ANE - Accpet the demand automatically if no errors
ASD - Always stop at demand.  User will accept demands manually.  */  
   AcceptType:string,
      /**  An internal identifier to group demand schedules together.  This will be changed every time a demand is received via EDI or changed manually.  This number will carry over to the DemandSchedule table.  This number can be manually entered, generated by the system, or come from EDI.  */  
   ScheduleNumber:string,
      /**  Holds the value of the last sequence used for ScheduleNumber.  When generating ScheduleNumbers, this field is incremented by 1 and is used to populate ScheduleNumber.  */  
   ScheduleNumberSeq:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   LockRate:boolean,
      /**  Indicates if this demand has been accepted or not.  */  
   Accepted:boolean,
      /**  Indicates if the DemandHead has been rejected by the user.  */  
   RejectedByUser:boolean,
      /**  Indicates if this demand is in an "open" status.  A demand is closed when the the Demand Contract is closed.  It can also be set if it is tied to an OrderHed and the OrderHed record is closed.  */  
   OpenDemand:boolean,
      /**  Indicates if this record and it's children (DemandDetail and DemandSchedule) have been written to the Forecast table or Order tables.  This can be toggled back on by the system as new demand schedules are created.  */  
   Posted:boolean,
      /**  Indicates if the DemandDetail has been rejected by the system.  */  
   RejectedBySystem:boolean,
      /**  Indicates if the system rejection should be overridden so the record can be accepted.  */  
   OverrideSystemReject:boolean,
      /**  For Epicor Development Use Only  */  
   DemandCharacter01:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter02:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter03:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter04:string,
      /**  For Epicor Development Use Only  */  
   DemandNumber01:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber02:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber03:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber04:number,
      /**  For Epicor Development Use Only  */  
   DemandDate01:string,
      /**  For Epicor Development Use Only  */  
   DemandDate02:string,
      /**  For Epicor Development Use Only  */  
   DemandDate03:string,
      /**  For Epicor Development Use Only  */  
   DemandDate04:string,
      /**  For Epicor Development Use Only  */  
   DemandLogical01:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical02:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical03:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical04:boolean,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Order created from EDI.  */  
   EDIOrder:boolean,
      /**  Indicates the demand has been selected for processing.  The value will be set back to false when processing has been done.  */  
   SelectedForProcessing:boolean,
      /**  Do Not Process  */  
   SCProcessing:boolean,
      /**  Indicates which customer ship to is to be used as the default for the Demand records. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new demands.  */  
   ShipToNum:string,
      /**  Flag at the Header Level that indicate that the demand can be process.  */  
   ReadyToProcess:boolean,
      /**  If turned on, this flag will rest the accumulative quantities stored in Epicor applications  */  
   ResetCums:boolean,
      /**  It will be used to identify POs that will generate an invoice at the shipment.  If the order is created manually the default for this order will be taken from the customer master file. If the order is created via EDI, the default will be taken from the value in the inbound file.  */  
   ERSOrder:boolean,
      /**  It will be displayed when the user ask to cancel the whole order. There is a field in the inbound EDI message to ask for this.  */  
   CancelPO:boolean,
      /**  new orders will be created when it is set to true  */  
   CreateNewOrder:boolean,
      /**  Sales Order linked to this Demand  */  
   LinkedOrders:string,
      /**  EDI Transaction Control Number  */  
   TCtrlNum:string,
      /**  EDI Batch Control Number  */  
   BatchNum:string,
      /**  Quote Number to which this record is related.  */  
   QuoteNum:number,
      /**  Date in which the related demand was last processed.  */  
   DemandProcessDate:string,
      /**  System Time when demand was last processed.  */  
   DemandProcessTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping Country Number  */  
   OTSCountryNum:number,
      /**  OTS Tax Liability Code (Header)  */  
   OTSTaxRegionCode:string,
      /**  Indicates if the One Time Shipto information is to be used.  */  
   UseOTS:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Holds a string with the customer address  */  
   CustAddrList:string,
      /**  Indicates if this record is in read-only mode.  */  
   ReadOnly:boolean,
   BTCustID:string,
   BillToCustomerName:string,
   BTAddressList:string,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   AvailBTCustList:string,
      /**  Indicates if the Get Contract Lines option is available.  */  
   EnableGetLines:boolean,
      /**  Indicates if the Reject option is available  */  
   EnableReject:boolean,
      /**  Indicates if the Process action item is available.  */  
   EnableProcess:boolean,
   DemandContract:string,
   EnableUnreject:boolean,
   EnableLog:boolean,
   DemandSchedAvail:boolean,
      /**  Indicates if the recently created order should be placed on hold. Defaults from Contract.  */  
   OrderHoldForReview:boolean,
      /**  Ship To Address List.  */  
   ShipToAddressList:string,
      /**  This Field is used to be related to the CustomerName Field on the Table CustomerDocs for EDI.  */  
   EDITran_Type:string,
      /**  Used to pass the value of Customer.AllowOTS to the client so that it can easily be used in Row Rules.  */  
   OTSAllowed:boolean,
   ShipToCustID:string,
      /**  The value of the Customer.AllowShipTo3 of the Cusomer by the DemandHead. If this is false then the DemandHead.ShipToCustNum is  disabled  */  
   CustNumAllowShipTo3:boolean,
      /**  Support for OTSCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTSCountryNum will be populated based on it  */  
   EDI_OTSCountry:string,
      /**  It will be displayed when the value of the ERS flag at the demand entry is different from the value in the customer master file.  */  
   ERSOverride:boolean,
      /**  Description of the currency  */  
   CurrencyCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyDocumentDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCurrName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  The unique identifier of the demand contract.  This must be unique for a customer.  */  
   DemandContractHdrDemandContract:string,
      /**  Full description of the FOB Code.  */  
   FOBDescription:string,
      /**  Country name  */  
   OTSCountryDescription:string,
      /**  Full description for the Tax Region.  */  
   OTSTaxRegionCodeDescription:string,
      /**  Description of the reservation priority. Example "High".  */  
   ReservePriDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  Full description of the terms which prints on sales orders and invoices.  */  
   TermsDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandHeadListTableset{
   DemandHeadList:Erp_Tablesets_DemandHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DemandHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   DemandHeadSeq:number,
      /**  The OrderHed record this demand is linked to.  */  
   OrderNum:number,
      /**  Contains the Customer number that the demand is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  This is a mandatory field used to enter the customers Purchase Order Number.  */  
   PONum:string,
      /**  The date before which the order cannot be shipped.  */  
   DoNotShipBeforeDate:string,
      /**  The date after which the order cannot be shipped.  */  
   DoNotShipAfterDate:string,
      /**  The date after which the sales order should be canceled.  */  
   CancelAfterDate:string,
      /**  An optional field that describes the FOB policy.  */  
   FOB:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  */  
   TermsCode:string,
      /**  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  */  
   AllocPriorityCode:string,
      /**  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  */  
   ReservePriorityCode:string,
      /**  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  */  
   ShipOrderComplete:boolean,
      /**  Contains comments about the overall order. These will be printed on the Sales Acknowledgements.  */  
   OrderComment:string,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   AutoOrderBasedDisc:boolean,
      /**  Determines whether or not this line is being run in a test mode.  */  
   TestRecord:boolean,
      /**  The PO Type.  This is set by Service Connect when the record is created.  Reference only.  */  
   POType:string,
      /**   The type of acknowledgement that is expected by the trading partner.  Values are:
OutSOAck - Outgoing Acknowledgement
OutChgRsp - Outgoing Response to Change
OutStatus - Outgoing Order Status  */  
   AcknowledgementType:string,
      /**   The type of action to take for this demand.  Values are:
ALW - Always accept the demand automatically
ANE - Accpet the demand automatically if no errors
ASD - Always stop at demand.  User will accept demands manually.  */  
   AcceptType:string,
      /**  An internal identifier to group demand schedules together.  This will be changed every time a demand is received via EDI or changed manually.  This number will carry over to the DemandSchedule table.  This number can be manually entered, generated by the system, or come from EDI.  */  
   ScheduleNumber:string,
      /**  Holds the value of the last sequence used for ScheduleNumber.  When generating ScheduleNumbers, this field is incremented by 1 and is used to populate ScheduleNumber.  */  
   ScheduleNumberSeq:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   LockRate:boolean,
      /**  Indicates if this demand has been accepted or not.  */  
   Accepted:boolean,
      /**  Indicates if the DemandHead has been rejected by the user.  */  
   RejectedByUser:boolean,
      /**  Indicates if this demand is in an "open" status.  A demand is closed when the the Demand Contract is closed.  It can also be set if it is tied to an OrderHed and the OrderHed record is closed.  */  
   OpenDemand:boolean,
      /**  Indicates if this record and it's children (DemandDetail and DemandSchedule) have been written to the Forecast table or Order tables.  This can be toggled back on by the system as new demand schedules are created.  */  
   Posted:boolean,
      /**  Indicates if the DemandDetail has been rejected by the system.  */  
   RejectedBySystem:boolean,
      /**  Indicates if the system rejection should be overridden so the record can be accepted.  */  
   OverrideSystemReject:boolean,
      /**  For Epicor Development Use Only  */  
   DemandCharacter01:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter02:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter03:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter04:string,
      /**  For Epicor Development Use Only  */  
   DemandNumber01:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber02:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber03:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber04:number,
      /**  For Epicor Development Use Only  */  
   DemandDate01:string,
      /**  For Epicor Development Use Only  */  
   DemandDate02:string,
      /**  For Epicor Development Use Only  */  
   DemandDate03:string,
      /**  For Epicor Development Use Only  */  
   DemandDate04:string,
      /**  For Epicor Development Use Only  */  
   DemandLogical01:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical02:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical03:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical04:boolean,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Order created from EDI.  */  
   EDIOrder:boolean,
      /**  Indicates the demand has been selected for processing.  The value will be set back to false when processing has been done.  */  
   SelectedForProcessing:boolean,
      /**  Do Not Process  */  
   SCProcessing:boolean,
      /**  Indicates which customer ship to is to be used as the default for the Demand records. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new demands.  */  
   ShipToNum:string,
      /**  Flag at the Header Level that indicate that the demand can be process.  */  
   ReadyToProcess:boolean,
      /**  If turned on, this flag will rest the accumulative quantities stored in Epicor applications  */  
   ResetCums:boolean,
      /**  It will be used to identify POs that will generate an invoice at the shipment.  If the order is created manually the default for this order will be taken from the customer master file. If the order is created via EDI, the default will be taken from the value in the inbound file.  */  
   ERSOrder:boolean,
      /**  It will be displayed when the user ask to cancel the whole order. There is a field in the inbound EDI message to ask for this.  */  
   CancelPO:boolean,
      /**  new orders will be created when it is set to true  */  
   CreateNewOrder:boolean,
      /**  Sales Order linked to this Demand  */  
   LinkedOrders:string,
      /**  EDI Transaction Control Number  */  
   TCtrlNum:string,
      /**  EDI Batch Control Number  */  
   BatchNum:string,
      /**  Quote Number to which this record is related.  */  
   QuoteNum:number,
      /**  Date in which the related demand was last processed.  */  
   DemandProcessDate:string,
      /**  System Time when demand was last processed.  */  
   DemandProcessTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  UserChar1  */  
   UserChar1:string,
      /**  UserChar2  */  
   UserChar2:string,
      /**  UserChar3  */  
   UserChar3:string,
      /**  UserChar4  */  
   UserChar4:string,
      /**  UserDate1  */  
   UserDate1:string,
      /**  UserDate2  */  
   UserDate2:string,
      /**  UserDate3  */  
   UserDate3:string,
      /**  UserDate4  */  
   UserDate4:string,
      /**  UserDecimal1  */  
   UserDecimal1:number,
      /**  UserDecimal2  */  
   UserDecimal2:number,
      /**  UserInteger1  */  
   UserInteger1:number,
      /**  UserInteger2  */  
   UserInteger2:number,
      /**  Ship the good by this time  */  
   ShipByTime:number,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping Country Number  */  
   OTSCountryNum:number,
      /**  OTS Tax Liability Code (Header)  */  
   OTSTaxRegionCode:string,
      /**  True if Customer or ShipTo record was created using the  OTS info.  */  
   OTSCustSaved:boolean,
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   OTSSaveAs:string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   OTSSaveCustID:string,
      /**  OTSSaved  */  
   OTSSaved:boolean,
      /**  OTS ShipToNum  */  
   OTSShipToNum:string,
      /**  Indicates if the One Time Shipto information is to be used.  */  
   UseOTS:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
   BaseCurrencyCode:string,
   CurrencySwitch:boolean,
      /**  Indicates if the Process action item is available.  */  
   EnableProcess:boolean,
      /**  Indicates if the Reject option is available  */  
   EnableReject:boolean,
   EnableUnreject:boolean,
      /**  It will be displayed when the value of the ERS flag at the demand entry is different from the value in the customer master file.  */  
   ERSOverride:boolean,
   OpenContract:boolean,
      /**  Indicates if the recently created order should be placed on hold. Defaults from Contract.  */  
   OrderHoldForReview:boolean,
      /**  Used to pass the value of Customer.AllowOTS to the client so that it can easily be used in Row Rules.  */  
   OTSAllowed:boolean,
      /**  OTS Country Description  */  
   OTSCountryDescription:string,
      /**  OTS Tax Region Description  */  
   OTSTaxRegionCodeDescription:string,
      /**  Indicates if this record is in read-only mode.  */  
   ReadOnly:boolean,
      /**  Ship To Address List.  */  
   ShipToAddressList:string,
   ShipToCustID:string,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   AvailBTCustList:string,
   BillToCustomerName:string,
   BTAddressList:string,
   BTCustID:string,
      /**  Holds a string with the customer address  */  
   CustAddrList:string,
      /**  The value of the Customer.AllowShipTo3 of the Cusomer by the DemandHead. If this is false then the DemandHead.ShipToCustNum is  disabled  */  
   CustNumAllowShipTo3:boolean,
   DemandContract:string,
   DemandSchedAvail:boolean,
      /**  Support for OTSCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTSCountryNum will be populated based on it  */  
   EDI_OTSCountry:string,
      /**  This Field is used to be related to the CustomerName Field on the Table CustomerDocs for EDI.  */  
   EDITran_Type:string,
      /**  Indicates if the Get Contract Lines option is available.  */  
   EnableGetLines:boolean,
   EnableLog:boolean,
   BitFlag:number,
   BTCustNumInactive:boolean,
   CurrencyCurrSymbol:string,
   CurrencyCurrencyID:string,
   CurrencyCurrDesc:string,
   CurrencyCurrName:string,
   CurrencyDocumentDesc:string,
   CustomerInactive:boolean,
   CustomerCustID:string,
   CustomerName:string,
   CustomerBTName:string,
   DemandContractHdrDemandContract:string,
   FOBDescription:string,
   OTSCountryISOCode:string,
   OTSCountryEUMember:boolean,
   OTSCountryDescription_:string,
   ReservePriDescription:string,
   ShipToCustNumInactive:boolean,
   ShipToNumInactive:boolean,
   ShipViaCodeWebDesc:string,
   ShipViaCodeDescription:string,
   TermsDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandMatchingTableset{
   DemandDtlMatching:Erp_Tablesets_DemandDtlMatchingRow[],
   OrderRelToMatch:Erp_Tablesets_OrderRelToMatchRow[],
   DemandScheduleToMatch:Erp_Tablesets_DemandScheduleToMatchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DemandMiscChgDHRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The demand contract this demand misc charge is for.  */  
   DemandContractNum:number,
      /**  The DemandHead this charge is for.  */  
   DemandHeadSeq:number,
      /**  Demand Detail sequence that this miscellaneous record is related to. If related to the DemandHead then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when miscellaneous maintenance was requested.  */  
   DemandDtlSeq:number,
      /**  This along with Company, DemandHeadSeq and DemandDetailSeq make up the unique keys for this record.  */  
   SeqNum:number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. The default is provided by MiscChrg.Description, but it's overridable by the user. This can't be blank.  */  
   Description:string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   MiscAmt:number,
      /**  The amount of the Miscellaneous Charge/Credit(display value). Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   DocMiscAmt:number,
      /**  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  */  
   FreqCode:string,
      /**  An internally used flag which indicates that this record was created from a Quote via the "Get Quote" function. "Q" = related to the QuoteQty record, "L" = related to the overall QuoteDtl record. This flag is used so that the OrderMsc file can be refreshed from the QuoteMsc when Quantity or Quote/Line # changes occur. The logic is that if a change in order quantity of a order line that is linked to a quote causes a different price break to be selected then all the existing all OrderMsc records where Quoting = "Q" are deleted and then re-pulled in based on the new qty. If the Quote # or QuoteLine are changed then all OrderMsc records where Quoting is either a "Q" or "L" are deleted then re-pulled in from the newly referenced quote.  */  
   Quoting:string,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Indicates if this record is in read-only mode.  */  
   ReadOnly:boolean,
   CurrencySwitch:boolean,
   BitFlag:number,
   MiscCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandMiscChgRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The demand contract this demand misc charge is for.  */  
   DemandContractNum:number,
      /**  The DemandHead this charge is for.  */  
   DemandHeadSeq:number,
      /**  Demand Detail sequence that this miscellaneous record is related to. If related to the DemandHead then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when miscellaneous maintenance was requested.  */  
   DemandDtlSeq:number,
      /**  This along with Company, DemandHeadSeq and DemandDetailSeq make up the unique keys for this record.  */  
   SeqNum:number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. The default is provided by MiscChrg.Description, but it's overridable by the user. This can't be blank.  */  
   Description:string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   MiscAmt:number,
      /**  The amount of the Miscellaneous Charge/Credit(display value). Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   DocMiscAmt:number,
      /**  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  */  
   FreqCode:string,
      /**  An internally used flag which indicates that this record was created from a Quote via the "Get Quote" function. "Q" = related to the QuoteQty record, "L" = related to the overall QuoteDtl record. This flag is used so that the OrderMsc file can be refreshed from the QuoteMsc when Quantity or Quote/Line # changes occur. The logic is that if a change in order quantity of a order line that is linked to a quote causes a different price break to be selected then all the existing all OrderMsc records where Quoting = "Q" are deleted and then re-pulled in based on the new qty. If the Quote # or QuoteLine are changed then all OrderMsc records where Quoting is either a "Q" or "L" are deleted then re-pulled in from the newly referenced quote.  */  
   Quoting:string,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Indicates if this record is in read-only mode.  */  
   ReadOnly:boolean,
   CurrencySwitch:boolean,
   BitFlag:number,
   MiscCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandReviewTableset{
   DemandDtlReview:Erp_Tablesets_DemandDtlReviewRow[],
   DemandSchedReview:Erp_Tablesets_DemandSchedReviewRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DemandSchedReviewRow{
   Company:string,
   DemandContractNum:number,
   DemandHeadSeq:number,
   DemandDtlSeq:number,
   DemandReviewSeq:number,
   ReqDate:string,
   NeedByDate:string,
   CurDemandQty:number,
   CurBalance:number,
   ProposedDemandQty:number,
   ProposedBalance:number,
   DemandReference:string,
   QuantityDifference:number,
   BalanceDifference:number,
   CostQtyDifference:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandScheduleCreateRow{
   Company:string,
   DemandContractNum:number,
   DemandHeadSeq:number,
   DemandDtlSeq:number,
   PartNum:string,
   BeginDate:string,
   EndDate:string,
   DateType:string,
   QuantityPer:number,
   CreateCycle:string,
   CreateType:string,
      /**  The contract name  */  
   DemandContract:string,
      /**  The description of the line the schedule is being created for.  */  
   LineDesc:string,
   CustNum:number,
   ShipToNum:string,
   ShipToAddrList:string,
   CustID:string,
   CustName:string,
   Plant:string,
   PlantName:string,
   ScheduleNumber:string,
   ShipToCustNum:number,
   ShipToCustID:string,
   CustNumAllowShipTo3:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandScheduleCreateTableset{
   DemandScheduleCreate:Erp_Tablesets_DemandScheduleCreateRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DemandScheduleRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The demand contract this demand schedule is for.  */  
   DemandContractNum:number,
      /**  The sequence from the DemandHead record this DemandSchedule is related to.  */  
   DemandHeadSeq:number,
      /**  The sequence from the DemandDetail record this DemandSchedule is related to.  */  
   DemandDtlSeq:number,
      /**  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDetailSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandSchedulel record for the DemandDetail and the adding 1 to it.  */  
   DemandScheduleSeq:number,
      /**  All invoices belong to a group until the group is closed. The GroupID is assigned by the user.  */  
   GroupID:string,
      /**  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   OurReqQty:number,
      /**  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  */  
   ShipViaCode:string,
      /**  Quantity ,using Selling U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   SellingReqQty:number,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  */  
   ReqDate:string,
      /**  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  */  
   NeedByDate:string,
      /**  The Mark For to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file.  */  
   MarkForNum:string,
      /**  The delivery days required for the shipment to reach its destination.  Defaults from Customer.DemandDeliveryDays or ShipTo.DemandDeliveryDays.  */  
   DeliveryDays:number,
      /**  An internal identifier to group demand schedules together.  This will be changed every time a demand is received via EDI or changed manually.  This number will carry over to the DemandSchedule table.  This number can be manually entered, generated by the system, or come from EDI.  */  
   ScheduleNumber:string,
      /**   The type of demand this line represents.  Values are:
InForecast - Incoming Forecast (Forecasts)
InUnfirm - Incoming Unfirm Releases (Unfirm OrderRel)
InShSched - Incoming Shipping Schedule (Firm OrderRel)  */  
   DemandType:string,
      /**  Sales order number of the OrderRel record this DemandSchedule is linked to.  */  
   OrderNum:number,
      /**  Sales order Line number of the OrderRel record this DemandSchedule is linked to.  */  
   OrderLine:number,
      /**  Sales order release number of the OrderRel record this DemandSchedule is linked to.  */  
   OrderRelNum:number,
      /**  Indicates if the DemandSchedule has been rejected by the user.  */  
   RejectedByUser:boolean,
      /**  RAN Number.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  */  
   RAN:string,
      /**  Demand Reference.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  */  
   DemandReference:string,
      /**  Indicates if this record has been written to an OrderDtl.  */  
   Posted:boolean,
      /**  Indicates if the DemandDetail has been rejected by the system.  */  
   RejectedBySystem:boolean,
      /**  Indicates if the system rejection should be overridden so the record can be accepted.  */  
   OverrideSystemReject:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Indicates if this schedule is open.  */  
   OpenSchedule:boolean,
      /**  For Epicor Development Use Only  */  
   DemandCharacter01:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter02:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter03:string,
      /**  For Epicor Development Use Only  */  
   DemandCharacter04:string,
      /**  For Epicor Development Use Only  */  
   DemandNumber01:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber02:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber03:number,
      /**  For Epicor Development Use Only  */  
   DemandNumber04:number,
      /**  For Epicor Development Use Only  */  
   DemandDate01:string,
      /**  For Epicor Development Use Only  */  
   DemandDate02:string,
      /**  For Epicor Development Use Only  */  
   DemandDate03:string,
      /**  For Epicor Development Use Only  */  
   DemandDate04:string,
      /**  For Epicor Development Use Only  */  
   DemandLogical01:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical02:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical03:boolean,
      /**  For Epicor Development Use Only  */  
   DemandLogical04:boolean,
      /**  The document that initiated the demand.  Will be blank when the demand is manually entered.  */  
   DocumentName:string,
      /**  Date until this forecast is considered effective. for information purposes only. for future use.  */  
   ForecastEndDate:string,
      /**  The dockingstation of the shipto address.  For future use.  */  
   DockingStation:string,
      /**  The location within the customer shipto address.  For future use.  */  
   Location:string,
      /**  The code of the transport routing/time. For future use.  */  
   TransportID:string,
      /**  Ship the good by this time.  */  
   ShipbyTime:number,
      /**  Indicates that the One Time ShipTO information defined for this release should be used.  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping Country Number  */  
   OTSCountryNum:number,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a store description.
Will be printed on the packing slip  */  
   SubShipTo:string,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a routing description.
Will be printed on the packing slip  */  
   ShipRouting:string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  Last update to the demand schedule record  */  
   CreateDate:string,
      /**  Bookdate of the related bookrel by the sales order releases on the demand schedule  */  
   ProcessDate:string,
      /**  Booktime of the related bookrel by the sales order releases on the demand schedule  */  
   ProcessTime:number,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   MFCustNum:number,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   UseOTMF:boolean,
      /**  One Time Mark For Name of the ShipTo.  */  
   OTMFName:string,
      /**  One Time Mark For first line of the ShipTo address.  */  
   OTMFAddress1:string,
      /**  One Time Mark For second line of the ShipTo address.  */  
   OTMFAddress2:string,
      /**  One Time Mark For third line of the ShipTo address.  */  
   OTMFAddress3:string,
      /**  City portion of the One Time Mark For address.  */  
   OTMFCity:string,
      /**  The state or province portion of the One Time Mark For address.  */  
   OTMFState:string,
      /**  The zip or postal code portion of the One Time Mark For address.  */  
   OTMFZIP:string,
      /**  One Time Mark For Contact Name  */  
   OTMFContact:string,
      /**  Fax number for the One Time Mark For.  */  
   OTMFFaxNum:string,
      /**  Phone number for the One Time Mark For  */  
   OTMFPhoneNum:string,
      /**  Country number for the One Time Mark For  */  
   OTMFCountryNum:number,
      /**  Quote Number to which this record is related.  */  
   QuoteNum:number,
      /**  Quote Line Number to which this record is related.  */  
   QuoteLine:number,
      /**  The release number to which this schedule is related.  */  
   QuoteRelNum:number,
      /**  Date customer needs the item to be delivered and calculated by CTP  */  
   CTPNeedByDate:string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date and calculated by CTP.  */  
   CTPShipDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  OTSCustSaved  */  
   OTSCustSaved:boolean,
      /**  OTSSaveAs  */  
   OTSSaveAs:string,
      /**  OTSSaveCustID  */  
   OTSSaveCustID:string,
      /**  OTSSaved  */  
   OTSSaved:boolean,
      /**  OTSShipToNum  */  
   OTSShipToNum:string,
      /**  The value will be set to true  if a manual CTP calculation was confirmed for this demand schedule. It will prevent auto CTP calculation for this demand schedule during process demand.  */  
   CTPManualConfirm:boolean,
      /**  The value will be set to the calculated CapPromiseDtl  JobNum (Source)  if a manual CTP calculation was confirmed for this demand schedule.  */  
   CTPSource:string,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  The value of the Customer.AllowShipTo3 of the Cusomer by the DemandHead. If this is false then the DemandSchedule.ShipToCustNum is  disabled  */  
   CustNumAllowShipTo3:boolean,
   DemandContractLine:number,
      /**  Support for OTMFCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTMFCountryNum will be populated based on it  */  
   EDI_OTMFCountry:string,
      /**  Support for OTSCountryNum, when being sent from EDI the country id will be sent instead of the number, this field will be a placeholder for that ID, then the OTSCountryNum will be populated based on it  */  
   EDI_OTSCountry:string,
      /**  Indicates if the Log action item is available.  */  
   EnableLog:boolean,
      /**  Indicates if the OverrideSystemReject option is available or not.  */  
   EnableOverrideReject:boolean,
      /**  Indicates if the user Reject option is available.  */  
   EnableReject:boolean,
   EnableUnreject:boolean,
   IUM:string,
      /**  Contains the Mark For Address  */  
   MarkForAddrList:string,
   MFCustID:string,
      /**  Used to pass the value of Customer.AllowOTS to the client so that it can easily be used in Row Rules.  */  
   OTSAllowed:boolean,
   PartNum:string,
   PONum:string,
      /**  Indicates if this record is in read-only mode.  */  
   ReadOnly:boolean,
   SalesUM:string,
      /**  Contains the Ship To Address  */  
   ShipToAddrList:string,
   ShipToCustID:string,
   BitFlag:number,
   DemandContractHdrDemandContract:string,
   DmdMassGrpCreatedBy:string,
   MarkForNumInactive:boolean,
   OTMFCountryDescription:string,
   OTSCountryISOCode:string,
   OTSCountryDescription:string,
   OTSCountryEUMember:boolean,
   OTSTaxRegionCodeDescription:string,
   ShipToNumInactive:boolean,
   ShipViaWebDesc:string,
   ShipViaDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandScheduleToMatchRow{
   Company:string,
   DemandContractNum:number,
   DemandHeadSeq:number,
   DemandDtlSeq:number,
   DemandScheduleSeq:number,
   ReqDate:string,
   NeedByDate:string,
      /**  .  */  
   OurReqQty:number,
   SellingReqQty:number,
   OrderNum:number,
   OrderLine:number,
   OrderRelNum:number,
   DemandReference:string,
      /**  Indicates if this record has been rejected by the user.  */  
   Rejected:boolean,
      /**  Indicates if the Demand Schedule has been matched either by the system or by the user.  */  
   IsMatched:boolean,
   SalesUM:string,
   IUM:string,
      /**  Same as DemandSchedule.DemandType  */  
   DemandType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderRelToMatchRow{
   Company:string,
   OrderNum:number,
   OrderLine:number,
   OrderRelNum:number,
   ReqDate:string,
   NeedByDate:string,
   OurReqQty:number,
      /**  .  */  
   SellingReqQty:number,
   DemandReference:string,
   DemandContractNum:number,
   DemandHeadSeq:number,
   DemandDtlSeq:number,
   Matched:boolean,
   SalesUM:string,
   IUM:string,
      /**  Same as DemandSchedule.DemandType  */  
   DemandType:string,
      /**  Same as OrderRel.OpenRelease  */  
   OpenRelease:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtDemandEntryTableset{
   DemandHead:Erp_Tablesets_DemandHeadRow[],
   DemandDetail:Erp_Tablesets_DemandDetailRow[],
   DemandMiscChg:Erp_Tablesets_DemandMiscChgRow[],
   DemandSchedule:Erp_Tablesets_DemandScheduleRow[],
   DemandMiscChgDH:Erp_Tablesets_DemandMiscChgDHRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param sourceSysRowID
   */  
export interface GetBasePartAndConfigType_input{
      /**  DemandDtl sysrowid  */  
   sourceSysRowID:string,
}

export interface GetBasePartAndConfigType_output{
parameters : {
      /**  output parameters  */  
   cfgPartNum:string,
   cfgRevisionNum:string,
   configType:string,
   configURL:string,
   configID:string,
}
}

   /** Required : 
      @param sourceSysRowID
   */  
export interface GetBasePartForConfig_input{
      /**  Order Number of the target Assembly  */  
   sourceSysRowID:string,
}

export interface GetBasePartForConfig_output{
parameters : {
      /**  output parameters  */  
   cfgPartNum:string,
   cfgRevisionNum:string,
}
}

   /** Required : 
      @param demandContractNum
      @param demandHeadSeq
   */  
export interface GetByID_input{
   demandContractNum:number,
   demandHeadSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
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
      @param iCustNum
      @param cShipToNum
   */  
export interface GetCreateCycleListValues_input{
   iCustNum:number,
   cShipToNum:string,
}

export interface GetCreateCycleListValues_output{
parameters : {
      /**  output parameters  */  
   CreateCycleList:string,
}
}

   /** Required : 
      @param iDemandContractNum
   */  
export interface GetDemandContractDtl_input{
      /**  The Demand Contract Number to get the lines from  */  
   iDemandContractNum:number,
}

export interface GetDemandContractDtl_output{
   returnObj:Erp_Tablesets_DemandContractDtlTableset[],
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
   */  
export interface GetDemandDtlReview_input{
      /**  The Demand Header Contract Number  */  
   iDemandContractNum:number,
      /**  The Demand Header Sequence Number  */  
   iDemandHeadSeq:number,
}

export interface GetDemandDtlReview_output{
   returnObj:Erp_Tablesets_DemandReviewTableset[],
}

   /** Required : 
      @param whereClauseDemandHead
      @param pageSize
      @param absolutePage
   */  
export interface GetDemandHeadData_input{
      /**  The search criteria  */  
   whereClauseDemandHead:string,
      /**  Size of a page  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetDemandHeadData_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
   */  
export interface GetDemandMatching_input{
      /**  The Demand Header Contract Number  */  
   iDemandContractNum:number,
      /**  The Demand Header Sequence Number  */  
   iDemandHeadSeq:number,
}

export interface GetDemandMatching_output{
   returnObj:Erp_Tablesets_DemandMatchingTableset[],
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
   */  
export interface GetDemandScheduleCreate_input{
      /**  The Demand Header Contract Number  */  
   iDemandContractNum:number,
      /**  The Demand Header Sequence Number  */  
   iDemandHeadSeq:number,
      /**  The Demand Detail Sequence Number  */  
   iDemandDtlSeq:number,
}

export interface GetDemandScheduleCreate_output{
   returnObj:Erp_Tablesets_DemandScheduleCreateTableset[],
parameters : {
      /**  output parameters  */  
   cCreateCycleList:string,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListCustomWithPaging_input{
      /**  The search criteria  */  
   whereClause:string,
      /**  Size of a page  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetListCustomWithPaging_output{
   returnObj:Erp_Tablesets_DemandHeadListTableset[],
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
export interface GetListCustom_input{
      /**  The search criteria  */  
   whereClause:string,
      /**  Size of a page  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetListCustom_output{
   returnObj:Erp_Tablesets_DemandHeadListTableset[],
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
   returnObj:Erp_Tablesets_DemandHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param demandContractNum
      @param demandHeadSeq
   */  
export interface GetNewDemandDetail_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
   demandContractNum:number,
   demandHeadSeq:number,
}

export interface GetNewDemandDetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param demandContractNum
   */  
export interface GetNewDemandHead_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
   demandContractNum:number,
}

export interface GetNewDemandHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param demandContractNum
      @param demandHeadSeq
      @param demandDtlSeq
   */  
export interface GetNewDemandMiscChgDH_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
   demandContractNum:number,
   demandHeadSeq:number,
   demandDtlSeq:number,
}

export interface GetNewDemandMiscChgDH_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param demandContractNum
      @param demandHeadSeq
      @param demandDtlSeq
   */  
export interface GetNewDemandMiscChg_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
   demandContractNum:number,
   demandHeadSeq:number,
   demandDtlSeq:number,
}

export interface GetNewDemandMiscChg_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param demandContractNum
      @param demandHeadSeq
      @param demandDtlSeq
   */  
export interface GetNewDemandSchedule_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
   demandContractNum:number,
   demandHeadSeq:number,
   demandDtlSeq:number,
}

export interface GetNewDemandSchedule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ipCustNum
      @param ipPONum
      @param ipUnitPrice
      @param ipEDIUnitPrice
      @param ipDemandDtlSeq
   */  
export interface GetPriceDiscrepancy_input{
      /**  CustNum  */  
   ipCustNum:number,
      /**  poNum_ex  */  
   ipPONum:string,
      /**  UnitPrice  */  
   ipUnitPrice:number,
      /**  EDIUnitPrice  */  
   ipEDIUnitPrice:number,
      /**  DemandDtlSeq  */  
   ipDemandDtlSeq:number,
}

export interface GetPriceDiscrepancy_output{
parameters : {
      /**  output parameters  */  
   opPriceDiscrepancy:boolean,
}
}

   /** Required : 
      @param whereClauseDemandHead
      @param whereClauseDemandDetail
      @param whereClauseDemandMiscChg
      @param whereClauseDemandSchedule
      @param whereClauseDemandMiscChgDH
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDemandHead:string,
   whereClauseDemandDetail:string,
   whereClauseDemandMiscChg:string,
   whereClauseDemandSchedule:string,
   whereClauseDemandMiscChgDH:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
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
   */  
export interface MassCreateDemandSchedule_input{
   ds:Erp_Tablesets_DemandScheduleCreateTableset[],
}

export interface MassCreateDemandSchedule_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandScheduleCreateTableset[],
   cReturnText:string,
}
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
   */  
export interface OpenDemandDetail_input{
      /**  The Demand Detail Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Detail Header Sequence number  */  
   iDemandHeadSeq:number,
      /**  The Demand Detail Detail Sequence number  */  
   iDemandDtlSeq:number,
}

export interface OpenDemandDetail_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param ds
   */  
export interface OpenDemandHeadKeepDemandDetail_input{
      /**  The Demand Header Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Header Sequence number  */  
   iDemandHeadSeq:number,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface OpenDemandHeadKeepDemandDetail_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
   */  
export interface OpenDemandHead_input{
      /**  The Demand Header Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Header Sequence number  */  
   iDemandHeadSeq:number,
}

export interface OpenDemandHead_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
      @param iDemandScheduleSeq
   */  
export interface OpenDemandSchedule_input{
      /**  The Demand Schedule Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Schedule Header Sequence number  */  
   iDemandHeadSeq:number,
      /**  The Demand Schedule Detail Sequence number  */  
   iDemandDtlSeq:number,
      /**  The Demand Schedule Sequence number  */  
   iDemandScheduleSeq:number,
}

export interface OpenDemandSchedule_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param iContractNum
      @param iHeadSeq
      @param iDocName
      @param iPartNum
      @param iXPartNum
   */  
export interface PartValidation_input{
   iContractNum:number,
   iHeadSeq:number,
   iDocName:string,
   iPartNum:string,
   iXPartNum:string,
}

export interface PartValidation_output{
parameters : {
      /**  output parameters  */  
   iPartNum:string,
   oValidPart:boolean,
   oPartDesc:string,
   oUOM:string,
   oXRefPartType:string,
}
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
   */  
export interface ProcessDemand_input{
      /**  The Demand Header Contract Number  */  
   iDemandContractNum:number,
      /**  The Demand Header Sequence Number  */  
   iDemandHeadSeq:number,
}

export interface ProcessDemand_output{
parameters : {
      /**  output parameters  */  
   cReturnMessage:string,
   cRejectFlag:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface ProcessMatching_input{
   ds:Erp_Tablesets_DemandMatchingTableset[],
}

export interface ProcessMatching_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandMatchingTableset[],
}
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
   */  
export interface RejectDemandDetail_input{
      /**  The Demand Detail Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Detail Header Sequence number  */  
   iDemandHeadSeq:number,
      /**  The Demand Detail Detail Sequence number  */  
   iDemandDtlSeq:number,
}

export interface RejectDemandDetail_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
   */  
export interface RejectDemandHead_input{
      /**  The Demand Header Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Header Sequence number  */  
   iDemandHeadSeq:number,
}

export interface RejectDemandHead_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
      @param iDemandScheduleSeq
      @param ds
   */  
export interface RejectDemandScheduleKeepSchedules_input{
      /**  The Demand Schedule Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Schedule Header Sequence number  */  
   iDemandHeadSeq:number,
      /**  The Demand Schedule Detail Sequence number  */  
   iDemandDtlSeq:number,
      /**  The Demand Schedule Sequence number  */  
   iDemandScheduleSeq:number,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface RejectDemandScheduleKeepSchedules_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
      @param iDemandScheduleSeq
   */  
export interface RejectDemandSchedule_input{
      /**  The Demand Schedule Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Schedule Header Sequence number  */  
   iDemandHeadSeq:number,
      /**  The Demand Schedule Detail Sequence number  */  
   iDemandDtlSeq:number,
      /**  The Demand Schedule Sequence number  */  
   iDemandScheduleSeq:number,
}

export interface RejectDemandSchedule_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param lReady
   */  
export interface SetReadyToProcess_input{
      /**  The Demand Header Contract Number  */  
   iDemandContractNum:number,
      /**  The Demand Header Sequence Number  */  
   iDemandHeadSeq:number,
      /**  Indicates if the demand is ready to be processed  */  
   lReady:boolean,
}

export interface SetReadyToProcess_output{
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
   */  
export interface UnlockDemand_input{
      /**  The Demand Header Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Header Sequence number  */  
   iDemandHeadSeq:number,
      /**  The Demand Detail Detail Sequence number  */  
   iDemandDtlSeq:number,
}

export interface UnlockDemand_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
   */  
export interface UnrejectDemandDetail_input{
      /**  The Demand Detail Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Detail Header Sequence number  */  
   iDemandHeadSeq:number,
      /**  The Demand Detail Detail Sequence number  */  
   iDemandDtlSeq:number,
}

export interface UnrejectDemandDetail_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
   */  
export interface UnrejectDemandHead_input{
      /**  The Demand Header Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Header Sequence number  */  
   iDemandHeadSeq:number,
}

export interface UnrejectDemandHead_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
      @param iDemandScheduleSeq
      @param ds
   */  
export interface UnrejectDemandScheduleKeepSchedules_input{
      /**  The Demand Schedule Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Schedule Header Sequence number  */  
   iDemandHeadSeq:number,
      /**  The Demand Schedule Detail Sequence number  */  
   iDemandDtlSeq:number,
      /**  The Demand Schedule Sequence number  */  
   iDemandScheduleSeq:number,
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface UnrejectDemandScheduleKeepSchedules_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
      @param iDemandScheduleSeq
   */  
export interface UnrejectDemandSchedule_input{
      /**  The Demand Schedule Contract Num  */  
   iDemandContractNum:number,
      /**  The Demand Schedule Header Sequence number  */  
   iDemandHeadSeq:number,
      /**  The Demand Schedule Detail Sequence number  */  
   iDemandDtlSeq:number,
      /**  The Demand Schedule Sequence number  */  
   iDemandScheduleSeq:number,
}

export interface UnrejectDemandSchedule_output{
   returnObj:Erp_Tablesets_DemandEntryTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtDemandEntryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDemandEntryTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param manualValidation
      @param hmrcFraudPrevHeader
   */  
export interface ValidateOTSTaxID_input{
   ds:Erp_Tablesets_DemandEntryTableset[],
   manualValidation:boolean,
   hmrcFraudPrevHeader:string,
}

export interface ValidateOTSTaxID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandEntryTableset[],
   opMessage:string,
}
}

