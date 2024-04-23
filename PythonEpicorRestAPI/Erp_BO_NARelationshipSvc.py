import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.NARelationshipSvc
# Description: National Account Business Object
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_NARelationships(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get NARelationships items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NARelationships
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RlsHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships",headers=creds) as resp:
           return await resp.json()

async def post_NARelationships(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NARelationships
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RlsHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RlsHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_NARelationships_Company_RlsClassCode_TopCustNum_CustNum(Company, RlsClassCode, TopCustNum, CustNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NARelationship item
   Description: Calls GetByID to retrieve the NARelationship item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NARelationship
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RlsHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_NARelationships_Company_RlsClassCode_TopCustNum_CustNum(Company, RlsClassCode, TopCustNum, CustNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update NARelationship for the service
   Description: Calls UpdateExt to update NARelationship. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NARelationship
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RlsHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_NARelationships_Company_RlsClassCode_TopCustNum_CustNum(Company, RlsClassCode, TopCustNum, CustNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete NARelationship item
   Description: Call UpdateExt to delete NARelationship item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NARelationship
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_NARelationships_Company_RlsClassCode_TopCustNum_CustNum_RlsParents(Company, RlsClassCode, TopCustNum, CustNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RlsParents items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RlsParents1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RlsParentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + ")/RlsParents",headers=creds) as resp:
           return await resp.json()

async def get_NARelationships_Company_RlsClassCode_TopCustNum_CustNum_RlsParents_Company_RlsClassCode_TopCustNum_CustNum_ParentCustNum(Company, RlsClassCode, TopCustNum, CustNum, ParentCustNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RlsParent item
   Description: Calls GetByID to retrieve the RlsParent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RlsParent1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param ParentCustNum: Desc: ParentCustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RlsParentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/NARelationships(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + ")/RlsParents(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + "," + ParentCustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_RlsParents(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RlsParents items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RlsParents
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RlsParentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/RlsParents",headers=creds) as resp:
           return await resp.json()

async def post_RlsParents(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RlsParents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RlsParentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RlsParentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/RlsParents", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RlsParents_Company_RlsClassCode_TopCustNum_CustNum_ParentCustNum(Company, RlsClassCode, TopCustNum, CustNum, ParentCustNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RlsParent item
   Description: Calls GetByID to retrieve the RlsParent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RlsParent
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param ParentCustNum: Desc: ParentCustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RlsParentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/RlsParents(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + "," + ParentCustNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RlsParents_Company_RlsClassCode_TopCustNum_CustNum_ParentCustNum(Company, RlsClassCode, TopCustNum, CustNum, ParentCustNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RlsParent for the service
   Description: Calls UpdateExt to update RlsParent. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RlsParent
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param ParentCustNum: Desc: ParentCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RlsParentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/RlsParents(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + "," + ParentCustNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RlsParents_Company_RlsClassCode_TopCustNum_CustNum_ParentCustNum(Company, RlsClassCode, TopCustNum, CustNum, ParentCustNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RlsParent item
   Description: Call UpdateExt to delete RlsParent item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RlsParent
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param ParentCustNum: Desc: ParentCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/RlsParents(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CustNum + "," + ParentCustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CreditPoolHeads(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CreditPoolHeads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CreditPoolHeads
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditPoolHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads",headers=creds) as resp:
           return await resp.json()

async def post_CreditPoolHeads(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CreditPoolHeads
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CreditPoolHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CreditPoolHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CreditPoolHeads_Company_RlsClassCode_TopCustNum_CrdPoolCode(Company, RlsClassCode, TopCustNum, CrdPoolCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CreditPoolHead item
   Description: Calls GetByID to retrieve the CreditPoolHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditPoolHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CrdPoolCode: Desc: CrdPoolCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditPoolHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CreditPoolHeads_Company_RlsClassCode_TopCustNum_CrdPoolCode(Company, RlsClassCode, TopCustNum, CrdPoolCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CreditPoolHead for the service
   Description: Calls UpdateExt to update CreditPoolHead. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CreditPoolHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CrdPoolCode: Desc: CrdPoolCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CreditPoolHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CreditPoolHeads_Company_RlsClassCode_TopCustNum_CrdPoolCode(Company, RlsClassCode, TopCustNum, CrdPoolCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CreditPoolHead item
   Description: Call UpdateExt to delete CreditPoolHead item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CreditPoolHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CrdPoolCode: Desc: CrdPoolCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_CreditPoolHeads_Company_RlsClassCode_TopCustNum_CrdPoolCode_CreditPoolDtls(Company, RlsClassCode, TopCustNum, CrdPoolCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CreditPoolDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CreditPoolDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CrdPoolCode: Desc: CrdPoolCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditPoolDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + ")/CreditPoolDtls",headers=creds) as resp:
           return await resp.json()

async def get_CreditPoolHeads_Company_RlsClassCode_TopCustNum_CrdPoolCode_CreditPoolDtls_Company_RlsClassCode_TopCustNum_CrdPoolCode_ShareCustNum(Company, RlsClassCode, TopCustNum, CrdPoolCode, ShareCustNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CreditPoolDtl item
   Description: Calls GetByID to retrieve the CreditPoolDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditPoolDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CrdPoolCode: Desc: CrdPoolCode   Required: True   Allow empty value : True
      :param ShareCustNum: Desc: ShareCustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditPoolDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolHeads(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + ")/CreditPoolDtls(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + "," + ShareCustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CreditPoolDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CreditPoolDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CreditPoolDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditPoolDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolDtls",headers=creds) as resp:
           return await resp.json()

async def post_CreditPoolDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CreditPoolDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CreditPoolDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CreditPoolDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CreditPoolDtls_Company_RlsClassCode_TopCustNum_CrdPoolCode_ShareCustNum(Company, RlsClassCode, TopCustNum, CrdPoolCode, ShareCustNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CreditPoolDtl item
   Description: Calls GetByID to retrieve the CreditPoolDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditPoolDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CrdPoolCode: Desc: CrdPoolCode   Required: True   Allow empty value : True
      :param ShareCustNum: Desc: ShareCustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditPoolDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolDtls(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + "," + ShareCustNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CreditPoolDtls_Company_RlsClassCode_TopCustNum_CrdPoolCode_ShareCustNum(Company, RlsClassCode, TopCustNum, CrdPoolCode, ShareCustNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CreditPoolDtl for the service
   Description: Calls UpdateExt to update CreditPoolDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CreditPoolDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CrdPoolCode: Desc: CrdPoolCode   Required: True   Allow empty value : True
      :param ShareCustNum: Desc: ShareCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CreditPoolDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolDtls(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + "," + ShareCustNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CreditPoolDtls_Company_RlsClassCode_TopCustNum_CrdPoolCode_ShareCustNum(Company, RlsClassCode, TopCustNum, CrdPoolCode, ShareCustNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CreditPoolDtl item
   Description: Call UpdateExt to delete CreditPoolDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CreditPoolDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RlsClassCode: Desc: RlsClassCode   Required: True   Allow empty value : True
      :param TopCustNum: Desc: TopCustNum   Required: True
      :param CrdPoolCode: Desc: CrdPoolCode   Required: True   Allow empty value : True
      :param ShareCustNum: Desc: ShareCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/CreditPoolDtls(" + Company + "," + RlsClassCode + "," + TopCustNum + "," + CrdPoolCode + "," + ShareCustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RlsHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRlsHead, whereClauseRlsParent, whereClauseCreditPoolHead, whereClauseCreditPoolDtl, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRlsHead=" + whereClauseRlsHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRlsParent=" + whereClauseRlsParent
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCreditPoolHead=" + whereClauseCreditPoolHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCreditPoolDtl=" + whereClauseCreditPoolDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(rlsClassCode, topCustNum, custNum, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "rlsClassCode=" + rlsClassCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "topCustNum=" + topCustNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "custNum=" + custNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AddChildCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddChildCustomer
   Description: Add Child to the Customer for both tiered and non tiered classes
   OperationID: AddChildCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddChildCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddChildCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CustListPayFor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustListPayFor
   Description: Gets list CustNum of customers which can be payed by Customer ipPayerCustNum
   OperationID: CustListPayFor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustListPayFor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustListPayFor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNAData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNAData
   Description: Get National Accout dataset by RlsClass and any Customer from Relationship (TODO-rename parameters TopCust with Cust)
   OperationID: GetNAData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNAData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNAData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveChildCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveChildCustomer
   Description: MoveChildCustomer
   OperationID: MoveChildCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveChildCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveChildCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCustID
   Description: Check Cust Id, get Name, Num
   OperationID: OnChangeCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeGlobalNAGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeGlobalNAGroup
   Description: Check all customers if they are Global if the flag was set
   OperationID: OnChangeGlobalNAGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeGlobalNAGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeGlobalNAGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeParentCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeParentCustID
   Description: Check Parent Cust Id for non tiered Relationship
   OperationID: OnChangeParentCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeParentCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeParentCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRlsClassCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRlsClassCode
   Description: Check Rls Class Code
   OperationID: OnChangeRlsClassCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRlsClassCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRlsClassCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetGlobalCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetGlobalCustomer
   Description: Purpose: Set Glabal customer
   OperationID: SetGlobalCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetGlobalCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetGlobalCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetGlobalNACustomers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetGlobalNACustomers
   Description: Purpose: Set Global flag to all customers in National Account
   OperationID: SetGlobalNACustomers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetGlobalNACustomers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetGlobalNACustomers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRlsHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRlsHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRlsHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRlsHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRlsHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRlsParent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRlsParent
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRlsParent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRlsParent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRlsParent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCreditPoolHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCreditPoolHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCreditPoolHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCreditPoolHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCreditPoolHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCreditPoolDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCreditPoolDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCreditPoolDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCreditPoolDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCreditPoolDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NARelationshipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditPoolDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CreditPoolDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditPoolHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CreditPoolHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RlsHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RlsHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RlsParentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RlsParentRow] = obj["value"]
      pass

class Erp_Tablesets_CreditPoolDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RlsClassCode:str = obj["RlsClassCode"]
      """  Unique identifier for the Relationship Class  """  
      self.TopCustNum:int = obj["TopCustNum"]
      """  A  unique code of Customer on the Top  """  
      self.CrdPoolCode:str = obj["CrdPoolCode"]
      """  unique identifier for the credit pool  """  
      self.ShareCustNum:int = obj["ShareCustNum"]
      """  Customer from NA which has access to credit pool  """  
      self.PrcShare:int = obj["PrcShare"]
      """  The Maximum percentage of the credit pool amount that the customer could use  """  
      self.CreditUsed:int = obj["CreditUsed"]
      """  Credit used by this customer in base currency  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ShareCustomerName:str = obj["ShareCustomerName"]
      self.ShareCustomerBTName:str = obj["ShareCustomerBTName"]
      self.ShareCustomerCustID:str = obj["ShareCustomerCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CreditPoolHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RlsClassCode:str = obj["RlsClassCode"]
      """  Unique identifier for the Relationship Class  """  
      self.TopCustNum:int = obj["TopCustNum"]
      """  A  unique code of Customer on the Top  """  
      self.CrdPoolCode:str = obj["CrdPoolCode"]
      """  unique identifier for the credit pool  """  
      self.PoolAmount:int = obj["PoolAmount"]
      """  Credit amount that could be used by the customers with access to the credit pool - in base currency  """  
      self.AmtAvailable:int = obj["AmtAvailable"]
      """  Available Credit amount that could be used by the customers with access to the credit pool - in base currency  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RlsHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RlsClassCode:str = obj["RlsClassCode"]
      """  Unique identifier for the Relationship Class  """  
      self.TopCustNum:int = obj["TopCustNum"]
      """  A  unique code of Customer on the Top  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique code of the current Customer  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  Customer ID of the current customer (link)  """  
      self.RlsClassTiered:bool = obj["RlsClassTiered"]
      """  RlsClass is Tiered (link)  """  
      self.TopCustomerCustID:str = obj["TopCustomerCustID"]
      """  Cust Id of Top Customer (link)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RlsHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RlsClassCode:str = obj["RlsClassCode"]
      """  Unique identifier for the Relationship Class  """  
      self.TopCustNum:int = obj["TopCustNum"]
      """  A  unique code of Customer on the Top  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique code of the current Customer  """  
      self.UnTieredGroup:int = obj["UnTieredGroup"]
      """  key unique for whole UnTiered Group  """  
      self.TierLevelNum:int = obj["TierLevelNum"]
      """  Level number for tiered Relationship  """  
      self.GlobalNA:bool = obj["GlobalNA"]
      """  Determines whether or not National Account is shared between more than one company.  """  
      self.IsCreditUpdated:bool = obj["IsCreditUpdated"]
      """  shows if Credit Data or Credit Relationship has been updated, it is used for recalculation process  """  
      self.DocStartARTotal:int = obj["DocStartARTotal"]
      """  Starting AR Total when Customer was added to the National Account (in Customer Global Currency)  """  
      self.DocStartSOTotal:int = obj["DocStartSOTotal"]
      """  Starting SO Total when Customer was added to the National Account (in Customer Global Currency)  """  
      self.DocStartPITotal:int = obj["DocStartPITotal"]
      """  Starting PI Total when Customer was added to the National Account (in Customer Global Currency)  """  
      self.StartARTotal:int = obj["StartARTotal"]
      """  Starting AR Total when Customer was added to the National Account (in Base Currency)  """  
      self.StartSOTotal:int = obj["StartSOTotal"]
      """  Starting AR Total when Customer was added to the National Account (in Base Currency)  """  
      self.StartPITotal:int = obj["StartPITotal"]
      """  Starting AR Total when Customer was added to the National Account (in Base Currency)  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when System when customer was added to National Account  """  
      self.Seq:int = obj["Seq"]
      """  current number of the Sequence NACreditDocSeq when custromer was added to NA  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (CustNum) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.dspTierLabel:str = obj["dspTierLabel"]
      self.dspTierLevel:str = obj["dspTierLevel"]
      """  String level (for tiered Class), empty for non tiered  """  
      self.NewChildCustID:str = obj["NewChildCustID"]
      self.NewChildCustName:str = obj["NewChildCustName"]
      """  New Customer Name added as child for tiered relationship  """  
      self.NewCustID:str = obj["NewCustID"]
      """  New Customer ID added as child for tiered relationship or parent for non tiered relationship  """  
      self.NewCustName:str = obj["NewCustName"]
      """  New Customer Name added as parent for non tiered relationship  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  reference to Parent Customer Used for tiered Relationship  """  
      self.ParentCustID:str = obj["ParentCustID"]
      """  Parent Cust ID for tiered Class  """  
      self.TopCustomerIsGlobal:bool = obj["TopCustomerIsGlobal"]
      """  Top Customer is Global  """  
      self.GlobalNAGroup:bool = obj["GlobalNAGroup"]
      """  link to RlsGroup  """  
      self.IsCreditUpdatedGroup:bool = obj["IsCreditUpdatedGroup"]
      """  link to RlsGroup  """  
      self.SelectedCustID:str = obj["SelectedCustID"]
      """  Selected Customer ID - for tiered classes only  """  
      self.SelectedCustName:str = obj["SelectedCustName"]
      """  Selected Customer Name - for tiered classes only  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.RlsClassTiered:bool = obj["RlsClassTiered"]
      self.RlsClassDescription:str = obj["RlsClassDescription"]
      self.TopCustomerName:str = obj["TopCustomerName"]
      self.TopCustomerBTName:str = obj["TopCustomerBTName"]
      self.TopCustomerCustID:str = obj["TopCustomerCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RlsParentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RlsClassCode:str = obj["RlsClassCode"]
      """  Unique identifier for the Relationship Class  """  
      self.TopCustNum:int = obj["TopCustNum"]
      """  A  unique code of Customer on the Top  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique code of the current Customer  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  Code of the Parent for current Customer  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ParentCustomerName:str = obj["ParentCustomerName"]
      self.ParentCustomerCustID:str = obj["ParentCustomerCustID"]
      self.ParentCustomerBTName:str = obj["ParentCustomerBTName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddChildCustomer_input:
   """ Required : 
   ds
   ipRlsClassCode
   ipTopCustNum
   ipCustNum
   ipChildCustID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      self.ipRlsClassCode:str = obj["ipRlsClassCode"]
      """  RlsClass.RlsClassCode  """  
      self.ipTopCustNum:int = obj["ipTopCustNum"]
      """  Top Cust Num  """  
      self.ipCustNum:int = obj["ipCustNum"]
      """  Parent Cust Num  """  
      self.ipChildCustID:str = obj["ipChildCustID"]
      """  Child CustID  """  
      pass

class AddChildCustomer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CustListPayFor_input:
   """ Required : 
   ipPayerCustNum
   """  
   def __init__(self, obj):
      self.ipPayerCustNum:int = obj["ipPayerCustNum"]
      """  Payer Cust Num  """  
      pass

class CustListPayFor_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.listPayFor:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   rlsClassCode
   topCustNum
   custNum
   """  
   def __init__(self, obj):
      self.rlsClassCode:str = obj["rlsClassCode"]
      self.topCustNum:int = obj["topCustNum"]
      self.custNum:int = obj["custNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CreditPoolDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RlsClassCode:str = obj["RlsClassCode"]
      """  Unique identifier for the Relationship Class  """  
      self.TopCustNum:int = obj["TopCustNum"]
      """  A  unique code of Customer on the Top  """  
      self.CrdPoolCode:str = obj["CrdPoolCode"]
      """  unique identifier for the credit pool  """  
      self.ShareCustNum:int = obj["ShareCustNum"]
      """  Customer from NA which has access to credit pool  """  
      self.PrcShare:int = obj["PrcShare"]
      """  The Maximum percentage of the credit pool amount that the customer could use  """  
      self.CreditUsed:int = obj["CreditUsed"]
      """  Credit used by this customer in base currency  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ShareCustomerName:str = obj["ShareCustomerName"]
      self.ShareCustomerBTName:str = obj["ShareCustomerBTName"]
      self.ShareCustomerCustID:str = obj["ShareCustomerCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CreditPoolHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RlsClassCode:str = obj["RlsClassCode"]
      """  Unique identifier for the Relationship Class  """  
      self.TopCustNum:int = obj["TopCustNum"]
      """  A  unique code of Customer on the Top  """  
      self.CrdPoolCode:str = obj["CrdPoolCode"]
      """  unique identifier for the credit pool  """  
      self.PoolAmount:int = obj["PoolAmount"]
      """  Credit amount that could be used by the customers with access to the credit pool - in base currency  """  
      self.AmtAvailable:int = obj["AmtAvailable"]
      """  Available Credit amount that could be used by the customers with access to the credit pool - in base currency  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NARelationshipListTableset:
   def __init__(self, obj):
      self.RlsHeadList:list[Erp_Tablesets_RlsHeadListRow] = obj["RlsHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_NARelationshipTableset:
   def __init__(self, obj):
      self.RlsHead:list[Erp_Tablesets_RlsHeadRow] = obj["RlsHead"]
      self.RlsParent:list[Erp_Tablesets_RlsParentRow] = obj["RlsParent"]
      self.CreditPoolHead:list[Erp_Tablesets_CreditPoolHeadRow] = obj["CreditPoolHead"]
      self.CreditPoolDtl:list[Erp_Tablesets_CreditPoolDtlRow] = obj["CreditPoolDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RlsHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RlsClassCode:str = obj["RlsClassCode"]
      """  Unique identifier for the Relationship Class  """  
      self.TopCustNum:int = obj["TopCustNum"]
      """  A  unique code of Customer on the Top  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique code of the current Customer  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  Customer ID of the current customer (link)  """  
      self.RlsClassTiered:bool = obj["RlsClassTiered"]
      """  RlsClass is Tiered (link)  """  
      self.TopCustomerCustID:str = obj["TopCustomerCustID"]
      """  Cust Id of Top Customer (link)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RlsHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RlsClassCode:str = obj["RlsClassCode"]
      """  Unique identifier for the Relationship Class  """  
      self.TopCustNum:int = obj["TopCustNum"]
      """  A  unique code of Customer on the Top  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique code of the current Customer  """  
      self.UnTieredGroup:int = obj["UnTieredGroup"]
      """  key unique for whole UnTiered Group  """  
      self.TierLevelNum:int = obj["TierLevelNum"]
      """  Level number for tiered Relationship  """  
      self.GlobalNA:bool = obj["GlobalNA"]
      """  Determines whether or not National Account is shared between more than one company.  """  
      self.IsCreditUpdated:bool = obj["IsCreditUpdated"]
      """  shows if Credit Data or Credit Relationship has been updated, it is used for recalculation process  """  
      self.DocStartARTotal:int = obj["DocStartARTotal"]
      """  Starting AR Total when Customer was added to the National Account (in Customer Global Currency)  """  
      self.DocStartSOTotal:int = obj["DocStartSOTotal"]
      """  Starting SO Total when Customer was added to the National Account (in Customer Global Currency)  """  
      self.DocStartPITotal:int = obj["DocStartPITotal"]
      """  Starting PI Total when Customer was added to the National Account (in Customer Global Currency)  """  
      self.StartARTotal:int = obj["StartARTotal"]
      """  Starting AR Total when Customer was added to the National Account (in Base Currency)  """  
      self.StartSOTotal:int = obj["StartSOTotal"]
      """  Starting AR Total when Customer was added to the National Account (in Base Currency)  """  
      self.StartPITotal:int = obj["StartPITotal"]
      """  Starting AR Total when Customer was added to the National Account (in Base Currency)  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when System when customer was added to National Account  """  
      self.Seq:int = obj["Seq"]
      """  current number of the Sequence NACreditDocSeq when custromer was added to NA  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (CustNum) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.dspTierLabel:str = obj["dspTierLabel"]
      self.dspTierLevel:str = obj["dspTierLevel"]
      """  String level (for tiered Class), empty for non tiered  """  
      self.NewChildCustID:str = obj["NewChildCustID"]
      self.NewChildCustName:str = obj["NewChildCustName"]
      """  New Customer Name added as child for tiered relationship  """  
      self.NewCustID:str = obj["NewCustID"]
      """  New Customer ID added as child for tiered relationship or parent for non tiered relationship  """  
      self.NewCustName:str = obj["NewCustName"]
      """  New Customer Name added as parent for non tiered relationship  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  reference to Parent Customer Used for tiered Relationship  """  
      self.ParentCustID:str = obj["ParentCustID"]
      """  Parent Cust ID for tiered Class  """  
      self.TopCustomerIsGlobal:bool = obj["TopCustomerIsGlobal"]
      """  Top Customer is Global  """  
      self.GlobalNAGroup:bool = obj["GlobalNAGroup"]
      """  link to RlsGroup  """  
      self.IsCreditUpdatedGroup:bool = obj["IsCreditUpdatedGroup"]
      """  link to RlsGroup  """  
      self.SelectedCustID:str = obj["SelectedCustID"]
      """  Selected Customer ID - for tiered classes only  """  
      self.SelectedCustName:str = obj["SelectedCustName"]
      """  Selected Customer Name - for tiered classes only  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.RlsClassTiered:bool = obj["RlsClassTiered"]
      self.RlsClassDescription:str = obj["RlsClassDescription"]
      self.TopCustomerName:str = obj["TopCustomerName"]
      self.TopCustomerBTName:str = obj["TopCustomerBTName"]
      self.TopCustomerCustID:str = obj["TopCustomerCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RlsParentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RlsClassCode:str = obj["RlsClassCode"]
      """  Unique identifier for the Relationship Class  """  
      self.TopCustNum:int = obj["TopCustNum"]
      """  A  unique code of Customer on the Top  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique code of the current Customer  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  Code of the Parent for current Customer  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ParentCustomerName:str = obj["ParentCustomerName"]
      self.ParentCustomerCustID:str = obj["ParentCustomerCustID"]
      self.ParentCustomerBTName:str = obj["ParentCustomerBTName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtNARelationshipTableset:
   def __init__(self, obj):
      self.RlsHead:list[Erp_Tablesets_RlsHeadRow] = obj["RlsHead"]
      self.RlsParent:list[Erp_Tablesets_RlsParentRow] = obj["RlsParent"]
      self.CreditPoolHead:list[Erp_Tablesets_CreditPoolHeadRow] = obj["CreditPoolHead"]
      self.CreditPoolDtl:list[Erp_Tablesets_CreditPoolDtlRow] = obj["CreditPoolDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   rlsClassCode
   topCustNum
   custNum
   """  
   def __init__(self, obj):
      self.rlsClassCode:str = obj["rlsClassCode"]
      self.topCustNum:int = obj["topCustNum"]
      self.custNum:int = obj["custNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NARelationshipTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NARelationshipTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NARelationshipTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NARelationshipListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNAData_input:
   """ Required : 
   ipRlsClassCode
   ipTopCustID
   ipNewNA
   """  
   def __init__(self, obj):
      self.ipRlsClassCode:str = obj["ipRlsClassCode"]
      """  RlsClass.RlsClassCode  """  
      self.ipTopCustID:str = obj["ipTopCustID"]
      """  Customer CustID  """  
      self.ipNewNA:bool = obj["ipNewNA"]
      """  Is it a new record  """  
      pass

class GetNAData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NARelationshipTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pTopCustNum:int = obj["parameters"]
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewCreditPoolDtl_input:
   """ Required : 
   ds
   rlsClassCode
   topCustNum
   crdPoolCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      self.rlsClassCode:str = obj["rlsClassCode"]
      self.topCustNum:int = obj["topCustNum"]
      self.crdPoolCode:str = obj["crdPoolCode"]
      pass

class GetNewCreditPoolDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCreditPoolHead_input:
   """ Required : 
   ds
   rlsClassCode
   topCustNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      self.rlsClassCode:str = obj["rlsClassCode"]
      self.topCustNum:int = obj["topCustNum"]
      pass

class GetNewCreditPoolHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRlsHead_input:
   """ Required : 
   ds
   rlsClassCode
   topCustNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      self.rlsClassCode:str = obj["rlsClassCode"]
      self.topCustNum:int = obj["topCustNum"]
      pass

class GetNewRlsHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRlsParent_input:
   """ Required : 
   ds
   rlsClassCode
   topCustNum
   custNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      self.rlsClassCode:str = obj["rlsClassCode"]
      self.topCustNum:int = obj["topCustNum"]
      self.custNum:int = obj["custNum"]
      pass

class GetNewRlsParent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRlsHead
   whereClauseRlsParent
   whereClauseCreditPoolHead
   whereClauseCreditPoolDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRlsHead:str = obj["whereClauseRlsHead"]
      self.whereClauseRlsParent:str = obj["whereClauseRlsParent"]
      self.whereClauseCreditPoolHead:str = obj["whereClauseCreditPoolHead"]
      self.whereClauseCreditPoolDtl:str = obj["whereClauseCreditPoolDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NARelationshipTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class MoveChildCustomer_input:
   """ Required : 
   ds
   ipRlsClassCode
   ipTopCustNum
   ipCustNum
   ipTargetCustNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      self.ipRlsClassCode:str = obj["ipRlsClassCode"]
      """  RlsClass.RlsClassCode  """  
      self.ipTopCustNum:int = obj["ipTopCustNum"]
      """  Customer CustID  """  
      self.ipCustNum:int = obj["ipCustNum"]
      """  Customer CustID  """  
      self.ipTargetCustNum:int = obj["ipTargetCustNum"]
      """  Customer CustID  """  
      pass

class MoveChildCustomer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeCustID_input:
   """ Required : 
   ipCustID
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      """  Customer ID  """  
      pass

class OnChangeCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pCustName:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeGlobalNAGroup_input:
   """ Required : 
   ds
   ipRlsGlobal
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      self.ipRlsGlobal:bool = obj["ipRlsGlobal"]
      """  Global flag  """  
      pass

class OnChangeGlobalNAGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isSetGlobal:bool = obj["isSetGlobal"]
      pass

      """  output parameters  """  

class OnChangeParentCustID_input:
   """ Required : 
   ds
   ipParentCustID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      self.ipParentCustID:str = obj["ipParentCustID"]
      """  Parent CustID  """  
      pass

class OnChangeParentCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRlsClassCode_input:
   """ Required : 
   ipRlsClassCode
   """  
   def __init__(self, obj):
      self.ipRlsClassCode:str = obj["ipRlsClassCode"]
      """  Relationship Class Code  """  
      pass

class OnChangeRlsClassCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetGlobalCustomer_input:
   """ Required : 
   ipCustID
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      pass

class SetGlobalCustomer_output:
   def __init__(self, obj):
      pass

class SetGlobalNACustomers_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      pass

class SetGlobalNACustomers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtNARelationshipTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtNARelationshipTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NARelationshipTableset] = obj["ds"]
      pass

      """  output parameters  """  

