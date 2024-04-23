import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MobileLaborSvc
# Description: MobileLaborSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MobileLabors(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MobileLabors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileLabors
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors",headers=creds) as resp:
           return await resp.json()

async def post_MobileLabors(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileLabors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileLaborHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MobileLaborHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MobileLabors_Company_LaborHedSeq(Company, LaborHedSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileLabor item
   Description: Calls GetByID to retrieve the MobileLabor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLabor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileLaborHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors(" + Company + "," + LaborHedSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MobileLabors_Company_LaborHedSeq(Company, LaborHedSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MobileLabor for the service
   Description: Calls UpdateExt to update MobileLabor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileLabor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileLaborHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors(" + Company + "," + LaborHedSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MobileLabors_Company_LaborHedSeq(Company, LaborHedSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MobileLabor item
   Description: Call UpdateExt to delete MobileLabor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileLabor
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors(" + Company + "," + LaborHedSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileLabors_Company_LaborHedSeq_MobileLaborDtls(Company, LaborHedSeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MobileLaborDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MobileLaborDtls1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors(" + Company + "," + LaborHedSeq + ")/MobileLaborDtls",headers=creds) as resp:
           return await resp.json()

async def get_MobileLabors_Company_LaborHedSeq_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileLaborDtl item
   Description: Calls GetByID to retrieve the MobileLaborDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLaborDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLabors(" + Company + "," + LaborHedSeq + ")/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileLaborDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MobileLaborDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileLaborDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls",headers=creds) as resp:
           return await resp.json()

async def post_MobileLaborDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileLaborDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileLaborDtl item
   Description: Calls GetByID to retrieve the MobileLaborDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLaborDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MobileLaborDtl for the service
   Description: Calls UpdateExt to update MobileLaborDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileLaborDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MobileLaborDtl item
   Description: Call UpdateExt to delete MobileLaborDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileLaborDtl
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq_MobileLaborDtlComments(Company, LaborHedSeq, LaborDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MobileLaborDtlComments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MobileLaborDtlComments1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborDtlCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/MobileLaborDtlComments",headers=creds) as resp:
           return await resp.json()

async def get_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq_MobileLaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company, LaborHedSeq, LaborDtlSeq, CommentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileLaborDtlComment item
   Description: Calls GetByID to retrieve the MobileLaborDtlComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLaborDtlComment1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/MobileLaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq_MobileLaborDtlAttches(Company, LaborHedSeq, LaborDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MobileLaborDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MobileLaborDtlAttches1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/MobileLaborDtlAttches",headers=creds) as resp:
           return await resp.json()

async def get_MobileLaborDtls_Company_LaborHedSeq_LaborDtlSeq_MobileLaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company, LaborHedSeq, LaborDtlSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileLaborDtlAttch item
   Description: Calls GetByID to retrieve the MobileLaborDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLaborDtlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/MobileLaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileLaborDtlComments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MobileLaborDtlComments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileLaborDtlComments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborDtlCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlComments",headers=creds) as resp:
           return await resp.json()

async def post_MobileLaborDtlComments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileLaborDtlComments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlCommentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlCommentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlComments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MobileLaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company, LaborHedSeq, LaborDtlSeq, CommentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileLaborDtlComment item
   Description: Calls GetByID to retrieve the MobileLaborDtlComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLaborDtlComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MobileLaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company, LaborHedSeq, LaborDtlSeq, CommentNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MobileLaborDtlComment for the service
   Description: Calls UpdateExt to update MobileLaborDtlComment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileLaborDtlComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlCommentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MobileLaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company, LaborHedSeq, LaborDtlSeq, CommentNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MobileLaborDtlComment item
   Description: Call UpdateExt to delete MobileLaborDtlComment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileLaborDtlComment
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileLaborDtlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MobileLaborDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileLaborDtlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlAttches",headers=creds) as resp:
           return await resp.json()

async def post_MobileLaborDtlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileLaborDtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MobileLaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company, LaborHedSeq, LaborDtlSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileLaborDtlAttch item
   Description: Calls GetByID to retrieve the MobileLaborDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileLaborDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MobileLaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company, LaborHedSeq, LaborDtlSeq, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MobileLaborDtlAttch for the service
   Description: Calls UpdateExt to update MobileLaborDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileLaborDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileLaborDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MobileLaborDtlAttches_Company_LaborHedSeq_LaborDtlSeq_DrawingSeq(Company, LaborHedSeq, LaborDtlSeq, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MobileLaborDtlAttch item
   Description: Call UpdateExt to delete MobileLaborDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileLaborDtlAttch
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileLaborDtlAttches(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileApproverLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MobileApproverLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileApproverLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileApproverListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileApproverLists",headers=creds) as resp:
           return await resp.json()

async def post_MobileApproverLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileApproverLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileApproverListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MobileApproverListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileApproverLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MobileApproverLists_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileApproverList item
   Description: Calls GetByID to retrieve the MobileApproverList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileApproverList
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileApproverListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileApproverLists(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MobileApproverLists_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MobileApproverList for the service
   Description: Calls UpdateExt to update MobileApproverList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileApproverList
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileApproverListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileApproverLists(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MobileApproverLists_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MobileApproverList item
   Description: Call UpdateExt to delete MobileApproverList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileApproverList
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileApproverLists(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileQuickEntryViews(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MobileQuickEntryViews items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileQuickEntryViews
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileQuickEntryViewRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileQuickEntryViews",headers=creds) as resp:
           return await resp.json()

async def post_MobileQuickEntryViews(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileQuickEntryViews
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileQuickEntryViewRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MobileQuickEntryViewRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileQuickEntryViews", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MobileQuickEntryViews_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileQuickEntryView item
   Description: Calls GetByID to retrieve the MobileQuickEntryView item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileQuickEntryView
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileQuickEntryViewRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileQuickEntryViews(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MobileQuickEntryViews_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MobileQuickEntryView for the service
   Description: Calls UpdateExt to update MobileQuickEntryView. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileQuickEntryView
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileQuickEntryViewRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileQuickEntryViews(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MobileQuickEntryViews_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MobileQuickEntryView item
   Description: Call UpdateExt to delete MobileQuickEntryView item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileQuickEntryView
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileQuickEntryViews(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_MobileTimeWeeklyViews(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MobileTimeWeeklyViews items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MobileTimeWeeklyViews
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileTimeWeeklyViewRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileTimeWeeklyViews",headers=creds) as resp:
           return await resp.json()

async def post_MobileTimeWeeklyViews(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MobileTimeWeeklyViews
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MobileTimeWeeklyViewRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MobileTimeWeeklyViewRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileTimeWeeklyViews", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MobileTimeWeeklyViews_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MobileTimeWeeklyView item
   Description: Calls GetByID to retrieve the MobileTimeWeeklyView item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MobileTimeWeeklyView
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MobileTimeWeeklyViewRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileTimeWeeklyViews(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MobileTimeWeeklyViews_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MobileTimeWeeklyView for the service
   Description: Calls UpdateExt to update MobileTimeWeeklyView. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MobileTimeWeeklyView
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MobileTimeWeeklyViewRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileTimeWeeklyViews(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MobileTimeWeeklyViews_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MobileTimeWeeklyView item
   Description: Call UpdateExt to delete MobileTimeWeeklyView item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MobileTimeWeeklyView
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/MobileTimeWeeklyViews(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MobileLaborListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMobileLaborHed, whereClauseMobileLaborDtl, whereClauseMobileLaborDtlAttch, whereClauseMobileLaborDtlComment, whereClauseMobileApproverList, whereClauseMobileQuickEntryView, whereClauseMobileTimeWeeklyView, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMobileLaborHed=" + whereClauseMobileLaborHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMobileLaborDtl=" + whereClauseMobileLaborDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMobileLaborDtlAttch=" + whereClauseMobileLaborDtlAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMobileLaborDtlComment=" + whereClauseMobileLaborDtlComment
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMobileApproverList=" + whereClauseMobileApproverList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMobileQuickEntryView=" + whereClauseMobileQuickEntryView
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMobileTimeWeeklyView=" + whereClauseMobileTimeWeeklyView
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetApprovalStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetApprovalStatus
   Description: Populates the MobileApproverList Temp Table with the current expense's approver data.
   OperationID: MobileGetApprovalStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetApprovalStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetApprovalStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetQuickEntry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetQuickEntry
   Description: Populates the MobileQuickEntryView Temp Table with the current employee QuickEntry data.
   OperationID: MobileGetQuickEntry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetQuickEntry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetQuickEntry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: MobileGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetRowsWithFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetRowsWithFilter
   Description: Returns a dataset containing all rows that satisfy the where clauses and filters.
   OperationID: MobileGetRowsWithFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetRowsWithFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRowsWithFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetByID
   Description: Returns a DataSet given the primary key.
   OperationID: MobileGetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileLaborGetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileLaborGetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: MobileLaborGetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileLaborGetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileLaborGetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMobileLaborDtlAttchs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMobileLaborDtlAttchs
   Description: Custom Method to retrieve only the MobileLaborDtlAttch records for the current labor
   OperationID: GetMobileLaborDtlAttchs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMobileLaborDtlAttchs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMobileLaborDtlAttchs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMobileLaborDtlComments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMobileLaborDtlComments
   Description: Custom Method to retrieve only the MobileLaborDtlComment records for the current labor
   OperationID: GetMobileLaborDtlComments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMobileLaborDtlComments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMobileLaborDtlComments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetNewLaborHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetNewLaborHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: MobileGetNewLaborHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetNewLaborDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetNewLaborDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: MobileGetNewLaborDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetNewLaborDtlComment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetNewLaborDtlComment
   Description: Calls GetNewLaborDtlComment base method then assign selected and default values.
   OperationID: MobileGetNewLaborDtlComment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborDtlComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborDtlComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetNewLaborDtlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetNewLaborDtlAttch
   Description: Calls GetNewLaborDtlAttch base method then assign selected and default values.
   OperationID: MobileGetNewLaborDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetNewLaborDtlOnSelectForWork(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetNewLaborDtlOnSelectForWork
   Description: Call GetNewLaborDtl base method then assign selected values and default values
   OperationID: MobileGetNewLaborDtlOnSelectForWork
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborDtlOnSelectForWork_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborDtlOnSelectForWork_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetNewLaborDtlNoHdr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetNewLaborDtlNoHdr
   Description: This method is called to add a new labor detail without having a labor header
   OperationID: MobileGetNewLaborDtlNoHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborDtlNoHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborDtlNoHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetNewLaborDtlWithHdr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetNewLaborDtlWithHdr
   Description: This method is called to add a new labor detail without having a labor header record available
   OperationID: MobileGetNewLaborDtlWithHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetNewLaborDtlWithHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewLaborDtlWithHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetNewTimeWeeklyView(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetNewTimeWeeklyView
   Description: Gets a new TimeWeeklyView record for the current week
   OperationID: MobileGetNewTimeWeeklyView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetNewTimeWeeklyView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetNewTimeWeeklyView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileDeleteLaborDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileDeleteLaborDtl
   Description: This method delete records related to HCM PTO.
   OperationID: MobileDeleteLaborDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileDeleteLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDeleteLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileDelete
   Description: Method to call to delete expense records
   OperationID: MobileDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileLaborUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileLaborUpdate
   Description: Commits the DataSet changes to the data store.
   OperationID: MobileLaborUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileLaborUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileLaborUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileChangeEquipID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileChangeEquipID
   Description: This method should call when EquipID is changed
   OperationID: MobileChangeEquipID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileChangeEquipID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileChangeEquipID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileChangeIndirectCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileChangeIndirectCode
   Description: This method should call when IndirectCode is changed
   OperationID: MobileChangeIndirectCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileChangeIndirectCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileChangeIndirectCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileChangeLaborType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileChangeLaborType
   Description: This method should call when LaborType is changed
   OperationID: MobileChangeLaborType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileChangeLaborType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileChangeLaborType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileChangeResourceId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileChangeResourceId
   Description: This method should call when ResourceID is changed
   OperationID: MobileChangeResourceId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileChangeResourceId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileChangeResourceId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileCheckResourceGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileCheckResourceGroup
   Description: This method should call when ResourceGroup is changed
   OperationID: MobileCheckResourceGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileCheckResourceGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileCheckResourceGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileCheckWarnings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileCheckWarnings
   Description: This method runs the labor warning routine and returns any warnings the user
needs to be aware of. This needs to be run right before the update method. If
the user answers okay to all of the questions, then the update method can be
run. Otherwise the labor record needs to be corrected
   OperationID: MobileCheckWarnings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileCheckWarnings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileCheckWarnings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileDefaultDtlTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileDefaultDtlTime
   Description: Sets Default DtlTime
   OperationID: MobileDefaultDtlTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileDefaultDtlTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultDtlTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileDefaultIndirect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileDefaultIndirect
   Description: Sets Default Indirect
   OperationID: MobileDefaultIndirect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileDefaultIndirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultIndirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileDefaultJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileDefaultJobNum
   Description: Sets Default JobNum
   OperationID: MobileDefaultJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileDefaultJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileDefaultLaborHrs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileDefaultLaborHrs
   Description: Sets Default LaborHrs
   OperationID: MobileDefaultLaborHrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileDefaultLaborHrs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultLaborHrs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileDefaultLaborQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileDefaultLaborQty
   Description: Sets Default LaborQty
   OperationID: MobileDefaultLaborQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileDefaultLaborQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultLaborQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileDefaultPhaseOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileDefaultPhaseOprSeq
   Description: Sets Default PhaseOprSeq
   OperationID: MobileDefaultPhaseOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileDefaultPhaseOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultPhaseOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileDefaultOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileDefaultOprSeq
   Description: Sets Default OprSeq
   OperationID: MobileDefaultOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileDefaultOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileVerifyScrapQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileVerifyScrapQty
   Description: This method defaults fields when the scrap qty field changes. Also checks for any labor warnings the user needs to be aware of
   OperationID: MobileVerifyScrapQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileVerifyScrapQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileVerifyScrapQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileDefaultLaborType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileDefaultLaborType
   Description: Sets Default LaborType
   OperationID: MobileDefaultLaborType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileDefaultLaborType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultLaborType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRecall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRecall
   Description: The procedure is called prior to performing a recall.  It will check
if subsequent approvals have occurred.  If they have the user
will have the opportunity to cancel the recall.
   OperationID: CheckRecall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRecall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRecall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecallTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecallTrans
   Description: Method to call when recalling from approval entry
   OperationID: RecallTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecallTrans_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallTrans_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyLaborDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyLaborDetail
   Description: Method to copy the values from one LaborDtl record to a new LaborDtl record.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileSync(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileSync
   Description: Method to call to synchronize draft records to the database
   OperationID: MobileSync
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileSync_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileSync_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileSyncSuccessful(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileSyncSuccessful
   Description: Receives the fields needed to find and delete the validation record created when synchronization is successful
   OperationID: MobileSyncSuccessful
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileSyncSuccessful_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileSyncSuccessful_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileAttachmentUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileAttachmentUpdate
   Description: Method to call to update attachment record and upload file to the storage defined by document type (or default company storage)
   OperationID: MobileAttachmentUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileAttachmentUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileAttachmentUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetHomePageData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetHomePageData
   OperationID: MobileGetHomePageData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetHomePageData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetHomePageData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileOverrides(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileOverrides
   Description: Method to be called by Mobile Time entry. Overrides the Resource Group and Operation Code in a job.
   OperationID: MobileOverrides
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileOverrides_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileOverrides_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileDefaultPhaseID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileDefaultPhaseID
   Description: This method to be called by Mobile Time entry. Defaults dataset fields when the PhaseID field changes.
   OperationID: MobileDefaultPhaseID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileDefaultPhaseID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileDefaultPhaseID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileRecallFromApproval(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileRecallFromApproval
   Description: Method to recall Labor for Approval.
   OperationID: MobileRecallFromApproval
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileRecallFromApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileRecallFromApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVersion(epicorHeaders = None):
   """  
   Summary: Invoke method GetVersion
   Description: Returns BO Version
   OperationID: GetVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SubmitSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SubmitSelected
   Description: Method to call to submit selected time
   OperationID: SubmitSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ApproveReject(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApproveReject
   Description: The procedure is called when the user selects EmpExpense records for reject or approve
   OperationID: ApproveReject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveReject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveReject_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetRowsPendingApproval(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetRowsPendingApproval
   OperationID: MobileGetRowsPendingApproval
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetRowsPendingApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRowsPendingApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetRowsPendingApprovalWithFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetRowsPendingApprovalWithFilter
   OperationID: MobileGetRowsPendingApprovalWithFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetRowsPendingApprovalWithFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRowsPendingApprovalWithFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMobileLaborHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMobileLaborHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileLaborHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMobileLaborHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileLaborHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMobileLaborDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMobileLaborDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileLaborDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMobileLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMobileLaborDtlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMobileLaborDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileLaborDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMobileLaborDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileLaborDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMobileLaborDtlComment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMobileLaborDtlComment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMobileLaborDtlComment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMobileLaborDtlComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMobileLaborDtlComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileLaborSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileApproverListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MobileApproverListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MobileLaborDtlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlCommentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MobileLaborDtlCommentRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MobileLaborDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MobileLaborHedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileLaborListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MobileLaborListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileQuickEntryViewRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MobileQuickEntryViewRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MobileTimeWeeklyViewRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MobileTimeWeeklyViewRow] = obj["value"]
      pass

class Erp_Tablesets_MobileApproverListRow:
   def __init__(self, obj):
      self.ApprovalStatus:str = obj["ApprovalStatus"]
      """  The status of the current approval task.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  Date when the approval task was completed.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For a task related to an Expense this field would contain the related EmployeeID. For a task related to Labor this field would contain the related LaborHed.  """  
      self.Key2:str = obj["Key2"]
      """  Second component of the foreign key to the related master record. For a task related to an Expense, this field would contain the related ExpenseID. For a task related to Labor, this field would contain the related LaborDtl.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the task is related.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep that this task is assigned to.  """  
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name corresponding to the SalesRepCode.  """  
      self.SequenceNum:int = obj["SequenceNum"]
      """  Number used to display the records in their correct sequence in the mobile app.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileLaborDtlAttchRow:
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

class Erp_Tablesets_MobileLaborDtlCommentRow:
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
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileLaborDtlRow:
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
      self.HasAttachments:bool = obj["HasAttachments"]
      """  Indicates if the labor detail has attachments  """  
      self.HasComments:bool = obj["HasComments"]
      """  Indicates if the labor detail has comments  """  
      self.EnableComplete:bool = obj["EnableComplete"]
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.EnteredOnCurPlant:bool = obj["EnteredOnCurPlant"]
      """  To know if the LaborDtl was created on the current plant  """  
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      self.ApprovedBy:str = obj["ApprovedBy"]
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available for an approver  """  
      self.JobType:str = obj["JobType"]
      """  This field is used to get the translated value of JobTypeCode.  """  
      self.JobTypeCode:str = obj["JobTypeCode"]
      """   Indicates the type of job. Possible values are:
MFG - Manufacture
SRV - Service
PRJ - Project
MNT - Maintenance  """  
      self.GroupByLaborType:str = obj["GroupByLaborType"]
      """  Used for the Labor Type grouping. A new column was needed to differentiate between records with the same Labor Type (e.g. Production and Maintenance).  """  
      self.EquipID:str = obj["EquipID"]
      """  The ID of the Equipment that this "Maintenance Job" is for.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.IndirectDescription:str = obj["IndirectDescription"]
      self.JobAsmblDescription:str = obj["JobAsmblDescription"]
      self.JobAsmblPartNum:str = obj["JobAsmblPartNum"]
      self.OpDescOpDesc:str = obj["OpDescOpDesc"]
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileLaborHedRow:
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
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileLaborListRow:
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileQuickEntryViewRow:
   def __init__(self, obj):
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.ExpenseCode:str = obj["ExpenseCode"]
      self.IndirectCode:str = obj["IndirectCode"]
      self.JobNum:str = obj["JobNum"]
      self.JobTypeCode:str = obj["JobTypeCode"]
      """   Indicates the type of job. Possible values are:
MFG - Manufacture
SRV - Service
PRJ - Project
MNT - Maintenance  """  
      self.LaborHrs:int = obj["LaborHrs"]
      self.LaborType:str = obj["LaborType"]
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      self.OpCode:str = obj["OpCode"]
      self.OperDesc:str = obj["OperDesc"]
      """  Operation Description  """  
      self.OprSeq:int = obj["OprSeq"]
      self.PhaseID:str = obj["PhaseID"]
      self.ProjectID:str = obj["ProjectID"]
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.ResourceID:str = obj["ResourceID"]
      self.RoleCode:str = obj["RoleCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileTimeWeeklyViewRow:
   def __init__(self, obj):
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.ASMdesc:str = obj["ASMdesc"]
      """  Job Assembly description  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.Company:str = obj["Company"]
      self.Complete:bool = obj["Complete"]
      self.DeleteRow:bool = obj["DeleteRow"]
      self.DisLaborType:bool = obj["DisLaborType"]
      self.DisPrjRoleCd:bool = obj["DisPrjRoleCd"]
      self.DisTimeTypCd:bool = obj["DisTimeTypCd"]
      self.EmployeeNum:str = obj["EmployeeNum"]
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy function is available  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if recall is available  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if submit is available  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HCMTotWeeklyPayHours:int = obj["HCMTotWeeklyPayHours"]
      """  HCM Integration Total Weekly Pay Hours  """  
      self.HoursFri:int = obj["HoursFri"]
      self.HoursMon:int = obj["HoursMon"]
      self.HoursSat:int = obj["HoursSat"]
      self.HoursSun:int = obj["HoursSun"]
      self.HoursThu:int = obj["HoursThu"]
      self.HoursTotal:int = obj["HoursTotal"]
      self.HoursTue:int = obj["HoursTue"]
      self.HoursWed:int = obj["HoursWed"]
      self.IndirectCode:str = obj["IndirectCode"]
      self.IndirectCodeDescription:str = obj["IndirectCodeDescription"]
      self.JCDept:str = obj["JCDept"]
      self.JobNum:str = obj["JobNum"]
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      self.LaborRate:int = obj["LaborRate"]
      self.LaborType:str = obj["LaborType"]
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      self.MessageText:str = obj["MessageText"]
      self.NewRowType:str = obj["NewRowType"]
      """  Valid values are "A" for an Add of a new TimeWeeklyView row and "C" for a Copy of an existing TimeWeeklyView row.  """  
      self.OpCode:str = obj["OpCode"]
      self.OpComplete:bool = obj["OpComplete"]
      self.OperDesc:str = obj["OperDesc"]
      """  Operation Description  """  
      self.OprSeq:int = obj["OprSeq"]
      self.PhaseID:str = obj["PhaseID"]
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      self.ProjDesc:str = obj["ProjDesc"]
      self.ProjectID:str = obj["ProjectID"]
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.ResourceGrpIDDescription:str = obj["ResourceGrpIDDescription"]
      self.ResourceID:str = obj["ResourceID"]
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      self.RoleCd:str = obj["RoleCd"]
      self.RoleCdDescription:str = obj["RoleCdDescription"]
      self.Shift:int = obj["Shift"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """   If the Time is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  """  
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TimeStatus:str = obj["TimeStatus"]
      self.TimeTypCd:str = obj["TimeTypCd"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.WBSPhaseDesc:str = obj["WBSPhaseDesc"]
      """  WBS Phase Project Description  """  
      self.WeekBeginDate:str = obj["WeekBeginDate"]
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.WeekEndDate:str = obj["WeekEndDate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ApproveReject_input:
   """ Required : 
   salesRepCode
   action
   comment
   ds
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      """  The sales Rep Code of the approver.  """  
      self.action:str = obj["action"]
      """  Action to take A = approver, R = reject.  """  
      self.comment:str = obj["comment"]
      """  Comment text if comments are to be created.  """  
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class ApproveReject_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckRecall_input:
   """ Required : 
   salesRepCode
   ds
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      """  The sales Rep Code of the approver.  """  
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class CheckRecall_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.outRecallMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CopyLaborDetail_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class CopyLaborDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.messageText:str = obj["parameters"]
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

class Erp_Tablesets_MobileApproverListRow:
   def __init__(self, obj):
      self.ApprovalStatus:str = obj["ApprovalStatus"]
      """  The status of the current approval task.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  Date when the approval task was completed.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For a task related to an Expense this field would contain the related EmployeeID. For a task related to Labor this field would contain the related LaborHed.  """  
      self.Key2:str = obj["Key2"]
      """  Second component of the foreign key to the related master record. For a task related to an Expense, this field would contain the related ExpenseID. For a task related to Labor, this field would contain the related LaborDtl.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the task is related.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep that this task is assigned to.  """  
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name corresponding to the SalesRepCode.  """  
      self.SequenceNum:int = obj["SequenceNum"]
      """  Number used to display the records in their correct sequence in the mobile app.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileLaborDtlAttchRow:
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

class Erp_Tablesets_MobileLaborDtlCommentRow:
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
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileLaborDtlRow:
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
      self.HasAttachments:bool = obj["HasAttachments"]
      """  Indicates if the labor detail has attachments  """  
      self.HasComments:bool = obj["HasComments"]
      """  Indicates if the labor detail has comments  """  
      self.EnableComplete:bool = obj["EnableComplete"]
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.EnteredOnCurPlant:bool = obj["EnteredOnCurPlant"]
      """  To know if the LaborDtl was created on the current plant  """  
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      self.ApprovedBy:str = obj["ApprovedBy"]
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available for an approver  """  
      self.JobType:str = obj["JobType"]
      """  This field is used to get the translated value of JobTypeCode.  """  
      self.JobTypeCode:str = obj["JobTypeCode"]
      """   Indicates the type of job. Possible values are:
MFG - Manufacture
SRV - Service
PRJ - Project
MNT - Maintenance  """  
      self.GroupByLaborType:str = obj["GroupByLaborType"]
      """  Used for the Labor Type grouping. A new column was needed to differentiate between records with the same Labor Type (e.g. Production and Maintenance).  """  
      self.EquipID:str = obj["EquipID"]
      """  The ID of the Equipment that this "Maintenance Job" is for.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.IndirectDescription:str = obj["IndirectDescription"]
      self.JobAsmblDescription:str = obj["JobAsmblDescription"]
      self.JobAsmblPartNum:str = obj["JobAsmblPartNum"]
      self.OpDescOpDesc:str = obj["OpDescOpDesc"]
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileLaborHedRow:
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
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileLaborListRow:
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileLaborListTableset:
   def __init__(self, obj):
      self.MobileLaborList:list[Erp_Tablesets_MobileLaborListRow] = obj["MobileLaborList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MobileLaborTableset:
   def __init__(self, obj):
      self.MobileLaborHed:list[Erp_Tablesets_MobileLaborHedRow] = obj["MobileLaborHed"]
      self.MobileLaborDtl:list[Erp_Tablesets_MobileLaborDtlRow] = obj["MobileLaborDtl"]
      self.MobileLaborDtlAttch:list[Erp_Tablesets_MobileLaborDtlAttchRow] = obj["MobileLaborDtlAttch"]
      self.MobileLaborDtlComment:list[Erp_Tablesets_MobileLaborDtlCommentRow] = obj["MobileLaborDtlComment"]
      self.MobileApproverList:list[Erp_Tablesets_MobileApproverListRow] = obj["MobileApproverList"]
      self.MobileQuickEntryView:list[Erp_Tablesets_MobileQuickEntryViewRow] = obj["MobileQuickEntryView"]
      self.MobileTimeWeeklyView:list[Erp_Tablesets_MobileTimeWeeklyViewRow] = obj["MobileTimeWeeklyView"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MobileQuickEntryViewRow:
   def __init__(self, obj):
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.ExpenseCode:str = obj["ExpenseCode"]
      self.IndirectCode:str = obj["IndirectCode"]
      self.JobNum:str = obj["JobNum"]
      self.JobTypeCode:str = obj["JobTypeCode"]
      """   Indicates the type of job. Possible values are:
MFG - Manufacture
SRV - Service
PRJ - Project
MNT - Maintenance  """  
      self.LaborHrs:int = obj["LaborHrs"]
      self.LaborType:str = obj["LaborType"]
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      self.OpCode:str = obj["OpCode"]
      self.OperDesc:str = obj["OperDesc"]
      """  Operation Description  """  
      self.OprSeq:int = obj["OprSeq"]
      self.PhaseID:str = obj["PhaseID"]
      self.ProjectID:str = obj["ProjectID"]
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.ResourceID:str = obj["ResourceID"]
      self.RoleCode:str = obj["RoleCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileTimeWeeklyViewRow:
   def __init__(self, obj):
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.ASMdesc:str = obj["ASMdesc"]
      """  Job Assembly description  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.Company:str = obj["Company"]
      self.Complete:bool = obj["Complete"]
      self.DeleteRow:bool = obj["DeleteRow"]
      self.DisLaborType:bool = obj["DisLaborType"]
      self.DisPrjRoleCd:bool = obj["DisPrjRoleCd"]
      self.DisTimeTypCd:bool = obj["DisTimeTypCd"]
      self.EmployeeNum:str = obj["EmployeeNum"]
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy function is available  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if recall is available  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if submit is available  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HCMTotWeeklyPayHours:int = obj["HCMTotWeeklyPayHours"]
      """  HCM Integration Total Weekly Pay Hours  """  
      self.HoursFri:int = obj["HoursFri"]
      self.HoursMon:int = obj["HoursMon"]
      self.HoursSat:int = obj["HoursSat"]
      self.HoursSun:int = obj["HoursSun"]
      self.HoursThu:int = obj["HoursThu"]
      self.HoursTotal:int = obj["HoursTotal"]
      self.HoursTue:int = obj["HoursTue"]
      self.HoursWed:int = obj["HoursWed"]
      self.IndirectCode:str = obj["IndirectCode"]
      self.IndirectCodeDescription:str = obj["IndirectCodeDescription"]
      self.JCDept:str = obj["JCDept"]
      self.JobNum:str = obj["JobNum"]
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      self.LaborRate:int = obj["LaborRate"]
      self.LaborType:str = obj["LaborType"]
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      self.MessageText:str = obj["MessageText"]
      self.NewRowType:str = obj["NewRowType"]
      """  Valid values are "A" for an Add of a new TimeWeeklyView row and "C" for a Copy of an existing TimeWeeklyView row.  """  
      self.OpCode:str = obj["OpCode"]
      self.OpComplete:bool = obj["OpComplete"]
      self.OperDesc:str = obj["OperDesc"]
      """  Operation Description  """  
      self.OprSeq:int = obj["OprSeq"]
      self.PhaseID:str = obj["PhaseID"]
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      self.ProjDesc:str = obj["ProjDesc"]
      self.ProjectID:str = obj["ProjectID"]
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.ResourceGrpIDDescription:str = obj["ResourceGrpIDDescription"]
      self.ResourceID:str = obj["ResourceID"]
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      self.RoleCd:str = obj["RoleCd"]
      self.RoleCdDescription:str = obj["RoleCdDescription"]
      self.Shift:int = obj["Shift"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """   If the Time is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  """  
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TimeStatus:str = obj["TimeStatus"]
      self.TimeTypCd:str = obj["TimeTypCd"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.WBSPhaseDesc:str = obj["WBSPhaseDesc"]
      """  WBS Phase Project Description  """  
      self.WeekBeginDate:str = obj["WeekBeginDate"]
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.WeekEndDate:str = obj["WeekEndDate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtMobileLaborTableset:
   def __init__(self, obj):
      self.MobileLaborHed:list[Erp_Tablesets_MobileLaborHedRow] = obj["MobileLaborHed"]
      self.MobileLaborDtl:list[Erp_Tablesets_MobileLaborDtlRow] = obj["MobileLaborDtl"]
      self.MobileLaborDtlAttch:list[Erp_Tablesets_MobileLaborDtlAttchRow] = obj["MobileLaborDtlAttch"]
      self.MobileLaborDtlComment:list[Erp_Tablesets_MobileLaborDtlCommentRow] = obj["MobileLaborDtlComment"]
      self.MobileApproverList:list[Erp_Tablesets_MobileApproverListRow] = obj["MobileApproverList"]
      self.MobileQuickEntryView:list[Erp_Tablesets_MobileQuickEntryViewRow] = obj["MobileQuickEntryView"]
      self.MobileTimeWeeklyView:list[Erp_Tablesets_MobileTimeWeeklyViewRow] = obj["MobileTimeWeeklyView"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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
      self.returnObj:list[Erp_Tablesets_MobileLaborTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MobileLaborTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MobileLaborTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MobileLaborListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMobileLaborDtlAttchs_input:
   """ Required : 
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.laborHedSeq:int = obj["laborHedSeq"]
      """  Labor Header Seq  """  
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      """  Labor Detail Seq  """  
      pass

class GetMobileLaborDtlAttchs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileLaborTableset] = obj["returnObj"]
      pass

class GetMobileLaborDtlComments_input:
   """ Required : 
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.laborHedSeq:int = obj["laborHedSeq"]
      """  Labor Header Seq  """  
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      """  Labor Detail Seq  """  
      pass

class GetMobileLaborDtlComments_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileLaborTableset] = obj["returnObj"]
      pass

class GetNewMobileLaborDtlAttch_input:
   """ Required : 
   ds
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      pass

class GetNewMobileLaborDtlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMobileLaborDtlComment_input:
   """ Required : 
   ds
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      pass

class GetNewMobileLaborDtlComment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMobileLaborDtl_input:
   """ Required : 
   ds
   laborHedSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      pass

class GetNewMobileLaborDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMobileLaborHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class GetNewMobileLaborHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMobileLaborHed
   whereClauseMobileLaborDtl
   whereClauseMobileLaborDtlAttch
   whereClauseMobileLaborDtlComment
   whereClauseMobileApproverList
   whereClauseMobileQuickEntryView
   whereClauseMobileTimeWeeklyView
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMobileLaborHed:str = obj["whereClauseMobileLaborHed"]
      self.whereClauseMobileLaborDtl:str = obj["whereClauseMobileLaborDtl"]
      self.whereClauseMobileLaborDtlAttch:str = obj["whereClauseMobileLaborDtlAttch"]
      self.whereClauseMobileLaborDtlComment:str = obj["whereClauseMobileLaborDtlComment"]
      self.whereClauseMobileApproverList:str = obj["whereClauseMobileApproverList"]
      self.whereClauseMobileQuickEntryView:str = obj["whereClauseMobileQuickEntryView"]
      self.whereClauseMobileTimeWeeklyView:str = obj["whereClauseMobileTimeWeeklyView"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileLaborTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetVersion_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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

class MobileAttachmentUpdate_input:
   """ Required : 
   ds
   docTypeID
   parentTable
   fileName
   data
   metadata
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.docTypeID:str = obj["docTypeID"]
      """  Document Type ID  """  
      self.parentTable:str = obj["parentTable"]
      """  Parent Table e.g. LaborDtl  """  
      self.fileName:str = obj["fileName"]
      """  Physical name of the file  """  
      self.data:str = obj["data"]
      """  Array of bytes representing the data of the attachment  """  
      self.metadata      #schema had no properties on an object.
      """  Metadata  """  
      pass

class MobileAttachmentUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileChangeEquipID_input:
   """ Required : 
   equipID
   ds
   """  
   def __init__(self, obj):
      self.equipID:str = obj["equipID"]
      """  The new equipID  """  
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class MobileChangeEquipID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileChangeIndirectCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class MobileChangeIndirectCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileChangeLaborType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class MobileChangeLaborType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileChangeResourceId_input:
   """ Required : 
   ds
   pcResourceID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.pcResourceID:str = obj["pcResourceID"]
      """  The ID of the machine that was used to do the work  """  
      pass

class MobileChangeResourceId_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class MobileCheckResourceGroup_input:
   """ Required : 
   ds
   ProposedResourceID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.ProposedResourceID:str = obj["ProposedResourceID"]
      """  Proposed Resource ID  """  
      pass

class MobileCheckResourceGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class MobileCheckWarnings_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class MobileCheckWarnings_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class MobileDefaultDtlTime_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class MobileDefaultDtlTime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileDefaultIndirect_input:
   """ Required : 
   ds
   indirectCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.indirectCode:str = obj["indirectCode"]
      """  Proposed change to the indirect code  """  
      pass

class MobileDefaultIndirect_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileDefaultJobNum_input:
   """ Required : 
   ds
   jobNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      """  Proposed change to the JobNum field  """  
      pass

class MobileDefaultJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileDefaultLaborHrs_input:
   """ Required : 
   ds
   laborHrs
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.laborHrs:int = obj["laborHrs"]
      """  Proposed Labor Hrs change  """  
      pass

class MobileDefaultLaborHrs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileDefaultLaborQty_input:
   """ Required : 
   ds
   laborQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.laborQty:int = obj["laborQty"]
      """  Proposed change to LaborQty field  """  
      pass

class MobileDefaultLaborQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class MobileDefaultLaborType_input:
   """ Required : 
   ds
   ipLaborType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.ipLaborType:str = obj["ipLaborType"]
      """  Proposed LaborType change  """  
      pass

class MobileDefaultLaborType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileDefaultOprSeq_input:
   """ Required : 
   ds
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.oprSeq:int = obj["oprSeq"]
      """  Proposed PhaseOprSeq change  """  
      pass

class MobileDefaultOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class MobileDefaultPhaseID_input:
   """ Required : 
   ds
   ipPhaseID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.ipPhaseID:str = obj["ipPhaseID"]
      """  Proposed value for ipPhaseID  """  
      pass

class MobileDefaultPhaseID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileDefaultPhaseOprSeq_input:
   """ Required : 
   ds
   idPhaseOprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.idPhaseOprSeq:int = obj["idPhaseOprSeq"]
      """  Proposed PhaseOprSeq change  """  
      pass

class MobileDefaultPhaseOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class MobileDeleteLaborDtl_input:
   """ Required : 
   LaborHedSeq
   LaborDtlSeq
   CallFrom
   """  
   def __init__(self, obj):
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  The LaborHedSeq value for the record to be deleted  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  The LaborDtlSeq value for the record to be deleted  """  
      self.CallFrom:str = obj["CallFrom"]
      """  Indicates where this method is called from  """  
      pass

class MobileDeleteLaborDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class MobileDelete_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class MobileDelete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileGetApprovalStatus_input:
   """ Required : 
   key1
   key2
   approvedBy
   pendingApprovalBy
   """  
   def __init__(self, obj):
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.approvedBy:str = obj["approvedBy"]
      self.pendingApprovalBy:str = obj["pendingApprovalBy"]
      pass

class MobileGetApprovalStatus_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileLaborTableset] = obj["returnObj"]
      pass

class MobileGetByID_input:
   """ Required : 
   laborHedSeq
   """  
   def __init__(self, obj):
      self.laborHedSeq:int = obj["laborHedSeq"]
      """  The LaborHed seq value for which the LaborHed record is returned.  """  
      pass

class MobileGetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileLaborTableset] = obj["returnObj"]
      pass

class MobileGetHomePageData_input:
   """ Required : 
   employeeID
   salesRepCode
   numberOfDays
   """  
   def __init__(self, obj):
      self.employeeID:str = obj["employeeID"]
      self.salesRepCode:str = obj["salesRepCode"]
      self.numberOfDays:int = obj["numberOfDays"]
      pass

class MobileGetHomePageData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.entered:int = obj["parameters"]
      self.submitted:int = obj["parameters"]
      self.approved:int = obj["parameters"]
      self.rejected:int = obj["parameters"]
      self.forApproval:int = obj["parameters"]
      self.oldestRecordDate:str = obj["parameters"]
      self.enteredHours:int = obj["parameters"]
      self.submittedHours:int = obj["parameters"]
      self.approvedHours:int = obj["parameters"]
      self.rejectedHours:int = obj["parameters"]
      self.forApprovalHours:int = obj["parameters"]
      pass

      """  output parameters  """  

class MobileGetNewLaborDtlAttch_input:
   """ Required : 
   ds
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      """  The Labor Header Seq value for which the LaborDtlComment record is created.  """  
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      """  The Labor Detail Seq value for which the LaborDtlComment record is created.  """  
      pass

class MobileGetNewLaborDtlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileGetNewLaborDtlComment_input:
   """ Required : 
   ds
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      """  The Labor Header Seq value for which the LaborDtlComment record is created.  """  
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      """  The Labor Detail Seq value for which the LaborDtlComment record is created.  """  
      pass

class MobileGetNewLaborDtlComment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileGetNewLaborDtlNoHdr_input:
   """ Required : 
   ds
   employeeNum
   shopFloor
   ClockInDate
   ClockInTime
   ClockOutDate
   ClockOutTTime
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.employeeNum:str = obj["employeeNum"]
      """  The Employee for which the record is being generated  """  
      self.shopFloor:bool = obj["shopFloor"]
      """  Indicates whether this is being called from the shop floor labor entry program  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date  """  
      self.ClockInTime:int = obj["ClockInTime"]
      """  The clock in time  """  
      self.ClockOutDate:str = obj["ClockOutDate"]
      """  The clock out date  """  
      self.ClockOutTTime:int = obj["ClockOutTTime"]
      """  The clock out time  """  
      pass

class MobileGetNewLaborDtlNoHdr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileGetNewLaborDtlOnSelectForWork_input:
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
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      """  The LaborHed seq value for which the LaborDtl record is created.  """  
      self.sJobNum:str = obj["sJobNum"]
      """  The JobNum that will be linked to the LaborDtl record  """  
      self.iAssemblySeq:int = obj["iAssemblySeq"]
      """  The Assembly sequence for the LaborDtl record  """  
      self.iOprSeq:int = obj["iOprSeq"]
      """  The Operation sequence for the LaborDtl record  """  
      self.sResourceGrpID:str = obj["sResourceGrpID"]
      """  The Resource group for the LaborDtl record  """  
      self.setupOrProd:str = obj["setupOrProd"]
      """  Setup or Prod value string  """  
      pass

class MobileGetNewLaborDtlOnSelectForWork_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.bMachinePrompt:bool = obj["bMachinePrompt"]
      pass

      """  output parameters  """  

class MobileGetNewLaborDtlWithHdr_input:
   """ Required : 
   ds
   ClockInDate
   ClockInTime
   ClockOutDate
   ClockOutTTime
   laborHedSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date  """  
      self.ClockInTime:int = obj["ClockInTime"]
      """  The clock in time  """  
      self.ClockOutDate:str = obj["ClockOutDate"]
      """  The clock out date  """  
      self.ClockOutTTime:int = obj["ClockOutTTime"]
      """  The clock out time  """  
      self.laborHedSeq:int = obj["laborHedSeq"]
      """  The LaborHed seq value for which the LaborDtl record is created.  """  
      pass

class MobileGetNewLaborDtlWithHdr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileGetNewLaborDtl_input:
   """ Required : 
   ds
   laborHedSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      """  The LaborHed seq value for which the LaborDtl record is created.  """  
      pass

class MobileGetNewLaborDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileGetNewLaborHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class MobileGetNewLaborHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileGetNewTimeWeeklyView_input:
   """ Required : 
   ds
   ipEmployeeNum
   ipDateInWeek
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.ipEmployeeNum:str = obj["ipEmployeeNum"]
      """  The Employee for which the record is being generated  """  
      self.ipDateInWeek:str = obj["ipDateInWeek"]
      """  Date within the week for which a new TimeWeeklyView record is to be created  """  
      pass

class MobileGetNewTimeWeeklyView_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileGetQuickEntry_input:
   """ Required : 
   company
   empNum
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.empNum:str = obj["empNum"]
      pass

class MobileGetQuickEntry_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileQuickEntryViewRow] = obj["returnObj"]
      pass

class MobileGetRowsPendingApprovalWithFilter_input:
   """ Required : 
   salesRepCode
   laborType
   laborStatus
   fromDate
   toDate
   employeeName
   includeMaintenance
   includeProduction
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      self.laborType:str = obj["laborType"]
      self.laborStatus:str = obj["laborStatus"]
      self.fromDate:str = obj["fromDate"]
      self.toDate:str = obj["toDate"]
      self.employeeName:str = obj["employeeName"]
      self.includeMaintenance:bool = obj["includeMaintenance"]
      """  Bool to include Maintenance type on the filter  """  
      self.includeProduction:bool = obj["includeProduction"]
      """  Bool to include Production type on the filter  """  
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class MobileGetRowsPendingApprovalWithFilter_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileLaborTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class MobileGetRowsPendingApproval_input:
   """ Required : 
   salesRepCode
   laborType
   laborStatus
   fromDate
   toDate
   employeeName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      self.laborType:str = obj["laborType"]
      self.laborStatus:str = obj["laborStatus"]
      self.fromDate:str = obj["fromDate"]
      self.toDate:str = obj["toDate"]
      self.employeeName:str = obj["employeeName"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class MobileGetRowsPendingApproval_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileLaborTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class MobileGetRowsWithFilter_input:
   """ Required : 
   whereClauseMobileLaborHed
   whereClauseMobileLaborDtl
   whereClauseMobileLaborDtlComment
   whereClauseTimeWeeklyView
   includeMaintenance
   includeProduction
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMobileLaborHed:str = obj["whereClauseMobileLaborHed"]
      """  The string containing the where clause for LaborHed  """  
      self.whereClauseMobileLaborDtl:str = obj["whereClauseMobileLaborDtl"]
      """  The string containing the where clause for LaborDtl  """  
      self.whereClauseMobileLaborDtlComment:str = obj["whereClauseMobileLaborDtlComment"]
      """  The string containing the where clause for LaborDtlComment  """  
      self.whereClauseTimeWeeklyView:str = obj["whereClauseTimeWeeklyView"]
      """  The string containing the where clause for TimeWeeklyView  """  
      self.includeMaintenance:bool = obj["includeMaintenance"]
      """  Bool to include Maintenance type on the filter  """  
      self.includeProduction:bool = obj["includeProduction"]
      """  Bool to include Production type on the filter  """  
      self.pageSize:int = obj["pageSize"]
      """  The Page Size for the resulting dataset  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The Absolute Page for the resulting dataset  """  
      pass

class MobileGetRowsWithFilter_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileLaborTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class MobileGetRows_input:
   """ Required : 
   whereClauseMobileLaborHed
   whereClauseMobileLaborDtl
   whereClauseMobileLaborDtlComment
   whereClauseTimeWeeklyView
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMobileLaborHed:str = obj["whereClauseMobileLaborHed"]
      """  The string containing the where clause for LaborHed  """  
      self.whereClauseMobileLaborDtl:str = obj["whereClauseMobileLaborDtl"]
      """  The string containing the where clause for LaborDtl  """  
      self.whereClauseMobileLaborDtlComment:str = obj["whereClauseMobileLaborDtlComment"]
      """  The string containing the where clause for LaborDtlComment  """  
      self.whereClauseTimeWeeklyView:str = obj["whereClauseTimeWeeklyView"]
      """  The string containing the where clause for TimeWeeklyView  """  
      self.pageSize:int = obj["pageSize"]
      """  The Page Size for the resulting dataset  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The Absolute Page for the resulting dataset  """  
      pass

class MobileGetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileLaborTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class MobileLaborGetList_input:
   """ Required : 
   mobileLaborWhereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.mobileLaborWhereClause:str = obj["mobileLaborWhereClause"]
      """  The string containing the where clause for LaborHed  """  
      self.pageSize:int = obj["pageSize"]
      """  The Page Size for the resulting dataset  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The Absolute Page for the resulting dataset  """  
      pass

class MobileLaborGetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MobileLaborListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class MobileLaborUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class MobileLaborUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileOverrides_input:
   """ Required : 
   ds
   inOpCode
   inResGrpID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.inOpCode:str = obj["inOpCode"]
      """  OpCode to override  """  
      self.inResGrpID:str = obj["inResGrpID"]
      """  Resource Group OD to override  """  
      pass

class MobileOverrides_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MobileRecallFromApproval_input:
   """ Required : 
   ds
   lWeeklyView
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.lWeeklyView:bool = obj["lWeeklyView"]
      """  Is this method being called with WeeklyView records?  """  
      pass

class MobileRecallFromApproval_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class MobileSyncSuccessful_input:
   """ Required : 
   company
   tableName
   sysRowID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company where the record was created  """  
      self.tableName:str = obj["tableName"]
      """  Name of the table related to the patch field  """  
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID of the record on the Mobile  """  
      pass

class MobileSyncSuccessful_output:
   def __init__(self, obj):
      pass

class MobileSync_input:
   """ Required : 
   tableName
   ds
   comments
   salesRepCode
   isWeeklyView
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Name of the table that is being synchronized.  """  
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.comments:str = obj["comments"]
      """  Comments for approved and rejected records  """  
      self.salesRepCode:str = obj["salesRepCode"]
      """  Sales Rep Code  """  
      self.isWeeklyView:bool = obj["isWeeklyView"]
      """  Is this method being called with WeeklyView records?  """  
      pass

class MobileSync_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class MobileVerifyScrapQty_input:
   """ Required : 
   ds
   scrapQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.scrapQty:int = obj["scrapQty"]
      """  Proposed change to ScrapQty field  """  
      pass

class MobileVerifyScrapQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class RecallTrans_input:
   """ Required : 
   salesRepCode
   ds
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      """  The sales Rep Code of the approver.  """  
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class RecallTrans_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class SubmitSelected_input:
   """ Required : 
   ds
   isWeeklyView
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.isWeeklyView:bool = obj["isWeeklyView"]
      """  Indicates if a WeeklyView is being processed  """  
      pass

class SubmitSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMobileLaborTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMobileLaborTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileLaborTableset] = obj["ds"]
      pass

      """  output parameters  """  

