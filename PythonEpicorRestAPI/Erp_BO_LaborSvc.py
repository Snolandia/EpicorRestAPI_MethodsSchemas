import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LaborSvc
# Description: Labor Entry Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Labors(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Labors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Labors
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors",headers=creds) as resp:
           return await resp.json()

async def post_Labors(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Labors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Labors_Company_LaborHedSeq(Company, LaborHedSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Labor item
   Description: Calls GetByID to retrieve the Labor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Labor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors(" + Company + "," + LaborHedSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Labors_Company_LaborHedSeq(Company, LaborHedSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Labor for the service
   Description: Calls UpdateExt to update Labor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Labor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors(" + Company + "," + LaborHedSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Labors_Company_LaborHedSeq(Company, LaborHedSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Labor item
   Description: Call UpdateExt to delete Labor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Labor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors(" + Company + "," + LaborHedSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_Labors_Company_LaborHedSeq_LaborDtls(Company, LaborHedSeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaborDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors(" + Company + "," + LaborHedSeq + ")/LaborDtls",headers=creds) as resp:
           return await resp.json()

async def get_Labors_Company_LaborHedSeq_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtl item
   Description: Calls GetByID to retrieve the LaborDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/Labors(" + Company + "," + LaborHedSeq + ")/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls",headers=creds) as resp:
           return await resp.json()

async def post_LaborDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtl item
   Description: Calls GetByID to retrieve the LaborDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborDtl for the service
   Description: Calls UpdateExt to update LaborDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborDtl item
   Description: Call UpdateExt to delete LaborDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborDtlActions(Company, LaborHedSeq, LaborDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaborDtlActions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborDtlActions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlActions",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborDtlActions_Company_LaborHedSeq_LaborDtlSeq_ActionSeq(Company, LaborHedSeq, LaborDtlSeq, ActionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtlAction item
   Description: Calls GetByID to retrieve the LaborDtlAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlAction1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlActions(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + ActionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborDtlComments(Company, LaborHedSeq, LaborDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaborDtlComments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborDtlComments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlComments",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company, LaborHedSeq, LaborDtlSeq, CommentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtlComment item
   Description: Calls GetByID to retrieve the LaborDtlComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlComment1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborEquips(Company, LaborHedSeq, LaborDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaborEquips items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborEquips1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborEquipRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborEquips",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborEquips_Company_LaborHedSeq_LaborDtlSeq_EquipID(Company, LaborHedSeq, LaborDtlSeq, EquipID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborEquip item
   Description: Calls GetByID to retrieve the LaborEquip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborEquip1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborEquipRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborEquips(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborParts(Company, LaborHedSeq, LaborDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaborParts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborParts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborParts",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborParts_Company_LaborHedSeq_LaborDtlSeq_PartNum(Company, LaborHedSeq, LaborDtlSeq, PartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborPart item
   Description: Calls GetByID to retrieve the LaborPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborPart1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborParts(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LbrScrapSerialNumbers(Company, LaborHedSeq, LaborDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LbrScrapSerialNumbers items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LbrScrapSerialNumbers1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LbrScrapSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LbrScrapSerialNumbers",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LbrScrapSerialNumbers_Company_LaborHedSeq_LaborDtlSeq_SerialNumber_AssemblySeq_OprSeq(Company, LaborHedSeq, LaborDtlSeq, SerialNumber, AssemblySeq, OprSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LbrScrapSerialNumber item
   Description: Calls GetByID to retrieve the LbrScrapSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LbrScrapSerialNumber1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LbrScrapSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LbrScrapSerialNumbers(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + SerialNumber + "," + AssemblySeq + "," + OprSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborDtlAttches(Company, LaborHedSeq, LaborDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaborDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborDtlAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlAttches",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq_LaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company, LaborHedSeq, LaborDtlSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtlAttch item
   Description: Calls GetByID to retrieve the LaborDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlActions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborDtlActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtlActions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlActions",headers=creds) as resp:
           return await resp.json()

async def post_LaborDtlActions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtlActions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlActionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborDtlActionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlActions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlActions_Company_LaborHedSeq_LaborDtlSeq_ActionSeq(Company, LaborHedSeq, LaborDtlSeq, ActionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtlAction item
   Description: Calls GetByID to retrieve the LaborDtlAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlActions(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + ActionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborDtlActions_Company_LaborHedSeq_LaborDtlSeq_ActionSeq(Company, LaborHedSeq, LaborDtlSeq, ActionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborDtlAction for the service
   Description: Calls UpdateExt to update LaborDtlAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtlAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlActionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlActions(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + ActionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborDtlActions_Company_LaborHedSeq_LaborDtlSeq_ActionSeq(Company, LaborHedSeq, LaborDtlSeq, ActionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborDtlAction item
   Description: Call UpdateExt to delete LaborDtlAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtlAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlActions(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + ActionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlComments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborDtlComments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtlComments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlComments",headers=creds) as resp:
           return await resp.json()

async def post_LaborDtlComments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtlComments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlCommentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborDtlCommentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlComments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company, LaborHedSeq, LaborDtlSeq, CommentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtlComment item
   Description: Calls GetByID to retrieve the LaborDtlComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company, LaborHedSeq, LaborDtlSeq, CommentNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborDtlComment for the service
   Description: Calls UpdateExt to update LaborDtlComment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtlComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlCommentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company, LaborHedSeq, LaborDtlSeq, CommentNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborDtlComment item
   Description: Call UpdateExt to delete LaborDtlComment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtlComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborEquips(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborEquips items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborEquips
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborEquipRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborEquips",headers=creds) as resp:
           return await resp.json()

async def post_LaborEquips(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborEquips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborEquipRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborEquipRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborEquips", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborEquips_Company_LaborHedSeq_LaborDtlSeq_EquipID(Company, LaborHedSeq, LaborDtlSeq, EquipID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborEquip item
   Description: Calls GetByID to retrieve the LaborEquip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborEquip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborEquipRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborEquips(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborEquips_Company_LaborHedSeq_LaborDtlSeq_EquipID(Company, LaborHedSeq, LaborDtlSeq, EquipID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborEquip for the service
   Description: Calls UpdateExt to update LaborEquip. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborEquip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborEquipRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborEquips(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborEquips_Company_LaborHedSeq_LaborDtlSeq_EquipID(Company, LaborHedSeq, LaborDtlSeq, EquipID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborEquip item
   Description: Call UpdateExt to delete LaborEquip item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborEquip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborEquips(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborParts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborParts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborParts",headers=creds) as resp:
           return await resp.json()

async def post_LaborParts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborParts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborParts_Company_LaborHedSeq_LaborDtlSeq_PartNum(Company, LaborHedSeq, LaborDtlSeq, PartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborPart item
   Description: Calls GetByID to retrieve the LaborPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborParts(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborParts_Company_LaborHedSeq_LaborDtlSeq_PartNum(Company, LaborHedSeq, LaborDtlSeq, PartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborPart for the service
   Description: Calls UpdateExt to update LaborPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborParts(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborParts_Company_LaborHedSeq_LaborDtlSeq_PartNum(Company, LaborHedSeq, LaborDtlSeq, PartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborPart item
   Description: Call UpdateExt to delete LaborPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborParts(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_LbrScrapSerialNumbers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LbrScrapSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LbrScrapSerialNumbers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LbrScrapSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LbrScrapSerialNumbers",headers=creds) as resp:
           return await resp.json()

async def post_LbrScrapSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LbrScrapSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LbrScrapSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LbrScrapSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LbrScrapSerialNumbers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LbrScrapSerialNumbers_Company_LaborHedSeq_LaborDtlSeq_SerialNumber_AssemblySeq_OprSeq(Company, LaborHedSeq, LaborDtlSeq, SerialNumber, AssemblySeq, OprSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LbrScrapSerialNumber item
   Description: Calls GetByID to retrieve the LbrScrapSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LbrScrapSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LbrScrapSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LbrScrapSerialNumbers(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + SerialNumber + "," + AssemblySeq + "," + OprSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LbrScrapSerialNumbers_Company_LaborHedSeq_LaborDtlSeq_SerialNumber_AssemblySeq_OprSeq(Company, LaborHedSeq, LaborDtlSeq, SerialNumber, AssemblySeq, OprSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LbrScrapSerialNumber for the service
   Description: Calls UpdateExt to update LbrScrapSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LbrScrapSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LbrScrapSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LbrScrapSerialNumbers(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + SerialNumber + "," + AssemblySeq + "," + OprSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LbrScrapSerialNumbers_Company_LaborHedSeq_LaborDtlSeq_SerialNumber_AssemblySeq_OprSeq(Company, LaborHedSeq, LaborDtlSeq, SerialNumber, AssemblySeq, OprSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LbrScrapSerialNumber item
   Description: Call UpdateExt to delete LbrScrapSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LbrScrapSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LbrScrapSerialNumbers(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + SerialNumber + "," + AssemblySeq + "," + OprSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlAttches",headers=creds) as resp:
           return await resp.json()

async def post_LaborDtlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company, LaborHedSeq, LaborDtlSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtlAttch item
   Description: Calls GetByID to retrieve the LaborDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company, LaborHedSeq, LaborDtlSeq, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborDtlAttch for the service
   Description: Calls UpdateExt to update LaborDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company, LaborHedSeq, LaborDtlSeq, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborDtlAttch item
   Description: Call UpdateExt to delete LaborDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlGroups(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborDtlGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtlGroups
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlGroups",headers=creds) as resp:
           return await resp.json()

async def post_LaborDtlGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtlGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborDtlGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlGroups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlGroups_Company_EmployeeNum_ClaimRef(Company, EmployeeNum, ClaimRef, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtlGroup item
   Description: Calls GetByID to retrieve the LaborDtlGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmployeeNum: Desc: EmployeeNum   Required: True   Allow empty value : True
      :param ClaimRef: Desc: ClaimRef   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlGroups(" + Company + "," + EmployeeNum + "," + ClaimRef + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborDtlGroups_Company_EmployeeNum_ClaimRef(Company, EmployeeNum, ClaimRef, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborDtlGroup for the service
   Description: Calls UpdateExt to update LaborDtlGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtlGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmployeeNum: Desc: EmployeeNum   Required: True   Allow empty value : True
      :param ClaimRef: Desc: ClaimRef   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlGroups(" + Company + "," + EmployeeNum + "," + ClaimRef + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborDtlGroups_Company_EmployeeNum_ClaimRef(Company, EmployeeNum, ClaimRef, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborDtlGroup item
   Description: Call UpdateExt to delete LaborDtlGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtlGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmployeeNum: Desc: EmployeeNum   Required: True   Allow empty value : True
      :param ClaimRef: Desc: ClaimRef   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/LaborDtlGroups(" + Company + "," + EmployeeNum + "," + ClaimRef + ")",headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SelectedSerialNumbers",headers=creds) as resp:
           return await resp.json()

async def post_SelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_SNFormats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SNFormats",headers=creds) as resp:
           return await resp.json()

async def post_SNFormats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SNFormats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_TimeWeeklyViews(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TimeWeeklyViews items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TimeWeeklyViews
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TimeWeeklyViewRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWeeklyViews",headers=creds) as resp:
           return await resp.json()

async def post_TimeWeeklyViews(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TimeWeeklyViews
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TimeWeeklyViewRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TimeWeeklyViewRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWeeklyViews", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TimeWeeklyViews_Company_EmployeeNum_WeekBeginDate_WeekEndDate_LaborTypePseudo_ProjectID_PhaseID_TimeTypCd_JobNum_AssemblySeq_OprSeq_IndirectCode_RoleCd_ResourceGrpID_ResourceID_ExpenseCode_NewRowType_QuickEntryCode_TimeStatus_Shift(Company, EmployeeNum, WeekBeginDate, WeekEndDate, LaborTypePseudo, ProjectID, PhaseID, TimeTypCd, JobNum, AssemblySeq, OprSeq, IndirectCode, RoleCd, ResourceGrpID, ResourceID, ExpenseCode, NewRowType, QuickEntryCode, TimeStatus, Shift, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TimeWeeklyView item
   Description: Calls GetByID to retrieve the TimeWeeklyView item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TimeWeeklyView
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmployeeNum: Desc: EmployeeNum   Required: True   Allow empty value : True
      :param WeekBeginDate: Desc: WeekBeginDate   Required: True   Allow empty value : True
      :param WeekEndDate: Desc: WeekEndDate   Required: True   Allow empty value : True
      :param LaborTypePseudo: Desc: LaborTypePseudo   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param PhaseID: Desc: PhaseID   Required: True   Allow empty value : True
      :param TimeTypCd: Desc: TimeTypCd   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param IndirectCode: Desc: IndirectCode   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
      :param NewRowType: Desc: NewRowType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param TimeStatus: Desc: TimeStatus   Required: True   Allow empty value : True
      :param Shift: Desc: Shift   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TimeWeeklyViewRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWeeklyViews(" + Company + "," + EmployeeNum + "," + WeekBeginDate + "," + WeekEndDate + "," + LaborTypePseudo + "," + ProjectID + "," + PhaseID + "," + TimeTypCd + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + IndirectCode + "," + RoleCd + "," + ResourceGrpID + "," + ResourceID + "," + ExpenseCode + "," + NewRowType + "," + QuickEntryCode + "," + TimeStatus + "," + Shift + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TimeWeeklyViews_Company_EmployeeNum_WeekBeginDate_WeekEndDate_LaborTypePseudo_ProjectID_PhaseID_TimeTypCd_JobNum_AssemblySeq_OprSeq_IndirectCode_RoleCd_ResourceGrpID_ResourceID_ExpenseCode_NewRowType_QuickEntryCode_TimeStatus_Shift(Company, EmployeeNum, WeekBeginDate, WeekEndDate, LaborTypePseudo, ProjectID, PhaseID, TimeTypCd, JobNum, AssemblySeq, OprSeq, IndirectCode, RoleCd, ResourceGrpID, ResourceID, ExpenseCode, NewRowType, QuickEntryCode, TimeStatus, Shift, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TimeWeeklyView for the service
   Description: Calls UpdateExt to update TimeWeeklyView. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TimeWeeklyView
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmployeeNum: Desc: EmployeeNum   Required: True   Allow empty value : True
      :param WeekBeginDate: Desc: WeekBeginDate   Required: True   Allow empty value : True
      :param WeekEndDate: Desc: WeekEndDate   Required: True   Allow empty value : True
      :param LaborTypePseudo: Desc: LaborTypePseudo   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param PhaseID: Desc: PhaseID   Required: True   Allow empty value : True
      :param TimeTypCd: Desc: TimeTypCd   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param IndirectCode: Desc: IndirectCode   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
      :param NewRowType: Desc: NewRowType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param TimeStatus: Desc: TimeStatus   Required: True   Allow empty value : True
      :param Shift: Desc: Shift   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TimeWeeklyViewRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWeeklyViews(" + Company + "," + EmployeeNum + "," + WeekBeginDate + "," + WeekEndDate + "," + LaborTypePseudo + "," + ProjectID + "," + PhaseID + "," + TimeTypCd + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + IndirectCode + "," + RoleCd + "," + ResourceGrpID + "," + ResourceID + "," + ExpenseCode + "," + NewRowType + "," + QuickEntryCode + "," + TimeStatus + "," + Shift + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TimeWeeklyViews_Company_EmployeeNum_WeekBeginDate_WeekEndDate_LaborTypePseudo_ProjectID_PhaseID_TimeTypCd_JobNum_AssemblySeq_OprSeq_IndirectCode_RoleCd_ResourceGrpID_ResourceID_ExpenseCode_NewRowType_QuickEntryCode_TimeStatus_Shift(Company, EmployeeNum, WeekBeginDate, WeekEndDate, LaborTypePseudo, ProjectID, PhaseID, TimeTypCd, JobNum, AssemblySeq, OprSeq, IndirectCode, RoleCd, ResourceGrpID, ResourceID, ExpenseCode, NewRowType, QuickEntryCode, TimeStatus, Shift, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TimeWeeklyView item
   Description: Call UpdateExt to delete TimeWeeklyView item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TimeWeeklyView
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmployeeNum: Desc: EmployeeNum   Required: True   Allow empty value : True
      :param WeekBeginDate: Desc: WeekBeginDate   Required: True   Allow empty value : True
      :param WeekEndDate: Desc: WeekEndDate   Required: True   Allow empty value : True
      :param LaborTypePseudo: Desc: LaborTypePseudo   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param PhaseID: Desc: PhaseID   Required: True   Allow empty value : True
      :param TimeTypCd: Desc: TimeTypCd   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param IndirectCode: Desc: IndirectCode   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
      :param NewRowType: Desc: NewRowType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param TimeStatus: Desc: TimeStatus   Required: True   Allow empty value : True
      :param Shift: Desc: Shift   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWeeklyViews(" + Company + "," + EmployeeNum + "," + WeekBeginDate + "," + WeekEndDate + "," + LaborTypePseudo + "," + ProjectID + "," + PhaseID + "," + TimeTypCd + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + IndirectCode + "," + RoleCd + "," + ResourceGrpID + "," + ResourceID + "," + ExpenseCode + "," + NewRowType + "," + QuickEntryCode + "," + TimeStatus + "," + Shift + ")",headers=creds) as resp:
           return await resp.json()

async def get_TimeWorkHours(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TimeWorkHours items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TimeWorkHours
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TimeWorkHoursRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWorkHours",headers=creds) as resp:
           return await resp.json()

async def post_TimeWorkHours(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TimeWorkHours
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TimeWorkHoursRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TimeWorkHoursRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWorkHours", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TimeWorkHours_Company_EmployeeNum_WeekBeginDate_WeekEndDate(Company, EmployeeNum, WeekBeginDate, WeekEndDate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TimeWorkHour item
   Description: Calls GetByID to retrieve the TimeWorkHour item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TimeWorkHour
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmployeeNum: Desc: EmployeeNum   Required: True   Allow empty value : True
      :param WeekBeginDate: Desc: WeekBeginDate   Required: True   Allow empty value : True
      :param WeekEndDate: Desc: WeekEndDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TimeWorkHoursRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWorkHours(" + Company + "," + EmployeeNum + "," + WeekBeginDate + "," + WeekEndDate + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TimeWorkHours_Company_EmployeeNum_WeekBeginDate_WeekEndDate(Company, EmployeeNum, WeekBeginDate, WeekEndDate, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TimeWorkHour for the service
   Description: Calls UpdateExt to update TimeWorkHour. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TimeWorkHour
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmployeeNum: Desc: EmployeeNum   Required: True   Allow empty value : True
      :param WeekBeginDate: Desc: WeekBeginDate   Required: True   Allow empty value : True
      :param WeekEndDate: Desc: WeekEndDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TimeWorkHoursRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWorkHours(" + Company + "," + EmployeeNum + "," + WeekBeginDate + "," + WeekEndDate + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TimeWorkHours_Company_EmployeeNum_WeekBeginDate_WeekEndDate(Company, EmployeeNum, WeekBeginDate, WeekEndDate, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TimeWorkHour item
   Description: Call UpdateExt to delete TimeWorkHour item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TimeWorkHour
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmployeeNum: Desc: EmployeeNum   Required: True   Allow empty value : True
      :param WeekBeginDate: Desc: WeekBeginDate   Required: True   Allow empty value : True
      :param WeekEndDate: Desc: WeekEndDate   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/TimeWorkHours(" + Company + "," + EmployeeNum + "," + WeekBeginDate + "," + WeekEndDate + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseLaborHed, whereClauseLaborDtl, whereClauseLaborDtlAttch, whereClauseLaborDtlAction, whereClauseLaborDtlComment, whereClauseLaborEquip, whereClauseLaborPart, whereClauseLbrScrapSerialNumbers, whereClauseLaborDtlGroup, whereClauseSelectedSerialNumbers, whereClauseSNFormat, whereClauseTimeWeeklyView, whereClauseTimeWorkHours, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborHed=" + whereClauseLaborHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborDtl=" + whereClauseLaborDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborDtlAttch=" + whereClauseLaborDtlAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborDtlAction=" + whereClauseLaborDtlAction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborDtlComment=" + whereClauseLaborDtlComment
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborEquip=" + whereClauseLaborEquip
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborPart=" + whereClauseLaborPart
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLbrScrapSerialNumbers=" + whereClauseLbrScrapSerialNumbers
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborDtlGroup=" + whereClauseLaborDtlGroup
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSNFormat=" + whereClauseSNFormat
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTimeWeeklyView=" + whereClauseTimeWeeklyView
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTimeWorkHours=" + whereClauseTimeWorkHours
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(laborHedSeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "laborHedSeq=" + laborHedSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_LaborHedPayrollDateChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LaborHedPayrollDateChanging
   Description: Called when LaborHed Payroll Date is changing
   OperationID: LaborHedPayrollDateChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LaborHedPayrollDateChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LaborHedPayrollDateChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultsAddLaborDtlFromCalendar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultsAddLaborDtlFromCalendar
   OperationID: GetDefaultsAddLaborDtlFromCalendar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultsAddLaborDtlFromCalendar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultsAddLaborDtlFromCalendar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLaborPartScrapQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLaborPartScrapQty
   Description: This method sets Complete checkbox when scrap qty field changes in End Activity.
   OperationID: OnChangeLaborPartScrapQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLaborPartScrapQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLaborPartScrapQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLaborPartAttributeSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLaborPartAttributeSetID
   Description: This method updates the revision field when the attribute ID field changes.
   OperationID: ChangeLaborPartAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborPartAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborPartAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AfterChangeLaborPartDiscrepQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AfterChangeLaborPartDiscrepQty
   Description: Called after LaborDtl.DiscrepQty has been changed.
   OperationID: AfterChangeLaborPartDiscrepQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AfterChangeLaborPartDiscrepQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterChangeLaborPartDiscrepQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborDtlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborDtlAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborDtlAction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtlAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborDtlComment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborDtlComment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtlComment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborEquip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborEquip
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborEquip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborEquip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborEquip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborDtlGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborDtlGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtlGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildJobOperPrjRoleList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildJobOperPrjRoleList
   Description: This proc will return the whereclause for the role code combo
Customers
   OperationID: BuildJobOperPrjRoleList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildJobOperPrjRoleList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildJobOperPrjRoleList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEquipID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEquipID
   Description: This method should call when EquipID is changed
   OperationID: ChangeEquipID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEquipID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEquipID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeIndirectCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeIndirectCode
   Description: This method clears the JobNumber and Quantity fields when the LaborType changes to Indirect
leaves the values as is if changed between Production and Setup
   OperationID: ChangeIndirectCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeIndirectCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeIndirectCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLaborType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLaborType
   Description: This method clears the JobNumber and Quantity fields when the LaborType changes to Indirect
leaves the values as is if changed between Production and Setup
   OperationID: ChangeLaborType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckResourceId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckResourceId
   Description: Main logic from ChangeResourceId to validate the resource id assigned to a Job.
This method does not depend on a tableset or LaborDtl record.
   OperationID: CheckResourceId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckResourceId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckResourceId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeResourceId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeResourceId
   Description: For use with MES (ShopFloor) only.
This method checks the Resource Group of the proposed Resource, and if it
is different than the current Resource Group, provides a warning question
suitable for presenting to the user.
The UI code should place the user's answer to the question in the
ttLaborDtl.OkToChangeResourceGrpID.
This method should be called prior to calling the DefaultResourceID method.
   OperationID: ChangeResourceId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeResourceId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResourceId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckEmployeeActivity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckEmployeeActivity
   Description: This method checks if the current employee is already working on a Job/Asm/Opr/Resource combination
If he/she is already working on it, the opMessage will be populated with an error message
   OperationID: CheckEmployeeActivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckEmployeeActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEmployeeActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckNonConformance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckNonConformance
   Description: Check if there are NonConformance records, if they exists it will ask the user for his approval to delete them
   OperationID: CheckNonConformance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckNonConformance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckNonConformance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckFirstArticleWarning(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckFirstArticleWarning
   Description: Performs all First Article Validations
   OperationID: CheckFirstArticleWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckFirstArticleWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFirstArticleWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckInspResults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckInspResults
   Description: This method validates if InspResults has been entered when the Inspection Data is allowed for the current OprSeq.
   OperationID: CheckInspResults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckInspResults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckInspResults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckResourceGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckResourceGroup
   Description: This method checks to see if the new resource is in the current resource group.
This needs to be run right before the DefaultResourceID.  If the user answers
okay then the group will be changed in the DefaultResourceID method.
   OperationID: CheckResourceGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckResourceGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckResourceGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckWarnings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckWarnings
   Description: This method runs the labor warning routine and returns any warnings the user needs
to be aware of.  This needs to be run right before the update method.  If the user answers
okay to all of the questions, then the update method can be run.  Otherwise the labor record
needs to be corrected
   OperationID: CheckWarnings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckWarnings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckWarnings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_chkReportQtyShopWarn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method chkReportQtyShopWarn
   OperationID: chkReportQtyShopWarn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/chkReportQtyShopWarn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/chkReportQtyShopWarn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyLaborDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyLaborDetail
   Description: Method to copy the vales from one Labor record to a new Labor record.
   OperationID: CopyLaborDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyLaborDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyLaborDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyTimeWeeklyView(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyTimeWeeklyView
   Description: Method to copy the vales from one Weekly Time record to a new Weekly Time record.
   OperationID: CopyTimeWeeklyView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyTimeWeeklyView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyTimeWeeklyView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultAssemblySeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultAssemblySeq
   Description: This method sets dataset fields when the AssemblySeq field changes
   OperationID: DefaultAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultComplete
   Description: This method updates the dataset after complete flag is set
   OperationID: DefaultComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultDate
   Description: This method updates the clock in and clock out dates for the LaborHed and LaborDtl
tables when the payroll date has changed.
   OperationID: DefaultDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultDiscrpRsnCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultDiscrpRsnCode
   Description: This method defaults fields when the discrepancy reason code field changes.
Also checks for any warnings the user needs to be aware of
   OperationID: DefaultDiscrpRsnCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultDiscrpRsnCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultDiscrpRsnCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultReworkReasonCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultReworkReasonCode
   Description: This method defaults fields when the discrepancy reason code field changes.
Also checks for any warnings the user needs to be aware of
   OperationID: DefaultReworkReasonCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultReworkReasonCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultReworkReasonCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultDtlTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultDtlTime
   Description: This method updates the hours when a time field changes
   OperationID: DefaultDtlTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultDtlTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultDtlTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultIndirect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultIndirect
   Description: This method defaults the expense code when the indirect code has changed
   OperationID: DefaultIndirect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultIndirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultIndirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectAllForWork(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectAllForWork
   Description: This method will take the selected rows from the work queue and process them in one server call.
GetNewLaborDtlOnSelectForWork is called for each work queue row, after that SelectForWork will be called filling required information in all the added LaborDtl rows
If there is any warning that needs user input the method will finish before calling Update and the prompts will be shown to the user, after the UI will call Update to finish.
   OperationID: SelectAllForWork
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectAllForWork_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectAllForWork_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultJobNum
   Description: This method defaults dataset fields when the JobNum field changes
   OperationID: DefaultJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultLaborHrs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultLaborHrs
   Description: This method updates the tot hours display field when the labor hours clock in/out
time changes
   OperationID: DefaultLaborHrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultLaborHrs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultLaborHrs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultLaborQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultLaborQty
   Description: This method defaults fields when the labor qty fields changes.  Also checks
for any labor warnings the user needs to be aware of
   OperationID: DefaultLaborQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultLaborQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultLaborQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultNonConformanceQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultNonConformanceQty
   Description: This method defaults fields when the labor qty fields changes.  Also checks
for any labor warnings the user needs to be aware of
   OperationID: DefaultNonConformanceQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultNonConformanceQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultNonConformanceQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VerifyScrapQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifyScrapQty
   Description: This method defaults fields when the scrap qty field changes.  Also checks
for any labor warnings the user needs to be aware of
   OperationID: VerifyScrapQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyScrapQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyScrapQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartQty
   Description: This method sets Complete checkbox when part qty field changes in End Activity.
   OperationID: OnChangePartQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultLaborType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultLaborType
   Description: This method defaults dataset fields when the LaborType field changes.
   OperationID: DefaultLaborType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultLaborType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultLaborType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultLunchBreak(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultLunchBreak
   Description: This method defaults the Lunch Time fields when the Lunch Break field changes.
   OperationID: DefaultLunchBreak
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultLunchBreak_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultLunchBreak_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultNextOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultNextOprSeq
   Description: This method updates the dataset after next operation seq is set
   OperationID: DefaultNextOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultNextOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultNextOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultOpCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultOpCode
   Description: This method checks for any warnings user needs to know on change of OpCode
   OperationID: DefaultOpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultOpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultOpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultOprSeq
   Description: This method defaults fields when Operation sequence changes.  Also returns any
warnings user needs to know.
   OperationID: DefaultOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborDtlOnSelectForWork(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborDtlOnSelectForWork
   Description: Call GetNewLaborDtl base method then assign selected values and default values for MES/Work Queue/Select for Work.
ResourceID is defaulted the same way than for MES- Start Production Activity. ResourceID must be required only if Company Configuration MachinePrompt is true, otherwise is optional.
   OperationID: GetNewLaborDtlOnSelectForWork
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlOnSelectForWork_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlOnSelectForWork_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultPhaseID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultPhaseID
   Description: This method defaults dataset fields when the PhaseID field changes.
   OperationID: DefaultPhaseID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultPhaseID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultPhaseID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultPhaseOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultPhaseOprSeq
   Description: This method defaults dataset fields when the PhaseOprSeq field changes.
   OperationID: DefaultPhaseOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultPhaseOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultPhaseOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultProjectID
   Description: This method defaults dataset fields when the ProjectID field changes.
   OperationID: DefaultProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultResourceID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultResourceID
   Description: This method updates dataset fields when the ResourceID field changes.
   OperationID: DefaultResourceID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultResourceID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultResourceID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultRoleCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultRoleCd
   Description: This method defaults dataset fields when the RoleCd field changes.
   OperationID: DefaultRoleCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultRoleCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultRoleCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultScrapReasonCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultScrapReasonCode
   Description: This method defaults fields when the scrap reason code fields changes.  Also checks
for any labor warnings the user needs to be aware of
   OperationID: DefaultScrapReasonCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultScrapReasonCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultScrapReasonCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultSetupPctComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultSetupPctComplete
   Description: This method validates and reassigns the setup percent complete field.
   OperationID: DefaultSetupPctComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultSetupPctComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultSetupPctComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultShift(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultShift
   Description: This method updates clock in/out and lunch in/out fields after shift field changes
   OperationID: DefaultShift
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultShift_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultShift_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultTime
   Description: This method updates time and pay hours when a time field changes
   OperationID: DefaultTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultTimeTypCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultTimeTypCd
   Description: This method defaults dataset fields when the TimeTypCd field changes.
   OperationID: DefaultTimeTypCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultTimeTypCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultTimeTypCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultWCCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultWCCode
   Description: This method updates dataset fields when the ResourceGroup field changes.  Also checks
for any warning the user needs to know
   OperationID: DefaultWCCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultWCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultWCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteLaborDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteLaborDtl
   Description: This method delete records related to HCM PTO.
   OperationID: DeleteLaborDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EndActivity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EndActivity
   Description: Method to call to end an activity in Shop Floor.  This method will mark
the EndActivity flag in LaborDtl so when the Update method is run, special
end activity processing can occur.  It will also default values in other
fields that apply to the end activity.  Before this method is called, the
LaborDtl.RowMod value needs to be set to 'U'.
   OperationID: EndActivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EndActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EndActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EndActivityComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EndActivityComplete
   Description: This method checks for any necessary labor warning when the complete flag is checked in MES End Activity
   OperationID: EndActivityComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EndActivityComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EndActivityComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetActiveLaborDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetActiveLaborDtl
   Description: Method to retrieve the active Labor Details and header records by employee.
   OperationID: GetActiveLaborDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetActiveLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActiveLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InitiateDowntime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InitiateDowntime
   Description: Method to Begin Downtime for Kinetic MES
   OperationID: InitiateDowntime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitiateDowntime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitiateDowntime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EndDowntime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EndDowntime
   Description: Method to End Downtime for Kinetic MES
   OperationID: EndDowntime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EndDowntime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EndDowntime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDetail
   Description: Method to call to retrieve the Labor dataset with just the header
and a specific detail record.
   OperationID: GetDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getElapsedTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getElapsedTime
   Description: This method gets the elapsed time from a start date-startTime until now
   OperationID: getElapsedTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getElapsedTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getElapsedTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborDtlNoHdr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborDtlNoHdr
   Description: This method is called to add a new labor detail without having a
labor header record available
   OperationID: GetNewLaborDtlNoHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlNoHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlNoHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborDtlWithHdr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborDtlWithHdr
   Description: This method is called to add a new labor detail without having a
labor header record available
   OperationID: GetNewLaborDtlWithHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlWithHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlWithHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborHed1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborHed1
   Description: This method to be used in place of GetNewLaborHed.  This method asks for an
employee number to default fields based on the employee.
   OperationID: GetNewLaborHed1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborHed1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborHed1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLbrScrapSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLbrScrapSerialNumbers
   Description: Gets a new LbrScrapSerialNumbers record for current LaborDtl
   OperationID: GetNewLbrScrapSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLbrScrapSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLbrScrapSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTimeWeeklyView(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTimeWeeklyView
   Description: Gets a new TimeWeeklyView record for the current week
   OperationID: GetNewTimeWeeklyView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTimeWeeklyView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTimeWeeklyView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCalendarView(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCalendarView
   OperationID: GetRowsCalendarView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCalendarView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCalendarView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsWhoIsHere(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsWhoIsHere
   OperationID: GetRowsWhoIsHere
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWhoIsHere_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWhoIsHere_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTERetrieveApproved(epicorHeaders = None):
   """  
   Summary: Invoke method GetTERetrieveApproved
   Description: Method to get the value UserFile.TERetrieveApproved
   OperationID: GetTERetrieveApproved
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTERetrieveApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetTERetrieveByOption(epicorHeaders = None):
   """  
   Summary: Invoke method GetTERetrieveByOption
   Description: Method to get retrieve by options
   OperationID: GetTERetrieveByOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTERetrieveByOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetTERetrieveEntered(epicorHeaders = None):
   """  
   Summary: Invoke method GetTERetrieveEntered
   Description: Method to get the value UserFile.TERetrieveEntered
   OperationID: GetTERetrieveEntered
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTERetrieveEntered_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetTERetrievePartiallyApproved(epicorHeaders = None):
   """  
   Summary: Invoke method GetTERetrievePartiallyApproved
   Description: Method to get the value UserFile.TERetrievePartiallyApproved
   OperationID: GetTERetrievePartiallyApproved
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTERetrievePartiallyApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetTERetrieveRejected(epicorHeaders = None):
   """  
   Summary: Invoke method GetTERetrieveRejected
   Description: Method to get the value UserFile.TERetrieveRejected
   OperationID: GetTERetrieveRejected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTERetrieveRejected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetTERetrieveSubmitted(epicorHeaders = None):
   """  
   Summary: Invoke method GetTERetrieveSubmitted
   Description: Method to get the value UserFile.TERetrieveSubmitted
   OperationID: GetTERetrieveSubmitted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTERetrieveSubmitted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_IsValidAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsValidAssembly
   Description: Validate if an assembly is valid for a job. if not returns false,
otherwise returns true.
   OperationID: IsValidAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsValidAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LaborDtlAfterGetRowsWrapper(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LaborDtlAfterGetRowsWrapper
   Description: Calls LaborDtlAfterGetRows for the passed in LaborDtl row
   OperationID: LaborDtlAfterGetRowsWrapper
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LaborDtlAfterGetRowsWrapper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LaborDtlAfterGetRowsWrapper_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LaborRateCalc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LaborRateCalc
   OperationID: LaborRateCalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LaborRateCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LaborRateCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeClockInDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeClockInDate
   Description: Call this procedure when LaborDtl.ClockInDate changes
   OperationID: OnChangeClockInDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeClockInDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClockInDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCID
   Description: This method validates the PCID
   OperationID: OnChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQuickEntryCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQuickEntryCode
   Description: This method validates field QuickEntryCode, and if it is valid, uses the
values from the QuickEntry record to populate the LaborDtl values.
   OperationID: OnChangeQuickEntryCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQuickEntryCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuickEntryCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeResourceGrpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeResourceGrpID
   Description: Call this procedure when TimeWeeklyView.ResourceGrpID changes
   OperationID: OnChangeResourceGrpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeResourceGrpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResourceGrpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnLoadEndActivity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnLoadEndActivity
   Description: Call this method when loading end activity on Kinetic-MES.
   OperationID: OnLoadEndActivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnLoadEndActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnLoadEndActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Overrides(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Overrides
   Description: Call this procedure to override the Resource Group and Operation Code in a
job.
   OperationID: Overrides
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Overrides_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Overrides_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OverridesResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OverridesResource
   Description: Call this procedure to override the Resource in a LaborDtl record
   OperationID: OverridesResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OverridesResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OverridesResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecallFromApproval(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecallFromApproval
   Description: Method to recall Labor for Approval.
   OperationID: RecallFromApproval
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecallFromApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallFromApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectForWork(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectForWork
   Description: This method is intended to be used when the MES/ShopFloor user selects an
operation from the WorkQueue to work on.  Use this method in place of the
Update method in this situation.
            
This method expects a LaborDataSet containing a single LaborHed with a
RowMod indicating a changed row, and a LaborDtl row with a RowMod indicating
a changed row.  This can be obtained with a call to Labor.GetRows() with a
whereClauseLaborHed of
ActiveTrans = YES and EmployeeNum = xxxx
substituting the desired employeeNum for the xxxx.
followed by a call to LaborDtlGetNew.
            
After validating the given Job, Assembly, Operation, ResourceID, ResourceGrpID
and LaborType, and additional validations are applied, the LaborDtl is updated.
            
An exception is thrown if:
- a changed Laborhed row is not found.
- the given Job, Assembly and Operation is not valid
- the LaborHed.ActiveTrans = no.  This method is for MES (ShopFloor) use only.
- the given LaborType is not "S" or "P"
   OperationID: SelectForWork
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectForWork_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectForWork_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectForWorkCheckWarnings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectForWorkCheckWarnings
   Description: This method runs the shop warning routine and returns any warnings the user needs
to be aware of.  This needs to be run right before the SelectForWork method.  If the user answers
okay to all of the questions, then the SelectForWork method can be run.  Otherwise the labor record
needs to be corrected
   OperationID: SelectForWorkCheckWarnings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectForWorkCheckWarnings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectForWorkCheckWarnings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetClockInAndDisplayTimeMES(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetClockInAndDisplayTimeMES
   Description: Sets the Time Stamp in which the Employee Starts his/her activity and
also populates the field that displays the time correctly.
   OperationID: SetClockInAndDisplayTimeMES
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetClockInAndDisplayTimeMES_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetClockInAndDisplayTimeMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetTERetrieveApproved(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetTERetrieveApproved
   Description: Method to set the value UserFile.TERetrieveApproved
   OperationID: SetTERetrieveApproved
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetTERetrieveApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetTERetrieveByDay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetTERetrieveByDay
   Description: Method to set the value for retrieve by day
   OperationID: SetTERetrieveByDay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetTERetrieveByDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveByDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetTERetrieveByMonth(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetTERetrieveByMonth
   Description: Method to set the value for retrieve by month
   OperationID: SetTERetrieveByMonth
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetTERetrieveByMonth_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveByMonth_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetTERetrieveByWeek(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetTERetrieveByWeek
   Description: Method to set the value for retrieve by week
   OperationID: SetTERetrieveByWeek
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetTERetrieveByWeek_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveByWeek_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetTERetrieveEntered(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetTERetrieveEntered
   Description: Method to set the value UserFile.TERetrieveEntered
   OperationID: SetTERetrieveEntered
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetTERetrieveEntered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveEntered_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetTERetrievePartiallyApproved(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetTERetrievePartiallyApproved
   Description: Method to set the value UserFile.TERetrievePartiallyApproved
   OperationID: SetTERetrievePartiallyApproved
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetTERetrievePartiallyApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrievePartiallyApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetTERetrieveRejected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetTERetrieveRejected
   Description: Method to set the value UserFile.TERetrieveRejected
   OperationID: SetTERetrieveRejected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetTERetrieveRejected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveRejected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetTERetrieveSubmitted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetTERetrieveSubmitted
   Description: Method to set the value UserFile.TERetrieveSubmitted
   OperationID: SetTERetrieveSubmitted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetTERetrieveSubmitted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTERetrieveSubmitted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartActivity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartActivity
   Description: Method to call to start an activity in Shop Floor.
   OperationID: StartActivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartActivityByEmp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartActivityByEmp
   Description: Method to call to start an activity in Shop Floor by Employee.
   OperationID: StartActivityByEmp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartActivityByEmp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartActivityByEmp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SubmitForApproval(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SubmitForApproval
   Description: Method to submit Labor for Approval.
   OperationID: SubmitForApproval
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitForApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitForApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateIndirectCodeIsDowntime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateIndirectCodeIsDowntime
   Description: This method validates the IndirectCode is marked as Downtime
   OperationID: ValidateIndirectCodeIsDowntime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateIndirectCodeIsDowntime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateIndirectCodeIsDowntime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_validateNonConfProcessed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method validateNonConfProcessed
   Description: This method validates the Non Conformance value and validates if it has already been processed
   OperationID: validateNonConfProcessed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/validateNonConfProcessed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/validateNonConfProcessed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateProjectClosed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateProjectClosed
   Description: this method validates if the Project linked to the Job in Labor Detail is closed.
   OperationID: ValidateProjectClosed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateProjectClosed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateProjectClosed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSerialAfterSelect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSerialAfterSelect
   Description: Validates after calling SN selection screen
   OperationID: ValidateSerialAfterSelect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSerialAfterSelect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialAfterSelect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSerialScanInterface(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSerialScanInterface
   Description: Validates if serial number is valid after selecting SN on scan interface kinetic MES
   OperationID: ValidateSerialScanInterface
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSerialScanInterface_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialScanInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSerialBeforeSelect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSerialBeforeSelect
   Description: Call before allowing the select of serial numbers
   OperationID: ValidateSerialBeforeSelect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSerialBeforeSelect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialBeforeSelect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VerifySerialMatch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifySerialMatch
   Description: Verifies if the user should enter child serial numbers for the serial numbers
being received depending on the setting of the Serial Number Matching before save.
   OperationID: VerifySerialMatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifySerialMatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifySerialMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetClockTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetClockTime
   Description: This method is called to update the values of the Display columns
DspClockInTime and DspClockOutTime
   OperationID: GetClockTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetClockTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetClockTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDspClockTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDspClockTime
   Description: This method is called to update the values of the Display columns
DspClockInTime and DspClockOutTime
   OperationID: GetDspClockTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDspClockTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDspClockTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReportPartQtyAllowed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReportPartQtyAllowed
   Description: Returns TRUE if Part Quantity Reporting is allowed for a given operation.
   OperationID: ReportPartQtyAllowed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReportPartQtyAllowed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReportPartQtyAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExternalMESDowntime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExternalMESDowntime
   Description: Methods updates Downtime codes
   OperationID: ExternalMESDowntime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExternalMESDowntime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExternalMESDowntime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExternalMESEndDowntime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExternalMESEndDowntime
   Description: Methods updates Downtime codes
   OperationID: ExternalMESEndDowntime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExternalMESEndDowntime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExternalMESEndDowntime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HCMGetLaborRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HCMGetLaborRecords
   Description: Description: Public method which retrieves the labor information HCM third party requires.
   OperationID: HCMGetLaborRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HCMGetLaborRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HCMGetLaborRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HCMSetLaborStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HCMSetLaborStatus
   OperationID: HCMSetLaborStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HCMSetLaborStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HCMSetLaborStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateChargeRateForTimeType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateChargeRateForTimeType
   Description: Validates if there is no valid Charge Rate according to selected Time Type.
This validation can also be found on BO/LaborApproval.
   OperationID: ValidateChargeRateForTimeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateChargeRateForTimeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateChargeRateForTimeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReviewIsDocumentLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReviewIsDocumentLock
   Description: Review if the document is Lock when user tries to recall the record from UI
   OperationID: ReviewIsDocumentLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReviewIsDocumentLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReviewIsDocumentLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsHCMEnabledAtCompany(epicorHeaders = None):
   """  
   Summary: Invoke method IsHCMEnabledAtCompany
   Description: Returns true if HCM is enable at company level.
   OperationID: IsHCMEnabledAtCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsHCMEnabledAtCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ChangeTimeWeeklyViewWeekBeginDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTimeWeeklyViewWeekBeginDate
   Description: Called when Time Weekly View Week Begin Date is changing
   OperationID: ChangeTimeWeeklyViewWeekBeginDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTimeWeeklyViewWeekBeginDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTimeWeeklyViewWeekBeginDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLaborDtlOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLaborDtlOprSeq
   Description: This method defaults LaborDtl fields when Operation sequence changes.  Also returns any
warnings user needs to know.
   OperationID: ChangeLaborDtlOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborDtlOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborDtlOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLaborDtlScrapQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLaborDtlScrapQty
   Description: This method defaults fields when the scrap qty field changes.
   OperationID: ChangeLaborDtlScrapQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborDtlScrapQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborDtlScrapQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLaborDtlAttributeSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLaborDtlAttributeSetID
   Description: This method updates the revision field when the attribute ID field changes.
   OperationID: ChangeLaborDtlAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborDtlAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborDtlAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AfterChangeLaborDtlDiscrepQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AfterChangeLaborDtlDiscrepQty
   Description: Called after LaborDtl.DiscrepQty has been changed.
   OperationID: AfterChangeLaborDtlDiscrepQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AfterChangeLaborDtlDiscrepQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterChangeLaborDtlDiscrepQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLaborDtlTimeField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLaborDtlTimeField
   Description: Called when labor clock in or clock out time is changing
   OperationID: ChangeLaborDtlTimeField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborDtlTimeField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborDtlTimeField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLaborDtlDspTimeField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLaborDtlDspTimeField
   Description: Called when labor display clock in or clock out time is changing
   OperationID: ChangeLaborDtlDspTimeField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborDtlDspTimeField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborDtlDspTimeField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetJobProductionCompanySettings(epicorHeaders = None):
   """  
   Summary: Invoke method GetJobProductionCompanySettings
   Description: Returns company job production settings for Advance Labor Rate, Clock Format
   OperationID: GetJobProductionCompanySettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobProductionCompanySettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SubmitForApprovalBySelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SubmitForApprovalBySelected
   Description: Method to submit Labor for Approval using RowSelected flag.
   OperationID: SubmitForApprovalBySelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitForApprovalBySelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitForApprovalBySelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecallFromApprovalBySelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecallFromApprovalBySelected
   Description: Method to recall Labor for Approval using RowSelected flag.
   OperationID: RecallFromApprovalBySelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecallFromApprovalBySelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallFromApprovalBySelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyLaborDtlBySelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyLaborDtlBySelected
   Description: Method to copy Labor detail record(s) using RowSelected flag.
   OperationID: CopyLaborDtlBySelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyLaborDtlBySelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyLaborDtlBySelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyTimeWeeklyViewBySelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyTimeWeeklyViewBySelected
   Description: Method to copy TimeWeeklyView record(s) using RowSelected flag.
   OperationID: CopyTimeWeeklyViewBySelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyTimeWeeklyViewBySelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyTimeWeeklyViewBySelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsTimeEntry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsTimeEntry
   Description: Get rows for Time Entry.  This method will consider user time retrieval options for retrieving approved, entered, partially approved, rejected, and submitted records.
   OperationID: GetRowsTimeEntry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsTimeEntry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsTimeEntry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLaborTypeList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLaborTypeList
   Description: Returns valid labor types based on the employee
   OperationID: GetLaborTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLaborTypeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLaborTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateLbrScrapSerialNumbersFromList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateLbrScrapSerialNumbersFromList
   Description: Create LbrScrapSerialNumbers dataset records from a list of selected serial numbers
   OperationID: CreateLbrScrapSerialNumbersFromList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateLbrScrapSerialNumbersFromList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateLbrScrapSerialNumbersFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlActionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborDtlActionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborDtlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlCommentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborDtlCommentRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlGroupRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborDtlGroupRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborEquipRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborEquipRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborHedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborPartRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborPartRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LbrScrapSerialNumbersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LbrScrapSerialNumbersRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SNFormatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TimeWeeklyViewRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TimeWeeklyViewRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TimeWorkHoursRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TimeWorkHoursRow] = obj["value"]
      pass

class Erp_Tablesets_LaborDtlActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionDesc:str = obj["ActionDesc"]
      """  Description of Action.  """  
      self.Required:bool = obj["Required"]
      """  Indicated if this Action must be completed before Operation can be completed.  """  
      self.Completed:bool = obj["Completed"]
      """  Indicates if this Action was completed.  """  
      self.CompletedBy:str = obj["CompletedBy"]
      """  The number of the employee that performed the work.  """  
      self.CompletedOn:str = obj["CompletedOn"]
      """  Date the Action was completed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlCommentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  The unique identifier of the Labor Header the comment relates to.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.CommentNum:int = obj["CommentNum"]
      """  Internal identifier of the comment record.  Used in conjunction with EmpTimeNum to make the record unique.  """  
      self.CommentType:str = obj["CommentType"]
      """   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  The identifier of the Task record the comment is related to.  Can be zero, which indicates the comment is not related to a specific task.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.TimeEntryCommentTypeList:str = obj["TimeEntryCommentTypeList"]
      """  List of valid comment types for Time Entry  """  
      self.CommentTypeDesc:str = obj["CommentTypeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are

concurrently active for an employee in order to distribute the labor hours.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the expense.  Can be used to expenses together, for example, all expenses incurred on the same trip can be assigned the same reference.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LaborType:str = obj["LaborType"]
      """   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.ReWork:bool = obj["ReWork"]
      """  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  """  
      self.ReworkReasonCode:str = obj["ReworkReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  """  
      self.OprSeq:int = obj["OprSeq"]
      """   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  """  
      self.JCDept:str = obj["JCDept"]
      """  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  """  
      self.OpCode:str = obj["OpCode"]
      """  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  """  
      self.BurdenHrs:int = obj["BurdenHrs"]
      """  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  """  
      self.LaborQty:int = obj["LaborQty"]
      """  The Total production quantity reported.  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  The reported scrap quantity.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates if this transaction "completes" either the setup or production for this operation.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  """  
      self.LaborNote:str = obj["LaborNote"]
      """  A short note that the user can make about the labor transaction.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.AppliedToSchedule:bool = obj["AppliedToSchedule"]
      """  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  """  
      self.ClockInMInute:int = obj["ClockInMInute"]
      """  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  """  
      self.ClockOutMinute:int = obj["ClockOutMinute"]
      """  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  """  
      self.ClockinTime:int = obj["ClockinTime"]
      """   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  """  
      self.OverRidePayRate:int = obj["OverRidePayRate"]
      """  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  """  
      self.BurdenRate:int = obj["BurdenRate"]
      """  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.OpComplete:bool = obj["OpComplete"]
      """  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  """  
      self.EarnedHrs:int = obj["EarnedHrs"]
      """  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  """  
      self.AddedOper:bool = obj["AddedOper"]
      """  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  Indicates if the labordtl record inspection has completed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this service record belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The line number of the service call this labor detail is for.  """  
      self.ServNum:int = obj["ServNum"]
      """  the service that is being performed on this line.  """  
      self.ServCode:str = obj["ServCode"]
      """  A unique code that identifies the Service  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.WipPosted:bool = obj["WipPosted"]
      """  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  """  
      self.ParentLaborDtlSeq:int = obj["ParentLaborDtlSeq"]
      """  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BFLaborReq:bool = obj["BFLaborReq"]
      """  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID,used in PostingEngine  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Project Role Code  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  Time Type Code  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  The Project Billing Invoice Number where these charges were processed.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the time.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the time received final approval.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  """  
      self.TimeStatus:str = obj["TimeStatus"]
      """   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CreatedViaTEWeekView:bool = obj["CreatedViaTEWeekView"]
      """  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The User ID of the submitter.  """  
      self.PBRateFrom:str = obj["PBRateFrom"]
      """  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  """  
      self.PBCurrencyCode:str = obj["PBCurrencyCode"]
      """  Project Billing calculation in COSandWIP: Currency code is got from Project  """  
      self.PBHours:int = obj["PBHours"]
      """  Project Billing calculation in COSandWIP: Hours used for charge  """  
      self.PBChargeRate:int = obj["PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  """  
      self.PBChargeAmt:int = obj["PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  """  
      self.DocPBChargeRate:int = obj["DocPBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  """  
      self.Rpt1PBChargeRate:int = obj["Rpt1PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt2PBChargeRate:int = obj["Rpt2PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt3PBChargeRate:int = obj["Rpt3PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.DocPBChargeAmt:int = obj["DocPBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  """  
      self.Rpt1PBChargeAmt:int = obj["Rpt1PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt2PBChargeAmt:int = obj["Rpt2PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt3PBChargeAmt:int = obj["Rpt3PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ActID:int = obj["ActID"]
      """  Links to PActDtl.ActID  """  
      self.DtailID:int = obj["DtailID"]
      """  System assigned unique id number for the detail. Links to PActDtl.DetailID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used By Project Analysis Process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process.  """  
      self.JDFInputFiles:str = obj["JDFInputFiles"]
      """  JDFInputFiles  """  
      self.JDFNumberOfPages:str = obj["JDFNumberOfPages"]
      """  JDFNumberOfPages  """  
      self.BatchWasSaved:str = obj["BatchWasSaved"]
      """  BatchWasSaved  """  
      self.AssignToBatch:bool = obj["AssignToBatch"]
      """  AssignToBatch  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchRequestMove:bool = obj["BatchRequestMove"]
      """  BatchRequestMove  """  
      self.BatchPrint:bool = obj["BatchPrint"]
      """  BatchPrint  """  
      self.BatchLaborHrs:int = obj["BatchLaborHrs"]
      """  BatchLaborHrs  """  
      self.BatchPctOfTotHrs:int = obj["BatchPctOfTotHrs"]
      """  BatchPctOfTotHrs  """  
      self.BatchQty:int = obj["BatchQty"]
      """  BatchQty  """  
      self.BatchTotalExpectedHrs:int = obj["BatchTotalExpectedHrs"]
      """  BatchTotalExpectedHrs  """  
      self.JDFOpCompleted:str = obj["JDFOpCompleted"]
      """  JDFOpCompleted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Downtime:bool = obj["Downtime"]
      """  Downtime  """  
      self.RefJobNum:str = obj["RefJobNum"]
      """  RefJobNum  """  
      self.RefAssemblySeq:int = obj["RefAssemblySeq"]
      """  RefAssemblySeq  """  
      self.RefOprSeq:int = obj["RefOprSeq"]
      """  RefOprSeq  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.BillServiceRate:int = obj["BillServiceRate"]
      """  BillServiceRate  """  
      self.HCMPayHours:int = obj["HCMPayHours"]
      """  Pay Hours used for HCM  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.DiscrepAttributeSetID:int = obj["DiscrepAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  """  
      self.LaborAttributeSetID:int = obj["LaborAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the Labor Qty  """  
      self.ScrapAttributeSetID:int = obj["ScrapAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.NonConfPCID:str = obj["NonConfPCID"]
      """  NonConfPCID  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.ApprovalPhaseDesc:str = obj["ApprovalPhaseDesc"]
      """  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalPhaseID:str = obj["ApprovalPhaseID"]
      """  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectDesc:str = obj["ApprovalProjectDesc"]
      """  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectID:str = obj["ApprovalProjectID"]
      """  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      self.ApprvrHasOpenTask:bool = obj["ApprvrHasOpenTask"]
      """  Used in approval entry.  Indicates if the approver has an open task or not.  """  
      self.BaseCurrCodeDesc:str = obj["BaseCurrCodeDesc"]
      """  Company Base currency code description for display in LaborDtl grid.  """  
      self.BurdenCost:int = obj["BurdenCost"]
      """  calculated field: BurdenHrs * BurdenRate  """  
      self.CallCode:str = obj["CallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.CapabilityDescription:str = obj["CapabilityDescription"]
      self.CapabilityID:str = obj["CapabilityID"]
      self.ChargeRate:int = obj["ChargeRate"]
      """  Charge rate calculated for Time and Expense approval  """  
      self.ChargeRateSRC:str = obj["ChargeRateSRC"]
      """  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  """  
      self.ChgRateCurrDesc:str = obj["ChgRateCurrDesc"]
      """  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  """  
      self.CompleteFlag:bool = obj["CompleteFlag"]
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.DiscrepUOM:str = obj["DiscrepUOM"]
      """  Unit of Measure used for DiscrepQty  """  
      self.DisLaborType:bool = obj["DisLaborType"]
      """  Field that indicates if field DisLaborTypeshould be disabled.  """  
      self.DisplayJob:str = obj["DisplayJob"]
      self.DisPrjRoleCd:bool = obj["DisPrjRoleCd"]
      """  Field that indicates if field PrjRoleCd should be disabled.  """  
      self.DisTimeTypCd:bool = obj["DisTimeTypCd"]
      """  Field that indicates if field TimeTypCd should be disabled.  """  
      self.DowntimeTotal:int = obj["DowntimeTotal"]
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.DspTotHours:str = obj["DspTotHours"]
      self.DtClockIn:str = obj["DtClockIn"]
      self.DtClockOut:str = obj["DtClockOut"]
      self.EfficiencyPercentage:int = obj["EfficiencyPercentage"]
      """  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  Labor Detail Employee Name  """  
      self.EnableComplete:bool = obj["EnableComplete"]
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.EnableDiscrepQty:bool = obj["EnableDiscrepQty"]
      self.EnableInspection:bool = obj["EnableInspection"]
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.EnableNextOprSeq:bool = obj["EnableNextOprSeq"]
      self.EnablePrintTagsList:bool = obj["EnablePrintTagsList"]
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available for an approver  """  
      self.EnableRequestMove:bool = obj["EnableRequestMove"]
      self.EnableResourceGrpID:bool = obj["EnableResourceGrpID"]
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Enable the SN Button?  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.EndActivity:bool = obj["EndActivity"]
      self.EnteredOnCurPlant:bool = obj["EnteredOnCurPlant"]
      """  To know if the LaborDtl was created on the current plant  """  
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.FSComplete:bool = obj["FSComplete"]
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.HasAccessToRow:bool = obj["HasAccessToRow"]
      """  Indicates if the user has access to the row  """  
      self.HasComments:bool = obj["HasComments"]
      """  Indicates if the labor detail has comments  """  
      self.HH:bool = obj["HH"]
      """  To tell the bo that this transaction was being modified from HH.  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.ISFixHourAndQtyOnly:bool = obj["ISFixHourAndQtyOnly"]
      """  Indicates if the job operation is marked as fixed hours and quantity only.  """  
      self.JCSystReworkReasons:bool = obj["JCSystReworkReasons"]
      self.JCSystScrapReasons:bool = obj["JCSystScrapReasons"]
      self.JobOperComplete:bool = obj["JobOperComplete"]
      self.JobType:str = obj["JobType"]
      self.JobTypeCode:str = obj["JobTypeCode"]
      """  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  """  
      self.LaborCost:int = obj["LaborCost"]
      """  calculated field: LaborHrs * LaborRate  """  
      self.LaborUOM:str = obj["LaborUOM"]
      """  Unit of Measure used for LaborQty  """  
      self.LbrDay:str = obj["LbrDay"]
      """  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrMonth:str = obj["LbrMonth"]
      """  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrWeek:str = obj["LbrWeek"]
      """  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  """  
      self.MES:bool = obj["MES"]
      self.MultipleEmployeesText:str = obj["MultipleEmployeesText"]
      self.NewDifDateFlag:int = obj["NewDifDateFlag"]
      self.NewPrjRoleCd:str = obj["NewPrjRoleCd"]
      """  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  """  
      self.NewRoleCdDesc:str = obj["NewRoleCdDesc"]
      """  Holds the description for NewPrjRoleCd  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      self.NextOperDesc:str = obj["NextOperDesc"]
      self.NextOprSeq:int = obj["NextOprSeq"]
      self.NextResourceDesc:str = obj["NextResourceDesc"]
      self.NonConfProcessed:bool = obj["NonConfProcessed"]
      """  To evaluate if the NonComformance has been already processed in inspection and no changes can be applied on LaborDtl then.  """  
      self.NotSubmitted:bool = obj["NotSubmitted"]
      self.OkToChangeResourceGrpID:bool = obj["OkToChangeResourceGrpID"]
      """  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  """  
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.PBAllowModify:bool = obj["PBAllowModify"]
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      self.PhaseJobNum:str = obj["PhaseJobNum"]
      """  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  """  
      self.PhaseOprSeq:int = obj["PhaseOprSeq"]
      """  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  """  
      self.PrintNCTag:bool = obj["PrintNCTag"]
      self.PrjUsedTran:str = obj["PrjUsedTran"]
      self.ProdDesc:str = obj["ProdDesc"]
      self.ProjPhaseID:str = obj["ProjPhaseID"]
      self.RequestMove:bool = obj["RequestMove"]
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.RoleCdDisplayAll:bool = obj["RoleCdDisplayAll"]
      self.ScrapUOM:str = obj["ScrapUOM"]
      """  Unit of Measure used for ScrapQty.  """  
      self.SentFromMES:bool = obj["SentFromMES"]
      """  Flag field to identify if the row is being sent from MES  """  
      self.StartActivity:bool = obj["StartActivity"]
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.UnapprovedFirstArt:bool = obj["UnapprovedFirstArt"]
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.EnablePCID:bool = obj["EnablePCID"]
      """  EnablePCID  """  
      self.OutputBin:str = obj["OutputBin"]
      """  The output bin from the resource  """  
      self.OutputWarehouse:str = obj["OutputWarehouse"]
      """  The output warehouse from the resource  """  
      self.EnableLot:bool = obj["EnableLot"]
      """  Internal flag used for the row rules to control whether the Lot columns should be enabled.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot number that is to be added to the PCID  """  
      self.PrintPCIDContents:bool = obj["PrintPCIDContents"]
      """  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  """  
      self.HasAttachments:bool = obj["HasAttachments"]
      """  Indicates if the labor detail has attachments  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.DiscrepAttributeSetDescription:str = obj["DiscrepAttributeSetDescription"]
      """  The Full Description of the Attribute Set for DiscrepQty  """  
      self.DiscrepAttributeSetShortDescription:str = obj["DiscrepAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for DiscrepQty  """  
      self.ScrapAttributeSetDescription:str = obj["ScrapAttributeSetDescription"]
      """  The Full Description of the Attribute Set for ScrapQty  """  
      self.ScrapAttributeSetShortDescription:str = obj["ScrapAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for ScrapQty  """  
      self.LaborAttributeSetDescription:str = obj["LaborAttributeSetDescription"]
      """  The Full Description of the Attribute Set for LaborQty  """  
      self.LaborAttributeSetShortDescription:str = obj["LaborAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for LaborQty  """  
      self.DisableRecallAndDelete:bool = obj["DisableRecallAndDelete"]
      """  Indicates if recall and delete should be disabled  """  
      self.RoleCdList:str = obj["RoleCdList"]
      """  List of available role codes  """  
      self.RowSelected:bool = obj["RowSelected"]
      """  Indicates if the row is selected for submit, recall, or copy  """  
      self.AppointmentStart:str = obj["AppointmentStart"]
      """  Start date/time for calendar appoinment  """  
      self.AppointmentEnd:str = obj["AppointmentEnd"]
      """  End date/time for calendar appoinment  """  
      self.AppointmentTitle:str = obj["AppointmentTitle"]
      """  Title to display for the calendar appointment  """  
      self.TemplateID:str = obj["TemplateID"]
      """  PDF Form Template linked to the Job Operation  """  
      self.WIPTransaction:bool = obj["WIPTransaction"]
      """  Flag to validate if the transaction includes WIP  """  
      self.DiscrepRevision:str = obj["DiscrepRevision"]
      """  Revision for DiscrepQty  """  
      self.LaborRevision:str = obj["LaborRevision"]
      """  Revision for LaborQty  """  
      self.ScrapRevision:str = obj["ScrapRevision"]
      """  Revision for ScrapQty  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.ReportPartQtyAllowed:bool = obj["ReportPartQtyAllowed"]
      """  Indicates whether co-parts can be entered  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DiscrpRsnDescription:str = obj["DiscrpRsnDescription"]
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HCMIntregationHCMEnabled:bool = obj["HCMIntregationHCMEnabled"]
      self.HCMStatusStatus:str = obj["HCMStatusStatus"]
      self.IndirectDescription:str = obj["IndirectDescription"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.JobAsmblPartNum:str = obj["JobAsmblPartNum"]
      self.JobAsmblDescription:str = obj["JobAsmblDescription"]
      self.MachineDescription:str = obj["MachineDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.OpDescOpDesc:str = obj["OpDescOpDesc"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      self.ResReasonDescription:str = obj["ResReasonDescription"]
      self.ReWorkReasonDescription:str = obj["ReWorkReasonDescription"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.ScrapReasonDescription:str = obj["ScrapReasonDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborEquipRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  """  
      self.Hours:int = obj["Hours"]
      """  Hours that will be added to Equip.CurrentMeter.  Relevant only when the related Equip.LaborOpt = "Hrs"  """  
      self.Qty:int = obj["Qty"]
      """  Quantity that will be added to Equip.CurrentMeter.  Relevant only when the related Equip.LaborOpt = "Qty"  """  
      self.CurrentMeter:int = obj["CurrentMeter"]
      """  Current Meter reading which will update the Equip.CurrentMeter. Relevant only when the related Equip.LaborOpt = "Mtr"  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EquipLaborMeterOpt:str = obj["EquipLaborMeterOpt"]
      self.EquipDescription:str = obj["EquipDescription"]
      self.EquipMeterUOM:str = obj["EquipMeterUOM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  The number of the employee that performed the work. This field is directly maintainable. A selection list is provided in labor entry to find the employee by name.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """   The Payroll date is the "Logical Day" that labor occurred. In most cases this is the same as the "Physical Day".  But when work is done before and after midnight then "Labor Collection" rolls the physical date forward or backward to create a Logical date. This date will be used to group transactions together by a logical date in order to calculate daily overtime during the transfer to payroll.
It will also be used in the selection criteria logic during the transfer to payroll.  This is duplicated into each LaborDtl.  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date of the clock in time field. It is created using the ActualDate and may be rolled forward/backward if the clock in time is adjusted across midnight. For example, when an employee clocks in prior to midnight, but shift starts at midnight or later, this situation causes the default to be ActualDateIn + 1.  """  
      self.ClockInTime:int = obj["ClockInTime"]
      """  The clock in time to be considered for payroll and costing purposes as the time when the employee starts work. Clock in time is stored as Hours.Hundreths. It is created using the ActualClockIn value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockin" is before the shift start time (JCShift.Start) and after ( JCShift. start - JCSyst.Grace) then the system adjusts the clockin time to be the start of the shift. Else it will be set to the actual system time.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ActualClockInTime:int = obj["ActualClockInTime"]
      """  Actual clock in time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocked in. In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.StartTime. Stored as Hours:Hundreths.  """  
      self.ActualClockinDate:str = obj["ActualClockinDate"]
      """  The actual date at the time of clockin. Labor Collection uses the system date to create this field.  Labor entry allows entry of this field and then uses it to generate the default for the adjusted  "ClockInDate".  This field is provided mainly for audit purposes.  """  
      self.LunchStatus:str = obj["LunchStatus"]
      """   An internal control byte used by Labor Collection when the system is configured not to take out lunch automatically (JCSyst.AutoLunch = N). It is used determine if what to do when the "Lunch" button is pressed.

The possible values are "N" - No lunch, "O" - Out to Lunch, "R" - Returned from lunch.  """  
      self.ActLunchOutTime:int = obj["ActLunchOutTime"]
      """   Actual Clock out time for Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchStart as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time for LunchOut.  """  
      self.LunchOutTime:int = obj["LunchOutTime"]
      """   Clock out time for Lunch that is used for costing/payroll determination. It is created by adjusting the ActLunchOutTime. . The adjusted time is where the system time is rolled back to the JCShift.LunchStart time when the employee clocks out for lunch after it has started but before it ends.

Stored as Hours.Hundreths.  """  
      self.ActLunchInTime:int = obj["ActLunchInTime"]
      """   Actual Clock In  time from Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchEnd as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time.  """  
      self.LunchInTime:int = obj["LunchInTime"]
      """   Clock In time from Lunch break that is used for costing/payroll determination. Created by adjusting the ActLunchInTime.
The adjusted time is where the system time is rolled forward to the JCShift.LunchEnd time when the employee clocks in from lunch before the lunch period ends. 
Stored as Hours.Hundreths.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """  The clockOut in time to be considered for payroll and costing purposes as the time when the employee stops work. ClockOut time is stored as Hours.Hundreths. It is defaulted using the ActualClockOut value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockOut" is after the shift end time (JCShift.End) and before ( JCShift.End + JC.Syst.Grace) then the system adjusts the ClockOut time to be the end of the shift. Else it will be set to the actual system time.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ActualClockOutTime:int = obj["ActualClockOutTime"]
      """  Actual clock Out time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocks out.  In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.EndTime. Stored as Hours.Hundreths.  """  
      self.PayHours:int = obj["PayHours"]
      """   Hours for payroll.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5. This is calculated when the Start/Stop times are changed in labor entry. It can then be overridden.
The Logic for calculating hours from clockin, clockout is:
If ClockIn > ClockOut Gross Hours = ( (ClockOut + 24.00) - ClockIn) else Gross Hours = ClockOut - ClockIn. 
If LunchOut > LunchIn Lunch Hours = ( (LunchIn +24) - LunchOut )
else Lunch Hours = ( LunchIn - LunchOut ).
PayHours = GRoss Hours - Lunch Hours. 
Remember that the database clockin/clockout fields are stored as hours hundredths, while the entry widgets are either hours.hundreths or Hours:Minutes. So use the database fields in this calculation and there is no need to worry about conversions.  """  
      self.FeedPayroll:bool = obj["FeedPayroll"]
      """  Flag that indicates this labor transaction is eligible for transfer to DCD payroll application. The default is set from JCSyst.FeedPayroll.  """  
      self.TransferredToPayroll:bool = obj["TransferredToPayroll"]
      """  Indicates if this transaction has been transferred to payroll. This is updated via the Payroll function to transfer labor.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.TranSet:str = obj["TranSet"]
      """  An optional field where the user enters a string of characters that would be used to associate multiple transactions as being part of a transaction set. TranSet will be used for data selection type functions.  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborHed record is currently active. When the employee clocks out it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice, displaying which employees are clocked in and which ones have not clocked out. Labor entry can't access a record that is Open.  """  
      self.ChkLink:str = obj["ChkLink"]
      """   Encoded value PRChkDtl.HeadNum + PRChkDtl.LineNum.
Used to relate the labor to the payroll check detail.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotLbrHrs:int = obj["TotLbrHrs"]
      self.TotBurHrs:int = obj["TotBurHrs"]
      self.WipPosted:bool = obj["WipPosted"]
      self.ImagePath:str = obj["ImagePath"]
      """  Full Path of Employee PhotoFile  """  
      self.LunchBreak:bool = obj["LunchBreak"]
      """  Indicates if a lunch break is part of the shift  """  
      self.EmpBasicShift:int = obj["EmpBasicShift"]
      """  Normal work shift from EmpBasic  """  
      self.EmpBasicSupervisorID:str = obj["EmpBasicSupervisorID"]
      """  The ID of the supervisor for the employee  """  
      self.DspPayHours:int = obj["DspPayHours"]
      """  For display purposes  """  
      self.GetNewNoHdr:bool = obj["GetNewNoHdr"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.MES:bool = obj["MES"]
      self.EmployeeNumLastName:str = obj["EmployeeNumLastName"]
      """  Last name of employee  """  
      self.EmployeeNumName:str = obj["EmployeeNumName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.EmployeeNumFirstName:str = obj["EmployeeNumFirstName"]
      """  First name of employee.  """  
      self.ShiftDescription:str = obj["ShiftDescription"]
      """  A concatenation of Start + End time.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  The number of the employee that performed the work. This field is directly maintainable. A selection list is provided in labor entry to find the employee by name.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """   The Payroll date is the "Logical Day" that labor occurred. In most cases this is the same as the "Physical Day".  But when work is done before and after midnight then "Labor Collection" rolls the physical date forward or backward to create a Logical date. This date will be used to group transactions together by a logical date in order to calculate daily overtime during the transfer to payroll.
It will also be used in the selection criteria logic during the transfer to payroll.  This is duplicated into each LaborDtl.  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date of the clock in time field. It is created using the ActualDate and may be rolled forward/backward if the clock in time is adjusted across midnight. For example, when an employee clocks in prior to midnight, but shift starts at midnight or later, this situation causes the default to be ActualDateIn + 1.  """  
      self.ClockInTime:int = obj["ClockInTime"]
      """  The clock in time to be considered for payroll and costing purposes as the time when the employee starts work. Clock in time is stored as Hours.Hundreths. It is created using the ActualClockIn value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockin" is before the shift start time (JCShift.Start) and after ( JCShift. start - JCSyst.Grace) then the system adjusts the clockin time to be the start of the shift. Else it will be set to the actual system time.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ActualClockInTime:int = obj["ActualClockInTime"]
      """  Actual clock in time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocked in. In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.StartTime. Stored as Hours:Hundreths.  """  
      self.ActualClockinDate:str = obj["ActualClockinDate"]
      """  The actual date at the time of clockin. Labor Collection uses the system date to create this field.  Labor entry allows entry of this field and then uses it to generate the default for the adjusted  "ClockInDate".  This field is provided mainly for audit purposes.  """  
      self.LunchStatus:str = obj["LunchStatus"]
      """   An internal control byte used by Labor Collection when the system is configured not to take out lunch automatically (JCSyst.AutoLunch = N). It is used determine if what to do when the "Lunch" button is pressed.

The possible values are "N" - No lunch, "O" - Out to Lunch, "R" - Returned from lunch.  """  
      self.ActLunchOutTime:int = obj["ActLunchOutTime"]
      """   Actual Clock out time for Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchStart as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time for LunchOut.  """  
      self.LunchOutTime:int = obj["LunchOutTime"]
      """   Clock out time for Lunch that is used for costing/payroll determination. It is created by adjusting the ActLunchOutTime. . The adjusted time is where the system time is rolled back to the JCShift.LunchStart time when the employee clocks out for lunch after it has started but before it ends.

Stored as Hours.Hundreths.  """  
      self.ActLunchInTime:int = obj["ActLunchInTime"]
      """   Actual Clock In  time from Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchEnd as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time.  """  
      self.LunchInTime:int = obj["LunchInTime"]
      """   Clock In time from Lunch break that is used for costing/payroll determination. Created by adjusting the ActLunchInTime.
The adjusted time is where the system time is rolled forward to the JCShift.LunchEnd time when the employee clocks in from lunch before the lunch period ends. 
Stored as Hours.Hundreths.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """  The clockOut in time to be considered for payroll and costing purposes as the time when the employee stops work. ClockOut time is stored as Hours.Hundreths. It is defaulted using the ActualClockOut value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockOut" is after the shift end time (JCShift.End) and before ( JCShift.End + JC.Syst.Grace) then the system adjusts the ClockOut time to be the end of the shift. Else it will be set to the actual system time.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ActualClockOutTime:int = obj["ActualClockOutTime"]
      """  Actual clock Out time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocks out.  In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.EndTime. Stored as Hours.Hundreths.  """  
      self.PayHours:int = obj["PayHours"]
      """   Hours for payroll.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5. This is calculated when the Start/Stop times are changed in labor entry. It can then be overridden.
The Logic for calculating hours from clockin, clockout is:
If ClockIn > ClockOut Gross Hours = ( (ClockOut + 24.00) - ClockIn) else Gross Hours = ClockOut - ClockIn. 
If LunchOut > LunchIn Lunch Hours = ( (LunchIn +24) - LunchOut )
else Lunch Hours = ( LunchIn - LunchOut ).
PayHours = GRoss Hours - Lunch Hours. 
Remember that the database clockin/clockout fields are stored as hours hundredths, while the entry widgets are either hours.hundreths or Hours:Minutes. So use the database fields in this calculation and there is no need to worry about conversions.  """  
      self.FeedPayroll:bool = obj["FeedPayroll"]
      """  Flag that indicates this labor transaction is eligible for transfer to DCD payroll application. The default is set from JCSyst.FeedPayroll.  """  
      self.TransferredToPayroll:bool = obj["TransferredToPayroll"]
      """  Indicates if this transaction has been transferred to payroll. This is updated via the Payroll function to transfer labor.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.TranSet:str = obj["TranSet"]
      """  An optional field where the user enters a string of characters that would be used to associate multiple transactions as being part of a transaction set. TranSet will be used for data selection type functions.  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborHed record is currently active. When the employee clocks out it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice, displaying which employees are clocked in and which ones have not clocked out. Labor entry can't access a record that is Open.  """  
      self.ChkLink:str = obj["ChkLink"]
      """   Encoded value PRChkDtl.HeadNum + PRChkDtl.LineNum.
Used to relate the labor to the payroll check detail.  """  
      self.BatchTotalHrsDisp:str = obj["BatchTotalHrsDisp"]
      """  BatchTotalHrsDisp  """  
      self.BatchHrsRemainDisp:str = obj["BatchHrsRemainDisp"]
      """  BatchHrsRemainDisp  """  
      self.BatchHrsRemainPctDisp:str = obj["BatchHrsRemainPctDisp"]
      """  BatchHrsRemainPctDisp  """  
      self.BatchSplitHrsMethod:str = obj["BatchSplitHrsMethod"]
      """  BatchSplitHrsMethod  """  
      self.BatchAssignTo:bool = obj["BatchAssignTo"]
      """  BatchAssignTo  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchStartHrs:str = obj["BatchStartHrs"]
      """  BatchStartHrs  """  
      self.BatchEndHrs:str = obj["BatchEndHrs"]
      """  BatchEndHrs  """  
      self.BatchTotalHrs:int = obj["BatchTotalHrs"]
      """  BatchTotalHrs  """  
      self.BatchHrsRemain:int = obj["BatchHrsRemain"]
      """  BatchHrsRemain  """  
      self.BatchHrsRemainPct:int = obj["BatchHrsRemainPct"]
      """  BatchHrsRemainPct  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.HCMPayHoursCalcType:str = obj["HCMPayHoursCalcType"]
      """  Indicates which type of Pay time calculation will be used when HCM Integration is on.  """  
      self.EmpBasicShift:int = obj["EmpBasicShift"]
      """  Normal work shift from EmpBasic  """  
      self.EmpBasicSupervisorID:str = obj["EmpBasicSupervisorID"]
      """  The ID of the supervisor for the employee  """  
      self.GetNewNoHdr:bool = obj["GetNewNoHdr"]
      self.HCMTotPayHours:int = obj["HCMTotPayHours"]
      """  HCM Integration, Display the Total of Pay Hours of the Labor Details.  """  
      self.ImagePath:str = obj["ImagePath"]
      """  Full Path of Employee PhotoFile  """  
      self.LunchBreak:bool = obj["LunchBreak"]
      """  Indicates if a lunch break is part of the shift  """  
      self.MES:bool = obj["MES"]
      self.PayrollValuesForHCM:str = obj["PayrollValuesForHCM"]
      """  Temporal field that stores patch field value: HDR, DTL, NON  """  
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TotBurHrs:int = obj["TotBurHrs"]
      self.TotLbrHrs:int = obj["TotLbrHrs"]
      self.WipPosted:bool = obj["WipPosted"]
      self.DspPayHours:int = obj["DspPayHours"]
      """  For display purposes  """  
      self.FullyPosted:bool = obj["FullyPosted"]
      """  Indicates if all labor has been posted  """  
      self.PartiallyPosted:bool = obj["PartiallyPosted"]
      """  Indicates if some labor has been posted  """  
      self.HCMExistsWithStatus:bool = obj["HCMExistsWithStatus"]
      self.PayrollDateNav:str = obj["PayrollDateNav"]
      """  Payroll date for record navigation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmployeeNumFirstName:str = obj["EmployeeNumFirstName"]
      self.EmployeeNumName:str = obj["EmployeeNumName"]
      self.EmployeeNumLastName:str = obj["EmployeeNumLastName"]
      self.HCMStatusStatus:str = obj["HCMStatusStatus"]
      self.PRSystHCMEnabled:bool = obj["PRSystHCMEnabled"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of the manufactured item that the quantity is for. Must be defined on the Job in the JobPart table.  """  
      self.PartQty:int = obj["PartQty"]
      """  The number of individual parts completed on this labor transaction. Updates the JobPart.QtyCompleted.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """  Discrepant Reason Code  """  
      self.DiscrpAttributeSetID:int = obj["DiscrpAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  The reported scrap quantity.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  Scrap Reason Code  """  
      self.ScrapAttributeSetID:int = obj["ScrapAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  """  
      self.NonConfTranID:int = obj["NonConfTranID"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.LaborAttributeSetID:int = obj["LaborAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the PartQty  """  
      self.MESProcessing:bool = obj["MESProcessing"]
      """  UI Sets this to true when processing from MES Labor Entry.  The BL uses this to determine if PartWip/MtlQueue logic should be performed.  """  
      self.RequestMove:bool = obj["RequestMove"]
      self.PartUOM:str = obj["PartUOM"]
      """  Unit of Measure for the Part defined on the Operation  """  
      self.PartDescription:str = obj["PartDescription"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.DiscrepUOM:str = obj["DiscrepUOM"]
      """  Unit of Measure used for DiscrepQty  """  
      self.ScrapUOM:str = obj["ScrapUOM"]
      """  Unit of Measure used for ScrapQty.  """  
      self.DiscrepAttributeSetDescription:str = obj["DiscrepAttributeSetDescription"]
      """  The Full Description of the Attribute Set for DiscrepQty  """  
      self.DiscrepAttributeSetShortDescription:str = obj["DiscrepAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for DiscrepQty  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.LaborAttributeSetDescription:str = obj["LaborAttributeSetDescription"]
      """  The Full Description of the Attribute Set for PartQty  """  
      self.LaborAttributeSetShortDescription:str = obj["LaborAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for PartQty  """  
      self.ScrapAttributeSetDescription:str = obj["ScrapAttributeSetDescription"]
      """  The Full Description of the Attribute Set for ScrapQty  """  
      self.ScrapAttributeSetShortDescription:str = obj["ScrapAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for ScrapQty  """  
      self.DiscrepRevision:str = obj["DiscrepRevision"]
      """  Revision for DiscrepQty  """  
      self.ScrapRevision:str = obj["ScrapRevision"]
      """  Revision for ScrapQty  """  
      self.EnableDiscrpQty:bool = obj["EnableDiscrpQty"]
      """  Allow input of discrepant (nonconformance) quantity  """  
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      """  Allow input of scrap quantity  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DiscrpRsnDescription:str = obj["DiscrpRsnDescription"]
      self.ScrapReasonDescription:str = obj["ScrapReasonDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LbrScrapSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial Number  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq this scrap serial number is for  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq this scrap serial number is for  """  
      self.EnableStatus:bool = obj["EnableStatus"]
      """  Indicates whether the Status field can be updated.  """  
      self.SNStatus:str = obj["SNStatus"]
      """  New status for the serial number. This field will require Code/Desc definition: REJECTED`Scrap INSPECTION`Nonconformance WIP`WIP  """  
      self.SNStatusDesc:str = obj["SNStatusDesc"]
      """  The SNStatus description ? set same as SerialNo.SNStatusTrans  """  
      self.Selected:bool = obj["Selected"]
      """  Serial Number Selected for process  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat1:str = obj["SNFormat1"]
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TimeWeeklyViewRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmployeeNum:str = obj["EmployeeNum"]
      self.WeekBeginDate:str = obj["WeekBeginDate"]
      self.WeekEndDate:str = obj["WeekEndDate"]
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.LaborType:str = obj["LaborType"]
      self.ProjectID:str = obj["ProjectID"]
      self.PhaseID:str = obj["PhaseID"]
      self.TimeTypCd:str = obj["TimeTypCd"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.RoleCd:str = obj["RoleCd"]
      self.IndirectCode:str = obj["IndirectCode"]
      self.HoursSun:int = obj["HoursSun"]
      self.HoursMon:int = obj["HoursMon"]
      self.HoursTue:int = obj["HoursTue"]
      self.HoursWed:int = obj["HoursWed"]
      self.HoursThu:int = obj["HoursThu"]
      self.HoursFri:int = obj["HoursFri"]
      self.HoursSat:int = obj["HoursSat"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.RoleCdDescription:str = obj["RoleCdDescription"]
      self.IndirectCodeDescription:str = obj["IndirectCodeDescription"]
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      self.HoursTotal:int = obj["HoursTotal"]
      self.ExpenseCode:str = obj["ExpenseCode"]
      self.Complete:bool = obj["Complete"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.ResourceID:str = obj["ResourceID"]
      self.OpCode:str = obj["OpCode"]
      self.OpComplete:bool = obj["OpComplete"]
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      self.LaborRate:int = obj["LaborRate"]
      self.ResourceGrpIDDescription:str = obj["ResourceGrpIDDescription"]
      self.JCDept:str = obj["JCDept"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      self.Shift:int = obj["Shift"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.MessageText:str = obj["MessageText"]
      self.NewRowType:str = obj["NewRowType"]
      """  Valid values are "A" for an Add of a new TimeWeeklyView row and "C" for a Copy of an existing TimeWeeklyView row.  """  
      self.DisPrjRoleCd:bool = obj["DisPrjRoleCd"]
      self.DisTimeTypCd:bool = obj["DisTimeTypCd"]
      self.DisLaborType:bool = obj["DisLaborType"]
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if submit is available  """  
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy function is available  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if recall is available  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.TimeStatus:str = obj["TimeStatus"]
      self.ProjDesc:str = obj["ProjDesc"]
      self.WBSPhaseDesc:str = obj["WBSPhaseDesc"]
      """  WBS Phase Project Description  """  
      self.OperDesc:str = obj["OperDesc"]
      """  Operation Description  """  
      self.ASMdesc:str = obj["ASMdesc"]
      """  Job Assembly description  """  
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """   If the Time is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  """  
      self.DeleteRow:bool = obj["DeleteRow"]
      self.HCMTotWeeklyPayHours:int = obj["HCMTotWeeklyPayHours"]
      """  HCM Integration Total Weekly Pay Hours  """  
      self.RoleCdList:str = obj["RoleCdList"]
      """  List of avaialble role codes  """  
      self.RowSelected:bool = obj["RowSelected"]
      """  Indicates if the row is selected for submit, recall, or copy.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TimeWorkHoursRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CalendarID:str = obj["CalendarID"]
      self.WeekBeginDate:str = obj["WeekBeginDate"]
      self.WeekEndDate:str = obj["WeekEndDate"]
      self.SunDisplayDate:str = obj["SunDisplayDate"]
      self.MonDisplayDate:str = obj["MonDisplayDate"]
      self.TueDisplayDate:str = obj["TueDisplayDate"]
      self.WedDisplayDate:str = obj["WedDisplayDate"]
      self.ThuDisplayDate:str = obj["ThuDisplayDate"]
      self.FriDisplayDate:str = obj["FriDisplayDate"]
      self.SatDisplayDate:str = obj["SatDisplayDate"]
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.SunWorkHours:int = obj["SunWorkHours"]
      self.MonWorkHours:int = obj["MonWorkHours"]
      self.TueWorkHours:int = obj["TueWorkHours"]
      self.WedWorkHours:int = obj["WedWorkHours"]
      self.ThuWorkHours:int = obj["ThuWorkHours"]
      self.FriWorkHours:int = obj["FriWorkHours"]
      self.SatWorkHours:int = obj["SatWorkHours"]
      self.SunBookedHours:int = obj["SunBookedHours"]
      self.MonBookedHours:int = obj["MonBookedHours"]
      self.WedBookedHours:int = obj["WedBookedHours"]
      self.ThuBookedHours:int = obj["ThuBookedHours"]
      self.FriBookedHours:int = obj["FriBookedHours"]
      self.SunDiffHours:int = obj["SunDiffHours"]
      self.MonDiffHours:int = obj["MonDiffHours"]
      self.SatBookedHours:int = obj["SatBookedHours"]
      self.TueBookedHours:int = obj["TueBookedHours"]
      self.TueDiffHours:int = obj["TueDiffHours"]
      self.WedDiffHours:int = obj["WedDiffHours"]
      self.ThuDiffHours:int = obj["ThuDiffHours"]
      self.FriDiffHours:int = obj["FriDiffHours"]
      self.SatDiffHours:int = obj["SatDiffHours"]
      self.EmployeeNum:str = obj["EmployeeNum"]
      self.CalendarDescription:str = obj["CalendarDescription"]
      self.TotalWorkHours:int = obj["TotalWorkHours"]
      self.TotalBookedHours:int = obj["TotalBookedHours"]
      self.TotalDiffHours:int = obj["TotalDiffHours"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AfterChangeLaborDtlDiscrepQty_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class AfterChangeLaborDtlDiscrepQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class AfterChangeLaborPartDiscrepQty_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class AfterChangeLaborPartDiscrepQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildJobOperPrjRoleList_input:
   """ Required : 
   ipJobNum
   ipAssemblySeq
   ipOprSeq
   ipEmpID
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  JobNum  """  
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      """  AssemblySeq  """  
      self.ipOprSeq:int = obj["ipOprSeq"]
      """  OprSeq  """  
      self.ipEmpID:str = obj["ipEmpID"]
      """  EmpID  """  
      pass

class BuildJobOperPrjRoleList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.whereClause:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeEquipID_input:
   """ Required : 
   equipID
   ds
   """  
   def __init__(self, obj):
      self.equipID:str = obj["equipID"]
      """  equipID  """  
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class ChangeEquipID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeIndirectCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class ChangeIndirectCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLaborDtlAttributeSetID_input:
   """ Required : 
   ds
   attributeSetID
   type
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.attributeSetID:int = obj["attributeSetID"]
      """  Proposed change to ScrapQty field  """  
      self.type:str = obj["type"]
      """  Discrep, Scrap or Labor  """  
      pass

class ChangeLaborDtlAttributeSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLaborDtlDspTimeField_input:
   """ Required : 
   fieldName
   timeValue
   ds
   """  
   def __init__(self, obj):
      self.fieldName:str = obj["fieldName"]
      """  The name of the field that is changing  """  
      self.timeValue:str = obj["timeValue"]
      """  The new time value  """  
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class ChangeLaborDtlDspTimeField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLaborDtlOprSeq_input:
   """ Required : 
   ds
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.oprSeq:int = obj["oprSeq"]
      """  Proposed oprSeq change  """  
      pass

class ChangeLaborDtlOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeLaborDtlScrapQty_input:
   """ Required : 
   ds
   scrapQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.scrapQty:int = obj["scrapQty"]
      """  Proposed change to ScrapQty field  """  
      pass

class ChangeLaborDtlScrapQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLaborDtlTimeField_input:
   """ Required : 
   fieldName
   timeValue
   ds
   """  
   def __init__(self, obj):
      self.fieldName:str = obj["fieldName"]
      """  The name of the field that is changing  """  
      self.timeValue:int = obj["timeValue"]
      """  The new time value  """  
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class ChangeLaborDtlTimeField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLaborPartAttributeSetID_input:
   """ Required : 
   ds
   attributeSetID
   type
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.attributeSetID:int = obj["attributeSetID"]
      """  Proposed change to ScrapQty field  """  
      self.type:str = obj["type"]
      """  Discrep, Scrap or Labor  """  
      pass

class ChangeLaborPartAttributeSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLaborType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class ChangeLaborType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeResourceId_input:
   """ Required : 
   ds
   pcResourceID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.pcResourceID:str = obj["pcResourceID"]
      """  The ID of the machine that was used to do the work.  """  
      pass

class ChangeResourceId_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeTimeWeeklyViewWeekBeginDate_input:
   """ Required : 
   ds
   weekBeginDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.weekBeginDate:str = obj["weekBeginDate"]
      """  Proposed week begin date  """  
      pass

class ChangeTimeWeeklyViewWeekBeginDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckEmployeeActivity_input:
   """ Required : 
   ipEmpID
   ipLaborHedSeq
   ipJobNum
   ipAsmSeq
   ipOprSeq
   ipResourceID
   """  
   def __init__(self, obj):
      self.ipEmpID:str = obj["ipEmpID"]
      """  The current Employee ID  """  
      self.ipLaborHedSeq:int = obj["ipLaborHedSeq"]
      """  LaborHed Sequence  """  
      self.ipJobNum:str = obj["ipJobNum"]
      """  Job Number  """  
      self.ipAsmSeq:int = obj["ipAsmSeq"]
      """  Assembly Sequence  """  
      self.ipOprSeq:int = obj["ipOprSeq"]
      """  Operation Sequence  """  
      self.ipResourceID:str = obj["ipResourceID"]
      """  Resource ID  """  
      pass

class CheckEmployeeActivity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckFirstArticleWarning_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class CheckFirstArticleWarning_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckInspResults_input:
   """ Required : 
   ipJobNum
   ipAssemblySeq
   ipOprSeq
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  Current Job  """  
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      """  Current AssembleSeq  """  
      self.ipOprSeq:int = obj["ipOprSeq"]
      """  Current OprSeq  """  
      pass

class CheckInspResults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inspectionOK:bool = obj["inspectionOK"]
      pass

      """  output parameters  """  

class CheckNonConformance_input:
   """ Required : 
   jobNum
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  JobNumber  """  
      self.laborHedSeq:int = obj["laborHedSeq"]
      """  LaborHedSeq  """  
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      """  LaborDtlSeq  """  
      pass

class CheckNonConformance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckResourceGroup_input:
   """ Required : 
   ds
   ProposedResourceID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ProposedResourceID:str = obj["ProposedResourceID"]
      """  Proposed Resource ID  """  
      pass

class CheckResourceGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckResourceId_input:
   """ Required : 
   resourceGrpId
   proposedResId
   """  
   def __init__(self, obj):
      self.resourceGrpId:str = obj["resourceGrpId"]
      """  Resource Group of the Job  """  
      self.proposedResId:str = obj["proposedResId"]
      """  Proposed Resource ID to assign.  """  
      pass

class CheckResourceId_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckWarnings_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class CheckWarnings_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CopyLaborDetail_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class CopyLaborDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CopyLaborDtlBySelected_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class CopyLaborDtlBySelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.messageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CopyTimeWeeklyViewBySelected_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class CopyTimeWeeklyViewBySelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.messageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CopyTimeWeeklyView_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class CopyTimeWeeklyView_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CreateLbrScrapSerialNumbersFromList_input:
   """ Required : 
   serialNumberList
   partNumList
   ds
   """  
   def __init__(self, obj):
      self.serialNumberList:str = obj["serialNumberList"]
      """  Serial Number List  """  
      self.partNumList:str = obj["partNumList"]
      """  Part Number List  """  
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class CreateLbrScrapSerialNumbersFromList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultAssemblySeq_input:
   """ Required : 
   ds
   assemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.assemblySeq:int = obj["assemblySeq"]
      """  Proposed AssemblySeq change  """  
      pass

class DefaultAssemblySeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultComplete_input:
   """ Required : 
   ds
   cmplete
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.cmplete:bool = obj["cmplete"]
      """  Proposed change to the Complete field  """  
      pass

class DefaultComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DefaultDate_input:
   """ Required : 
   ds
   payrollDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.payrollDate:str = obj["payrollDate"]
      """  Proposed Payroll Date change  """  
      pass

class DefaultDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultDiscrpRsnCode_input:
   """ Required : 
   ds
   ProposedDiscrpRsnCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ProposedDiscrpRsnCode:str = obj["ProposedDiscrpRsnCode"]
      """  Proposed discrepancy reason  """  
      pass

class DefaultDiscrpRsnCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultDtlTime_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class DefaultDtlTime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultIndirect_input:
   """ Required : 
   ds
   indirectCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.indirectCode:str = obj["indirectCode"]
      """  Proposed change to the indirect code  """  
      pass

class DefaultIndirect_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultJobNum_input:
   """ Required : 
   ds
   jobNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      """  Proposed change to the JobNum field  """  
      pass

class DefaultJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultLaborHrs_input:
   """ Required : 
   ds
   laborHrs
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.laborHrs:int = obj["laborHrs"]
      """  Proposed Labor Hrs change  """  
      pass

class DefaultLaborHrs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultLaborQty_input:
   """ Required : 
   ds
   laborQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.laborQty:int = obj["laborQty"]
      """  Proposed change to LaborQty field  """  
      pass

class DefaultLaborQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DefaultLaborType_input:
   """ Required : 
   ds
   ipLaborType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ipLaborType:str = obj["ipLaborType"]
      """  Proposed LaborType change  """  
      pass

class DefaultLaborType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultLunchBreak_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class DefaultLunchBreak_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultNextOprSeq_input:
   """ Required : 
   ds
   ProposedNextOprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ProposedNextOprSeq:int = obj["ProposedNextOprSeq"]
      """  Proposed next operation sequence  """  
      pass

class DefaultNextOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultNonConformanceQty_input:
   """ Required : 
   ds
   nonConformanceQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.nonConformanceQty:int = obj["nonConformanceQty"]
      """  Proposed change to LaborQty field  """  
      pass

class DefaultNonConformanceQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultOpCode_input:
   """ Required : 
   ds
   opCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.opCode:str = obj["opCode"]
      """  Proposed OpCode field change  """  
      pass

class DefaultOpCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DefaultOprSeq_input:
   """ Required : 
   ds
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.oprSeq:int = obj["oprSeq"]
      """  Proposed oprSeq change  """  
      pass

class DefaultOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DefaultPhaseID_input:
   """ Required : 
   ds
   ipPhaseID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ipPhaseID:str = obj["ipPhaseID"]
      """  Proposed PhaseID change  """  
      pass

class DefaultPhaseID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultPhaseOprSeq_input:
   """ Required : 
   ds
   ipPhaseOprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ipPhaseOprSeq:int = obj["ipPhaseOprSeq"]
      """  Proposed PhaseOprSeq change  """  
      pass

class DefaultPhaseOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DefaultProjectID_input:
   """ Required : 
   ds
   ipProjectID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ipProjectID:str = obj["ipProjectID"]
      """  Proposed ProjectID change  """  
      pass

class DefaultProjectID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultResourceID_input:
   """ Required : 
   ds
   ProposedResourceID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ProposedResourceID:str = obj["ProposedResourceID"]
      """  The proposed resource id  """  
      pass

class DefaultResourceID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultReworkReasonCode_input:
   """ Required : 
   ds
   ProposedReworkReasonCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ProposedReworkReasonCode:str = obj["ProposedReworkReasonCode"]
      """  Proposed discrepancy reason  """  
      pass

class DefaultReworkReasonCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultRoleCd_input:
   """ Required : 
   ds
   ipRoleCd
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ipRoleCd:str = obj["ipRoleCd"]
      """  Proposed RoleCd change  """  
      pass

class DefaultRoleCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultScrapReasonCode_input:
   """ Required : 
   ds
   ProposedScrapReasonCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ProposedScrapReasonCode:str = obj["ProposedScrapReasonCode"]
      """  Proposed scrap reason  """  
      pass

class DefaultScrapReasonCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DefaultSetupPctComplete_input:
   """ Required : 
   ds
   PercentComplete
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.PercentComplete:int = obj["PercentComplete"]
      """  Proposed percent complete  """  
      pass

class DefaultSetupPctComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultShift_input:
   """ Required : 
   ds
   shift
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.shift:int = obj["shift"]
      """  Proposed Shift field change  """  
      pass

class DefaultShift_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultTimeTypCd_input:
   """ Required : 
   ds
   ipTimeTypCd
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ipTimeTypCd:str = obj["ipTimeTypCd"]
      """  Proposed TimeTypCd change  """  
      pass

class DefaultTimeTypCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DefaultTime_input:
   """ Required : 
   ds
   cFieldName
   timeValue
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.cFieldName:str = obj["cFieldName"]
      """  name of field being changed  """  
      self.timeValue:int = obj["timeValue"]
      """  proposed time change  """  
      pass

class DefaultTime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultWCCode_input:
   """ Required : 
   ds
   wcCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.wcCode:str = obj["wcCode"]
      """  Proposed WorkCenter Code change  """  
      pass

class DefaultWCCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   laborHedSeq
   """  
   def __init__(self, obj):
      self.laborHedSeq:int = obj["laborHedSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteLaborDtl_input:
   """ Required : 
   LaborHedSeq
   LaborDtlSeq
   CallFrom
   """  
   def __init__(self, obj):
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq  """  
      self.CallFrom:str = obj["CallFrom"]
      """  Proposed value to filter logic for HCM  """  
      pass

class DeleteLaborDtl_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class EndActivityComplete_input:
   """ Required : 
   ds
   cmplete
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.cmplete:bool = obj["cmplete"]
      """  Proposed change to the Complete field  """  
      pass

class EndActivityComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class EndActivity_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class EndActivity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class EndDowntime_input:
   """ Required : 
   employeeNum
   """  
   def __init__(self, obj):
      self.employeeNum:str = obj["employeeNum"]
      """  Employee Number  """  
      pass

class EndDowntime_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_HCMLaborDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.JCDept:str = obj["JCDept"]
      """  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  """  
      self.LaborNote:str = obj["LaborNote"]
      """  A short note that the user can make about the labor transaction.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PayHours:int = obj["PayHours"]
      self.HCMEnabledAt:str = obj["HCMEnabledAt"]
      """  String value which contains the values for the HCM Integration, HDR (Header) DTL (Detail). Those values help to know the source of the payHours.  """  
      self.Status:str = obj["Status"]
      """  Sent (S) = Submitted to HCM  Received (R) = Received from HCM  Error (E) = Error Submitting to HCM In Progress (IP) = In Progress  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HCMLaborDtlSyncRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LaborDtlSysRowID:str = obj["LaborDtlSysRowID"]
      """  Field to Link the SysRowID with HCMLaborDtlSync record.  """  
      self.Status:str = obj["Status"]
      """  Sent (S) = Submitted to HCM  Received (R) = Received from HCM  Error (E) = Error Submitting to HCM In Progress (IP) = In Progress  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.LaborSource:str = obj["LaborSource"]
      """  String value which indicates if the status should be applied to the header or the detail (HDR/DTL)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HCMLaborDtlTableset:
   def __init__(self, obj):
      self.HCMLaborDtl:list[Erp_Tablesets_HCMLaborDtlRow] = obj["HCMLaborDtl"]
      self.HCMLaborDtlSync:list[Erp_Tablesets_HCMLaborDtlSyncRow] = obj["HCMLaborDtlSync"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LaborDtlActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionDesc:str = obj["ActionDesc"]
      """  Description of Action.  """  
      self.Required:bool = obj["Required"]
      """  Indicated if this Action must be completed before Operation can be completed.  """  
      self.Completed:bool = obj["Completed"]
      """  Indicates if this Action was completed.  """  
      self.CompletedBy:str = obj["CompletedBy"]
      """  The number of the employee that performed the work.  """  
      self.CompletedOn:str = obj["CompletedOn"]
      """  Date the Action was completed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlCommentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  The unique identifier of the Labor Header the comment relates to.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.CommentNum:int = obj["CommentNum"]
      """  Internal identifier of the comment record.  Used in conjunction with EmpTimeNum to make the record unique.  """  
      self.CommentType:str = obj["CommentType"]
      """   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  The identifier of the Task record the comment is related to.  Can be zero, which indicates the comment is not related to a specific task.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.TimeEntryCommentTypeList:str = obj["TimeEntryCommentTypeList"]
      """  List of valid comment types for Time Entry  """  
      self.CommentTypeDesc:str = obj["CommentTypeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are

concurrently active for an employee in order to distribute the labor hours.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the expense.  Can be used to expenses together, for example, all expenses incurred on the same trip can be assigned the same reference.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LaborType:str = obj["LaborType"]
      """   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.ReWork:bool = obj["ReWork"]
      """  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  """  
      self.ReworkReasonCode:str = obj["ReworkReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  """  
      self.OprSeq:int = obj["OprSeq"]
      """   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  """  
      self.JCDept:str = obj["JCDept"]
      """  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  """  
      self.OpCode:str = obj["OpCode"]
      """  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  """  
      self.BurdenHrs:int = obj["BurdenHrs"]
      """  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  """  
      self.LaborQty:int = obj["LaborQty"]
      """  The Total production quantity reported.  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  The reported scrap quantity.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates if this transaction "completes" either the setup or production for this operation.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  """  
      self.LaborNote:str = obj["LaborNote"]
      """  A short note that the user can make about the labor transaction.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.AppliedToSchedule:bool = obj["AppliedToSchedule"]
      """  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  """  
      self.ClockInMInute:int = obj["ClockInMInute"]
      """  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  """  
      self.ClockOutMinute:int = obj["ClockOutMinute"]
      """  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  """  
      self.ClockinTime:int = obj["ClockinTime"]
      """   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  """  
      self.OverRidePayRate:int = obj["OverRidePayRate"]
      """  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  """  
      self.BurdenRate:int = obj["BurdenRate"]
      """  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.OpComplete:bool = obj["OpComplete"]
      """  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  """  
      self.EarnedHrs:int = obj["EarnedHrs"]
      """  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  """  
      self.AddedOper:bool = obj["AddedOper"]
      """  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  Indicates if the labordtl record inspection has completed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this service record belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The line number of the service call this labor detail is for.  """  
      self.ServNum:int = obj["ServNum"]
      """  the service that is being performed on this line.  """  
      self.ServCode:str = obj["ServCode"]
      """  A unique code that identifies the Service  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.WipPosted:bool = obj["WipPosted"]
      """  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  """  
      self.ParentLaborDtlSeq:int = obj["ParentLaborDtlSeq"]
      """  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BFLaborReq:bool = obj["BFLaborReq"]
      """  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID,used in PostingEngine  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Project Role Code  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  Time Type Code  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  The Project Billing Invoice Number where these charges were processed.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the time.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the time received final approval.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  """  
      self.TimeStatus:str = obj["TimeStatus"]
      """   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CreatedViaTEWeekView:bool = obj["CreatedViaTEWeekView"]
      """  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The User ID of the submitter.  """  
      self.PBRateFrom:str = obj["PBRateFrom"]
      """  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  """  
      self.PBCurrencyCode:str = obj["PBCurrencyCode"]
      """  Project Billing calculation in COSandWIP: Currency code is got from Project  """  
      self.PBHours:int = obj["PBHours"]
      """  Project Billing calculation in COSandWIP: Hours used for charge  """  
      self.PBChargeRate:int = obj["PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  """  
      self.PBChargeAmt:int = obj["PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  """  
      self.DocPBChargeRate:int = obj["DocPBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  """  
      self.Rpt1PBChargeRate:int = obj["Rpt1PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt2PBChargeRate:int = obj["Rpt2PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt3PBChargeRate:int = obj["Rpt3PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.DocPBChargeAmt:int = obj["DocPBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  """  
      self.Rpt1PBChargeAmt:int = obj["Rpt1PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt2PBChargeAmt:int = obj["Rpt2PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt3PBChargeAmt:int = obj["Rpt3PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ActID:int = obj["ActID"]
      """  Links to PActDtl.ActID  """  
      self.DtailID:int = obj["DtailID"]
      """  System assigned unique id number for the detail. Links to PActDtl.DetailID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used By Project Analysis Process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process.  """  
      self.JDFInputFiles:str = obj["JDFInputFiles"]
      """  JDFInputFiles  """  
      self.JDFNumberOfPages:str = obj["JDFNumberOfPages"]
      """  JDFNumberOfPages  """  
      self.BatchWasSaved:str = obj["BatchWasSaved"]
      """  BatchWasSaved  """  
      self.AssignToBatch:bool = obj["AssignToBatch"]
      """  AssignToBatch  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchRequestMove:bool = obj["BatchRequestMove"]
      """  BatchRequestMove  """  
      self.BatchPrint:bool = obj["BatchPrint"]
      """  BatchPrint  """  
      self.BatchLaborHrs:int = obj["BatchLaborHrs"]
      """  BatchLaborHrs  """  
      self.BatchPctOfTotHrs:int = obj["BatchPctOfTotHrs"]
      """  BatchPctOfTotHrs  """  
      self.BatchQty:int = obj["BatchQty"]
      """  BatchQty  """  
      self.BatchTotalExpectedHrs:int = obj["BatchTotalExpectedHrs"]
      """  BatchTotalExpectedHrs  """  
      self.JDFOpCompleted:str = obj["JDFOpCompleted"]
      """  JDFOpCompleted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Downtime:bool = obj["Downtime"]
      """  Downtime  """  
      self.RefJobNum:str = obj["RefJobNum"]
      """  RefJobNum  """  
      self.RefAssemblySeq:int = obj["RefAssemblySeq"]
      """  RefAssemblySeq  """  
      self.RefOprSeq:int = obj["RefOprSeq"]
      """  RefOprSeq  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.BillServiceRate:int = obj["BillServiceRate"]
      """  BillServiceRate  """  
      self.HCMPayHours:int = obj["HCMPayHours"]
      """  Pay Hours used for HCM  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.DiscrepAttributeSetID:int = obj["DiscrepAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  """  
      self.LaborAttributeSetID:int = obj["LaborAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the Labor Qty  """  
      self.ScrapAttributeSetID:int = obj["ScrapAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.NonConfPCID:str = obj["NonConfPCID"]
      """  NonConfPCID  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.ApprovalPhaseDesc:str = obj["ApprovalPhaseDesc"]
      """  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalPhaseID:str = obj["ApprovalPhaseID"]
      """  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectDesc:str = obj["ApprovalProjectDesc"]
      """  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectID:str = obj["ApprovalProjectID"]
      """  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      self.ApprvrHasOpenTask:bool = obj["ApprvrHasOpenTask"]
      """  Used in approval entry.  Indicates if the approver has an open task or not.  """  
      self.BaseCurrCodeDesc:str = obj["BaseCurrCodeDesc"]
      """  Company Base currency code description for display in LaborDtl grid.  """  
      self.BurdenCost:int = obj["BurdenCost"]
      """  calculated field: BurdenHrs * BurdenRate  """  
      self.CallCode:str = obj["CallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.CapabilityDescription:str = obj["CapabilityDescription"]
      self.CapabilityID:str = obj["CapabilityID"]
      self.ChargeRate:int = obj["ChargeRate"]
      """  Charge rate calculated for Time and Expense approval  """  
      self.ChargeRateSRC:str = obj["ChargeRateSRC"]
      """  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  """  
      self.ChgRateCurrDesc:str = obj["ChgRateCurrDesc"]
      """  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  """  
      self.CompleteFlag:bool = obj["CompleteFlag"]
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.DiscrepUOM:str = obj["DiscrepUOM"]
      """  Unit of Measure used for DiscrepQty  """  
      self.DisLaborType:bool = obj["DisLaborType"]
      """  Field that indicates if field DisLaborTypeshould be disabled.  """  
      self.DisplayJob:str = obj["DisplayJob"]
      self.DisPrjRoleCd:bool = obj["DisPrjRoleCd"]
      """  Field that indicates if field PrjRoleCd should be disabled.  """  
      self.DisTimeTypCd:bool = obj["DisTimeTypCd"]
      """  Field that indicates if field TimeTypCd should be disabled.  """  
      self.DowntimeTotal:int = obj["DowntimeTotal"]
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.DspTotHours:str = obj["DspTotHours"]
      self.DtClockIn:str = obj["DtClockIn"]
      self.DtClockOut:str = obj["DtClockOut"]
      self.EfficiencyPercentage:int = obj["EfficiencyPercentage"]
      """  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  Labor Detail Employee Name  """  
      self.EnableComplete:bool = obj["EnableComplete"]
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.EnableDiscrepQty:bool = obj["EnableDiscrepQty"]
      self.EnableInspection:bool = obj["EnableInspection"]
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.EnableNextOprSeq:bool = obj["EnableNextOprSeq"]
      self.EnablePrintTagsList:bool = obj["EnablePrintTagsList"]
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available for an approver  """  
      self.EnableRequestMove:bool = obj["EnableRequestMove"]
      self.EnableResourceGrpID:bool = obj["EnableResourceGrpID"]
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Enable the SN Button?  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.EndActivity:bool = obj["EndActivity"]
      self.EnteredOnCurPlant:bool = obj["EnteredOnCurPlant"]
      """  To know if the LaborDtl was created on the current plant  """  
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.FSComplete:bool = obj["FSComplete"]
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.HasAccessToRow:bool = obj["HasAccessToRow"]
      """  Indicates if the user has access to the row  """  
      self.HasComments:bool = obj["HasComments"]
      """  Indicates if the labor detail has comments  """  
      self.HH:bool = obj["HH"]
      """  To tell the bo that this transaction was being modified from HH.  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.ISFixHourAndQtyOnly:bool = obj["ISFixHourAndQtyOnly"]
      """  Indicates if the job operation is marked as fixed hours and quantity only.  """  
      self.JCSystReworkReasons:bool = obj["JCSystReworkReasons"]
      self.JCSystScrapReasons:bool = obj["JCSystScrapReasons"]
      self.JobOperComplete:bool = obj["JobOperComplete"]
      self.JobType:str = obj["JobType"]
      self.JobTypeCode:str = obj["JobTypeCode"]
      """  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  """  
      self.LaborCost:int = obj["LaborCost"]
      """  calculated field: LaborHrs * LaborRate  """  
      self.LaborUOM:str = obj["LaborUOM"]
      """  Unit of Measure used for LaborQty  """  
      self.LbrDay:str = obj["LbrDay"]
      """  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrMonth:str = obj["LbrMonth"]
      """  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrWeek:str = obj["LbrWeek"]
      """  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  """  
      self.MES:bool = obj["MES"]
      self.MultipleEmployeesText:str = obj["MultipleEmployeesText"]
      self.NewDifDateFlag:int = obj["NewDifDateFlag"]
      self.NewPrjRoleCd:str = obj["NewPrjRoleCd"]
      """  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  """  
      self.NewRoleCdDesc:str = obj["NewRoleCdDesc"]
      """  Holds the description for NewPrjRoleCd  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      self.NextOperDesc:str = obj["NextOperDesc"]
      self.NextOprSeq:int = obj["NextOprSeq"]
      self.NextResourceDesc:str = obj["NextResourceDesc"]
      self.NonConfProcessed:bool = obj["NonConfProcessed"]
      """  To evaluate if the NonComformance has been already processed in inspection and no changes can be applied on LaborDtl then.  """  
      self.NotSubmitted:bool = obj["NotSubmitted"]
      self.OkToChangeResourceGrpID:bool = obj["OkToChangeResourceGrpID"]
      """  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  """  
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.PBAllowModify:bool = obj["PBAllowModify"]
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      self.PhaseJobNum:str = obj["PhaseJobNum"]
      """  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  """  
      self.PhaseOprSeq:int = obj["PhaseOprSeq"]
      """  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  """  
      self.PrintNCTag:bool = obj["PrintNCTag"]
      self.PrjUsedTran:str = obj["PrjUsedTran"]
      self.ProdDesc:str = obj["ProdDesc"]
      self.ProjPhaseID:str = obj["ProjPhaseID"]
      self.RequestMove:bool = obj["RequestMove"]
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.RoleCdDisplayAll:bool = obj["RoleCdDisplayAll"]
      self.ScrapUOM:str = obj["ScrapUOM"]
      """  Unit of Measure used for ScrapQty.  """  
      self.SentFromMES:bool = obj["SentFromMES"]
      """  Flag field to identify if the row is being sent from MES  """  
      self.StartActivity:bool = obj["StartActivity"]
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.UnapprovedFirstArt:bool = obj["UnapprovedFirstArt"]
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.EnablePCID:bool = obj["EnablePCID"]
      """  EnablePCID  """  
      self.OutputBin:str = obj["OutputBin"]
      """  The output bin from the resource  """  
      self.OutputWarehouse:str = obj["OutputWarehouse"]
      """  The output warehouse from the resource  """  
      self.EnableLot:bool = obj["EnableLot"]
      """  Internal flag used for the row rules to control whether the Lot columns should be enabled.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot number that is to be added to the PCID  """  
      self.PrintPCIDContents:bool = obj["PrintPCIDContents"]
      """  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  """  
      self.HasAttachments:bool = obj["HasAttachments"]
      """  Indicates if the labor detail has attachments  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.DiscrepAttributeSetDescription:str = obj["DiscrepAttributeSetDescription"]
      """  The Full Description of the Attribute Set for DiscrepQty  """  
      self.DiscrepAttributeSetShortDescription:str = obj["DiscrepAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for DiscrepQty  """  
      self.ScrapAttributeSetDescription:str = obj["ScrapAttributeSetDescription"]
      """  The Full Description of the Attribute Set for ScrapQty  """  
      self.ScrapAttributeSetShortDescription:str = obj["ScrapAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for ScrapQty  """  
      self.LaborAttributeSetDescription:str = obj["LaborAttributeSetDescription"]
      """  The Full Description of the Attribute Set for LaborQty  """  
      self.LaborAttributeSetShortDescription:str = obj["LaborAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for LaborQty  """  
      self.DisableRecallAndDelete:bool = obj["DisableRecallAndDelete"]
      """  Indicates if recall and delete should be disabled  """  
      self.RoleCdList:str = obj["RoleCdList"]
      """  List of available role codes  """  
      self.RowSelected:bool = obj["RowSelected"]
      """  Indicates if the row is selected for submit, recall, or copy  """  
      self.AppointmentStart:str = obj["AppointmentStart"]
      """  Start date/time for calendar appoinment  """  
      self.AppointmentEnd:str = obj["AppointmentEnd"]
      """  End date/time for calendar appoinment  """  
      self.AppointmentTitle:str = obj["AppointmentTitle"]
      """  Title to display for the calendar appointment  """  
      self.TemplateID:str = obj["TemplateID"]
      """  PDF Form Template linked to the Job Operation  """  
      self.WIPTransaction:bool = obj["WIPTransaction"]
      """  Flag to validate if the transaction includes WIP  """  
      self.DiscrepRevision:str = obj["DiscrepRevision"]
      """  Revision for DiscrepQty  """  
      self.LaborRevision:str = obj["LaborRevision"]
      """  Revision for LaborQty  """  
      self.ScrapRevision:str = obj["ScrapRevision"]
      """  Revision for ScrapQty  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.ReportPartQtyAllowed:bool = obj["ReportPartQtyAllowed"]
      """  Indicates whether co-parts can be entered  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DiscrpRsnDescription:str = obj["DiscrpRsnDescription"]
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HCMIntregationHCMEnabled:bool = obj["HCMIntregationHCMEnabled"]
      self.HCMStatusStatus:str = obj["HCMStatusStatus"]
      self.IndirectDescription:str = obj["IndirectDescription"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.JobAsmblPartNum:str = obj["JobAsmblPartNum"]
      self.JobAsmblDescription:str = obj["JobAsmblDescription"]
      self.MachineDescription:str = obj["MachineDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.OpDescOpDesc:str = obj["OpDescOpDesc"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      self.ResReasonDescription:str = obj["ResReasonDescription"]
      self.ReWorkReasonDescription:str = obj["ReWorkReasonDescription"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.ScrapReasonDescription:str = obj["ScrapReasonDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborEquipRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  """  
      self.Hours:int = obj["Hours"]
      """  Hours that will be added to Equip.CurrentMeter.  Relevant only when the related Equip.LaborOpt = "Hrs"  """  
      self.Qty:int = obj["Qty"]
      """  Quantity that will be added to Equip.CurrentMeter.  Relevant only when the related Equip.LaborOpt = "Qty"  """  
      self.CurrentMeter:int = obj["CurrentMeter"]
      """  Current Meter reading which will update the Equip.CurrentMeter. Relevant only when the related Equip.LaborOpt = "Mtr"  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EquipLaborMeterOpt:str = obj["EquipLaborMeterOpt"]
      self.EquipDescription:str = obj["EquipDescription"]
      self.EquipMeterUOM:str = obj["EquipMeterUOM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  The number of the employee that performed the work. This field is directly maintainable. A selection list is provided in labor entry to find the employee by name.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """   The Payroll date is the "Logical Day" that labor occurred. In most cases this is the same as the "Physical Day".  But when work is done before and after midnight then "Labor Collection" rolls the physical date forward or backward to create a Logical date. This date will be used to group transactions together by a logical date in order to calculate daily overtime during the transfer to payroll.
It will also be used in the selection criteria logic during the transfer to payroll.  This is duplicated into each LaborDtl.  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date of the clock in time field. It is created using the ActualDate and may be rolled forward/backward if the clock in time is adjusted across midnight. For example, when an employee clocks in prior to midnight, but shift starts at midnight or later, this situation causes the default to be ActualDateIn + 1.  """  
      self.ClockInTime:int = obj["ClockInTime"]
      """  The clock in time to be considered for payroll and costing purposes as the time when the employee starts work. Clock in time is stored as Hours.Hundreths. It is created using the ActualClockIn value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockin" is before the shift start time (JCShift.Start) and after ( JCShift. start - JCSyst.Grace) then the system adjusts the clockin time to be the start of the shift. Else it will be set to the actual system time.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ActualClockInTime:int = obj["ActualClockInTime"]
      """  Actual clock in time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocked in. In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.StartTime. Stored as Hours:Hundreths.  """  
      self.ActualClockinDate:str = obj["ActualClockinDate"]
      """  The actual date at the time of clockin. Labor Collection uses the system date to create this field.  Labor entry allows entry of this field and then uses it to generate the default for the adjusted  "ClockInDate".  This field is provided mainly for audit purposes.  """  
      self.LunchStatus:str = obj["LunchStatus"]
      """   An internal control byte used by Labor Collection when the system is configured not to take out lunch automatically (JCSyst.AutoLunch = N). It is used determine if what to do when the "Lunch" button is pressed.

The possible values are "N" - No lunch, "O" - Out to Lunch, "R" - Returned from lunch.  """  
      self.ActLunchOutTime:int = obj["ActLunchOutTime"]
      """   Actual Clock out time for Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchStart as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time for LunchOut.  """  
      self.LunchOutTime:int = obj["LunchOutTime"]
      """   Clock out time for Lunch that is used for costing/payroll determination. It is created by adjusting the ActLunchOutTime. . The adjusted time is where the system time is rolled back to the JCShift.LunchStart time when the employee clocks out for lunch after it has started but before it ends.

Stored as Hours.Hundreths.  """  
      self.ActLunchInTime:int = obj["ActLunchInTime"]
      """   Actual Clock In  time from Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchEnd as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time.  """  
      self.LunchInTime:int = obj["LunchInTime"]
      """   Clock In time from Lunch break that is used for costing/payroll determination. Created by adjusting the ActLunchInTime.
The adjusted time is where the system time is rolled forward to the JCShift.LunchEnd time when the employee clocks in from lunch before the lunch period ends. 
Stored as Hours.Hundreths.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """  The clockOut in time to be considered for payroll and costing purposes as the time when the employee stops work. ClockOut time is stored as Hours.Hundreths. It is defaulted using the ActualClockOut value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockOut" is after the shift end time (JCShift.End) and before ( JCShift.End + JC.Syst.Grace) then the system adjusts the ClockOut time to be the end of the shift. Else it will be set to the actual system time.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ActualClockOutTime:int = obj["ActualClockOutTime"]
      """  Actual clock Out time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocks out.  In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.EndTime. Stored as Hours.Hundreths.  """  
      self.PayHours:int = obj["PayHours"]
      """   Hours for payroll.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5. This is calculated when the Start/Stop times are changed in labor entry. It can then be overridden.
The Logic for calculating hours from clockin, clockout is:
If ClockIn > ClockOut Gross Hours = ( (ClockOut + 24.00) - ClockIn) else Gross Hours = ClockOut - ClockIn. 
If LunchOut > LunchIn Lunch Hours = ( (LunchIn +24) - LunchOut )
else Lunch Hours = ( LunchIn - LunchOut ).
PayHours = GRoss Hours - Lunch Hours. 
Remember that the database clockin/clockout fields are stored as hours hundredths, while the entry widgets are either hours.hundreths or Hours:Minutes. So use the database fields in this calculation and there is no need to worry about conversions.  """  
      self.FeedPayroll:bool = obj["FeedPayroll"]
      """  Flag that indicates this labor transaction is eligible for transfer to DCD payroll application. The default is set from JCSyst.FeedPayroll.  """  
      self.TransferredToPayroll:bool = obj["TransferredToPayroll"]
      """  Indicates if this transaction has been transferred to payroll. This is updated via the Payroll function to transfer labor.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.TranSet:str = obj["TranSet"]
      """  An optional field where the user enters a string of characters that would be used to associate multiple transactions as being part of a transaction set. TranSet will be used for data selection type functions.  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborHed record is currently active. When the employee clocks out it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice, displaying which employees are clocked in and which ones have not clocked out. Labor entry can't access a record that is Open.  """  
      self.ChkLink:str = obj["ChkLink"]
      """   Encoded value PRChkDtl.HeadNum + PRChkDtl.LineNum.
Used to relate the labor to the payroll check detail.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotLbrHrs:int = obj["TotLbrHrs"]
      self.TotBurHrs:int = obj["TotBurHrs"]
      self.WipPosted:bool = obj["WipPosted"]
      self.ImagePath:str = obj["ImagePath"]
      """  Full Path of Employee PhotoFile  """  
      self.LunchBreak:bool = obj["LunchBreak"]
      """  Indicates if a lunch break is part of the shift  """  
      self.EmpBasicShift:int = obj["EmpBasicShift"]
      """  Normal work shift from EmpBasic  """  
      self.EmpBasicSupervisorID:str = obj["EmpBasicSupervisorID"]
      """  The ID of the supervisor for the employee  """  
      self.DspPayHours:int = obj["DspPayHours"]
      """  For display purposes  """  
      self.GetNewNoHdr:bool = obj["GetNewNoHdr"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.MES:bool = obj["MES"]
      self.EmployeeNumLastName:str = obj["EmployeeNumLastName"]
      """  Last name of employee  """  
      self.EmployeeNumName:str = obj["EmployeeNumName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.EmployeeNumFirstName:str = obj["EmployeeNumFirstName"]
      """  First name of employee.  """  
      self.ShiftDescription:str = obj["ShiftDescription"]
      """  A concatenation of Start + End time.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborHedListTableset:
   def __init__(self, obj):
      self.LaborHedList:list[Erp_Tablesets_LaborHedListRow] = obj["LaborHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LaborHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  The number of the employee that performed the work. This field is directly maintainable. A selection list is provided in labor entry to find the employee by name.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """   The Payroll date is the "Logical Day" that labor occurred. In most cases this is the same as the "Physical Day".  But when work is done before and after midnight then "Labor Collection" rolls the physical date forward or backward to create a Logical date. This date will be used to group transactions together by a logical date in order to calculate daily overtime during the transfer to payroll.
It will also be used in the selection criteria logic during the transfer to payroll.  This is duplicated into each LaborDtl.  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date of the clock in time field. It is created using the ActualDate and may be rolled forward/backward if the clock in time is adjusted across midnight. For example, when an employee clocks in prior to midnight, but shift starts at midnight or later, this situation causes the default to be ActualDateIn + 1.  """  
      self.ClockInTime:int = obj["ClockInTime"]
      """  The clock in time to be considered for payroll and costing purposes as the time when the employee starts work. Clock in time is stored as Hours.Hundreths. It is created using the ActualClockIn value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockin" is before the shift start time (JCShift.Start) and after ( JCShift. start - JCSyst.Grace) then the system adjusts the clockin time to be the start of the shift. Else it will be set to the actual system time.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ActualClockInTime:int = obj["ActualClockInTime"]
      """  Actual clock in time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocked in. In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.StartTime. Stored as Hours:Hundreths.  """  
      self.ActualClockinDate:str = obj["ActualClockinDate"]
      """  The actual date at the time of clockin. Labor Collection uses the system date to create this field.  Labor entry allows entry of this field and then uses it to generate the default for the adjusted  "ClockInDate".  This field is provided mainly for audit purposes.  """  
      self.LunchStatus:str = obj["LunchStatus"]
      """   An internal control byte used by Labor Collection when the system is configured not to take out lunch automatically (JCSyst.AutoLunch = N). It is used determine if what to do when the "Lunch" button is pressed.

The possible values are "N" - No lunch, "O" - Out to Lunch, "R" - Returned from lunch.  """  
      self.ActLunchOutTime:int = obj["ActLunchOutTime"]
      """   Actual Clock out time for Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchStart as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time for LunchOut.  """  
      self.LunchOutTime:int = obj["LunchOutTime"]
      """   Clock out time for Lunch that is used for costing/payroll determination. It is created by adjusting the ActLunchOutTime. . The adjusted time is where the system time is rolled back to the JCShift.LunchStart time when the employee clocks out for lunch after it has started but before it ends.

Stored as Hours.Hundreths.  """  
      self.ActLunchInTime:int = obj["ActLunchInTime"]
      """   Actual Clock In  time from Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchEnd as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time.  """  
      self.LunchInTime:int = obj["LunchInTime"]
      """   Clock In time from Lunch break that is used for costing/payroll determination. Created by adjusting the ActLunchInTime.
The adjusted time is where the system time is rolled forward to the JCShift.LunchEnd time when the employee clocks in from lunch before the lunch period ends. 
Stored as Hours.Hundreths.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """  The clockOut in time to be considered for payroll and costing purposes as the time when the employee stops work. ClockOut time is stored as Hours.Hundreths. It is defaulted using the ActualClockOut value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockOut" is after the shift end time (JCShift.End) and before ( JCShift.End + JC.Syst.Grace) then the system adjusts the ClockOut time to be the end of the shift. Else it will be set to the actual system time.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ActualClockOutTime:int = obj["ActualClockOutTime"]
      """  Actual clock Out time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocks out.  In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.EndTime. Stored as Hours.Hundreths.  """  
      self.PayHours:int = obj["PayHours"]
      """   Hours for payroll.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5. This is calculated when the Start/Stop times are changed in labor entry. It can then be overridden.
The Logic for calculating hours from clockin, clockout is:
If ClockIn > ClockOut Gross Hours = ( (ClockOut + 24.00) - ClockIn) else Gross Hours = ClockOut - ClockIn. 
If LunchOut > LunchIn Lunch Hours = ( (LunchIn +24) - LunchOut )
else Lunch Hours = ( LunchIn - LunchOut ).
PayHours = GRoss Hours - Lunch Hours. 
Remember that the database clockin/clockout fields are stored as hours hundredths, while the entry widgets are either hours.hundreths or Hours:Minutes. So use the database fields in this calculation and there is no need to worry about conversions.  """  
      self.FeedPayroll:bool = obj["FeedPayroll"]
      """  Flag that indicates this labor transaction is eligible for transfer to DCD payroll application. The default is set from JCSyst.FeedPayroll.  """  
      self.TransferredToPayroll:bool = obj["TransferredToPayroll"]
      """  Indicates if this transaction has been transferred to payroll. This is updated via the Payroll function to transfer labor.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.TranSet:str = obj["TranSet"]
      """  An optional field where the user enters a string of characters that would be used to associate multiple transactions as being part of a transaction set. TranSet will be used for data selection type functions.  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborHed record is currently active. When the employee clocks out it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice, displaying which employees are clocked in and which ones have not clocked out. Labor entry can't access a record that is Open.  """  
      self.ChkLink:str = obj["ChkLink"]
      """   Encoded value PRChkDtl.HeadNum + PRChkDtl.LineNum.
Used to relate the labor to the payroll check detail.  """  
      self.BatchTotalHrsDisp:str = obj["BatchTotalHrsDisp"]
      """  BatchTotalHrsDisp  """  
      self.BatchHrsRemainDisp:str = obj["BatchHrsRemainDisp"]
      """  BatchHrsRemainDisp  """  
      self.BatchHrsRemainPctDisp:str = obj["BatchHrsRemainPctDisp"]
      """  BatchHrsRemainPctDisp  """  
      self.BatchSplitHrsMethod:str = obj["BatchSplitHrsMethod"]
      """  BatchSplitHrsMethod  """  
      self.BatchAssignTo:bool = obj["BatchAssignTo"]
      """  BatchAssignTo  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchStartHrs:str = obj["BatchStartHrs"]
      """  BatchStartHrs  """  
      self.BatchEndHrs:str = obj["BatchEndHrs"]
      """  BatchEndHrs  """  
      self.BatchTotalHrs:int = obj["BatchTotalHrs"]
      """  BatchTotalHrs  """  
      self.BatchHrsRemain:int = obj["BatchHrsRemain"]
      """  BatchHrsRemain  """  
      self.BatchHrsRemainPct:int = obj["BatchHrsRemainPct"]
      """  BatchHrsRemainPct  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.HCMPayHoursCalcType:str = obj["HCMPayHoursCalcType"]
      """  Indicates which type of Pay time calculation will be used when HCM Integration is on.  """  
      self.EmpBasicShift:int = obj["EmpBasicShift"]
      """  Normal work shift from EmpBasic  """  
      self.EmpBasicSupervisorID:str = obj["EmpBasicSupervisorID"]
      """  The ID of the supervisor for the employee  """  
      self.GetNewNoHdr:bool = obj["GetNewNoHdr"]
      self.HCMTotPayHours:int = obj["HCMTotPayHours"]
      """  HCM Integration, Display the Total of Pay Hours of the Labor Details.  """  
      self.ImagePath:str = obj["ImagePath"]
      """  Full Path of Employee PhotoFile  """  
      self.LunchBreak:bool = obj["LunchBreak"]
      """  Indicates if a lunch break is part of the shift  """  
      self.MES:bool = obj["MES"]
      self.PayrollValuesForHCM:str = obj["PayrollValuesForHCM"]
      """  Temporal field that stores patch field value: HDR, DTL, NON  """  
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TotBurHrs:int = obj["TotBurHrs"]
      self.TotLbrHrs:int = obj["TotLbrHrs"]
      self.WipPosted:bool = obj["WipPosted"]
      self.DspPayHours:int = obj["DspPayHours"]
      """  For display purposes  """  
      self.FullyPosted:bool = obj["FullyPosted"]
      """  Indicates if all labor has been posted  """  
      self.PartiallyPosted:bool = obj["PartiallyPosted"]
      """  Indicates if some labor has been posted  """  
      self.HCMExistsWithStatus:bool = obj["HCMExistsWithStatus"]
      self.PayrollDateNav:str = obj["PayrollDateNav"]
      """  Payroll date for record navigation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmployeeNumFirstName:str = obj["EmployeeNumFirstName"]
      self.EmployeeNumName:str = obj["EmployeeNumName"]
      self.EmployeeNumLastName:str = obj["EmployeeNumLastName"]
      self.HCMStatusStatus:str = obj["HCMStatusStatus"]
      self.PRSystHCMEnabled:bool = obj["PRSystHCMEnabled"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of the manufactured item that the quantity is for. Must be defined on the Job in the JobPart table.  """  
      self.PartQty:int = obj["PartQty"]
      """  The number of individual parts completed on this labor transaction. Updates the JobPart.QtyCompleted.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """  Discrepant Reason Code  """  
      self.DiscrpAttributeSetID:int = obj["DiscrpAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  The reported scrap quantity.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  Scrap Reason Code  """  
      self.ScrapAttributeSetID:int = obj["ScrapAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  """  
      self.NonConfTranID:int = obj["NonConfTranID"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.LaborAttributeSetID:int = obj["LaborAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the PartQty  """  
      self.MESProcessing:bool = obj["MESProcessing"]
      """  UI Sets this to true when processing from MES Labor Entry.  The BL uses this to determine if PartWip/MtlQueue logic should be performed.  """  
      self.RequestMove:bool = obj["RequestMove"]
      self.PartUOM:str = obj["PartUOM"]
      """  Unit of Measure for the Part defined on the Operation  """  
      self.PartDescription:str = obj["PartDescription"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.DiscrepUOM:str = obj["DiscrepUOM"]
      """  Unit of Measure used for DiscrepQty  """  
      self.ScrapUOM:str = obj["ScrapUOM"]
      """  Unit of Measure used for ScrapQty.  """  
      self.DiscrepAttributeSetDescription:str = obj["DiscrepAttributeSetDescription"]
      """  The Full Description of the Attribute Set for DiscrepQty  """  
      self.DiscrepAttributeSetShortDescription:str = obj["DiscrepAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for DiscrepQty  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.LaborAttributeSetDescription:str = obj["LaborAttributeSetDescription"]
      """  The Full Description of the Attribute Set for PartQty  """  
      self.LaborAttributeSetShortDescription:str = obj["LaborAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for PartQty  """  
      self.ScrapAttributeSetDescription:str = obj["ScrapAttributeSetDescription"]
      """  The Full Description of the Attribute Set for ScrapQty  """  
      self.ScrapAttributeSetShortDescription:str = obj["ScrapAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for ScrapQty  """  
      self.DiscrepRevision:str = obj["DiscrepRevision"]
      """  Revision for DiscrepQty  """  
      self.ScrapRevision:str = obj["ScrapRevision"]
      """  Revision for ScrapQty  """  
      self.EnableDiscrpQty:bool = obj["EnableDiscrpQty"]
      """  Allow input of discrepant (nonconformance) quantity  """  
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      """  Allow input of scrap quantity  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DiscrpRsnDescription:str = obj["DiscrpRsnDescription"]
      self.ScrapReasonDescription:str = obj["ScrapReasonDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborTableset:
   def __init__(self, obj):
      self.LaborHed:list[Erp_Tablesets_LaborHedRow] = obj["LaborHed"]
      self.LaborDtl:list[Erp_Tablesets_LaborDtlRow] = obj["LaborDtl"]
      self.LaborDtlAttch:list[Erp_Tablesets_LaborDtlAttchRow] = obj["LaborDtlAttch"]
      self.LaborDtlAction:list[Erp_Tablesets_LaborDtlActionRow] = obj["LaborDtlAction"]
      self.LaborDtlComment:list[Erp_Tablesets_LaborDtlCommentRow] = obj["LaborDtlComment"]
      self.LaborEquip:list[Erp_Tablesets_LaborEquipRow] = obj["LaborEquip"]
      self.LaborPart:list[Erp_Tablesets_LaborPartRow] = obj["LaborPart"]
      self.LbrScrapSerialNumbers:list[Erp_Tablesets_LbrScrapSerialNumbersRow] = obj["LbrScrapSerialNumbers"]
      self.LaborDtlGroup:list[Erp_Tablesets_LaborDtlGroupRow] = obj["LaborDtlGroup"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.TimeWeeklyView:list[Erp_Tablesets_TimeWeeklyViewRow] = obj["TimeWeeklyView"]
      self.TimeWorkHours:list[Erp_Tablesets_TimeWorkHoursRow] = obj["TimeWorkHours"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LbrScrapSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial Number  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq this scrap serial number is for  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq this scrap serial number is for  """  
      self.EnableStatus:bool = obj["EnableStatus"]
      """  Indicates whether the Status field can be updated.  """  
      self.SNStatus:str = obj["SNStatus"]
      """  New status for the serial number. This field will require Code/Desc definition: REJECTED`Scrap INSPECTION`Nonconformance WIP`WIP  """  
      self.SNStatusDesc:str = obj["SNStatusDesc"]
      """  The SNStatus description ? set same as SerialNo.SNStatusTrans  """  
      self.Selected:bool = obj["Selected"]
      """  Serial Number Selected for process  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TimeWeeklyViewRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmployeeNum:str = obj["EmployeeNum"]
      self.WeekBeginDate:str = obj["WeekBeginDate"]
      self.WeekEndDate:str = obj["WeekEndDate"]
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.LaborType:str = obj["LaborType"]
      self.ProjectID:str = obj["ProjectID"]
      self.PhaseID:str = obj["PhaseID"]
      self.TimeTypCd:str = obj["TimeTypCd"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.RoleCd:str = obj["RoleCd"]
      self.IndirectCode:str = obj["IndirectCode"]
      self.HoursSun:int = obj["HoursSun"]
      self.HoursMon:int = obj["HoursMon"]
      self.HoursTue:int = obj["HoursTue"]
      self.HoursWed:int = obj["HoursWed"]
      self.HoursThu:int = obj["HoursThu"]
      self.HoursFri:int = obj["HoursFri"]
      self.HoursSat:int = obj["HoursSat"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.RoleCdDescription:str = obj["RoleCdDescription"]
      self.IndirectCodeDescription:str = obj["IndirectCodeDescription"]
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      self.HoursTotal:int = obj["HoursTotal"]
      self.ExpenseCode:str = obj["ExpenseCode"]
      self.Complete:bool = obj["Complete"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.ResourceID:str = obj["ResourceID"]
      self.OpCode:str = obj["OpCode"]
      self.OpComplete:bool = obj["OpComplete"]
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      self.LaborRate:int = obj["LaborRate"]
      self.ResourceGrpIDDescription:str = obj["ResourceGrpIDDescription"]
      self.JCDept:str = obj["JCDept"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      self.Shift:int = obj["Shift"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.MessageText:str = obj["MessageText"]
      self.NewRowType:str = obj["NewRowType"]
      """  Valid values are "A" for an Add of a new TimeWeeklyView row and "C" for a Copy of an existing TimeWeeklyView row.  """  
      self.DisPrjRoleCd:bool = obj["DisPrjRoleCd"]
      self.DisTimeTypCd:bool = obj["DisTimeTypCd"]
      self.DisLaborType:bool = obj["DisLaborType"]
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if submit is available  """  
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy function is available  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if recall is available  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.TimeStatus:str = obj["TimeStatus"]
      self.ProjDesc:str = obj["ProjDesc"]
      self.WBSPhaseDesc:str = obj["WBSPhaseDesc"]
      """  WBS Phase Project Description  """  
      self.OperDesc:str = obj["OperDesc"]
      """  Operation Description  """  
      self.ASMdesc:str = obj["ASMdesc"]
      """  Job Assembly description  """  
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """   If the Time is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  """  
      self.DeleteRow:bool = obj["DeleteRow"]
      self.HCMTotWeeklyPayHours:int = obj["HCMTotWeeklyPayHours"]
      """  HCM Integration Total Weekly Pay Hours  """  
      self.RoleCdList:str = obj["RoleCdList"]
      """  List of avaialble role codes  """  
      self.RowSelected:bool = obj["RowSelected"]
      """  Indicates if the row is selected for submit, recall, or copy.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TimeWorkHoursRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CalendarID:str = obj["CalendarID"]
      self.WeekBeginDate:str = obj["WeekBeginDate"]
      self.WeekEndDate:str = obj["WeekEndDate"]
      self.SunDisplayDate:str = obj["SunDisplayDate"]
      self.MonDisplayDate:str = obj["MonDisplayDate"]
      self.TueDisplayDate:str = obj["TueDisplayDate"]
      self.WedDisplayDate:str = obj["WedDisplayDate"]
      self.ThuDisplayDate:str = obj["ThuDisplayDate"]
      self.FriDisplayDate:str = obj["FriDisplayDate"]
      self.SatDisplayDate:str = obj["SatDisplayDate"]
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.SunWorkHours:int = obj["SunWorkHours"]
      self.MonWorkHours:int = obj["MonWorkHours"]
      self.TueWorkHours:int = obj["TueWorkHours"]
      self.WedWorkHours:int = obj["WedWorkHours"]
      self.ThuWorkHours:int = obj["ThuWorkHours"]
      self.FriWorkHours:int = obj["FriWorkHours"]
      self.SatWorkHours:int = obj["SatWorkHours"]
      self.SunBookedHours:int = obj["SunBookedHours"]
      self.MonBookedHours:int = obj["MonBookedHours"]
      self.WedBookedHours:int = obj["WedBookedHours"]
      self.ThuBookedHours:int = obj["ThuBookedHours"]
      self.FriBookedHours:int = obj["FriBookedHours"]
      self.SunDiffHours:int = obj["SunDiffHours"]
      self.MonDiffHours:int = obj["MonDiffHours"]
      self.SatBookedHours:int = obj["SatBookedHours"]
      self.TueBookedHours:int = obj["TueBookedHours"]
      self.TueDiffHours:int = obj["TueDiffHours"]
      self.WedDiffHours:int = obj["WedDiffHours"]
      self.ThuDiffHours:int = obj["ThuDiffHours"]
      self.FriDiffHours:int = obj["FriDiffHours"]
      self.SatDiffHours:int = obj["SatDiffHours"]
      self.EmployeeNum:str = obj["EmployeeNum"]
      self.CalendarDescription:str = obj["CalendarDescription"]
      self.TotalWorkHours:int = obj["TotalWorkHours"]
      self.TotalBookedHours:int = obj["TotalBookedHours"]
      self.TotalDiffHours:int = obj["TotalDiffHours"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtLaborTableset:
   def __init__(self, obj):
      self.LaborHed:list[Erp_Tablesets_LaborHedRow] = obj["LaborHed"]
      self.LaborDtl:list[Erp_Tablesets_LaborDtlRow] = obj["LaborDtl"]
      self.LaborDtlAttch:list[Erp_Tablesets_LaborDtlAttchRow] = obj["LaborDtlAttch"]
      self.LaborDtlAction:list[Erp_Tablesets_LaborDtlActionRow] = obj["LaborDtlAction"]
      self.LaborDtlComment:list[Erp_Tablesets_LaborDtlCommentRow] = obj["LaborDtlComment"]
      self.LaborEquip:list[Erp_Tablesets_LaborEquipRow] = obj["LaborEquip"]
      self.LaborPart:list[Erp_Tablesets_LaborPartRow] = obj["LaborPart"]
      self.LbrScrapSerialNumbers:list[Erp_Tablesets_LbrScrapSerialNumbersRow] = obj["LbrScrapSerialNumbers"]
      self.LaborDtlGroup:list[Erp_Tablesets_LaborDtlGroupRow] = obj["LaborDtlGroup"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.TimeWeeklyView:list[Erp_Tablesets_TimeWeeklyViewRow] = obj["TimeWeeklyView"]
      self.TimeWorkHours:list[Erp_Tablesets_TimeWorkHoursRow] = obj["TimeWorkHours"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WorkQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JCDept:str = obj["JCDept"]
      """  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  """  
      self.OpComplete:bool = obj["OpComplete"]
      """   Indicates if this operation is completed. This is normally set to complete via labor entry transactions.   Not maintainable by Job Entry. It can't be reset to "No" if the JobHead.Complete = Yes.
Labor entry setting logic is: If SetUpComplete = Yes and  EstProdHours = 0 or ProdComplete = Yes and EstSetHours = 0 or both ProdComplete = Yes and SetupComplete = Yes  then OpComplete = Yes.
This field is also set by PO receipt entry "issue complete" for subcontract operations.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this Operation is associated with.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OprQty:int = obj["OprQty"]
      """  The total operation quantity. This is a calculated field.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SetupLoadHrs:int = obj["SetupLoadHrs"]
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.ProdLoadHrs:int = obj["ProdLoadHrs"]
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.RegionCode:int = obj["RegionCode"]
      """  1=CurrentWork, 2=AvailableWork, 3=ExpectedWork  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  """  
      self.SortDate:str = obj["SortDate"]
      self.WIPQty:int = obj["WIPQty"]
      self.CrewCount:int = obj["CrewCount"]
      """  Number Of Employees Now Working On This Operation  """  
      self.QtyLeft:int = obj["QtyLeft"]
      self.SetupLeft:int = obj["SetupLeft"]
      self.WIPQtyDetails:bool = obj["WIPQtyDetails"]
      """  TRUE indicates there are WIP Qty Details available (i.e. the Staged Details button should be enabled)  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.CanRequest:bool = obj["CanRequest"]
      """  TRUE indicates the current employee is authorized to Request Material  """  
      self.CanSelect:bool = obj["CanSelect"]
      """  TRUE indicates the current employee can select this operation to work on (i.e. the Select For Work button should be enabled).  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.JobHeadPartNum:str = obj["JobHeadPartNum"]
      """  Part number of the manufactured item.  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.JobHeadPartDescription:str = obj["JobHeadPartDescription"]
      """  The description of the part that is to be manufactured.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  """  
      self.OprCommentText:str = obj["OprCommentText"]
      """  Editor widget for Job operation comments.  """  
      self.AsmCommentText:str = obj["AsmCommentText"]
      """  Editor widget for Job header comments.  """  
      self.JobHeadCommentText:str = obj["JobHeadCommentText"]
      """  Editor widget for Job header comments.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.RegionDescription:str = obj["RegionDescription"]
      """  "Current Work", "Available Work", or "Expected Work" as indicated by the RegionCode.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl.  System assigned.  """  
      self.OpDtlDescription:str = obj["OpDtlDescription"]
      """  Description is initially created when the JobOpDtl is created.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  """  
      self.OpDtlType:str = obj["OpDtlType"]
      """  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "Setup", "Production", or "Both".  """  
      self.Description:str = obj["Description"]
      """  Description used only for subcontract operations  """  
      self.SortHour:int = obj["SortHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.Selected:bool = obj["Selected"]
      """  Used by the UI to allow selection of rows  """  
      self.RunQty:int = obj["RunQty"]
      """   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description for PartNum  """  
      self.SchResourceList:str = obj["SchResourceList"]
      """  Delimited list of resources oper is schedueld to  """  
      self.CurQty:int = obj["CurQty"]
      """  Current Production Qty (for user reporting qty)  """  
      self.LaborQty:int = obj["LaborQty"]
      """  Qty currently being completed  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  Scrap Qty currently being entered  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  Discrep Qty currently being entered  """  
      self.DiscrepRsnCode:str = obj["DiscrepRsnCode"]
      """  Reason code for discrep qty currently being entered  """  
      self.ScrapRsnCode:str = obj["ScrapRsnCode"]
      """  Reason code for scrap currently being entered  """  
      self.ScrapRsnDesc:str = obj["ScrapRsnDesc"]
      """  Description for ScrapRsnCode  """  
      self.DiscrepRsnDesc:str = obj["DiscrepRsnDesc"]
      """  Description for DescrepRsnCode  """  
      self.Complete:bool = obj["Complete"]
      """  Operation complete  """  
      self.ResourceID:str = obj["ResourceID"]
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.FirstCustNum:int = obj["FirstCustNum"]
      """  CustNum from first order  """  
      self.FirstCustID:str = obj["FirstCustID"]
      self.FirstCustName:str = obj["FirstCustName"]
      self.FirstShipViaCode:str = obj["FirstShipViaCode"]
      self.FirstShipViaDesc:str = obj["FirstShipViaDesc"]
      self.SetupGrpDesc:str = obj["SetupGrpDesc"]
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  RequestMove  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.SetupOrProd:str = obj["SetupOrProd"]
      self.StartDateNullCheck:bool = obj["StartDateNullCheck"]
      """  Used to checks if the StartDate has a value or is null to later permit a Sorting of the records By the StartDate field , positioning the null values at the end.  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.CheckBox05:bool = obj["CheckBox05"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.Date01:str = obj["Date01"]
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.PageNum:int = obj["PageNum"]
      """  Used for caching pagination in UI  """  
      self.TotalRecords:int = obj["TotalRecords"]
      """  Used for caching pagination in UI  """  
      self.MorePages:bool = obj["MorePages"]
      """  Used for caching pagination in UI  """  
      self.LaborEntryMethodDesc:str = obj["LaborEntryMethodDesc"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) , "B" - Backflush or "X" - Time and Backflush Qty.  """  
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      self.EnableDiscrepQty:bool = obj["EnableDiscrepQty"]
      self.ResourceGrpDesc:str = obj["ResourceGrpDesc"]
      """  Resource Group Description.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Operation Code Description.  """  
      self.LaborUOM:str = obj["LaborUOM"]
      """  Unit of Measure used for editable quantity fields on the WorkQueue.  """  
      self.LaborType:str = obj["LaborType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class ExternalMESDowntime_input:
   """ Required : 
   ds
   indirectCode
   downtimeNote
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.indirectCode:str = obj["indirectCode"]
      """  IndirectCode  """  
      self.downtimeNote:str = obj["downtimeNote"]
      """  Downtime Note  """  
      pass

class ExternalMESDowntime_output:
   def __init__(self, obj):
      pass

class ExternalMESEndDowntime_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class ExternalMESEndDowntime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetActiveLaborDtl_input:
   """ Required : 
   employeeNum
   """  
   def __init__(self, obj):
      self.employeeNum:str = obj["employeeNum"]
      """  The Employee Num  """  
      pass

class GetActiveLaborDtl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LaborTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   laborHedSeq
   """  
   def __init__(self, obj):
      self.laborHedSeq:int = obj["laborHedSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LaborTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LaborTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LaborTableset] = obj["returnObj"]
      pass

class GetClockTime_input:
   """ Required : 
   dspClckTm
   """  
   def __init__(self, obj):
      self.dspClckTm:str = obj["dspClckTm"]
      """  The clock time to be parsed as Decimal  """  
      pass

class GetClockTime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.clckTm:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDefaultsAddLaborDtlFromCalendar_input:
   """ Required : 
   empID
   calendarStartDateTime
   calendarEndDateTime
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      self.calendarStartDateTime:str = obj["calendarStartDateTime"]
      self.calendarEndDateTime:str = obj["calendarEndDateTime"]
      pass

class GetDefaultsAddLaborDtlFromCalendar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.laborHedSeq:int = obj["parameters"]
      self.startDate:str = obj["parameters"]
      self.startTime:int = obj["parameters"]
      self.endDate:str = obj["parameters"]
      self.endTime:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetDetail_input:
   """ Required : 
   iLaborHedSeq
   iLaborDtlSeq
   """  
   def __init__(self, obj):
      self.iLaborHedSeq:int = obj["iLaborHedSeq"]
      """  The LaborHedSeq of the LaborHed record to retrieve  """  
      self.iLaborDtlSeq:int = obj["iLaborDtlSeq"]
      """  The LaborDtlSeq of the LaborDtl record to retrieve  """  
      pass

class GetDetail_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LaborTableset] = obj["returnObj"]
      pass

class GetDspClockTime_input:
   """ Required : 
   clckTm
   """  
   def __init__(self, obj):
      self.clckTm:int = obj["clckTm"]
      """  The clock time to be formatted  """  
      pass

class GetDspClockTime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dspClckTm:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetJobProductionCompanySettings_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.advanceLaborRate:bool = obj["advanceLaborRate"]
      self.clockFormat:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetLaborTypeList_input:
   """ Required : 
   employeeNum
   """  
   def __init__(self, obj):
      self.employeeNum:str = obj["employeeNum"]
      """  Employee Number  """  
      pass

class GetLaborTypeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.laborTypeList:str = obj["parameters"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_LaborHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewLaborDtlAction_input:
   """ Required : 
   ds
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      pass

class GetNewLaborDtlAction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborDtlAttch_input:
   """ Required : 
   ds
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      pass

class GetNewLaborDtlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborDtlComment_input:
   """ Required : 
   ds
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      pass

class GetNewLaborDtlComment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborDtlGroup_input:
   """ Required : 
   ds
   employeeNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.employeeNum:str = obj["employeeNum"]
      pass

class GetNewLaborDtlGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborDtlNoHdr_input:
   """ Required : 
   ds
   EmployeeNum
   ShopFloor
   ClockInDate
   ClockInTime
   ClockOutDate
   ClockOutTime
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  The employee id for this labor record  """  
      self.ShopFloor:bool = obj["ShopFloor"]
      """  Indicates whether this is being called from the shop floor
            labor entry program  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date  """  
      self.ClockInTime:int = obj["ClockInTime"]
      """  The clock in time  """  
      self.ClockOutDate:str = obj["ClockOutDate"]
      """  The clock out date  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """  The clock out time  """  
      pass

class GetNewLaborDtlNoHdr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborDtlOnSelectForWork_input:
   """ Required : 
   ds
   laborHedSeq
   sJobNum
   iAssemblySeq
   iOprSeq
   sResourceGrpID
   setupOrProd
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.sJobNum:str = obj["sJobNum"]
      self.iAssemblySeq:int = obj["iAssemblySeq"]
      self.iOprSeq:int = obj["iOprSeq"]
      self.sResourceGrpID:str = obj["sResourceGrpID"]
      self.setupOrProd:str = obj["setupOrProd"]
      pass

class GetNewLaborDtlOnSelectForWork_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.bMachinePrompt:bool = obj["bMachinePrompt"]
      pass

      """  output parameters  """  

class GetNewLaborDtlWithHdr_input:
   """ Required : 
   ds
   ipClockInDate
   ipClockInTime
   ipClockOutDate
   ipClockOutTime
   ipLaborHedSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ipClockInDate:str = obj["ipClockInDate"]
      """  The clock in date  """  
      self.ipClockInTime:int = obj["ipClockInTime"]
      """  The clock in time  """  
      self.ipClockOutDate:str = obj["ipClockOutDate"]
      """  The clock out date  """  
      self.ipClockOutTime:int = obj["ipClockOutTime"]
      """  The clock out time  """  
      self.ipLaborHedSeq:int = obj["ipLaborHedSeq"]
      """  Unique identifier of the LaborHed  """  
      pass

class GetNewLaborDtlWithHdr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborDtl_input:
   """ Required : 
   ds
   laborHedSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      pass

class GetNewLaborDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborEquip_input:
   """ Required : 
   ds
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      pass

class GetNewLaborEquip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborHed1_input:
   """ Required : 
   ds
   EmployeeNum
   ShopFloor
   payrollDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  The employee id for this labor record  """  
      self.ShopFloor:bool = obj["ShopFloor"]
      """  Indicates whether this is being called from the shop floor
            labor entry program  """  
      self.payrollDate:str = obj["payrollDate"]
      """  Payroll Date for this labor record  """  
      pass

class GetNewLaborHed1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class GetNewLaborHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborPart_input:
   """ Required : 
   ds
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      pass

class GetNewLaborPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLbrScrapSerialNumbers_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class GetNewLbrScrapSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTimeWeeklyView_input:
   """ Required : 
   ds
   ipEmployeeNum
   ipDateInWeek
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ipEmployeeNum:str = obj["ipEmployeeNum"]
      """  The employee id for this labor record  """  
      self.ipDateInWeek:str = obj["ipDateInWeek"]
      """  Date within the week for which a new TimeWeeklyView record is to be created  """  
      pass

class GetNewTimeWeeklyView_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsCalendarView_input:
   """ Required : 
   whereClauseLaborHed
   whereClauseLaborDtl
   whereClauseLaborDtlAttach
   whereClauseLaborDtlAction
   whereClauseLaborDtlCom
   whereClauseLaborEquip
   whereClauseLaborPart
   whereClauseLbrScrapSerialNumbers
   whereClauseTimeWorkHours
   whereClauseTimeWeeklyView
   whereClauseLaborDtlGroup
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   pageSize
   absolutePage
   ipEmployeeNum
   ipCalendarStartDate
   ipCalendarEndDate
   """  
   def __init__(self, obj):
      self.whereClauseLaborHed:str = obj["whereClauseLaborHed"]
      self.whereClauseLaborDtl:str = obj["whereClauseLaborDtl"]
      self.whereClauseLaborDtlAttach:str = obj["whereClauseLaborDtlAttach"]
      self.whereClauseLaborDtlAction:str = obj["whereClauseLaborDtlAction"]
      self.whereClauseLaborDtlCom:str = obj["whereClauseLaborDtlCom"]
      self.whereClauseLaborEquip:str = obj["whereClauseLaborEquip"]
      self.whereClauseLaborPart:str = obj["whereClauseLaborPart"]
      self.whereClauseLbrScrapSerialNumbers:str = obj["whereClauseLbrScrapSerialNumbers"]
      self.whereClauseTimeWorkHours:str = obj["whereClauseTimeWorkHours"]
      self.whereClauseTimeWeeklyView:str = obj["whereClauseTimeWeeklyView"]
      self.whereClauseLaborDtlGroup:str = obj["whereClauseLaborDtlGroup"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      self.ipEmployeeNum:str = obj["ipEmployeeNum"]
      self.ipCalendarStartDate:str = obj["ipCalendarStartDate"]
      self.ipCalendarEndDate:str = obj["ipCalendarEndDate"]
      pass

class GetRowsCalendarView_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LaborTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsTimeEntry_input:
   """ Required : 
   whereClauseLaborHed
   whereClauseLaborDtl
   whereClauseLaborDtlAttach
   whereClauseLaborDtlAction
   whereClauseLaborDtlCom
   whereClauseLaborEquip
   whereClauseLaborPart
   whereClauseLbrScrapSerialNumbers
   whereClauseTimeWorkHours
   whereClauseTimeWeeklyView
   whereClauseLaborDtlGroup
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   pageSize
   absolutePage
   employeeNum
   calendarStartDate
   calendarEndDate
   """  
   def __init__(self, obj):
      self.whereClauseLaborHed:str = obj["whereClauseLaborHed"]
      """  LaborHed where clause  """  
      self.whereClauseLaborDtl:str = obj["whereClauseLaborDtl"]
      """  LaborDtl where clause  """  
      self.whereClauseLaborDtlAttach:str = obj["whereClauseLaborDtlAttach"]
      """  LaborDtlAttach where clause  """  
      self.whereClauseLaborDtlAction:str = obj["whereClauseLaborDtlAction"]
      """  LaborDtlAction where clause  """  
      self.whereClauseLaborDtlCom:str = obj["whereClauseLaborDtlCom"]
      """  LaborDtlCom where clause  """  
      self.whereClauseLaborEquip:str = obj["whereClauseLaborEquip"]
      """  LaborEquip where clause  """  
      self.whereClauseLaborPart:str = obj["whereClauseLaborPart"]
      """  LaborPart where clause  """  
      self.whereClauseLbrScrapSerialNumbers:str = obj["whereClauseLbrScrapSerialNumbers"]
      """  LbrScrapSerialNumbers where clause  """  
      self.whereClauseTimeWorkHours:str = obj["whereClauseTimeWorkHours"]
      """  LaborTimeWorkHours where clause  """  
      self.whereClauseTimeWeeklyView:str = obj["whereClauseTimeWeeklyView"]
      """  LaborTimeWeeklyView where clause  """  
      self.whereClauseLaborDtlGroup:str = obj["whereClauseLaborDtlGroup"]
      """  LaborDtlGroup where clause  """  
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      """  SelectedSerialNumbers where clause  """  
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      """  SNFormat where clause  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page  """  
      self.employeeNum:str = obj["employeeNum"]
      """  Employee number  """  
      self.calendarStartDate:str = obj["calendarStartDate"]
      """  Calendar start date  """  
      self.calendarEndDate:str = obj["calendarEndDate"]
      """  Calendar end date  """  
      pass

class GetRowsTimeEntry_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LaborTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsWhoIsHere_input:
   """ Required : 
   whereClauseLaborHed
   whereClauseLaborDtl
   whereClauseLaborDtlCom
   whereClauseLaborEquip
   whereClauseLaborPart
   whereClauseLbrScrapSerialNumbers
   whereClauseTimeWorkHours
   whereClauseTimeWeeklyView
   whereClauseLaborDtlGroup
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   pageSize
   absolutePage
   ipSupervisorID
   """  
   def __init__(self, obj):
      self.whereClauseLaborHed:str = obj["whereClauseLaborHed"]
      self.whereClauseLaborDtl:str = obj["whereClauseLaborDtl"]
      self.whereClauseLaborDtlCom:str = obj["whereClauseLaborDtlCom"]
      self.whereClauseLaborEquip:str = obj["whereClauseLaborEquip"]
      self.whereClauseLaborPart:str = obj["whereClauseLaborPart"]
      self.whereClauseLbrScrapSerialNumbers:str = obj["whereClauseLbrScrapSerialNumbers"]
      self.whereClauseTimeWorkHours:str = obj["whereClauseTimeWorkHours"]
      self.whereClauseTimeWeeklyView:str = obj["whereClauseTimeWeeklyView"]
      self.whereClauseLaborDtlGroup:str = obj["whereClauseLaborDtlGroup"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      self.ipSupervisorID:str = obj["ipSupervisorID"]
      pass

class GetRowsWhoIsHere_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LaborTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseLaborHed
   whereClauseLaborDtl
   whereClauseLaborDtlAttch
   whereClauseLaborDtlAction
   whereClauseLaborDtlComment
   whereClauseLaborEquip
   whereClauseLaborPart
   whereClauseLbrScrapSerialNumbers
   whereClauseLaborDtlGroup
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   whereClauseTimeWeeklyView
   whereClauseTimeWorkHours
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLaborHed:str = obj["whereClauseLaborHed"]
      self.whereClauseLaborDtl:str = obj["whereClauseLaborDtl"]
      self.whereClauseLaborDtlAttch:str = obj["whereClauseLaborDtlAttch"]
      self.whereClauseLaborDtlAction:str = obj["whereClauseLaborDtlAction"]
      self.whereClauseLaborDtlComment:str = obj["whereClauseLaborDtlComment"]
      self.whereClauseLaborEquip:str = obj["whereClauseLaborEquip"]
      self.whereClauseLaborPart:str = obj["whereClauseLaborPart"]
      self.whereClauseLbrScrapSerialNumbers:str = obj["whereClauseLbrScrapSerialNumbers"]
      self.whereClauseLaborDtlGroup:str = obj["whereClauseLaborDtlGroup"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.whereClauseTimeWeeklyView:str = obj["whereClauseTimeWeeklyView"]
      self.whereClauseTimeWorkHours:str = obj["whereClauseTimeWorkHours"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LaborTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTERetrieveApproved_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTERetrieveApproved:bool = obj["opTERetrieveApproved"]
      pass

      """  output parameters  """  

class GetTERetrieveByOption_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTERetrieveByDay:bool = obj["opTERetrieveByDay"]
      self.opTERetrieveByWeek:bool = obj["opTERetrieveByWeek"]
      self.opTERetrieveByMonth:bool = obj["opTERetrieveByMonth"]
      pass

      """  output parameters  """  

class GetTERetrieveEntered_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTERetrieveEntered:bool = obj["opTERetrieveEntered"]
      pass

      """  output parameters  """  

class GetTERetrievePartiallyApproved_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTERetrievePartiallyApproved:bool = obj["opTERetrievePartiallyApproved"]
      pass

      """  output parameters  """  

class GetTERetrieveRejected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTERetrieveRejected:bool = obj["opTERetrieveRejected"]
      pass

      """  output parameters  """  

class GetTERetrieveSubmitted_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTERetrieveSubmitted:bool = obj["opTERetrieveSubmitted"]
      pass

      """  output parameters  """  

class HCMGetLaborRecords_input:
   """ Required : 
   employeeNum
   startDate
   endDate
   includeStatus
   """  
   def __init__(self, obj):
      self.employeeNum:str = obj["employeeNum"]
      """  String value with the list of employees  """  
      self.startDate:str = obj["startDate"]
      """  Start Date  """  
      self.endDate:str = obj["endDate"]
      """  End Date  """  
      self.includeStatus:str = obj["includeStatus"]
      """  String value with status value  """  
      pass

class HCMGetLaborRecords_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_HCMLaborDtlTableset] = obj["returnObj"]
      pass

class HCMSetLaborStatus_input:
   """ Required : 
   hcmDs
   """  
   def __init__(self, obj):
      self.hcmDs:list[Erp_Tablesets_HCMLaborDtlTableset] = obj["hcmDs"]
      pass

class HCMSetLaborStatus_output:
   def __init__(self, obj):
      pass

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

class InitiateDowntime_input:
   """ Required : 
   employeeNum
   indirectCode
   indirectNote
   """  
   def __init__(self, obj):
      self.employeeNum:str = obj["employeeNum"]
      """  Employee Number  """  
      self.indirectCode:str = obj["indirectCode"]
      """  Indirect Code  """  
      self.indirectNote:str = obj["indirectNote"]
      """  Indirect Labor Note  """  
      pass

class InitiateDowntime_output:
   def __init__(self, obj):
      pass

class IsHCMEnabledAtCompany_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class IsValidAssembly_input:
   """ Required : 
   pcJobNum
   piAssemblySeq
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  Job number to which this labor transaction applies.  """  
      self.piAssemblySeq:int = obj["piAssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to.  """  
      pass

class IsValidAssembly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.plFound:bool = obj["plFound"]
      pass

      """  output parameters  """  

class LaborDtlAfterGetRowsWrapper_input:
   """ Required : 
   laborDtlRow
   """  
   def __init__(self, obj):
      self.laborDtlRow:list[Erp_Tablesets_LaborDtlRow] = obj["laborDtlRow"]
      pass

class LaborDtlAfterGetRowsWrapper_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.laborDtlRow:list[Erp_Tablesets_LaborDtlRow] = obj["laborDtlRow"]
      pass

      """  output parameters  """  

class LaborHedPayrollDateChanging_input:
   """ Required : 
   payrollDate
   ds
   """  
   def __init__(self, obj):
      self.payrollDate:str = obj["payrollDate"]
      """  Payroll Date  """  
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class LaborHedPayrollDateChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LaborRateCalc_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class LaborRateCalc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeClockInDate_input:
   """ Required : 
   ds
   ipClockInDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ipClockInDate:str = obj["ipClockInDate"]
      """  Proposed Clock In Date  """  
      pass

class OnChangeClockInDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLaborPartScrapQty_input:
   """ Required : 
   ds
   scrapQty
   sysRowID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.scrapQty:int = obj["scrapQty"]
      """  Proposed change to PartQty field  """  
      self.sysRowID:str = obj["sysRowID"]
      """  sysRowID of line updated in LaborPart  """  
      pass

class OnChangeLaborPartScrapQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangePCID_input:
   """ Required : 
   pcid
   isNonConformance
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  PCID to validate  """  
      self.isNonConformance:bool = obj["isNonConformance"]
      """  Is this the NonConformance PCID  """  
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class OnChangePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartQty_input:
   """ Required : 
   ds
   partQty
   sysRowID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.partQty:int = obj["partQty"]
      """  Proposed change to PartQty field  """  
      self.sysRowID:str = obj["sysRowID"]
      """  sysRowID of line updated in LaborPart  """  
      pass

class OnChangePartQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeQuickEntryCode_input:
   """ Required : 
   ipEmpID
   ipQuickEntryCode
   ds
   """  
   def __init__(self, obj):
      self.ipEmpID:str = obj["ipEmpID"]
      """  Proposed EmpID value  """  
      self.ipQuickEntryCode:str = obj["ipQuickEntryCode"]
      """  Proposed QuickEntryCode value  """  
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class OnChangeQuickEntryCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeResourceGrpID_input:
   """ Required : 
   ds
   ipResourceGrpID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ipResourceGrpID:str = obj["ipResourceGrpID"]
      """  Proposed Resource Group  """  
      pass

class OnChangeResourceGrpID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnLoadEndActivity_input:
   """ Required : 
   iLaborHedSeq
   iLaborDtlSeq
   """  
   def __init__(self, obj):
      self.iLaborHedSeq:int = obj["iLaborHedSeq"]
      """  The LaborHedSeq of the LaborHed record to retrieve  """  
      self.iLaborDtlSeq:int = obj["iLaborDtlSeq"]
      """  The LaborDtlSeq of the LaborDtl record to retrieve  """  
      pass

class OnLoadEndActivity_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LaborTableset] = obj["returnObj"]
      pass

class OverridesResource_input:
   """ Required : 
   ds
   ProposedResourceID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.ProposedResourceID:str = obj["ProposedResourceID"]
      """  The proposed resource id  """  
      pass

class OverridesResource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Overrides_input:
   """ Required : 
   ds
   inOpCode
   inResGrpID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.inOpCode:str = obj["inOpCode"]
      """  OpCode to override  """  
      self.inResGrpID:str = obj["inResGrpID"]
      """  Resource Group OD to override  """  
      pass

class Overrides_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RecallFromApprovalBySelected_input:
   """ Required : 
   ds
   weeklyView
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.weeklyView:bool = obj["weeklyView"]
      """  Is this method being called with WeeklyView records?  """  
      pass

class RecallFromApprovalBySelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.messageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class RecallFromApproval_input:
   """ Required : 
   ds
   lWeeklyView
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.lWeeklyView:bool = obj["lWeeklyView"]
      """  Is this method being called with WeeklyView records?  """  
      pass

class RecallFromApproval_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class ReportPartQtyAllowed_input:
   """ Required : 
   ip_JobNum
   ip_AssemblySeq
   ip_OprSeq
   """  
   def __init__(self, obj):
      self.ip_JobNum:str = obj["ip_JobNum"]
      """  Job number  """  
      self.ip_AssemblySeq:int = obj["ip_AssemblySeq"]
      """  Assembly Sequence number  """  
      self.ip_OprSeq:int = obj["ip_OprSeq"]
      """  Operation Sequence number  """  
      pass

class ReportPartQtyAllowed_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ReviewIsDocumentLock_input:
   """ Required : 
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.laborHedSeq:str = obj["laborHedSeq"]
      """  Labor Hed Sequence  """  
      self.laborDtlSeq:str = obj["laborDtlSeq"]
      """  Labor Detail Sequence  """  
      pass

class ReviewIsDocumentLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class SelectAllForWork_input:
   """ Required : 
   laborDS
   selectedWorkQueueRows
   empID
   resourceGrpID
   resourceID
   laborType
   """  
   def __init__(self, obj):
      self.laborDS:list[Erp_Tablesets_LaborTableset] = obj["laborDS"]
      self.selectedWorkQueueRows:list[Erp_Tablesets_WorkQueueRow] = obj["selectedWorkQueueRows"]
      """  Selected rows from Work Queue / type WorkQueueTable  """  
      self.empID:str = obj["empID"]
      """  Employee ID which is starting the activities.  """  
      self.resourceGrpID:str = obj["resourceGrpID"]
      """  Resource Group ID for all activities.  """  
      self.resourceID:str = obj["resourceID"]
      """  Resource used for all activities.  """  
      self.laborType:str = obj["laborType"]
      """  Labor Type, can be 'P' for Production or 'S' for Setup  """  
      pass

class SelectAllForWork_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.laborDS:list[Erp_Tablesets_LaborTableset] = obj["laborDS"]
      self.warningsMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class SelectForWorkCheckWarnings_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class SelectForWorkCheckWarnings_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class SelectForWork_input:
   """ Required : 
   ds
   pcResourceGrpId
   pcResourceId
   pcLaborType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.pcResourceGrpId:str = obj["pcResourceGrpId"]
      """  The Resource Group id for this work.  """  
      self.pcResourceId:str = obj["pcResourceId"]
      """  The Resource id for this work.  """  
      self.pcLaborType:str = obj["pcLaborType"]
      """  Labor Type: S=Setup, P=Production  """  
      pass

class SelectForWork_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetClockInAndDisplayTimeMES_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class SetClockInAndDisplayTimeMES_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetTERetrieveApproved_input:
   """ Required : 
   ipTERetrieveApproved
   """  
   def __init__(self, obj):
      self.ipTERetrieveApproved:bool = obj["ipTERetrieveApproved"]
      """  Value to set UserFile.TERetrieveApproved Yes/No  """  
      pass

class SetTERetrieveApproved_output:
   def __init__(self, obj):
      pass

class SetTERetrieveByDay_input:
   """ Required : 
   ipTERetrieveByDay
   """  
   def __init__(self, obj):
      self.ipTERetrieveByDay:bool = obj["ipTERetrieveByDay"]
      """  Value to set the by day option Yes/No  """  
      pass

class SetTERetrieveByDay_output:
   def __init__(self, obj):
      pass

class SetTERetrieveByMonth_input:
   """ Required : 
   ipTERetrieveByMonth
   """  
   def __init__(self, obj):
      self.ipTERetrieveByMonth:bool = obj["ipTERetrieveByMonth"]
      """  Value to set the by month option Yes/No  """  
      pass

class SetTERetrieveByMonth_output:
   def __init__(self, obj):
      pass

class SetTERetrieveByWeek_input:
   """ Required : 
   ipTERetrieveByWeek
   """  
   def __init__(self, obj):
      self.ipTERetrieveByWeek:bool = obj["ipTERetrieveByWeek"]
      """  Value to set the by week option Yes/No  """  
      pass

class SetTERetrieveByWeek_output:
   def __init__(self, obj):
      pass

class SetTERetrieveEntered_input:
   """ Required : 
   ipTERetrieveEntered
   """  
   def __init__(self, obj):
      self.ipTERetrieveEntered:bool = obj["ipTERetrieveEntered"]
      """  Value to set UserFile.TERetrieveEntered Yes/No  """  
      pass

class SetTERetrieveEntered_output:
   def __init__(self, obj):
      pass

class SetTERetrievePartiallyApproved_input:
   """ Required : 
   ipTERetrievePartiallyApproved
   """  
   def __init__(self, obj):
      self.ipTERetrievePartiallyApproved:bool = obj["ipTERetrievePartiallyApproved"]
      """  Value to set UserFile.TERetrievePartiallyApproved Yes/No  """  
      pass

class SetTERetrievePartiallyApproved_output:
   def __init__(self, obj):
      pass

class SetTERetrieveRejected_input:
   """ Required : 
   ipTERetrieveRejected
   """  
   def __init__(self, obj):
      self.ipTERetrieveRejected:bool = obj["ipTERetrieveRejected"]
      """  Value to set UserFile.TERetrieveRejected Yes/No  """  
      pass

class SetTERetrieveRejected_output:
   def __init__(self, obj):
      pass

class SetTERetrieveSubmitted_input:
   """ Required : 
   ipTERetrieveSubmitted
   """  
   def __init__(self, obj):
      self.ipTERetrieveSubmitted:bool = obj["ipTERetrieveSubmitted"]
      """  Value to set UserFile.TERetrieveSubmitted Yes/No  """  
      pass

class SetTERetrieveSubmitted_output:
   def __init__(self, obj):
      pass

class StartActivityByEmp_input:
   """ Required : 
   employeeID
   startType
   ds
   """  
   def __init__(self, obj):
      self.employeeID:str = obj["employeeID"]
      """  Employee ID  """  
      self.startType:str = obj["startType"]
      """  The type of activity being started.
            Values are: P - Production
            I - Indirect
            S - Setup
            R - Rework  """  
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class StartActivityByEmp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StartActivity_input:
   """ Required : 
   LaborHedSeq
   StartType
   ds
   """  
   def __init__(self, obj):
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  The labor header sequence  """  
      self.StartType:str = obj["StartType"]
      """  The type of activity being started.
            Values are: P - Production
            I - Indirect
            S - Setup
            R - Rework  """  
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class StartActivity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SubmitForApprovalBySelected_input:
   """ Required : 
   ds
   weeklyView
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.weeklyView:bool = obj["weeklyView"]
      """  Is this method being called with WeeklyView records?  """  
      pass

class SubmitForApprovalBySelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.messageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class SubmitForApproval_input:
   """ Required : 
   ds
   lWeeklyView
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.lWeeklyView:bool = obj["lWeeklyView"]
      """  Is this method being called with WeeklyView records?  """  
      pass

class SubmitForApproval_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLaborTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLaborTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateChargeRateForTimeType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class ValidateChargeRateForTimeType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateIndirectCodeIsDowntime_input:
   """ Required : 
   indirectCode
   """  
   def __init__(self, obj):
      self.indirectCode:str = obj["indirectCode"]
      pass

class ValidateIndirectCodeIsDowntime_output:
   def __init__(self, obj):
      pass

class ValidateProjectClosed_input:
   """ Required : 
   projectID
   jobNum
   laborTypePseudo
   """  
   def __init__(self, obj):
      self.projectID:str = obj["projectID"]
      self.jobNum:str = obj["jobNum"]
      self.laborTypePseudo:str = obj["laborTypePseudo"]
      pass

class ValidateProjectClosed_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateSerialAfterSelect_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class ValidateSerialAfterSelect_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSerialBeforeSelect_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class ValidateSerialBeforeSelect_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.notEnoughSerials:str = obj["parameters"]
      self.totSNReq:int = obj["parameters"]
      self.totNewSNReq:int = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateSerialScanInterface_input:
   """ Required : 
   jobNum
   assemblySeq
   partNum
   proposedSN
   oprSeq
   laborHedSeq
   laborDtlSeq
   rework
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  JobNum of the SN  """  
      self.assemblySeq:int = obj["assemblySeq"]
      """  AssemblySeq of the SN  """  
      self.partNum:str = obj["partNum"]
      """  PartNum of the SN  """  
      self.proposedSN:str = obj["proposedSN"]
      """  Proposed SN  """  
      self.oprSeq:int = obj["oprSeq"]
      """  Operation sequence of the labor detail  """  
      self.laborHedSeq:int = obj["laborHedSeq"]
      """  Labor Head sequence of the labor detail  """  
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      """  Labor Detail sequence of the labor detail  """  
      self.rework:bool = obj["rework"]
      """  Indicates if labor record is rework  """  
      pass

class ValidateSerialScanInterface_output:
   def __init__(self, obj):
      pass

class VerifyScrapQty_input:
   """ Required : 
   ds
   scrapQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.scrapQty:int = obj["scrapQty"]
      """  Proposed change to ScrapQty field  """  
      pass

class VerifyScrapQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class VerifySerialMatch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      pass

class VerifySerialMatch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.pcMsg:str = obj["parameters"]
      self.piMsgType:int = obj["parameters"]
      pass

      """  output parameters  """  

class chkReportQtyShopWarn_input:
   """ Required : 
   company
   jobNum
   assemblySeq
   oprSeq
   empID
   activeTrans
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company ID in ReportQty record  """  
      self.jobNum:str = obj["jobNum"]
      """  Job Number in ReportQty record  """  
      self.assemblySeq:int = obj["assemblySeq"]
      """  Assembly Sequence Number in ReportQty record  """  
      self.oprSeq:int = obj["oprSeq"]
      """  Operation Sequence Number in ReportQty record  """  
      self.empID:str = obj["empID"]
      """  Employee ID in ReportQty record  """  
      self.activeTrans:bool = obj["activeTrans"]
      """  Active Transaction FLAG in ReportQty record  """  
      pass

class chkReportQtyShopWarn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class getElapsedTime_input:
   """ Required : 
   startDate
   startTime
   """  
   def __init__(self, obj):
      self.startDate:str = obj["startDate"]
      """  Initial Date  """  
      self.startTime:int = obj["startTime"]
      """  Initial Time  """  
      pass

class getElapsedTime_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class validateNonConfProcessed_input:
   """ Required : 
   ds
   laborHedSeq
   laborDtlSeq
   vDiscrepQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      self.vDiscrepQty:int = obj["vDiscrepQty"]
      pass

class validateNonConfProcessed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

