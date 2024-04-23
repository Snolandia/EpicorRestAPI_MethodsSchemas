import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ContainerTrackingSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ContainerTrackings(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContainerTrackings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerTrackings
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings",headers=creds) as resp:
           return await resp.json()

async def post_ContainerTrackings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerTrackings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContainerTrackings_Company_ContainerID(Company, ContainerID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerTracking item
   Description: Calls GetByID to retrieve the ContainerTracking item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerTracking
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContainerTrackings_Company_ContainerID(Company, ContainerID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContainerTracking for the service
   Description: Calls UpdateExt to update ContainerTracking. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerTracking
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContainerTrackings_Company_ContainerID(Company, ContainerID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContainerTracking item
   Description: Call UpdateExt to delete ContainerTracking item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerTracking
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerTrackings_Company_ContainerID_ContainerDetails(Company, ContainerID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ContainerDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerDetails1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerDetails",headers=creds) as resp:
           return await resp.json()

async def get_ContainerTrackings_Company_ContainerID_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum(Company, ContainerID, PONum, POLine, PORelNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerDetail item
   Description: Calls GetByID to retrieve the ContainerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDetail1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerTrackings_Company_ContainerID_ContainerHeaderTaxes(Company, ContainerID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ContainerHeaderTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerHeaderTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerHeaderTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerHeaderTaxes",headers=creds) as resp:
           return await resp.json()

async def get_ContainerTrackings_Company_ContainerID_ContainerHeaderTaxes_Company_ContainerID_TaxCode_RateCode_ECAcquisitionSeq(Company, ContainerID, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerHeaderTax item
   Description: Calls GetByID to retrieve the ContainerHeaderTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerHeaderTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerHeaderTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerHeaderTaxes(" + Company + "," + ContainerID + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerTrackings_Company_ContainerID_ContainerMiscs(Company, ContainerID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ContainerMiscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerMiscs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerMiscs",headers=creds) as resp:
           return await resp.json()

async def get_ContainerTrackings_Company_ContainerID_ContainerMiscs_Company_ContainerID_MiscSeq(Company, ContainerID, MiscSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerMisc item
   Description: Calls GetByID to retrieve the ContainerMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerMisc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerMiscs(" + Company + "," + ContainerID + "," + MiscSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerTrackings_Company_ContainerID_ContainerHeaderAttches(Company, ContainerID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ContainerHeaderAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerHeaderAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerHeaderAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerHeaderAttches",headers=creds) as resp:
           return await resp.json()

async def get_ContainerTrackings_Company_ContainerID_ContainerHeaderAttches_Company_ContainerID_DrawingSeq(Company, ContainerID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerHeaderAttch item
   Description: Calls GetByID to retrieve the ContainerHeaderAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerHeaderAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerHeaderAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerTrackings(" + Company + "," + ContainerID + ")/ContainerHeaderAttches(" + Company + "," + ContainerID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerDetails(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContainerDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerDetails
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails",headers=creds) as resp:
           return await resp.json()

async def post_ContainerDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContainerDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum(Company, ContainerID, PONum, POLine, PORelNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerDetail item
   Description: Calls GetByID to retrieve the ContainerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum(Company, ContainerID, PONum, POLine, PORelNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContainerDetail for the service
   Description: Calls UpdateExt to update ContainerDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum(Company, ContainerID, PONum, POLine, PORelNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContainerDetail item
   Description: Call UpdateExt to delete ContainerDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum_ContainerDetailTaxes(Company, ContainerID, PONum, POLine, PORelNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ContainerDetailTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerDetailTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDetailTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")/ContainerDetailTaxes",headers=creds) as resp:
           return await resp.json()

async def get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum_ContainerDetailTaxes_Company_ContainerID_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company, ContainerID, PONum, POLine, PORelNum, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerDetailTax item
   Description: Calls GetByID to retrieve the ContainerDetailTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDetailTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerDetailTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")/ContainerDetailTaxes(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum_ContainerDuties(Company, ContainerID, PONum, POLine, PORelNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ContainerDuties items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerDuties1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDutyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")/ContainerDuties",headers=creds) as resp:
           return await resp.json()

async def get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum_ContainerDuties_Company_ContainerID_PONum_POLine_PORelNum_DutySeq(Company, ContainerID, PONum, POLine, PORelNum, DutySeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerDuty item
   Description: Calls GetByID to retrieve the ContainerDuty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDuty1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param DutySeq: Desc: DutySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerDutyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")/ContainerDuties(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DutySeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum_ContainerDetailAttches(Company, ContainerID, PONum, POLine, PORelNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ContainerDetailAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerDetailAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDetailAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")/ContainerDetailAttches",headers=creds) as resp:
           return await resp.json()

async def get_ContainerDetails_Company_ContainerID_PONum_POLine_PORelNum_ContainerDetailAttches_Company_ContainerID_PONum_POLine_PORelNum_DrawingSeq(Company, ContainerID, PONum, POLine, PORelNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerDetailAttch item
   Description: Calls GetByID to retrieve the ContainerDetailAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDetailAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerDetailAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetails(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + ")/ContainerDetailAttches(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerDetailTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContainerDetailTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerDetailTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDetailTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailTaxes",headers=creds) as resp:
           return await resp.json()

async def post_ContainerDetailTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerDetailTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerDetailTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContainerDetailTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContainerDetailTaxes_Company_ContainerID_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company, ContainerID, PONum, POLine, PORelNum, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerDetailTax item
   Description: Calls GetByID to retrieve the ContainerDetailTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDetailTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerDetailTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailTaxes(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContainerDetailTaxes_Company_ContainerID_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company, ContainerID, PONum, POLine, PORelNum, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContainerDetailTax for the service
   Description: Calls UpdateExt to update ContainerDetailTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerDetailTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerDetailTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailTaxes(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContainerDetailTaxes_Company_ContainerID_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company, ContainerID, PONum, POLine, PORelNum, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContainerDetailTax item
   Description: Call UpdateExt to delete ContainerDetailTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerDetailTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailTaxes(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerDuties(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContainerDuties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerDuties
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDutyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDuties",headers=creds) as resp:
           return await resp.json()

async def post_ContainerDuties(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerDuties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerDutyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContainerDutyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDuties", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContainerDuties_Company_ContainerID_PONum_POLine_PORelNum_DutySeq(Company, ContainerID, PONum, POLine, PORelNum, DutySeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerDuty item
   Description: Calls GetByID to retrieve the ContainerDuty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDuty
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param DutySeq: Desc: DutySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerDutyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDuties(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DutySeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContainerDuties_Company_ContainerID_PONum_POLine_PORelNum_DutySeq(Company, ContainerID, PONum, POLine, PORelNum, DutySeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContainerDuty for the service
   Description: Calls UpdateExt to update ContainerDuty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerDuty
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param DutySeq: Desc: DutySeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerDutyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDuties(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DutySeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContainerDuties_Company_ContainerID_PONum_POLine_PORelNum_DutySeq(Company, ContainerID, PONum, POLine, PORelNum, DutySeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContainerDuty item
   Description: Call UpdateExt to delete ContainerDuty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerDuty
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param DutySeq: Desc: DutySeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDuties(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DutySeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerDetailAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContainerDetailAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerDetailAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerDetailAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailAttches",headers=creds) as resp:
           return await resp.json()

async def post_ContainerDetailAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerDetailAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerDetailAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContainerDetailAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContainerDetailAttches_Company_ContainerID_PONum_POLine_PORelNum_DrawingSeq(Company, ContainerID, PONum, POLine, PORelNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerDetailAttch item
   Description: Calls GetByID to retrieve the ContainerDetailAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerDetailAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerDetailAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailAttches(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContainerDetailAttches_Company_ContainerID_PONum_POLine_PORelNum_DrawingSeq(Company, ContainerID, PONum, POLine, PORelNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContainerDetailAttch for the service
   Description: Calls UpdateExt to update ContainerDetailAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerDetailAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerDetailAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailAttches(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContainerDetailAttches_Company_ContainerID_PONum_POLine_PORelNum_DrawingSeq(Company, ContainerID, PONum, POLine, PORelNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContainerDetailAttch item
   Description: Call UpdateExt to delete ContainerDetailAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerDetailAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerDetailAttches(" + Company + "," + ContainerID + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerHeaderTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContainerHeaderTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerHeaderTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerHeaderTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderTaxes",headers=creds) as resp:
           return await resp.json()

async def post_ContainerHeaderTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerHeaderTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContainerHeaderTaxes_Company_ContainerID_TaxCode_RateCode_ECAcquisitionSeq(Company, ContainerID, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerHeaderTax item
   Description: Calls GetByID to retrieve the ContainerHeaderTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerHeaderTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerHeaderTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderTaxes(" + Company + "," + ContainerID + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContainerHeaderTaxes_Company_ContainerID_TaxCode_RateCode_ECAcquisitionSeq(Company, ContainerID, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContainerHeaderTax for the service
   Description: Calls UpdateExt to update ContainerHeaderTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerHeaderTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderTaxes(" + Company + "," + ContainerID + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContainerHeaderTaxes_Company_ContainerID_TaxCode_RateCode_ECAcquisitionSeq(Company, ContainerID, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContainerHeaderTax item
   Description: Call UpdateExt to delete ContainerHeaderTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerHeaderTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderTaxes(" + Company + "," + ContainerID + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerMiscs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContainerMiscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerMiscs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs",headers=creds) as resp:
           return await resp.json()

async def post_ContainerMiscs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerMiscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerMiscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContainerMiscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContainerMiscs_Company_ContainerID_MiscSeq(Company, ContainerID, MiscSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerMisc item
   Description: Calls GetByID to retrieve the ContainerMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs(" + Company + "," + ContainerID + "," + MiscSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContainerMiscs_Company_ContainerID_MiscSeq(Company, ContainerID, MiscSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContainerMisc for the service
   Description: Calls UpdateExt to update ContainerMisc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerMiscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs(" + Company + "," + ContainerID + "," + MiscSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContainerMiscs_Company_ContainerID_MiscSeq(Company, ContainerID, MiscSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContainerMisc item
   Description: Call UpdateExt to delete ContainerMisc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param MiscSeq: Desc: MiscSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs(" + Company + "," + ContainerID + "," + MiscSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerMiscs_Company_ContainerID_MiscSeq_ContainerMiscTaxes(Company, ContainerID, MiscSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ContainerMiscTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContainerMiscTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs(" + Company + "," + ContainerID + "," + MiscSeq + ")/ContainerMiscTaxes",headers=creds) as resp:
           return await resp.json()

async def get_ContainerMiscs_Company_ContainerID_MiscSeq_ContainerMiscTaxes_Company_ContainerID_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company, ContainerID, MiscSeq, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerMiscTax item
   Description: Calls GetByID to retrieve the ContainerMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerMiscTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscs(" + Company + "," + ContainerID + "," + MiscSeq + ")/ContainerMiscTaxes(" + Company + "," + ContainerID + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerMiscTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContainerMiscTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerMiscTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscTaxes",headers=creds) as resp:
           return await resp.json()

async def post_ContainerMiscTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerMiscTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerMiscTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContainerMiscTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContainerMiscTaxes_Company_ContainerID_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company, ContainerID, MiscSeq, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerMiscTax item
   Description: Calls GetByID to retrieve the ContainerMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerMiscTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscTaxes(" + Company + "," + ContainerID + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContainerMiscTaxes_Company_ContainerID_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company, ContainerID, MiscSeq, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContainerMiscTax for the service
   Description: Calls UpdateExt to update ContainerMiscTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerMiscTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerMiscTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscTaxes(" + Company + "," + ContainerID + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContainerMiscTaxes_Company_ContainerID_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company, ContainerID, MiscSeq, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContainerMiscTax item
   Description: Call UpdateExt to delete ContainerMiscTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerMiscTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerMiscTaxes(" + Company + "," + ContainerID + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContainerHeaderAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContainerHeaderAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContainerHeaderAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerHeaderAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderAttches",headers=creds) as resp:
           return await resp.json()

async def post_ContainerHeaderAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContainerHeaderAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContainerHeaderAttches_Company_ContainerID_DrawingSeq(Company, ContainerID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContainerHeaderAttch item
   Description: Calls GetByID to retrieve the ContainerHeaderAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContainerHeaderAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContainerHeaderAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderAttches(" + Company + "," + ContainerID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContainerHeaderAttches_Company_ContainerID_DrawingSeq(Company, ContainerID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContainerHeaderAttch for the service
   Description: Calls UpdateExt to update ContainerHeaderAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContainerHeaderAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContainerHeaderAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderAttches(" + Company + "," + ContainerID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContainerHeaderAttches_Company_ContainerID_DrawingSeq(Company, ContainerID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContainerHeaderAttch item
   Description: Call UpdateExt to delete ContainerHeaderAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContainerHeaderAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContainerID: Desc: ContainerID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/ContainerHeaderAttches(" + Company + "," + ContainerID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContainerHeaderListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseContainerHeader, whereClauseContainerHeaderAttch, whereClauseContainerDetail, whereClauseContainerDetailAttch, whereClauseContainerDetailTax, whereClauseContainerDuty, whereClauseContainerHeaderTax, whereClauseContainerMisc, whereClauseContainerMiscTax, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseContainerHeader=" + whereClauseContainerHeader
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseContainerHeaderAttch=" + whereClauseContainerHeaderAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseContainerDetail=" + whereClauseContainerDetail
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseContainerDetailAttch=" + whereClauseContainerDetailAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseContainerDetailTax=" + whereClauseContainerDetailTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseContainerDuty=" + whereClauseContainerDuty
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseContainerHeaderTax=" + whereClauseContainerHeaderTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseContainerMisc=" + whereClauseContainerMisc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseContainerMiscTax=" + whereClauseContainerMiscTax
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(containerID, epicorHeaders = None):
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
   params += "containerID=" + containerID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CalculateContainerTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateContainerTaxes
   Description: CALCULATE VANTAGE\TAX CONNECT TAX CALCULATIONS UI NEEDS TO CALL A SAVE BEFORE CALLING THIS PROCEDURE
   OperationID: CalculateContainerTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateContainerTaxes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateContainerTaxes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateContainerIndCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateContainerIndCost
   Description: Creates the default Miscellaneous Charges for the Container based on the
selected APInvMsc records.
   OperationID: CreateContainerIndCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateContainerIndCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateContainerIndCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateMultiDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateMultiDetails
   Description: Purpose:
Parameters:
<param name="ds">Container Tracking Data Set</param><param name="containerErrors">List of PO releases not added as container details </param><param name="detailAdded">Indicates that at least one detail was added and is used by the UI to determine if the zero volume message is to be displayed </param>
Notes:
   OperationID: CreateMultiDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateMultiDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMultiDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DisburseLandedCosts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DisburseLandedCosts
   Description: Purpose:  Disburse the landed costs across the container details
<param name="ipContainerID">Container IDt</param><param name="opLCApplied">Total applied landed cost</param>
   OperationID: DisburseLandedCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisburseLandedCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisburseLandedCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAPInvMiscCharges(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAPInvMiscCharges
   Description: Gets the list of AP Invoice Miscellaneous Charges marked as Landed Cost and
and not linked to any container or receipt yet.
   OperationID: GetAPInvMiscCharges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAPInvMiscCharges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPInvMiscCharges_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContainerClassInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContainerClassInfo
   Description: This method defaults the container class information into
the conatiner header file whenever the container class is added/amended
   OperationID: GetContainerClassInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContainerClassInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContainerClassInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContainerDetailToSplit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContainerDetailToSplit
   Description: Gets the Detail of a specific Container Header to be splitted.
   OperationID: GetContainerDetailToSplit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContainerDetailToSplit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContainerDetailToSplit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContainerMiscToTransfer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContainerMiscToTransfer
   Description: Gets the Indirect Costs of a specific Container Header to be transfered.
   OperationID: GetContainerMiscToTransfer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContainerMiscToTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContainerMiscToTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReceiveContainerLCAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReceiveContainerLCAmt
   Description: Purpose:  Apply the disbursed Container's additional Landed Costs among the existing
Container Receipt details.  This procedure share similar logic used in the
ReceiveContainerLCAmt procedure for distributing the LCAmt as a regular receipt
mtlburden cost or variance cost. This procedure does not create new RcvDtl
record for the remainder of qty to be received.
<param name="inContainerID">Container ID</param><param name="opMessage">Message to return back to user.</param>
   OperationID: ReceiveContainerLCAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiveContainerLCAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveContainerLCAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshLCApplied(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshLCApplied
   Description: Purpose:  Refresh the external field LCAppliedAmt after a change to LC detail amount
Parameters:
<param name="ipContainerID">Container ID</param><param name="opLCApplied">Calculated Landed Cost applied amount</param>
Notes:
   OperationID: RefreshLCApplied
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshLCApplied_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshLCApplied_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetLandedCostDisbursements(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetLandedCostDisbursements
   Description: Initialize landed cost amounts to 0 and updates the landed cost disburse method.
   OperationID: ResetLandedCostDisbursements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetLandedCostDisbursements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetLandedCostDisbursements_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ShipContainer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ShipContainer
   Description: container To Ship
   OperationID: ShipContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ShipContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ShipContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SplitContainerShipment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SplitContainerShipment
   Description: Splits a Container by creating a new Container Header and assigning the
selected Container Detail lines into the new Container.
   OperationID: SplitContainerShipment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SplitContainerShipment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SplitContainerShipment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TransferIndirectCosts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TransferIndirectCosts
   Description: Transfers Indirect Costs from one container to another.
   OperationID: TransferIndirectCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TransferIndirectCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TransferIndirectCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnShipContainer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnShipContainer
   Description: container To UnShip
   OperationID: UnShipContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnShipContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnShipContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateLCAppliedAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateLCAppliedAmt
   Description: Purpose:  Update the applied landed cost
Parameters:  none
<param name="origLCAmt">original landed cost amount</param><param name="newLCAmt">new landed cost amount</param><param name="ipcontainerID">container ID</param><param name="ipAppliedAmt">current applied landed cost amount</param><param name="totApplied">total applied landed cost</param>
Notes:
   OperationID: UpdateLCAppliedAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateLCAppliedAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLCAppliedAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateLandedCostDisbursements(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateLandedCostDisbursements
   Description: Purpose: Validate the landed cost distributions
Parameters:
<param name="ipContainerID">Container ID</param><param name="ds">Container Tracking Data Set</param><param name="lcError">error message</param>
   OperationID: ValidateLandedCostDisbursements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateLandedCostDisbursements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLandedCostDisbursements_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalcDtlExtTransValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcDtlExtTransValue
   Description: Purpose: Calculate Container Indirect Costs / Extended Costs and Duty
Parameters:  none
<param name="ds">ContainerTrackingTableSet</param>
Notes:
   OperationID: CalcDtlExtTransValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcDtlExtTransValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcDtlExtTransValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateExtCostAndWeight(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateExtCostAndWeight
   Description: Purpose:  recalculates the weight and extcost and is called whenever the
ship qty changes
Parameters:
<param name="shipQty">Quantity to ship</param><param name="shipUOM">Shipping UOM</param><param name="partNum">Part number on container detail</param><param name="ourUnitCost">Unit Cost on container detail</param><param name="weight">Extended weight of detail</param><param name="grossWeight">Gross weight of detail</param><param name="vExtCost">Extended container cost or value</param><param name="poNum">Container PO Number</param><param name="poLine">Container PO Line</param>
Notes:
   OperationID: CalculateExtCostAndWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateExtCostAndWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateExtCostAndWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlPOInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlPOInfo
   Description: This method updates the dataset when the detail Line PONum field has changed.
   OperationID: GetDtlPOInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlPOInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlPOInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlPOLineInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlPOLineInfo
   Description: This method updates the dataset when the detail Line POLine field has changed.
   OperationID: GetDtlPOLineInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlPOLineInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlPOLineInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlQtyInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlQtyInfo
   Description: This method updates the dataset when the ShipQty or IUM field changes
   OperationID: GetDtlQtyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlQtyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlQtyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPOReleaseInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPOReleaseInfo
   Description: This method defaults the container class information into
the conatiner header file whenever the container class is added/amended
   OperationID: GetPOReleaseInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOReleaseInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOReleaseInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlCommodity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlCommodity
   Description: This method should be invoked when the CommodityCode in ContainerDetail changes.
This method will validate the commodity code and get defaults.
   OperationID: OnChangeDtlCommodity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlCommodity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlCommodity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlCountryNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlCountryNum
   Description: This method should be invoked when the OrigCountryNum in ContainerDetail changes.
This method will validate country of origin.
   OperationID: OnChangeDtlCountryNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlCountryNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlCountryNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlLCIndCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlLCIndCost
   Description: This method should be invoked when the LCIndCost in ContainerDetail changes.
This method will validate the manually disbursed indirect cost.
   OperationID: OnChangeDtlLCIndCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlLCIndCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlLCIndCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlUpliftPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlUpliftPercent
   Description: This method should be invoked when the UpliftPercent in ContainerDetail changes.
This method will validate the UpliftPercent and calculate the Uplift Indirect Cost.
   OperationID: OnChangeDtlUpliftPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlUpliftPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlUpliftPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedPOTransValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedPOTransValue
   Description: This method should be invoked when the PO Transaction Value has changed.
   OperationID: OnChangedPOTransValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPOTransValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPOTransValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateShipQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateShipQty
   Description: Purpose:  Validate the container detail ship qty
Parameters:
<param name="shipQty">Proposed Ship Qty</param><param name="shipUOM">Ship Qty UOM</param><param name="ium">PODetail.IUM</param><param name="partNum">PartNum</param><param name="poNum">Purchase order number</param><param name="poLine">Purchase order line number</param><param name="poRelNum">Purchase order release number</param><param name="WarningMsg">Warning mesage</param>
Notes:
   OperationID: ValidateShipQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateShipQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShipQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlTaxCatID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlTaxCatID
   Description: This method should be invoked when TaxCatID changes and is used to set the Taxable flag
   OperationID: OnChangeDtlTaxCatID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlTaxExempt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlTaxExempt
   Description: This method should be invoked when TaxExempt changes and is used to set the Taxable flag
   OperationID: OnChangeDtlTaxExempt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlTaxExempt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlTaxExempt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedDetailTaxManual(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedDetailTaxManual
   Description: Method to call when the Manual Tax Flag has Changed from True to False.  Updates DetailTax
tax amounts based on the new tax percent.
   OperationID: OnChangedDetailTaxManual
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedDetailTaxManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedDetailTaxManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDetailTaxFixedAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDetailTaxFixedAmount
   Description: Method to call when changing the fixed amount on the ContainerDetailTax table currently
   OperationID: OnChangeDetailTaxFixedAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDetailTaxTaxPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDetailTaxTaxPercent
   Description: Method to call when changing the tax percent on a tax record.  Updates ContainerDetailTax
tax amounts based on the new tax percent.
   OperationID: OnChangeDetailTaxTaxPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDetailTaxRateCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDetailTaxRateCode
   Description: Method to call when changing the rate code on a tax record.  Validates the rate and tax code
   OperationID: OnChangeDetailTaxRateCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDetailTaxReportableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDetailTaxReportableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates DetailTax
tax amounts based on the new taxable amount.
   OperationID: OnChangeDetailTaxReportableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDetailTaxTaxableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDetailTaxTaxableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates DetailTax
tax amounts based on the new taxable amount.
   OperationID: OnChangeDetailTaxTaxableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDetailTaxTaxAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDetailTaxTaxAmt
   Description: Method to call when changing the fixed tax amount on a tax record.  Updates DetailTax
tax amounts based on the new tax amount.
   OperationID: OnChangeDetailTaxTaxAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDetailTaxTaxDeductable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDetailTaxTaxDeductable
   Description: Method to call when changing the tax deductable on a tax record.  Updates DetailTax
tax amounts based on the new tax percent.
   OperationID: OnChangeDetailTaxTaxDeductable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxTaxDeductable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxTaxDeductable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDetailTaxTaxCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDetailTaxTaxCode
   Description: Method to call when changing the tax code on a DetailTax record.  Validates the tax code and
updates DetailTax tax amounts based on the new tax code.
   OperationID: OnChangeDetailTaxTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDetailTaxTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDetailTaxTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedMiscTaxManual(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedMiscTaxManual
   Description: Method to call when the Manual Tax Flag has Changed from True to False.  Updates MiscTax
tax amounts based on the new tax percent.
   OperationID: OnChangedMiscTaxManual
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedMiscTaxManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedMiscTaxManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscTaxFixedAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscTaxFixedAmount
   Description: Method to call when changing the fixed amount on the ContainerMiscTax table currently
   OperationID: OnChangeMiscTaxFixedAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscTaxTaxPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscTaxTaxPercent
   Description: Method to call when changing the tax percent on a tax record.  Updates ContainerMiscTax
tax amounts based on the new tax percent.
   OperationID: OnChangeMiscTaxTaxPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscTaxRateCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscTaxRateCode
   Description: Method to call when changing the rate code on a tax record.  Validates the rate and tax code
   OperationID: OnChangeMiscTaxRateCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscTaxReportableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscTaxReportableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates MiscTax
tax amounts based on the new taxable amount.
   OperationID: OnChangeMiscTaxReportableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscTaxTaxableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscTaxTaxableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates MiscTax
tax amounts based on the new taxable amount.
   OperationID: OnChangeMiscTaxTaxableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscTaxTaxAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscTaxTaxAmt
   Description: Method to call when changing the fixed tax amount on a tax record.  Updates MiscTax
tax amounts based on the new tax amount.
   OperationID: OnChangeMiscTaxTaxAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscTaxTaxDeductable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscTaxTaxDeductable
   Description: Method to call when changing the tax deductable on a tax record.  Updates MiscTax
tax amounts based on the new tax percent.
   OperationID: OnChangeMiscTaxTaxDeductable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxTaxDeductable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxTaxDeductable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscTaxTaxCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscTaxTaxCode
   Description: Method to call when changing the tax code on a MiscTax record.  Validates the tax code and
updates MiscTax tax amounts based on the new tax code.
   OperationID: OnChangeMiscTaxTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDutyTariffCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDutyTariffCode
   Description: This method should be invoked when the Tariff Code changes. This method will validate
the tariffcode and defaults the duty amount.
   OperationID: OnChangeDutyTariffCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDutyTariffCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDutyTariffCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckContainerBeforeShipping(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckContainerBeforeShipping
   Description: Purpose:  Edit container before allowing user to ship
Parameters:
<param name="ipContainerID">ContainerID</param>
Notes:
   OperationID: CheckContainerBeforeShipping
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckContainerBeforeShipping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckContainerBeforeShipping_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultContainerCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultContainerCost
   Description: Calculates container cost when CostPerVolume or Volume change
   OperationID: DefaultContainerCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultContainerCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultContainerCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultCostPerVolume(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultCostPerVolume
   Description: Calculates the CostPerVolume
   OperationID: DefaultCostPerVolume
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultCostPerVolume_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultCostPerVolume_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeContainerClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeContainerClass
   Description: This method should be invoked when the Kinetic Container Class ID changes. This method will validate
the container class and pull in the new default class information.
   OperationID: OnChangeContainerClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeContainerClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeContainerClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeShippingDays(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeShippingDays
   Description: This method should be invoked when the Kinetic Container Header Shipping Days changes.
   OperationID: OnChangeShippingDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeShippingDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShippingDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeShipDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeShipDate
   Description: This method should be invoked when the Kinetic Container Header Ship Date changes.
   OperationID: OnChangeShipDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeShipDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDueDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDueDate
   Description: This method should be invoked when the Kinetic Container Header Due Date changes.
   OperationID: OnChangeDueDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDueDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDueDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeContainerDetailLCIndCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeContainerDetailLCIndCost
   Description: This method should be invoked when the Kinetic ContainerDetail LCIndCost changes.
   OperationID: OnChangeContainerDetailLCIndCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeContainerDetailLCIndCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeContainerDetailLCIndCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateDetailExtValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateDetailExtValues
   Description: This method should be invoked when the Kinetic ContainerDetail ContainerShipQty or ShipQtyUOm changes.
   OperationID: CalculateDetailExtValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateDetailExtValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateDetailExtValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeClassCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeClassCode
   Description: This method should be invoked when the Container Class ID changes. This method will validate
the container class and pull in the new default class information.
   OperationID: OnChangeClassCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeClassCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClassCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeConNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeConNum
   Description: This method should be invoked when the ConNum changes. This method will validate
the VendCnt and pull in the new default information.
   OperationID: OnChangeConNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLoadPort(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLoadPort
   Description: This method should be invoked when the Loading Port ID changes.
This method validate selected Port and set default value of Country Imported From.
   OperationID: OnChangeLoadPort
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLoadPort_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLoadPort_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeShipStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeShipStatus
   Description: This method should be invoked when the Ship Status changes. This method will validate
the ship status and returns a value to indicate if the UI needs to run special method
to ship/unship container details when necessary.
   OperationID: OnChangeShipStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeShipStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendor
   Description: This method should be invoked when the vendor ID changes. This method will validate
the vendor and pull in the new default vendor information.
   OperationID: OnChangeVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdateContainer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdateContainer
   Description: This method will return a message if the Container Header has a change in
UpliftPercent. The user will be asked if the change should be applied to
all the Container Details as well. Also it will return a message if the Shipment Class has changed
asking if the indirect costs associated with the new class should be added to the container.
This method should be called when the user saves the record but before the Update method is called.
   OperationID: PreUpdateContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdateContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdateContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscApplyDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscApplyDate
   Description: This method should be invoked when the Apply Date in ContainerMisc changes.
This method will validate the date and get new exchange rate.
   OperationID: OnChangeMiscApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscCharge(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscCharge
   Description: This method should be invoked when the Miscellaneous Charge ID changes. This
method will validate the misc. charge and pull in the new default information.
   OperationID: OnChangeMiscCharge
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscTaxCatID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscTaxCatID
   Description: This method should be invoked when TaxCatID changes. It will retrieve the default tax flag based on entered Tax Cat ID.
   OperationID: OnChangeMiscTaxCatID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnUpdateMiscCharge(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnUpdateMiscCharge
   Description: This method should be invoked when the Container Detaile has changed and an update on Container Misc is needed. This
method will validate the misc. charge and pull in the new default information.
   OperationID: OnUpdateMiscCharge
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnUpdateMiscCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnUpdateMiscCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscCurrencyCode
   Description: This method should be invoked when the Currency Code in ContainerMisc changes.
This method will validate the currency code and pull in the new default information.
   OperationID: OnChangeMiscCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscDocEstimateAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscDocEstimateAmt
   Description: This method should be invoked when the ContainerMisc.EstimateAmt changes. This
method will validate the amount and convert it to the base currency.
   OperationID: OnChangeMiscDocEstimateAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscDocEstimateAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscDocEstimateAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscExchangeRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscExchangeRate
   Description: This method should be invoked when the Currency Exchange Rate in ContainerMisc changes.
   OperationID: OnChangeMiscExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscInvoiceLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscInvoiceLine
   Description: This method should be invoked when the Invoice Line in ContainerMisc changes.
This method will validate the invoice line and pull in the new default information.
   OperationID: OnChangeMiscInvoiceLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscInvoiceNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscInvoiceNum
   Description: This method should be invoked when the Invoice Number in ContainerMisc changes.
This method will validate the invoice number and pull in the new default information.
   OperationID: OnChangeMiscInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscMscNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscMscNum
   Description: This method should be invoked when the MscNum in ContainerMisc changes.
This method will validate the MscNum and pull in the new default information.
   OperationID: OnChangeMiscMscNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscMscNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscMscNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscPercentage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscPercentage
   Description: This method should be invoked when the percenate value changes on a container Misc Charge
   OperationID: OnChangeMiscPercentage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscPercentage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscPercentage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscRateGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscRateGrp
   Description: This method should be invoked when the Currency Rate Group in ContainerMisc changes.
This method will validate the rate group and get new exchange rate.
   OperationID: OnChangeMiscRateGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscTaxRegionCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscTaxRegionCode
   Description: This method should be invoked when the Tax Liability is changed.
   OperationID: OnChangeMiscTaxRegionCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxRegionCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxRegionCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscVendor
   Description: This method should be invoked when the vendor ID in ContainerMisc changes.
This method will validate the vendor and pull in the new default vendor information.
   OperationID: OnChangeMiscVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContainerHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContainerHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContainerHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContainerHeaderAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContainerHeaderAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerHeaderAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContainerHeaderAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerHeaderAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContainerDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContainerDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContainerDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContainerDetailAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContainerDetailAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerDetailAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContainerDetailAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerDetailAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContainerDetailTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContainerDetailTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerDetailTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContainerDetailTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerDetailTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContainerDuty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContainerDuty
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerDuty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContainerDuty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerDuty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContainerHeaderTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContainerHeaderTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerHeaderTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContainerHeaderTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerHeaderTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContainerMisc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContainerMisc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerMisc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContainerMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContainerMiscTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContainerMiscTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContainerMiscTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContainerMiscTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContainerMiscTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContainerTrackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContainerDetailAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContainerDetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDetailTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContainerDetailTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerDutyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContainerDutyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContainerHeaderAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContainerHeaderListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContainerHeaderRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerHeaderTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContainerHeaderTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerMiscRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContainerMiscRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContainerMiscTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContainerMiscTaxRow] = obj["value"]
      pass

class Erp_Tablesets_ContainerDetailAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ContainerID:int = obj["ContainerID"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
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

class Erp_Tablesets_ContainerDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.ContainerShipQty:int = obj["ContainerShipQty"]
      """  The quantity of the PO Release that is shipped on this container.  """  
      self.ShipQtyUOm:str = obj["ShipQtyUOm"]
      """  UOM of Shipment Quantity.  """  
      self.Comment:str = obj["Comment"]
      """  Free form text describing the container detail.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order on this container.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number on this container  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order on this container.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.Volume:int = obj["Volume"]
      """  Amount of space consumed in the container by this detail line, often specified in cubic square feet.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.LCAmt:int = obj["LCAmt"]
      """  The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.Weight:int = obj["Weight"]
      """  Nett Weight  """  
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost based on our unit of measure.  """  
      self.DocOurUnitCost:int = obj["DocOurUnitCost"]
      """  Unit cost based on our unit of measure in document currency.  """  
      self.Rpt1OurUnitCost:int = obj["Rpt1OurUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2OurUnitCost:int = obj["Rpt2OurUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3OurUnitCost:int = obj["Rpt3OurUnitCost"]
      """  Reporting currency value of this field  """  
      self.OrigCountryNum:int = obj["OrigCountryNum"]
      """  Country Number of the Origin Country from the PO?s Supplier Purchase Point.  """  
      self.ContainerLineRef:str = obj["ContainerLineRef"]
      """  Container shipment line reference or name.  """  
      self.ArrivedQty:int = obj["ArrivedQty"]
      """  Arrived Quantity as reported in the receipt line.  """  
      self.ArrivedQtyUOM:str = obj["ArrivedQtyUOM"]
      """  Unit of Measure of the Arrived Qty.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Received Quantity as reported in the receipt line.  """  
      self.ReceivedQtyUOM:str = obj["ReceivedQtyUOM"]
      """  Unit of Measure of the Received Qty  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  The total Duty Amount portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  The total Indirect Cost portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.POTransValue:int = obj["POTransValue"]
      """  This is by default the PO release value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.ExtTransValue:int = obj["ExtTransValue"]
      """  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  The date the container shipment detail is received. Defaults as current system date.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the container shipment detail arrived. Defaults as current system date.  """  
      self.LCSpecLineDutyAmt:int = obj["LCSpecLineDutyAmt"]
      """  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount received for this container shipment line.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.NetWeightUOM is not known.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Indicates if the Receipt line is Taxable  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  """  
      self.InAppliedLCVariance:int = obj["InAppliedLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  """  
      self.InAppliedRcptLCAmt:int = obj["InAppliedRcptLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount received for this container shipment line.  """  
      self.InExtTransValue:int = obj["InExtTransValue"]
      """  Internal usage for inclusive taxes - This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  """  
      self.InLCAmt:int = obj["InLCAmt"]
      """  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCDutyAmt:int = obj["InLCDutyAmt"]
      """  Internal usage for inclusive taxes - The total Duty Amount portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCIndCost:int = obj["InLCIndCost"]
      """  Internal usage for inclusive taxes - The total Indirect Cost portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCSpecLineDutyAmt:int = obj["InLCSpecLineDutyAmt"]
      """  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line.The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCUpliftIndCost:int = obj["InLCUpliftIndCost"]
      """  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InPOTransValue:int = obj["InPOTransValue"]
      """  Internal usage for inclusive taxes -This is by default the PO release value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  """  
      self.BaseWeight:int = obj["BaseWeight"]
      self.BaseWeightUOM:str = obj["BaseWeightUOM"]
      self.ContainerShipped:bool = obj["ContainerShipped"]
      """  Logical used by row rules to determine whether or not the container detail line is read only.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.EnableTransValue:bool = obj["EnableTransValue"]
      """  Flag to indicate if PO Trans Value can be updated.  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent can be updated.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended container detail unit cost  """  
      self.IUM:str = obj["IUM"]
      self.ManualLC:bool = obj["ManualLC"]
      """  Flag to indicate if LCIdCost can be manually updated.  """  
      self.OpenPoRelease:bool = obj["OpenPoRelease"]
      """  Indicates if the PO release tied to this detail entry is open or closed.  """  
      self.PartNum:str = obj["PartNum"]
      self.PlantName:str = obj["PlantName"]
      self.PoLineDesc:str = obj["PoLineDesc"]
      self.PORelRcvdQty:int = obj["PORelRcvdQty"]
      """  Quantity already received on this PO Release  """  
      self.PORelRemQty:int = obj["PORelRemQty"]
      """  Remaining Qty  """  
      self.PUM:str = obj["PUM"]
      self.ShipDate:str = obj["ShipDate"]
      """  Container Detail Shipped Date  """  
      self.SupplierPartNum:str = obj["SupplierPartNum"]
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Liability for the associated purchase order.  """  
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      """  Full description of Tax Region.  """  
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.ThisTranUOM:str = obj["ThisTranUOM"]
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount.  This is the sum of ContainerDetailTax.TaxAmt.  """  
      self.UpdatedKeyRow:bool = obj["UpdatedKeyRow"]
      """  Logical indicates to the UI when a key field has been changed.  Set this to yes if this is the row you want the UI to find and display.  """  
      self.ValidPOInfoEntered:bool = obj["ValidPOInfoEntered"]
      """  Logical indicating that a valid po number, po line and po release has been entered and the user may not update the other container detail values.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.BaseVolume:int = obj["BaseVolume"]
      self.BaseVolumeUOM:str = obj["BaseVolumeUOM"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains our revision. Default from the PartRev.RevisionNum field.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CommodityDescription:str = obj["CommodityDescription"]
      self.ContainerHeaderContainerDescription:str = obj["ContainerHeaderContainerDescription"]
      self.ContainerHeaderShipDate:str = obj["ContainerHeaderShipDate"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.POHeaderInPrice:bool = obj["POHeaderInPrice"]
      self.PORelBTOOrderNum:int = obj["PORelBTOOrderNum"]
      self.PORelBTOOrderLine:int = obj["PORelBTOOrderLine"]
      self.PORelRefCodeDesc:str = obj["PORelRefCodeDesc"]
      self.PORelPurchasingFactor:int = obj["PORelPurchasingFactor"]
      self.PORelXRelQty:int = obj["PORelXRelQty"]
      self.PORelOpenRelease:bool = obj["PORelOpenRelease"]
      self.PORelRelQty:int = obj["PORelRelQty"]
      self.PORelNeedByDate:str = obj["PORelNeedByDate"]
      self.PORelBTOOrderRelNum:int = obj["PORelBTOOrderRelNum"]
      self.PORelPromiseDt:str = obj["PORelPromiseDt"]
      self.PORelPurchasingFactorDirection:str = obj["PORelPurchasingFactorDirection"]
      self.PORelArrivedQty:int = obj["PORelArrivedQty"]
      self.PORelDueDate:str = obj["PORelDueDate"]
      self.PORelPlant:str = obj["PORelPlant"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerDetailTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  ReportableAmt  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time when the record was last changed.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.CollectionType:int = obj["CollectionType"]
      """  CollectionType  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution date.  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date to determine the tax rate.  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.EnableSuperGRate:str = obj["EnableSuperGRate"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.DocScrDedTaxAmt:int = obj["DocScrDedTaxAmt"]
      self.DocScrFixedAmount:int = obj["DocScrFixedAmount"]
      self.DocScrReportableAmt:int = obj["DocScrReportableAmt"]
      self.DocScrTaxableAmt:int = obj["DocScrTaxableAmt"]
      self.DocScrTaxAmt:int = obj["DocScrTaxAmt"]
      self.DocScrTaxAmtVar:int = obj["DocScrTaxAmtVar"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerDutyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order on this container.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number on this container  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order on this container.  """  
      self.DutySeq:int = obj["DutySeq"]
      """  Unique Number automatically assigned which is used along with ContainerID, PONum, POLine and PORelNum to uniquely identify the Duty record within the Container Shipment Line.  """  
      self.TariffCode:str = obj["TariffCode"]
      """  Tariff Code must be for a Preference Scheme that is linked to the Country of Origin.  """  
      self.DutyAmt:int = obj["DutyAmt"]
      """   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  """  
      self.CommentText:str = obj["CommentText"]
      """  Container Duty Comments  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InDutyAmt:int = obj["InDutyAmt"]
      """  InDutyAmt  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.ScrDutyAmt:int = obj["ScrDutyAmt"]
      """   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount - Screen Value  """  
      self.BitFlag:int = obj["BitFlag"]
      self.POHeaderTaxRegionCode:str = obj["POHeaderTaxRegionCode"]
      self.POHeaderInPrice:bool = obj["POHeaderInPrice"]
      self.TariffDescription:str = obj["TariffDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerHeaderAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ContainerID:int = obj["ContainerID"]
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

class Erp_Tablesets_ContainerHeaderListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Date the container is to ship.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Logical indicating if the container has shipped.  """  
      self.ContainerClass:str = obj["ContainerClass"]
      """  Class of this container.  Must be a valid entry in the ContainerClass master file.  """  
      self.ContainerCost:int = obj["ContainerCost"]
      """  Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ShippingDays:int = obj["ShippingDays"]
      """   Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.

This is intiially defaulted to the value on the ContainerClass but can be overridden by the end user.  """  
      self.ContainerComments:str = obj["ContainerComments"]
      """  Notes/comments about the container shipment.  """  
      self.ContainerDescription:str = obj["ContainerDescription"]
      """  Free form text that describes this particular container.  """  
      self.NewPoRelAtReceipt:bool = obj["NewPoRelAtReceipt"]
      """  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default.
Having a Volume UOM will provides the ability to calculate total volume  """  
      self.CostPerVolume:int = obj["CostPerVolume"]
      """  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  """  
      self.ContainerReference:str = obj["ContainerReference"]
      """  The container reference is typically the shipping company's assigned container ID.  """  
      self.LCReference:str = obj["LCReference"]
      """  Reference information for landed cost.  """  
      self.LCComment:str = obj["LCComment"]
      """  Landed Cost Comments  """  
      self.LCVariance:int = obj["LCVariance"]
      """  This field holds the variance amount for the landed costs.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost (container cost) was disbursed among the container details.  Valid options are Volume (default), Weight, Value and Manual.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.CurrencyDate:str = obj["CurrencyDate"]
      """  Currency Date  """  
      self.DocContainerCost:int = obj["DocContainerCost"]
      """  Total cost to ship this container in the doc currency.  """  
      self.PORelShipOption:str = obj["PORelShipOption"]
      """  Valid values = "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  This is an optional field.  """  
      self.Rpt1ContainerCost:int = obj["Rpt1ContainerCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ContainerCost:int = obj["Rpt2ContainerCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ContainerCost:int = obj["Rpt3ContainerCost"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.LoadPortID:str = obj["LoadPortID"]
      """  Valid Loading Port ID where goods are loaded on the vessel.  """  
      self.DechargePortID:str = obj["DechargePortID"]
      """  Valid port location where goods are unloaded.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  """  
      self.FOB:str = obj["FOB"]
      """  Descriptive code assigned by user which uniquely identifies the fob record.  """  
      self.ContainerCount:int = obj["ContainerCount"]
      """  Number of Containers in this shipment.  """  
      self.PackageCount:int = obj["PackageCount"]
      """  Number of Packages in this shipment.  """  
      self.Weight:int = obj["Weight"]
      """  Total Weight of the shipment.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.ConNum:int = obj["ConNum"]
      """  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  """  
      self.BOLading:str = obj["BOLading"]
      """  Bill of Lading Number  """  
      self.BOExchange:str = obj["BOExchange"]
      """  Bill of Exchange Number  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  """  
      self.PORelRcptOption:str = obj["PORelRcptOption"]
      """  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.Vessel:str = obj["Vessel"]
      """  Name of the vessel containing the shipment.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  """  
      self.AppliedLCAmt:int = obj["AppliedLCAmt"]
      """  The total Landed Cost Amount disbursed or applied to this container shipment.  """  
      self.ContainerDutyAmt:int = obj["ContainerDutyAmt"]
      """  This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ContainerIndCost:int = obj["ContainerIndCost"]
      """  This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ApplyToLC:bool = obj["ApplyToLC"]
      """  Flag to indicate if all of the shipment duties and indirect costs needs to be applied or disbursed.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the container shipment arrived. Defaults as current system date.  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  The date the container shipment is received. Defaults as current system date.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount received for this container shipment.  """  
      self.UpliftIndCost:int = obj["UpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.DueDate:str = obj["DueDate"]
      """  The date that the Container Shipment is due to arrive.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplayContainerID:str = obj["DisplayContainerID"]
      """  ContainerID in display format.  """  
      self.ResetPORelDates:bool = obj["ResetPORelDates"]
      """  Logical indicating whether or not on ship date change or shipping days change the po release due dates are to be upated.  """  
      self.eshReceived:bool = obj["eshReceived"]
      """  Logical used to indicate if all po rels for the current plant have been received.  """  
      self.TotalExtCost:int = obj["TotalExtCost"]
      """  Total shipment value  """  
      self.TotalWeight:int = obj["TotalWeight"]
      """  Total weight of the items shipped on the container detail.  """  
      self.LCAppliedAmt:int = obj["LCAppliedAmt"]
      """  Amount of Landed Cost applied  """  
      self.LCAccount:str = obj["LCAccount"]
      """  Landed Cost account for display  """  
      self.LCAccountDesc:str = obj["LCAccountDesc"]
      """  Account Description  """  
      self.SkipLandedCost:bool = obj["SkipLandedCost"]
      self.LCMessage:str = obj["LCMessage"]
      """  Landed cost message used to inform the user on retrieval of data that the applied and container costs do not equal.  """  
      self.PartialReceipt:bool = obj["PartialReceipt"]
      """  Logical indicating whether or not the container has been fully receipt.  If yes then the container has only been partially received.  """  
      self.DispShipStatus:str = obj["DispShipStatus"]
      """  Display Ship Status.  """  
      self.DispRcptStatus:str = obj["DispRcptStatus"]
      """  Display Receipt Status  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent should be enabled.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.EnableLCAfterRcpt:bool = obj["EnableLCAfterRcpt"]
      """  Flag to indicate if record can be updated after Receipt.  """  
      self.EnableSplitContainer:bool = obj["EnableSplitContainer"]
      """  Flag to indicate if container details can be split into another container shipment.  """  
      self.EnableTransferCost:bool = obj["EnableTransferCost"]
      """  Flag to indicate if indirect costs can be transferred into another container shipment.  """  
      self.UpdateDtlRecs:bool = obj["UpdateDtlRecs"]
      """  Flag to indicate if container details need to be refreshed after changing the UpliftPercent from header.  """  
      self.ReceiveAll:bool = obj["ReceiveAll"]
      """  Flag to indicate that all container receipt details will be "received" automatically.  """  
      self.TestImportFields:bool = obj["TestImportFields"]
      """  Test Import Fields "ImportNumber" and "ImportedFromDesc" to see if the Receipt Line had already non empty values for these fields and the Lot is set for this Receipt Line.  """  
      self.ContainerClassDescription:str = obj["ContainerClassDescription"]
      """  Descriptive text identifying the Container Class  """  
      self.DechargePortPortID:str = obj["DechargePortPortID"]
      """  A unique PortID within the Company and must always be associated with a Country.  """  
      self.DechargePortDescription:str = obj["DechargePortDescription"]
      """  Country Port Description.  This must be a unique port description within the Company.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.LoadPortPortID:str = obj["LoadPortPortID"]
      """  A unique PortID within the Company and must always be associated with a Country.  """  
      self.LoadPortDescription:str = obj["LoadPortDescription"]
      """  Country Port Description.  This must be a unique port description within the Company.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.VendCntName:str = obj["VendCntName"]
      """  Contact name.  """  
      self.VendCntEmailAddress:str = obj["VendCntEmailAddress"]
      """  Contact email address.  """  
      self.VendCntPhoneNum:str = obj["VendCntPhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  """  
      self.VendCntFaxNum:str = obj["VendCntFaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  """  
      self.VendorAddress2:str = obj["VendorAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorCountry:str = obj["VendorCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorAddress3:str = obj["VendorAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorState:str = obj["VendorState"]
      """  Can be blank.  """  
      self.VendorZIP:str = obj["VendorZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorAddress1:str = obj["VendorAddress1"]
      """  First address line of the Supplier  """  
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorCity:str = obj["VendorCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Date the container is to ship.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Logical indicating if the container has shipped.  """  
      self.ContainerClass:str = obj["ContainerClass"]
      """  Class of this container.  Must be a valid entry in the ContainerClass master file.  """  
      self.ContainerCost:int = obj["ContainerCost"]
      """  Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ShippingDays:int = obj["ShippingDays"]
      """   Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.

This is intiially defaulted to the value on the ContainerClass but can be overridden by the end user.  """  
      self.ContainerComments:str = obj["ContainerComments"]
      """  Notes/comments about the container shipment.  """  
      self.ContainerDescription:str = obj["ContainerDescription"]
      """  Free form text that describes this particular container.  """  
      self.NewPoRelAtReceipt:bool = obj["NewPoRelAtReceipt"]
      """  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default.
Having a Volume UOM will provides the ability to calculate total volume  """  
      self.CostPerVolume:int = obj["CostPerVolume"]
      """  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  """  
      self.ContainerReference:str = obj["ContainerReference"]
      """  The container reference is typically the shipping company's assigned container ID.  """  
      self.LCReference:str = obj["LCReference"]
      """  Reference information for landed cost.  """  
      self.LCComment:str = obj["LCComment"]
      """  Landed Cost Comments  """  
      self.LCVariance:int = obj["LCVariance"]
      """  This field holds the variance amount for the landed costs.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost (container cost) was disbursed among the container details.  Valid options are Volume (default), Weight, Value and Manual.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.CurrencyDate:str = obj["CurrencyDate"]
      """  Currency Date  """  
      self.DocContainerCost:int = obj["DocContainerCost"]
      """  Total cost to ship this container in the doc currency.  """  
      self.PORelShipOption:str = obj["PORelShipOption"]
      """  Valid values = "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  This is an optional field.  """  
      self.Rpt1ContainerCost:int = obj["Rpt1ContainerCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ContainerCost:int = obj["Rpt2ContainerCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ContainerCost:int = obj["Rpt3ContainerCost"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.LoadPortID:str = obj["LoadPortID"]
      """  Valid Loading Port ID where goods are loaded on the vessel.  """  
      self.DechargePortID:str = obj["DechargePortID"]
      """  Valid port location where goods are unloaded.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  """  
      self.FOB:str = obj["FOB"]
      """  Descriptive code assigned by user which uniquely identifies the fob record.  """  
      self.ContainerCount:int = obj["ContainerCount"]
      """  Number of Containers in this shipment.  """  
      self.PackageCount:int = obj["PackageCount"]
      """  Number of Packages in this shipment.  """  
      self.Weight:int = obj["Weight"]
      """  Total Weight of the shipment.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.ConNum:int = obj["ConNum"]
      """  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  """  
      self.BOLading:str = obj["BOLading"]
      """  Bill of Lading Number  """  
      self.BOExchange:str = obj["BOExchange"]
      """  Bill of Exchange Number  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  """  
      self.PORelRcptOption:str = obj["PORelRcptOption"]
      """  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.Vessel:str = obj["Vessel"]
      """  Name of the vessel containing the shipment.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  """  
      self.AppliedLCAmt:int = obj["AppliedLCAmt"]
      """  The total Landed Cost Amount disbursed or applied to this container shipment.  """  
      self.ContainerDutyAmt:int = obj["ContainerDutyAmt"]
      """  This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ContainerIndCost:int = obj["ContainerIndCost"]
      """  This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ApplyToLC:bool = obj["ApplyToLC"]
      """  Flag to indicate if all of the shipment duties and indirect costs needs to be applied or disbursed.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the container shipment arrived. Defaults as current system date.  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  The date the container shipment is received. Defaults as current system date.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount received for this container shipment.  """  
      self.UpliftIndCost:int = obj["UpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.DueDate:str = obj["DueDate"]
      """  The date that the Container Shipment is due to arrive.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AdditionalShippingDays:int = obj["AdditionalShippingDays"]
      """  **NOT USED - REMOVE**  """  
      self.EstimatedArrivalDate:str = obj["EstimatedArrivalDate"]
      """  **NOT USED - Remove **  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Set from the earliest need by date set against the po releases.  """  
      self.PromiseDate:str = obj["PromiseDate"]
      """  Specifies the date on which the supplier has promised to deliver the container.  """  
      self.TaxesCalculated:bool = obj["TaxesCalculated"]
      """  Reflects whether taxes have been calculated  """  
      self.InAppliedLCAmt:int = obj["InAppliedLCAmt"]
      """  Internal usage for inclusive taxes -The total Landed Cost Amount disbursed or applied to this container shipment.  """  
      self.InAppliedLCVariance:int = obj["InAppliedLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  """  
      self.InAppliedRcptLCAmt:int = obj["InAppliedRcptLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount received for this container shipment.  """  
      self.InContainerCost:int = obj["InContainerCost"]
      """  Internal usage for inclusive taxes - Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.InContainerDutyAmt:int = obj["InContainerDutyAmt"]
      """  Internal usage for inclusive taxes - This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.InContainerIndCost:int = obj["InContainerIndCost"]
      """  Internal usage for inclusive taxes - This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.InDocContainerCost:int = obj["InDocContainerCost"]
      """  Internal usage for inclusive taxes - Total cost to ship this container in the doc currency.  """  
      self.InLCAppliedAmt:int = obj["InLCAppliedAmt"]
      """  ** NOT USED TO BE DROPPED 10.2 **  """  
      self.InLCVariance:int = obj["InLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the variance amount for the landed costs.  """  
      self.InSpecDutyAmt:int = obj["InSpecDutyAmt"]
      """  Internal usage for inclusive taxes - This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  """  
      self.InUpliftIndCost:int = obj["InUpliftIndCost"]
      """  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.DisplayContainerID:str = obj["DisplayContainerID"]
      """  ContainerID in display format.  """  
      self.DispRcptStatus:str = obj["DispRcptStatus"]
      """  Display Receipt Status  """  
      self.DispShipStatus:str = obj["DispShipStatus"]
      """  Display Ship Status.  """  
      self.EnableCalcTaxes:bool = obj["EnableCalcTaxes"]
      """   Flag poplulated from XbSyst.ReceiptTaxCalculate 
Determines if taxes can be calculated at update or via action menu  """  
      self.EnableLCAfterRcpt:bool = obj["EnableLCAfterRcpt"]
      """  Flag to indicate if record can be updated after Receipt.  """  
      self.EnableSplitContainer:bool = obj["EnableSplitContainer"]
      """  Flag to indicate if container details can be split into another container shipment.  """  
      self.EnableTransferCost:bool = obj["EnableTransferCost"]
      """  Flag to indicate if indirect costs can be transferred into another container shipment.  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent should be enabled.  """  
      self.eshReceived:bool = obj["eshReceived"]
      """  Logical used to indicate if all po rels for the current plant have been received.  """  
      self.LCAccount:str = obj["LCAccount"]
      """  Landed Cost account for display  """  
      self.LCAccountDesc:str = obj["LCAccountDesc"]
      """  Account Description  """  
      self.LCAppliedAmt:int = obj["LCAppliedAmt"]
      """  Amount of Landed Cost applied  """  
      self.LCMessage:str = obj["LCMessage"]
      """  Landed cost message used to inform the user on retrieval of data that the applied and container costs do not equal.  """  
      self.PartialReceipt:bool = obj["PartialReceipt"]
      """  Logical indicating whether or not the container has been fully receipt.  If yes then the container has only been partially received.  """  
      self.ReceiveAll:bool = obj["ReceiveAll"]
      """  Flag to indicate that all container receipt details will be "received" automatically.  """  
      self.ResetPORelDates:bool = obj["ResetPORelDates"]
      """  Logical indicating whether or not on ship date change or shipping days change the po release due dates are to be upated.  """  
      self.SkipLandedCost:bool = obj["SkipLandedCost"]
      self.TestImportFields:bool = obj["TestImportFields"]
      """  Test Import Fields "ImportNumber" and "ImportedFromDesc" to see if the Receipt Line had already non empty values for these fields and the Lot is set for this Receipt Line.  """  
      self.TotalAmt:int = obj["TotalAmt"]
      """  Total amount.  This is the sum of all the other total fields.  """  
      self.TotalExtCost:int = obj["TotalExtCost"]
      """  Total shipment value  """  
      self.TotalWeight:int = obj["TotalWeight"]
      """  Total weight of the items shipped on the container detail.  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total Deductable Tax Amount  """  
      self.TotDutiesAmt:int = obj["TotDutiesAmt"]
      """  Total duties amount.  """  
      self.TotIndirectCostsAmt:int = obj["TotIndirectCostsAmt"]
      """  Total Indirect Costs amount.  """  
      self.TotLinesAmt:int = obj["TotLinesAmt"]
      """  Total amount for all Container Lines  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax Amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total Tax amount.  """  
      self.TotWHTaxAmt:int = obj["TotWHTaxAmt"]
      """  Total WithHolding Tax Amount  """  
      self.UpdateDtlRecs:bool = obj["UpdateDtlRecs"]
      """  Flag to indicate if container details need to be refreshed after changing the UpliftPercent from header.  """  
      self.UpdIndCosts:bool = obj["UpdIndCosts"]
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.EnableTaxAtLineLevel:bool = obj["EnableTaxAtLineLevel"]
      """   Flag poplulated from XbSyst.APTaxLnLevel.  
Determines if taxes are calculated at line level (true) or document level (false)  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.DisableApplyLandedCost:bool = obj["DisableApplyLandedCost"]
      """  Determine if the Apply Landed Cost button in Kinetic should be disabled.  """  
      self.OkToLeaveContainerHead:bool = obj["OkToLeaveContainerHead"]
      """  Flag to determine for Kinetic if use can leave the Container Header record/screen.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ContainerClassDescription:str = obj["ContainerClassDescription"]
      self.DechargePortDescription:str = obj["DechargePortDescription"]
      self.DechargePortPortID:str = obj["DechargePortPortID"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.LoadPortPortID:str = obj["LoadPortPortID"]
      self.LoadPortDescription:str = obj["LoadPortDescription"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.VendCntPhoneNum:str = obj["VendCntPhoneNum"]
      self.VendCntName:str = obj["VendCntName"]
      self.VendCntFaxNum:str = obj["VendCntFaxNum"]
      self.VendCntEmailAddress:str = obj["VendCntEmailAddress"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorState:str = obj["VendorState"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorName:str = obj["VendorName"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerHeaderTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time when the record was last changed.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution Date  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date to determine the tax rate.  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  TextCode  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SummaryOnly:bool = obj["SummaryOnly"]
      """  flag to indicate if this record is used only to total detail records,  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.EnableSuperGRate:bool = obj["EnableSuperGRate"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      """  Display field for Rpt1ScrFixedAmount  """  
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      """  Display field for Rpt2FixedAmount  """  
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      """  Display field for Rpt3rFixedAmount  """  
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrDocDedTaxAmt:int = obj["ScrDocDedTaxAmt"]
      self.ScrDocFixedAmount:int = obj["ScrDocFixedAmount"]
      """  Doc Fixed Amount  """  
      self.ScrDocReportableAmt:int = obj["ScrDocReportableAmt"]
      self.ScrDocTaxableAmt:int = obj["ScrDocTaxableAmt"]
      self.ScrDocTaxAmt:int = obj["ScrDocTaxAmt"]
      self.ScrDocTaxAmtVar:int = obj["ScrDocTaxAmtVar"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  FixedAmount  """  
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.MiscSeq:int = obj["MiscSeq"]
      """  Unique Number automatically assigned within the ContainerID to uniquely identify each Indirect Costs for this container shipment.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Miscellaneous Charge ID that is flagged for Landed Cost  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvMsc record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line from corresponding APInvMsc record.  """  
      self.MscNum:int = obj["MscNum"]
      """  The unique sequence number identifying the AP invoice miscellaneous charge.  """  
      self.ExcludeFromLC:bool = obj["ExcludeFromLC"]
      """  Flag to indicate if the Indirect Cost is to be excluded from the Landed Cost calculation.  Disabled when IncTransValue is checked.  """  
      self.IncTransValue:bool = obj["IncTransValue"]
      """  Flag to indicate if the Indirect Cost is to be included in the Transaction Value (statistical value) which is used to calculate duties.  Disabled when the ExcludeFromLC is checked.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.EstimateAmt:int = obj["EstimateAmt"]
      """  Estimated Amount used in landed cost calculation if actual amount is not available.  """  
      self.DocEstimateAmt:int = obj["DocEstimateAmt"]
      """  Estimated Amount in currency specified.  """  
      self.ActualAmt:int = obj["ActualAmt"]
      """  Actual Amount coming from the posted AP invoice miscellaneous charge.  """  
      self.DocActualAmt:int = obj["DocActualAmt"]
      """  Actual Amount in currency specified.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.CommentText:str = obj["CommentText"]
      """  Container Indirect Cost Comments  """  
      self.Rpt1EstimateAmt:int = obj["Rpt1EstimateAmt"]
      """  Reporting currency value of the Estimated Amount.  """  
      self.Rpt2EstimateAmt:int = obj["Rpt2EstimateAmt"]
      """  Reporting currency value of the Estimated Amount.  """  
      self.Rpt3EstimateAmt:int = obj["Rpt3EstimateAmt"]
      """  Reporting currency value of the Estimated Amount.  """  
      self.Rpt1ActualAmt:int = obj["Rpt1ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt2ActualAmt:int = obj["Rpt2ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt3ActualAmt:int = obj["Rpt3ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date that will be used to get the exchange rate if the indirect cost is not associated with an invoice miscellaneous charge.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocHstEstimateAmt:int = obj["DocHstEstimateAmt"]
      """  Historical Doc Estimate Amount  """  
      self.HstEstimateAmt:int = obj["HstEstimateAmt"]
      """  Historical Estimate Amount  """  
      self.Rpt1HstEstimateAmt:int = obj["Rpt1HstEstimateAmt"]
      """  Historical Rpt1 Estimate Amount  """  
      self.Rpt2HstEstimateAmt:int = obj["Rpt2HstEstimateAmt"]
      """  Historical Rpt2 Estimate Amount  """  
      self.Rpt3HstEstimateAmt:int = obj["Rpt3HstEstimateAmt"]
      """  Historical Rpt3 Estimate Amount  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Indirect Cost. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Indicates if the Indirect Cost is Taxable  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Liability for this Receipt  """  
      self.InEstimateAmt:int = obj["InEstimateAmt"]
      """  Internal usage for inclusive taxes - Estimated Amount used in landed cost calculation if actual amount is not available.  """  
      self.DocInEstimateAmt:int = obj["DocInEstimateAmt"]
      """  Internal usage for inclusive taxes - Estimated Amount in currency specified.  """  
      self.Rpt1InEstimateAmt:int = obj["Rpt1InEstimateAmt"]
      """  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  """  
      self.Rpt2InEstimateAmt:int = obj["Rpt2InEstimateAmt"]
      """  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  """  
      self.Rpt3InEstimateAmt:int = obj["Rpt3InEstimateAmt"]
      """  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  """  
      self.InHstEstimateAmt:int = obj["InHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Estimate Amount  """  
      self.DocInHstEstimateAmt:int = obj["DocInHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Doc Estimate Amount  """  
      self.Rpt1InHstEstimateAmt:int = obj["Rpt1InHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Rpt1 Estimate Amount  """  
      self.Rpt2InHstEstimateAmt:int = obj["Rpt2InHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Rpt2 Estimate Amount  """  
      self.Rpt3InHstEstimateAmt:int = obj["Rpt3InHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Rpt3 Estimate Amount  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for currency "BASE"  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount.  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this indirect cost.  """  
      self.RateLabel:str = obj["RateLabel"]
      """  Label for ExchangeRate  """  
      self.ScrEstimateAmt:int = obj["ScrEstimateAmt"]
      """  Estimated Amount used in landed cost calculation if actual amount is not available - Screen Value  """  
      self.Rpt1ScrEstimateAmt:int = obj["Rpt1ScrEstimateAmt"]
      """  Reporting currency value of the Estimated Amount - Screen Value  """  
      self.Rpt2ScrEstimateAmt:int = obj["Rpt2ScrEstimateAmt"]
      """  Reporting currency value of the Estimated Amount - Screen value  """  
      self.Rpt3ScrEstimateAmt:int = obj["Rpt3ScrEstimateAmt"]
      """  Reporting currency value of the Estimated Amount - Screen value  """  
      self.ScrHstEstimateAmt:int = obj["ScrHstEstimateAmt"]
      """  Historical Estimate Amount - Screen value  """  
      self.Rpt1ScrHstEstimateAmt:int = obj["Rpt1ScrHstEstimateAmt"]
      """  Historical Rpt1 Estimate Amount - Screen value  """  
      self.Rpt2ScrHstEstimateAmt:int = obj["Rpt2ScrHstEstimateAmt"]
      """  Historical Rpt2 Estimate Amount - Screen value  """  
      self.Rpt3ScrHstEstimateAmt:int = obj["Rpt3ScrHstEstimateAmt"]
      """  Historical Rpt3 Estimate Amount - Screen value  """  
      self.DocScrEstimateAmt:int = obj["DocScrEstimateAmt"]
      """  Estimated Amount in currency specified - Screen value  """  
      self.DocScrHstEstimateAmt:int = obj["DocScrHstEstimateAmt"]
      """  Estimated Amount used in landed cost calculation if actual amount is not available - Screen Value  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.PurMiscLCAmount:int = obj["PurMiscLCAmount"]
      self.PurMiscLCCurrencyCode:str = obj["PurMiscLCCurrencyCode"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.PurMiscLCDisburseMethod:str = obj["PurMiscLCDisburseMethod"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorName:str = obj["VendorName"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerMiscTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.MiscSeq:int = obj["MiscSeq"]
      """  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  ** NOT USED TO BE DROPPED 10.2 ** The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  ReportableAmt  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time when the record was last changed.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.CollectionType:int = obj["CollectionType"]
      """  CollectionType  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution date.  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date to determine the tax rate.  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DocScrDedTaxAmt:int = obj["DocScrDedTaxAmt"]
      self.DocScrReportableAmt:int = obj["DocScrReportableAmt"]
      self.DocScrTaxableAmt:int = obj["DocScrTaxableAmt"]
      self.DocScrTaxAmt:int = obj["DocScrTaxAmt"]
      self.DocScrTaxAmtVar:int = obj["DocScrTaxAmtVar"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.DocScrFixedAmount:int = obj["DocScrFixedAmount"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ContainerMiscApplyDate:str = obj["ContainerMiscApplyDate"]
      self.ContainerMiscInPrice:bool = obj["ContainerMiscInPrice"]
      self.ContainerMiscCurrencyCode:str = obj["ContainerMiscCurrencyCode"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CalcDtlExtTransValue_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class CalcDtlExtTransValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalculateContainerTaxes_input:
   """ Required : 
   containerID
   calledFromUI
   refreshTableSet
   ds
   """  
   def __init__(self, obj):
      self.containerID:int = obj["containerID"]
      self.calledFromUI:bool = obj["calledFromUI"]
      self.refreshTableSet:bool = obj["refreshTableSet"]
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class CalculateContainerTaxes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalculateDetailExtValues_input:
   """ Required : 
   ipShipQty
   ipShipQtyUOM
   ds
   """  
   def __init__(self, obj):
      self.ipShipQty:int = obj["ipShipQty"]
      """  Proposed ContainerDetail ContainerShipQty  """  
      self.ipShipQtyUOM:str = obj["ipShipQtyUOM"]
      """  Proposed ContainerDetail ShipQtyUOm  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class CalculateDetailExtValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalculateExtCostAndWeight_input:
   """ Required : 
   shipQty
   shipUOM
   partNum
   ourUnitCost
   poNum
   poLine
   """  
   def __init__(self, obj):
      self.shipQty:int = obj["shipQty"]
      self.shipUOM:str = obj["shipUOM"]
      self.partNum:str = obj["partNum"]
      self.ourUnitCost:int = obj["ourUnitCost"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      pass

class CalculateExtCostAndWeight_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.weight:int = obj["parameters"]
      self.grossWeight:int = obj["parameters"]
      self.vExtCost:int = obj["parameters"]
      pass

      """  output parameters  """  

class CheckContainerBeforeShipping_input:
   """ Required : 
   ipContainerID
   """  
   def __init__(self, obj):
      self.ipContainerID:int = obj["ipContainerID"]
      pass

class CheckContainerBeforeShipping_output:
   def __init__(self, obj):
      pass

class CreateContainerIndCost_input:
   """ Required : 
   ds
   ds1
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvMiscChargesTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds1"]
      pass

class CreateContainerIndCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvMiscChargesTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds1"]
      pass

      """  output parameters  """  

class CreateMultiDetails_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class CreateMultiDetails_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      self.containerErrors:str = obj["parameters"]
      self.detailAdded:bool = obj["detailAdded"]
      pass

      """  output parameters  """  

class DefaultContainerCost_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class DefaultContainerCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultCostPerVolume_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class DefaultCostPerVolume_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   containerID
   """  
   def __init__(self, obj):
      self.containerID:int = obj["containerID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DisburseLandedCosts_input:
   """ Required : 
   ipContainerID
   """  
   def __init__(self, obj):
      self.ipContainerID:int = obj["ipContainerID"]
      pass

class DisburseLandedCosts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opLCApplied:int = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_APInvMiscChargesTableset:
   def __init__(self, obj):
      self.APInvMsc:list[Erp_Tablesets_APInvMscRow] = obj["APInvMsc"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APInvMscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  Duplicated  from the related APInvHed record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the InvcDetl record for the Invoice and the adding 1 to it.  """  
      self.MscNum:int = obj["MscNum"]
      """  Number automatically assigned by invoice entry which is used along with VendorNum, InvoiceNum and InvoiceLine to uniquely identify the miscellaneous record within the invoice.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Code that relates this invoice miscellaneous charge to the PurMisc master. Entered via a DDSL widget.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. Defaulted from PurMisc.Description.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  miscellaneous amount.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  miscellaneous amount in the vendor currency.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that this miscellaneous record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence number of the Miscellaneous Charge  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """   Identifies Tax Category for this Misc. item.
Defaults from PurMisc.TaxCatID.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceLine:int = obj["GlbInvoiceLine"]
      """  Global Invoice Line identifier.  Used in Consolidated Purchasing.  """  
      self.GlbMscNum:int = obj["GlbMscNum"]
      """  Global Invoice Miscellaneous Charge identifier.  Used in Consolidated Purchasing.  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.InvExpSeq:int = obj["InvExpSeq"]
      """  Reference to the APInvExp record that contains the gl distribution for this charge.  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the AP Miscellaneous Charge is for Landed Cost.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  The Container Shipment ID (also known as the ContainerID).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID of the associated receipt's indirect cost.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the associated receipt's indirect cost.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.LCVendorNum:int = obj["LCVendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  This field, together with the PackSlip and PurPoint, is used to link the APInvMsc to the RcvMisc record that references this misc charge as a Landed Cost's Indirect Cost.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Like PurMisc.LCDisburseMethod. Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  miscellaneous amount including taxes.  """  
      self.DocInMiscAmt:int = obj["DocInMiscAmt"]
      """  miscellaneous amount in the vendor currency including taxes.  """  
      self.Rpt1InMiscAmt:int = obj["Rpt1InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InMiscAmt:int = obj["Rpt2InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InMiscAmt:int = obj["Rpt3InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.DevInt1:int = obj["DevInt1"]
      """  Reserved for Development - Integer  """  
      self.DevInt2:int = obj["DevInt2"]
      """  Reserved for Development - Integer  """  
      self.DevDec1:int = obj["DevDec1"]
      """  Reserved for development - decimal  """  
      self.DevDec2:int = obj["DevDec2"]
      """  Reserved for development - decimal  """  
      self.DevDec3:int = obj["DevDec3"]
      """  Reserved for development - decimal  """  
      self.DevDec4:int = obj["DevDec4"]
      """  Reserved for development - decimal  """  
      self.DevLog1:bool = obj["DevLog1"]
      """  Reserved for development  - logical  """  
      self.DevLog2:bool = obj["DevLog2"]
      """  Reserved for development - logical  """  
      self.DevChar1:str = obj["DevChar1"]
      """  Reserved for development  - character  """  
      self.DevChar2:str = obj["DevChar2"]
      """  Reserved for development - character  """  
      self.DevDate1:str = obj["DevDate1"]
      """  Reserved for development - date  """  
      self.DevDate2:str = obj["DevDate2"]
      """  Reserved for development - date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  NoTaxRecalc  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  Code1099ID  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  FormTypeID  """  
      self.Gen1099Code:str = obj["Gen1099Code"]
      """  Gen1099Code  """  
      self.TaxExemptReasonCode:str = obj["TaxExemptReasonCode"]
      """  TaxExemptReasonCode  """  
      self.PlasticPackTaxReportID:str = obj["PlasticPackTaxReportID"]
      """  The Plastic Packaging Tax Report ID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DebitMemo:bool = obj["DebitMemo"]
      self.DocScrTotalDedTax:int = obj["DocScrTotalDedTax"]
      self.DocScrTotalSATax:int = obj["DocScrTotalSATax"]
      self.DocScrTotalTax:int = obj["DocScrTotalTax"]
      self.GroupID:str = obj["GroupID"]
      self.InPrice:bool = obj["InPrice"]
      self.LCEnabled:bool = obj["LCEnabled"]
      self.Posted:bool = obj["Posted"]
      self.RecordSource:str = obj["RecordSource"]
      self.Rpt1ScrMiscAmt:int = obj["Rpt1ScrMiscAmt"]
      self.Rpt1ScrTotalDedTax:int = obj["Rpt1ScrTotalDedTax"]
      self.Rpt1ScrTotalSATax:int = obj["Rpt1ScrTotalSATax"]
      self.Rpt1ScrTotalTax:int = obj["Rpt1ScrTotalTax"]
      self.Rpt2ScrMiscAmt:int = obj["Rpt2ScrMiscAmt"]
      self.Rpt2ScrTotalDedTax:int = obj["Rpt2ScrTotalDedTax"]
      self.Rpt2ScrTotalSATax:int = obj["Rpt2ScrTotalSATax"]
      self.Rpt2ScrTotalTax:int = obj["Rpt2ScrTotalTax"]
      self.Rpt3ScrMiscAmt:int = obj["Rpt3ScrMiscAmt"]
      self.Rpt3ScrTotalDedTax:int = obj["Rpt3ScrTotalDedTax"]
      self.Rpt3ScrTotalSATax:int = obj["Rpt3ScrTotalSATax"]
      self.Rpt3ScrTotalTax:int = obj["Rpt3ScrTotalTax"]
      self.ScrDocMiscAmt:int = obj["ScrDocMiscAmt"]
      self.ScrMiscAmt:int = obj["ScrMiscAmt"]
      self.ScrTotalDedTax:int = obj["ScrTotalDedTax"]
      self.ScrTotalSATax:int = obj["ScrTotalSATax"]
      self.ScrTotalTax:int = obj["ScrTotalTax"]
      self.Selected:bool = obj["Selected"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BitFlag:int = obj["BitFlag"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerDetailAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ContainerID:int = obj["ContainerID"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
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

class Erp_Tablesets_ContainerDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.ContainerShipQty:int = obj["ContainerShipQty"]
      """  The quantity of the PO Release that is shipped on this container.  """  
      self.ShipQtyUOm:str = obj["ShipQtyUOm"]
      """  UOM of Shipment Quantity.  """  
      self.Comment:str = obj["Comment"]
      """  Free form text describing the container detail.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order on this container.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number on this container  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order on this container.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.Volume:int = obj["Volume"]
      """  Amount of space consumed in the container by this detail line, often specified in cubic square feet.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.LCAmt:int = obj["LCAmt"]
      """  The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.Weight:int = obj["Weight"]
      """  Nett Weight  """  
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost based on our unit of measure.  """  
      self.DocOurUnitCost:int = obj["DocOurUnitCost"]
      """  Unit cost based on our unit of measure in document currency.  """  
      self.Rpt1OurUnitCost:int = obj["Rpt1OurUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2OurUnitCost:int = obj["Rpt2OurUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3OurUnitCost:int = obj["Rpt3OurUnitCost"]
      """  Reporting currency value of this field  """  
      self.OrigCountryNum:int = obj["OrigCountryNum"]
      """  Country Number of the Origin Country from the PO?s Supplier Purchase Point.  """  
      self.ContainerLineRef:str = obj["ContainerLineRef"]
      """  Container shipment line reference or name.  """  
      self.ArrivedQty:int = obj["ArrivedQty"]
      """  Arrived Quantity as reported in the receipt line.  """  
      self.ArrivedQtyUOM:str = obj["ArrivedQtyUOM"]
      """  Unit of Measure of the Arrived Qty.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Received Quantity as reported in the receipt line.  """  
      self.ReceivedQtyUOM:str = obj["ReceivedQtyUOM"]
      """  Unit of Measure of the Received Qty  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  The total Duty Amount portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  The total Indirect Cost portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.POTransValue:int = obj["POTransValue"]
      """  This is by default the PO release value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.ExtTransValue:int = obj["ExtTransValue"]
      """  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  The date the container shipment detail is received. Defaults as current system date.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the container shipment detail arrived. Defaults as current system date.  """  
      self.LCSpecLineDutyAmt:int = obj["LCSpecLineDutyAmt"]
      """  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount received for this container shipment line.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.NetWeightUOM is not known.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Indicates if the Receipt line is Taxable  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  """  
      self.InAppliedLCVariance:int = obj["InAppliedLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  """  
      self.InAppliedRcptLCAmt:int = obj["InAppliedRcptLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount received for this container shipment line.  """  
      self.InExtTransValue:int = obj["InExtTransValue"]
      """  Internal usage for inclusive taxes - This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  """  
      self.InLCAmt:int = obj["InLCAmt"]
      """  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCDutyAmt:int = obj["InLCDutyAmt"]
      """  Internal usage for inclusive taxes - The total Duty Amount portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCIndCost:int = obj["InLCIndCost"]
      """  Internal usage for inclusive taxes - The total Indirect Cost portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCSpecLineDutyAmt:int = obj["InLCSpecLineDutyAmt"]
      """  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line.The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCUpliftIndCost:int = obj["InLCUpliftIndCost"]
      """  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InPOTransValue:int = obj["InPOTransValue"]
      """  Internal usage for inclusive taxes -This is by default the PO release value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  """  
      self.BaseWeight:int = obj["BaseWeight"]
      self.BaseWeightUOM:str = obj["BaseWeightUOM"]
      self.ContainerShipped:bool = obj["ContainerShipped"]
      """  Logical used by row rules to determine whether or not the container detail line is read only.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.EnableTransValue:bool = obj["EnableTransValue"]
      """  Flag to indicate if PO Trans Value can be updated.  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent can be updated.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended container detail unit cost  """  
      self.IUM:str = obj["IUM"]
      self.ManualLC:bool = obj["ManualLC"]
      """  Flag to indicate if LCIdCost can be manually updated.  """  
      self.OpenPoRelease:bool = obj["OpenPoRelease"]
      """  Indicates if the PO release tied to this detail entry is open or closed.  """  
      self.PartNum:str = obj["PartNum"]
      self.PlantName:str = obj["PlantName"]
      self.PoLineDesc:str = obj["PoLineDesc"]
      self.PORelRcvdQty:int = obj["PORelRcvdQty"]
      """  Quantity already received on this PO Release  """  
      self.PORelRemQty:int = obj["PORelRemQty"]
      """  Remaining Qty  """  
      self.PUM:str = obj["PUM"]
      self.ShipDate:str = obj["ShipDate"]
      """  Container Detail Shipped Date  """  
      self.SupplierPartNum:str = obj["SupplierPartNum"]
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Liability for the associated purchase order.  """  
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      """  Full description of Tax Region.  """  
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.ThisTranUOM:str = obj["ThisTranUOM"]
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount.  This is the sum of ContainerDetailTax.TaxAmt.  """  
      self.UpdatedKeyRow:bool = obj["UpdatedKeyRow"]
      """  Logical indicates to the UI when a key field has been changed.  Set this to yes if this is the row you want the UI to find and display.  """  
      self.ValidPOInfoEntered:bool = obj["ValidPOInfoEntered"]
      """  Logical indicating that a valid po number, po line and po release has been entered and the user may not update the other container detail values.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.BaseVolume:int = obj["BaseVolume"]
      self.BaseVolumeUOM:str = obj["BaseVolumeUOM"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains our revision. Default from the PartRev.RevisionNum field.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CommodityDescription:str = obj["CommodityDescription"]
      self.ContainerHeaderContainerDescription:str = obj["ContainerHeaderContainerDescription"]
      self.ContainerHeaderShipDate:str = obj["ContainerHeaderShipDate"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.POHeaderInPrice:bool = obj["POHeaderInPrice"]
      self.PORelBTOOrderNum:int = obj["PORelBTOOrderNum"]
      self.PORelBTOOrderLine:int = obj["PORelBTOOrderLine"]
      self.PORelRefCodeDesc:str = obj["PORelRefCodeDesc"]
      self.PORelPurchasingFactor:int = obj["PORelPurchasingFactor"]
      self.PORelXRelQty:int = obj["PORelXRelQty"]
      self.PORelOpenRelease:bool = obj["PORelOpenRelease"]
      self.PORelRelQty:int = obj["PORelRelQty"]
      self.PORelNeedByDate:str = obj["PORelNeedByDate"]
      self.PORelBTOOrderRelNum:int = obj["PORelBTOOrderRelNum"]
      self.PORelPromiseDt:str = obj["PORelPromiseDt"]
      self.PORelPurchasingFactorDirection:str = obj["PORelPurchasingFactorDirection"]
      self.PORelArrivedQty:int = obj["PORelArrivedQty"]
      self.PORelDueDate:str = obj["PORelDueDate"]
      self.PORelPlant:str = obj["PORelPlant"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerDetailTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  ReportableAmt  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time when the record was last changed.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.CollectionType:int = obj["CollectionType"]
      """  CollectionType  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution date.  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date to determine the tax rate.  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.EnableSuperGRate:str = obj["EnableSuperGRate"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.DocScrDedTaxAmt:int = obj["DocScrDedTaxAmt"]
      self.DocScrFixedAmount:int = obj["DocScrFixedAmount"]
      self.DocScrReportableAmt:int = obj["DocScrReportableAmt"]
      self.DocScrTaxableAmt:int = obj["DocScrTaxableAmt"]
      self.DocScrTaxAmt:int = obj["DocScrTaxAmt"]
      self.DocScrTaxAmtVar:int = obj["DocScrTaxAmtVar"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerDetailToSplitRow:
   def __init__(self, obj):
      self.CommCodeDesc:str = obj["CommCodeDesc"]
      self.ContainerID:int = obj["ContainerID"]
      self.ContainerLineRef:str = obj["ContainerLineRef"]
      self.CountryDesc:str = obj["CountryDesc"]
      self.PartNum:str = obj["PartNum"]
      self.POLine:int = obj["POLine"]
      self.PONum:int = obj["PONum"]
      self.PORelNum:int = obj["PORelNum"]
      self.POTransValue:int = obj["POTransValue"]
      self.Selected:bool = obj["Selected"]
      self.UpliftPercent:int = obj["UpliftPercent"]
      self.Volume:int = obj["Volume"]
      self.Weight:int = obj["Weight"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerDetailToSplitTableset:
   def __init__(self, obj):
      self.ContainerDetailToSplit:list[Erp_Tablesets_ContainerDetailToSplitRow] = obj["ContainerDetailToSplit"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ContainerDutyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order on this container.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number on this container  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order on this container.  """  
      self.DutySeq:int = obj["DutySeq"]
      """  Unique Number automatically assigned which is used along with ContainerID, PONum, POLine and PORelNum to uniquely identify the Duty record within the Container Shipment Line.  """  
      self.TariffCode:str = obj["TariffCode"]
      """  Tariff Code must be for a Preference Scheme that is linked to the Country of Origin.  """  
      self.DutyAmt:int = obj["DutyAmt"]
      """   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  """  
      self.CommentText:str = obj["CommentText"]
      """  Container Duty Comments  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InDutyAmt:int = obj["InDutyAmt"]
      """  InDutyAmt  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.ScrDutyAmt:int = obj["ScrDutyAmt"]
      """   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount - Screen Value  """  
      self.BitFlag:int = obj["BitFlag"]
      self.POHeaderTaxRegionCode:str = obj["POHeaderTaxRegionCode"]
      self.POHeaderInPrice:bool = obj["POHeaderInPrice"]
      self.TariffDescription:str = obj["TariffDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerHeaderAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ContainerID:int = obj["ContainerID"]
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

class Erp_Tablesets_ContainerHeaderListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Date the container is to ship.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Logical indicating if the container has shipped.  """  
      self.ContainerClass:str = obj["ContainerClass"]
      """  Class of this container.  Must be a valid entry in the ContainerClass master file.  """  
      self.ContainerCost:int = obj["ContainerCost"]
      """  Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ShippingDays:int = obj["ShippingDays"]
      """   Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.

This is intiially defaulted to the value on the ContainerClass but can be overridden by the end user.  """  
      self.ContainerComments:str = obj["ContainerComments"]
      """  Notes/comments about the container shipment.  """  
      self.ContainerDescription:str = obj["ContainerDescription"]
      """  Free form text that describes this particular container.  """  
      self.NewPoRelAtReceipt:bool = obj["NewPoRelAtReceipt"]
      """  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default.
Having a Volume UOM will provides the ability to calculate total volume  """  
      self.CostPerVolume:int = obj["CostPerVolume"]
      """  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  """  
      self.ContainerReference:str = obj["ContainerReference"]
      """  The container reference is typically the shipping company's assigned container ID.  """  
      self.LCReference:str = obj["LCReference"]
      """  Reference information for landed cost.  """  
      self.LCComment:str = obj["LCComment"]
      """  Landed Cost Comments  """  
      self.LCVariance:int = obj["LCVariance"]
      """  This field holds the variance amount for the landed costs.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost (container cost) was disbursed among the container details.  Valid options are Volume (default), Weight, Value and Manual.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.CurrencyDate:str = obj["CurrencyDate"]
      """  Currency Date  """  
      self.DocContainerCost:int = obj["DocContainerCost"]
      """  Total cost to ship this container in the doc currency.  """  
      self.PORelShipOption:str = obj["PORelShipOption"]
      """  Valid values = "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  This is an optional field.  """  
      self.Rpt1ContainerCost:int = obj["Rpt1ContainerCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ContainerCost:int = obj["Rpt2ContainerCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ContainerCost:int = obj["Rpt3ContainerCost"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.LoadPortID:str = obj["LoadPortID"]
      """  Valid Loading Port ID where goods are loaded on the vessel.  """  
      self.DechargePortID:str = obj["DechargePortID"]
      """  Valid port location where goods are unloaded.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  """  
      self.FOB:str = obj["FOB"]
      """  Descriptive code assigned by user which uniquely identifies the fob record.  """  
      self.ContainerCount:int = obj["ContainerCount"]
      """  Number of Containers in this shipment.  """  
      self.PackageCount:int = obj["PackageCount"]
      """  Number of Packages in this shipment.  """  
      self.Weight:int = obj["Weight"]
      """  Total Weight of the shipment.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.ConNum:int = obj["ConNum"]
      """  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  """  
      self.BOLading:str = obj["BOLading"]
      """  Bill of Lading Number  """  
      self.BOExchange:str = obj["BOExchange"]
      """  Bill of Exchange Number  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  """  
      self.PORelRcptOption:str = obj["PORelRcptOption"]
      """  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.Vessel:str = obj["Vessel"]
      """  Name of the vessel containing the shipment.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  """  
      self.AppliedLCAmt:int = obj["AppliedLCAmt"]
      """  The total Landed Cost Amount disbursed or applied to this container shipment.  """  
      self.ContainerDutyAmt:int = obj["ContainerDutyAmt"]
      """  This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ContainerIndCost:int = obj["ContainerIndCost"]
      """  This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ApplyToLC:bool = obj["ApplyToLC"]
      """  Flag to indicate if all of the shipment duties and indirect costs needs to be applied or disbursed.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the container shipment arrived. Defaults as current system date.  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  The date the container shipment is received. Defaults as current system date.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount received for this container shipment.  """  
      self.UpliftIndCost:int = obj["UpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.DueDate:str = obj["DueDate"]
      """  The date that the Container Shipment is due to arrive.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplayContainerID:str = obj["DisplayContainerID"]
      """  ContainerID in display format.  """  
      self.ResetPORelDates:bool = obj["ResetPORelDates"]
      """  Logical indicating whether or not on ship date change or shipping days change the po release due dates are to be upated.  """  
      self.eshReceived:bool = obj["eshReceived"]
      """  Logical used to indicate if all po rels for the current plant have been received.  """  
      self.TotalExtCost:int = obj["TotalExtCost"]
      """  Total shipment value  """  
      self.TotalWeight:int = obj["TotalWeight"]
      """  Total weight of the items shipped on the container detail.  """  
      self.LCAppliedAmt:int = obj["LCAppliedAmt"]
      """  Amount of Landed Cost applied  """  
      self.LCAccount:str = obj["LCAccount"]
      """  Landed Cost account for display  """  
      self.LCAccountDesc:str = obj["LCAccountDesc"]
      """  Account Description  """  
      self.SkipLandedCost:bool = obj["SkipLandedCost"]
      self.LCMessage:str = obj["LCMessage"]
      """  Landed cost message used to inform the user on retrieval of data that the applied and container costs do not equal.  """  
      self.PartialReceipt:bool = obj["PartialReceipt"]
      """  Logical indicating whether or not the container has been fully receipt.  If yes then the container has only been partially received.  """  
      self.DispShipStatus:str = obj["DispShipStatus"]
      """  Display Ship Status.  """  
      self.DispRcptStatus:str = obj["DispRcptStatus"]
      """  Display Receipt Status  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent should be enabled.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.EnableLCAfterRcpt:bool = obj["EnableLCAfterRcpt"]
      """  Flag to indicate if record can be updated after Receipt.  """  
      self.EnableSplitContainer:bool = obj["EnableSplitContainer"]
      """  Flag to indicate if container details can be split into another container shipment.  """  
      self.EnableTransferCost:bool = obj["EnableTransferCost"]
      """  Flag to indicate if indirect costs can be transferred into another container shipment.  """  
      self.UpdateDtlRecs:bool = obj["UpdateDtlRecs"]
      """  Flag to indicate if container details need to be refreshed after changing the UpliftPercent from header.  """  
      self.ReceiveAll:bool = obj["ReceiveAll"]
      """  Flag to indicate that all container receipt details will be "received" automatically.  """  
      self.TestImportFields:bool = obj["TestImportFields"]
      """  Test Import Fields "ImportNumber" and "ImportedFromDesc" to see if the Receipt Line had already non empty values for these fields and the Lot is set for this Receipt Line.  """  
      self.ContainerClassDescription:str = obj["ContainerClassDescription"]
      """  Descriptive text identifying the Container Class  """  
      self.DechargePortPortID:str = obj["DechargePortPortID"]
      """  A unique PortID within the Company and must always be associated with a Country.  """  
      self.DechargePortDescription:str = obj["DechargePortDescription"]
      """  Country Port Description.  This must be a unique port description within the Company.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.LoadPortPortID:str = obj["LoadPortPortID"]
      """  A unique PortID within the Company and must always be associated with a Country.  """  
      self.LoadPortDescription:str = obj["LoadPortDescription"]
      """  Country Port Description.  This must be a unique port description within the Company.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.VendCntName:str = obj["VendCntName"]
      """  Contact name.  """  
      self.VendCntEmailAddress:str = obj["VendCntEmailAddress"]
      """  Contact email address.  """  
      self.VendCntPhoneNum:str = obj["VendCntPhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  """  
      self.VendCntFaxNum:str = obj["VendCntFaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  """  
      self.VendorAddress2:str = obj["VendorAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorCountry:str = obj["VendorCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorAddress3:str = obj["VendorAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorState:str = obj["VendorState"]
      """  Can be blank.  """  
      self.VendorZIP:str = obj["VendorZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorAddress1:str = obj["VendorAddress1"]
      """  First address line of the Supplier  """  
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorCity:str = obj["VendorCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerHeaderListTableset:
   def __init__(self, obj):
      self.ContainerHeaderList:list[Erp_Tablesets_ContainerHeaderListRow] = obj["ContainerHeaderList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ContainerHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Date the container is to ship.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Logical indicating if the container has shipped.  """  
      self.ContainerClass:str = obj["ContainerClass"]
      """  Class of this container.  Must be a valid entry in the ContainerClass master file.  """  
      self.ContainerCost:int = obj["ContainerCost"]
      """  Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ShippingDays:int = obj["ShippingDays"]
      """   Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.

This is intiially defaulted to the value on the ContainerClass but can be overridden by the end user.  """  
      self.ContainerComments:str = obj["ContainerComments"]
      """  Notes/comments about the container shipment.  """  
      self.ContainerDescription:str = obj["ContainerDescription"]
      """  Free form text that describes this particular container.  """  
      self.NewPoRelAtReceipt:bool = obj["NewPoRelAtReceipt"]
      """  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default.
Having a Volume UOM will provides the ability to calculate total volume  """  
      self.CostPerVolume:int = obj["CostPerVolume"]
      """  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  """  
      self.ContainerReference:str = obj["ContainerReference"]
      """  The container reference is typically the shipping company's assigned container ID.  """  
      self.LCReference:str = obj["LCReference"]
      """  Reference information for landed cost.  """  
      self.LCComment:str = obj["LCComment"]
      """  Landed Cost Comments  """  
      self.LCVariance:int = obj["LCVariance"]
      """  This field holds the variance amount for the landed costs.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost (container cost) was disbursed among the container details.  Valid options are Volume (default), Weight, Value and Manual.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.CurrencyDate:str = obj["CurrencyDate"]
      """  Currency Date  """  
      self.DocContainerCost:int = obj["DocContainerCost"]
      """  Total cost to ship this container in the doc currency.  """  
      self.PORelShipOption:str = obj["PORelShipOption"]
      """  Valid values = "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  This is an optional field.  """  
      self.Rpt1ContainerCost:int = obj["Rpt1ContainerCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ContainerCost:int = obj["Rpt2ContainerCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ContainerCost:int = obj["Rpt3ContainerCost"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.LoadPortID:str = obj["LoadPortID"]
      """  Valid Loading Port ID where goods are loaded on the vessel.  """  
      self.DechargePortID:str = obj["DechargePortID"]
      """  Valid port location where goods are unloaded.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  """  
      self.FOB:str = obj["FOB"]
      """  Descriptive code assigned by user which uniquely identifies the fob record.  """  
      self.ContainerCount:int = obj["ContainerCount"]
      """  Number of Containers in this shipment.  """  
      self.PackageCount:int = obj["PackageCount"]
      """  Number of Packages in this shipment.  """  
      self.Weight:int = obj["Weight"]
      """  Total Weight of the shipment.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.ConNum:int = obj["ConNum"]
      """  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  """  
      self.BOLading:str = obj["BOLading"]
      """  Bill of Lading Number  """  
      self.BOExchange:str = obj["BOExchange"]
      """  Bill of Exchange Number  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  """  
      self.PORelRcptOption:str = obj["PORelRcptOption"]
      """  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.Vessel:str = obj["Vessel"]
      """  Name of the vessel containing the shipment.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  """  
      self.AppliedLCAmt:int = obj["AppliedLCAmt"]
      """  The total Landed Cost Amount disbursed or applied to this container shipment.  """  
      self.ContainerDutyAmt:int = obj["ContainerDutyAmt"]
      """  This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ContainerIndCost:int = obj["ContainerIndCost"]
      """  This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ApplyToLC:bool = obj["ApplyToLC"]
      """  Flag to indicate if all of the shipment duties and indirect costs needs to be applied or disbursed.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the container shipment arrived. Defaults as current system date.  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  The date the container shipment is received. Defaults as current system date.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount received for this container shipment.  """  
      self.UpliftIndCost:int = obj["UpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.DueDate:str = obj["DueDate"]
      """  The date that the Container Shipment is due to arrive.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AdditionalShippingDays:int = obj["AdditionalShippingDays"]
      """  **NOT USED - REMOVE**  """  
      self.EstimatedArrivalDate:str = obj["EstimatedArrivalDate"]
      """  **NOT USED - Remove **  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Set from the earliest need by date set against the po releases.  """  
      self.PromiseDate:str = obj["PromiseDate"]
      """  Specifies the date on which the supplier has promised to deliver the container.  """  
      self.TaxesCalculated:bool = obj["TaxesCalculated"]
      """  Reflects whether taxes have been calculated  """  
      self.InAppliedLCAmt:int = obj["InAppliedLCAmt"]
      """  Internal usage for inclusive taxes -The total Landed Cost Amount disbursed or applied to this container shipment.  """  
      self.InAppliedLCVariance:int = obj["InAppliedLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  """  
      self.InAppliedRcptLCAmt:int = obj["InAppliedRcptLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount received for this container shipment.  """  
      self.InContainerCost:int = obj["InContainerCost"]
      """  Internal usage for inclusive taxes - Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.InContainerDutyAmt:int = obj["InContainerDutyAmt"]
      """  Internal usage for inclusive taxes - This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.InContainerIndCost:int = obj["InContainerIndCost"]
      """  Internal usage for inclusive taxes - This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.InDocContainerCost:int = obj["InDocContainerCost"]
      """  Internal usage for inclusive taxes - Total cost to ship this container in the doc currency.  """  
      self.InLCAppliedAmt:int = obj["InLCAppliedAmt"]
      """  ** NOT USED TO BE DROPPED 10.2 **  """  
      self.InLCVariance:int = obj["InLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the variance amount for the landed costs.  """  
      self.InSpecDutyAmt:int = obj["InSpecDutyAmt"]
      """  Internal usage for inclusive taxes - This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  """  
      self.InUpliftIndCost:int = obj["InUpliftIndCost"]
      """  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.DisplayContainerID:str = obj["DisplayContainerID"]
      """  ContainerID in display format.  """  
      self.DispRcptStatus:str = obj["DispRcptStatus"]
      """  Display Receipt Status  """  
      self.DispShipStatus:str = obj["DispShipStatus"]
      """  Display Ship Status.  """  
      self.EnableCalcTaxes:bool = obj["EnableCalcTaxes"]
      """   Flag poplulated from XbSyst.ReceiptTaxCalculate 
Determines if taxes can be calculated at update or via action menu  """  
      self.EnableLCAfterRcpt:bool = obj["EnableLCAfterRcpt"]
      """  Flag to indicate if record can be updated after Receipt.  """  
      self.EnableSplitContainer:bool = obj["EnableSplitContainer"]
      """  Flag to indicate if container details can be split into another container shipment.  """  
      self.EnableTransferCost:bool = obj["EnableTransferCost"]
      """  Flag to indicate if indirect costs can be transferred into another container shipment.  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent should be enabled.  """  
      self.eshReceived:bool = obj["eshReceived"]
      """  Logical used to indicate if all po rels for the current plant have been received.  """  
      self.LCAccount:str = obj["LCAccount"]
      """  Landed Cost account for display  """  
      self.LCAccountDesc:str = obj["LCAccountDesc"]
      """  Account Description  """  
      self.LCAppliedAmt:int = obj["LCAppliedAmt"]
      """  Amount of Landed Cost applied  """  
      self.LCMessage:str = obj["LCMessage"]
      """  Landed cost message used to inform the user on retrieval of data that the applied and container costs do not equal.  """  
      self.PartialReceipt:bool = obj["PartialReceipt"]
      """  Logical indicating whether or not the container has been fully receipt.  If yes then the container has only been partially received.  """  
      self.ReceiveAll:bool = obj["ReceiveAll"]
      """  Flag to indicate that all container receipt details will be "received" automatically.  """  
      self.ResetPORelDates:bool = obj["ResetPORelDates"]
      """  Logical indicating whether or not on ship date change or shipping days change the po release due dates are to be upated.  """  
      self.SkipLandedCost:bool = obj["SkipLandedCost"]
      self.TestImportFields:bool = obj["TestImportFields"]
      """  Test Import Fields "ImportNumber" and "ImportedFromDesc" to see if the Receipt Line had already non empty values for these fields and the Lot is set for this Receipt Line.  """  
      self.TotalAmt:int = obj["TotalAmt"]
      """  Total amount.  This is the sum of all the other total fields.  """  
      self.TotalExtCost:int = obj["TotalExtCost"]
      """  Total shipment value  """  
      self.TotalWeight:int = obj["TotalWeight"]
      """  Total weight of the items shipped on the container detail.  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total Deductable Tax Amount  """  
      self.TotDutiesAmt:int = obj["TotDutiesAmt"]
      """  Total duties amount.  """  
      self.TotIndirectCostsAmt:int = obj["TotIndirectCostsAmt"]
      """  Total Indirect Costs amount.  """  
      self.TotLinesAmt:int = obj["TotLinesAmt"]
      """  Total amount for all Container Lines  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax Amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total Tax amount.  """  
      self.TotWHTaxAmt:int = obj["TotWHTaxAmt"]
      """  Total WithHolding Tax Amount  """  
      self.UpdateDtlRecs:bool = obj["UpdateDtlRecs"]
      """  Flag to indicate if container details need to be refreshed after changing the UpliftPercent from header.  """  
      self.UpdIndCosts:bool = obj["UpdIndCosts"]
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.EnableTaxAtLineLevel:bool = obj["EnableTaxAtLineLevel"]
      """   Flag poplulated from XbSyst.APTaxLnLevel.  
Determines if taxes are calculated at line level (true) or document level (false)  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.DisableApplyLandedCost:bool = obj["DisableApplyLandedCost"]
      """  Determine if the Apply Landed Cost button in Kinetic should be disabled.  """  
      self.OkToLeaveContainerHead:bool = obj["OkToLeaveContainerHead"]
      """  Flag to determine for Kinetic if use can leave the Container Header record/screen.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ContainerClassDescription:str = obj["ContainerClassDescription"]
      self.DechargePortDescription:str = obj["DechargePortDescription"]
      self.DechargePortPortID:str = obj["DechargePortPortID"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.LoadPortPortID:str = obj["LoadPortPortID"]
      self.LoadPortDescription:str = obj["LoadPortDescription"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.VendCntPhoneNum:str = obj["VendCntPhoneNum"]
      self.VendCntName:str = obj["VendCntName"]
      self.VendCntFaxNum:str = obj["VendCntFaxNum"]
      self.VendCntEmailAddress:str = obj["VendCntEmailAddress"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorState:str = obj["VendorState"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorName:str = obj["VendorName"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerHeaderTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time when the record was last changed.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution Date  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date to determine the tax rate.  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  TextCode  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SummaryOnly:bool = obj["SummaryOnly"]
      """  flag to indicate if this record is used only to total detail records,  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.EnableSuperGRate:bool = obj["EnableSuperGRate"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      """  Display field for Rpt1ScrFixedAmount  """  
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      """  Display field for Rpt2FixedAmount  """  
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      """  Display field for Rpt3rFixedAmount  """  
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrDocDedTaxAmt:int = obj["ScrDocDedTaxAmt"]
      self.ScrDocFixedAmount:int = obj["ScrDocFixedAmount"]
      """  Doc Fixed Amount  """  
      self.ScrDocReportableAmt:int = obj["ScrDocReportableAmt"]
      self.ScrDocTaxableAmt:int = obj["ScrDocTaxableAmt"]
      self.ScrDocTaxAmt:int = obj["ScrDocTaxAmt"]
      self.ScrDocTaxAmtVar:int = obj["ScrDocTaxAmtVar"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  FixedAmount  """  
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.MiscSeq:int = obj["MiscSeq"]
      """  Unique Number automatically assigned within the ContainerID to uniquely identify each Indirect Costs for this container shipment.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Miscellaneous Charge ID that is flagged for Landed Cost  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvMsc record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line from corresponding APInvMsc record.  """  
      self.MscNum:int = obj["MscNum"]
      """  The unique sequence number identifying the AP invoice miscellaneous charge.  """  
      self.ExcludeFromLC:bool = obj["ExcludeFromLC"]
      """  Flag to indicate if the Indirect Cost is to be excluded from the Landed Cost calculation.  Disabled when IncTransValue is checked.  """  
      self.IncTransValue:bool = obj["IncTransValue"]
      """  Flag to indicate if the Indirect Cost is to be included in the Transaction Value (statistical value) which is used to calculate duties.  Disabled when the ExcludeFromLC is checked.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.EstimateAmt:int = obj["EstimateAmt"]
      """  Estimated Amount used in landed cost calculation if actual amount is not available.  """  
      self.DocEstimateAmt:int = obj["DocEstimateAmt"]
      """  Estimated Amount in currency specified.  """  
      self.ActualAmt:int = obj["ActualAmt"]
      """  Actual Amount coming from the posted AP invoice miscellaneous charge.  """  
      self.DocActualAmt:int = obj["DocActualAmt"]
      """  Actual Amount in currency specified.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.CommentText:str = obj["CommentText"]
      """  Container Indirect Cost Comments  """  
      self.Rpt1EstimateAmt:int = obj["Rpt1EstimateAmt"]
      """  Reporting currency value of the Estimated Amount.  """  
      self.Rpt2EstimateAmt:int = obj["Rpt2EstimateAmt"]
      """  Reporting currency value of the Estimated Amount.  """  
      self.Rpt3EstimateAmt:int = obj["Rpt3EstimateAmt"]
      """  Reporting currency value of the Estimated Amount.  """  
      self.Rpt1ActualAmt:int = obj["Rpt1ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt2ActualAmt:int = obj["Rpt2ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt3ActualAmt:int = obj["Rpt3ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date that will be used to get the exchange rate if the indirect cost is not associated with an invoice miscellaneous charge.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocHstEstimateAmt:int = obj["DocHstEstimateAmt"]
      """  Historical Doc Estimate Amount  """  
      self.HstEstimateAmt:int = obj["HstEstimateAmt"]
      """  Historical Estimate Amount  """  
      self.Rpt1HstEstimateAmt:int = obj["Rpt1HstEstimateAmt"]
      """  Historical Rpt1 Estimate Amount  """  
      self.Rpt2HstEstimateAmt:int = obj["Rpt2HstEstimateAmt"]
      """  Historical Rpt2 Estimate Amount  """  
      self.Rpt3HstEstimateAmt:int = obj["Rpt3HstEstimateAmt"]
      """  Historical Rpt3 Estimate Amount  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Indirect Cost. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Indicates if the Indirect Cost is Taxable  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Liability for this Receipt  """  
      self.InEstimateAmt:int = obj["InEstimateAmt"]
      """  Internal usage for inclusive taxes - Estimated Amount used in landed cost calculation if actual amount is not available.  """  
      self.DocInEstimateAmt:int = obj["DocInEstimateAmt"]
      """  Internal usage for inclusive taxes - Estimated Amount in currency specified.  """  
      self.Rpt1InEstimateAmt:int = obj["Rpt1InEstimateAmt"]
      """  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  """  
      self.Rpt2InEstimateAmt:int = obj["Rpt2InEstimateAmt"]
      """  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  """  
      self.Rpt3InEstimateAmt:int = obj["Rpt3InEstimateAmt"]
      """  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  """  
      self.InHstEstimateAmt:int = obj["InHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Estimate Amount  """  
      self.DocInHstEstimateAmt:int = obj["DocInHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Doc Estimate Amount  """  
      self.Rpt1InHstEstimateAmt:int = obj["Rpt1InHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Rpt1 Estimate Amount  """  
      self.Rpt2InHstEstimateAmt:int = obj["Rpt2InHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Rpt2 Estimate Amount  """  
      self.Rpt3InHstEstimateAmt:int = obj["Rpt3InHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Rpt3 Estimate Amount  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for currency "BASE"  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount.  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this indirect cost.  """  
      self.RateLabel:str = obj["RateLabel"]
      """  Label for ExchangeRate  """  
      self.ScrEstimateAmt:int = obj["ScrEstimateAmt"]
      """  Estimated Amount used in landed cost calculation if actual amount is not available - Screen Value  """  
      self.Rpt1ScrEstimateAmt:int = obj["Rpt1ScrEstimateAmt"]
      """  Reporting currency value of the Estimated Amount - Screen Value  """  
      self.Rpt2ScrEstimateAmt:int = obj["Rpt2ScrEstimateAmt"]
      """  Reporting currency value of the Estimated Amount - Screen value  """  
      self.Rpt3ScrEstimateAmt:int = obj["Rpt3ScrEstimateAmt"]
      """  Reporting currency value of the Estimated Amount - Screen value  """  
      self.ScrHstEstimateAmt:int = obj["ScrHstEstimateAmt"]
      """  Historical Estimate Amount - Screen value  """  
      self.Rpt1ScrHstEstimateAmt:int = obj["Rpt1ScrHstEstimateAmt"]
      """  Historical Rpt1 Estimate Amount - Screen value  """  
      self.Rpt2ScrHstEstimateAmt:int = obj["Rpt2ScrHstEstimateAmt"]
      """  Historical Rpt2 Estimate Amount - Screen value  """  
      self.Rpt3ScrHstEstimateAmt:int = obj["Rpt3ScrHstEstimateAmt"]
      """  Historical Rpt3 Estimate Amount - Screen value  """  
      self.DocScrEstimateAmt:int = obj["DocScrEstimateAmt"]
      """  Estimated Amount in currency specified - Screen value  """  
      self.DocScrHstEstimateAmt:int = obj["DocScrHstEstimateAmt"]
      """  Estimated Amount used in landed cost calculation if actual amount is not available - Screen Value  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.PurMiscLCAmount:int = obj["PurMiscLCAmount"]
      self.PurMiscLCCurrencyCode:str = obj["PurMiscLCCurrencyCode"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.PurMiscLCDisburseMethod:str = obj["PurMiscLCDisburseMethod"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorName:str = obj["VendorName"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerMiscTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.MiscSeq:int = obj["MiscSeq"]
      """  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  ** NOT USED TO BE DROPPED 10.2 ** The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  ReportableAmt  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time when the record was last changed.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.CollectionType:int = obj["CollectionType"]
      """  CollectionType  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution date.  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date to determine the tax rate.  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DocScrDedTaxAmt:int = obj["DocScrDedTaxAmt"]
      self.DocScrReportableAmt:int = obj["DocScrReportableAmt"]
      self.DocScrTaxableAmt:int = obj["DocScrTaxableAmt"]
      self.DocScrTaxAmt:int = obj["DocScrTaxAmt"]
      self.DocScrTaxAmtVar:int = obj["DocScrTaxAmtVar"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.DocScrFixedAmount:int = obj["DocScrFixedAmount"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ContainerMiscApplyDate:str = obj["ContainerMiscApplyDate"]
      self.ContainerMiscInPrice:bool = obj["ContainerMiscInPrice"]
      self.ContainerMiscCurrencyCode:str = obj["ContainerMiscCurrencyCode"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerMiscToTransferRow:
   def __init__(self, obj):
      self.ContainerID:int = obj["ContainerID"]
      self.DocActualAmt:int = obj["DocActualAmt"]
      self.DocEstimateAmt:int = obj["DocEstimateAmt"]
      self.EstimateAmt:int = obj["EstimateAmt"]
      self.InvoiceLine:int = obj["InvoiceLine"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      self.MiscSeq:int = obj["MiscSeq"]
      self.MscNum:int = obj["MscNum"]
      self.Selected:bool = obj["Selected"]
      self.MiscCodeDesc:str = obj["MiscCodeDesc"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.Type:str = obj["Type"]
      self.Percentage:int = obj["Percentage"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerMiscToTransferTableset:
   def __init__(self, obj):
      self.ContainerMiscToTransfer:list[Erp_Tablesets_ContainerMiscToTransferRow] = obj["ContainerMiscToTransfer"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ContainerTrackingTableset:
   def __init__(self, obj):
      self.ContainerHeader:list[Erp_Tablesets_ContainerHeaderRow] = obj["ContainerHeader"]
      self.ContainerHeaderAttch:list[Erp_Tablesets_ContainerHeaderAttchRow] = obj["ContainerHeaderAttch"]
      self.ContainerDetail:list[Erp_Tablesets_ContainerDetailRow] = obj["ContainerDetail"]
      self.ContainerDetailAttch:list[Erp_Tablesets_ContainerDetailAttchRow] = obj["ContainerDetailAttch"]
      self.ContainerDetailTax:list[Erp_Tablesets_ContainerDetailTaxRow] = obj["ContainerDetailTax"]
      self.ContainerDuty:list[Erp_Tablesets_ContainerDutyRow] = obj["ContainerDuty"]
      self.ContainerHeaderTax:list[Erp_Tablesets_ContainerHeaderTaxRow] = obj["ContainerHeaderTax"]
      self.ContainerMisc:list[Erp_Tablesets_ContainerMiscRow] = obj["ContainerMisc"]
      self.ContainerMiscTax:list[Erp_Tablesets_ContainerMiscTaxRow] = obj["ContainerMiscTax"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtContainerTrackingTableset:
   def __init__(self, obj):
      self.ContainerHeader:list[Erp_Tablesets_ContainerHeaderRow] = obj["ContainerHeader"]
      self.ContainerHeaderAttch:list[Erp_Tablesets_ContainerHeaderAttchRow] = obj["ContainerHeaderAttch"]
      self.ContainerDetail:list[Erp_Tablesets_ContainerDetailRow] = obj["ContainerDetail"]
      self.ContainerDetailAttch:list[Erp_Tablesets_ContainerDetailAttchRow] = obj["ContainerDetailAttch"]
      self.ContainerDetailTax:list[Erp_Tablesets_ContainerDetailTaxRow] = obj["ContainerDetailTax"]
      self.ContainerDuty:list[Erp_Tablesets_ContainerDutyRow] = obj["ContainerDuty"]
      self.ContainerHeaderTax:list[Erp_Tablesets_ContainerHeaderTaxRow] = obj["ContainerHeaderTax"]
      self.ContainerMisc:list[Erp_Tablesets_ContainerMiscRow] = obj["ContainerMisc"]
      self.ContainerMiscTax:list[Erp_Tablesets_ContainerMiscTaxRow] = obj["ContainerMiscTax"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAPInvMiscCharges_input:
   """ Required : 
   ipContainerID
   """  
   def __init__(self, obj):
      self.ipContainerID:int = obj["ipContainerID"]
      """  Container ID  """  
      pass

class GetAPInvMiscCharges_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APInvMiscChargesTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   containerID
   """  
   def __init__(self, obj):
      self.containerID:int = obj["containerID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContainerTrackingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ContainerTrackingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ContainerTrackingTableset] = obj["returnObj"]
      pass

class GetContainerClassInfo_input:
   """ Required : 
   cclass
   """  
   def __init__(self, obj):
      self.cclass:str = obj["cclass"]
      """  cclass  """  
      pass

class GetContainerClassInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.volume:int = obj["parameters"]
      self.containerCost:int = obj["parameters"]
      self.CostPerVolume:int = obj["parameters"]
      self.shippingDays:int = obj["parameters"]
      self.validContainer:bool = obj["validContainer"]
      pass

      """  output parameters  """  

class GetContainerDetailToSplit_input:
   """ Required : 
   ipContainerID
   """  
   def __init__(self, obj):
      self.ipContainerID:int = obj["ipContainerID"]
      """  Container ID  """  
      pass

class GetContainerDetailToSplit_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContainerDetailToSplitTableset] = obj["returnObj"]
      pass

class GetContainerMiscToTransfer_input:
   """ Required : 
   ipContainerID
   """  
   def __init__(self, obj):
      self.ipContainerID:int = obj["ipContainerID"]
      """  Container ID  """  
      pass

class GetContainerMiscToTransfer_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContainerMiscToTransferTableset] = obj["returnObj"]
      pass

class GetDtlPOInfo_input:
   """ Required : 
   ds
   poLine
   poNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      self.poLine:int = obj["poLine"]
      """  Receipt Line to check  """  
      self.poNum:int = obj["poNum"]
      """  New PO Number  """  
      pass

class GetDtlPOInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDtlPOLineInfo_input:
   """ Required : 
   poNum
   poLine
   ds
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      """  New POLine Number  """  
      self.poLine:int = obj["poLine"]
      """  Receipt Line to check  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class GetDtlPOLineInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDtlQtyInfo_input:
   """ Required : 
   ds
   poNum
   poLine
   poRelNum
   inputShipQty
   inputIUM
   whichField
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      """  Container PO Number  """  
      self.poLine:int = obj["poLine"]
      """  Container PO Line  """  
      self.poRelNum:int = obj["poRelNum"]
      """  Container PO Rel  """  
      self.inputShipQty:int = obj["inputShipQty"]
      """  Proposed change to the Ship qty field  """  
      self.inputIUM:str = obj["inputIUM"]
      """  Proposed change to the IUM field  """  
      self.whichField:str = obj["whichField"]
      """  Indicates either 'QTY' or 'UOM' field changed  """  
      pass

class GetDtlQtyInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      self.warnMsg:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_ContainerHeaderListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewContainerDetailAttch_input:
   """ Required : 
   ds
   containerID
   poNum
   poLine
   poRelNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      self.containerID:int = obj["containerID"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      self.poRelNum:int = obj["poRelNum"]
      pass

class GetNewContainerDetailAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContainerDetailTax_input:
   """ Required : 
   ds
   containerID
   poNum
   poLine
   poRelNum
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      self.containerID:int = obj["containerID"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      self.poRelNum:int = obj["poRelNum"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewContainerDetailTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContainerDetail_input:
   """ Required : 
   ds
   containerID
   poNum
   poLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      self.containerID:int = obj["containerID"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      pass

class GetNewContainerDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContainerDuty_input:
   """ Required : 
   ds
   containerID
   poNum
   poLine
   poRelNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      self.containerID:int = obj["containerID"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      self.poRelNum:int = obj["poRelNum"]
      pass

class GetNewContainerDuty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContainerHeaderAttch_input:
   """ Required : 
   ds
   containerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      self.containerID:int = obj["containerID"]
      pass

class GetNewContainerHeaderAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContainerHeaderTax_input:
   """ Required : 
   ds
   containerID
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      self.containerID:int = obj["containerID"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewContainerHeaderTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContainerHeader_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class GetNewContainerHeader_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContainerMiscTax_input:
   """ Required : 
   ds
   containerID
   miscSeq
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      self.containerID:int = obj["containerID"]
      self.miscSeq:int = obj["miscSeq"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewContainerMiscTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContainerMisc_input:
   """ Required : 
   ds
   containerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      self.containerID:int = obj["containerID"]
      pass

class GetNewContainerMisc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPOReleaseInfo_input:
   """ Required : 
   porelnum
   ds
   """  
   def __init__(self, obj):
      self.porelnum:int = obj["porelnum"]
      """  pore num  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class GetPOReleaseInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseContainerHeader
   whereClauseContainerHeaderAttch
   whereClauseContainerDetail
   whereClauseContainerDetailAttch
   whereClauseContainerDetailTax
   whereClauseContainerDuty
   whereClauseContainerHeaderTax
   whereClauseContainerMisc
   whereClauseContainerMiscTax
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseContainerHeader:str = obj["whereClauseContainerHeader"]
      self.whereClauseContainerHeaderAttch:str = obj["whereClauseContainerHeaderAttch"]
      self.whereClauseContainerDetail:str = obj["whereClauseContainerDetail"]
      self.whereClauseContainerDetailAttch:str = obj["whereClauseContainerDetailAttch"]
      self.whereClauseContainerDetailTax:str = obj["whereClauseContainerDetailTax"]
      self.whereClauseContainerDuty:str = obj["whereClauseContainerDuty"]
      self.whereClauseContainerHeaderTax:str = obj["whereClauseContainerHeaderTax"]
      self.whereClauseContainerMisc:str = obj["whereClauseContainerMisc"]
      self.whereClauseContainerMiscTax:str = obj["whereClauseContainerMiscTax"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContainerTrackingTableset] = obj["returnObj"]
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

class OnChangeClassCode_input:
   """ Required : 
   ipClassCode
   ds
   """  
   def __init__(self, obj):
      self.ipClassCode:str = obj["ipClassCode"]
      """  Proposed Container Class Code to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeClassCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeConNum_input:
   """ Required : 
   ipConNum
   ds
   """  
   def __init__(self, obj):
      self.ipConNum:int = obj["ipConNum"]
      """  Proposed ConNum to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeConNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeContainerClass_input:
   """ Required : 
   ipClassCode
   ds
   """  
   def __init__(self, obj):
      self.ipClassCode:str = obj["ipClassCode"]
      """  Proposed Container Class Code to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeContainerClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeContainerDetailLCIndCost_input:
   """ Required : 
   ipLCIndCost
   ds
   """  
   def __init__(self, obj):
      self.ipLCIndCost:int = obj["ipLCIndCost"]
      """  Proposed LCIndCost  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeContainerDetailLCIndCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDetailTaxFixedAmount_input:
   """ Required : 
   proposedFixedAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedFixedAmt:int = obj["proposedFixedAmt"]
      """  The proposed reportable amount  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDetailTaxFixedAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDetailTaxRateCode_input:
   """ Required : 
   proposedRateCode
   ds
   """  
   def __init__(self, obj):
      self.proposedRateCode:str = obj["proposedRateCode"]
      """  The proposed rate code  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDetailTaxRateCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDetailTaxReportableAmt_input:
   """ Required : 
   proposedReportableAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedReportableAmt:int = obj["proposedReportableAmt"]
      """  The proposed reportable amount  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDetailTaxReportableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDetailTaxTaxAmt_input:
   """ Required : 
   proposedTaxAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxAmt:int = obj["proposedTaxAmt"]
      """  The proposed tax amount  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDetailTaxTaxAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDetailTaxTaxCode_input:
   """ Required : 
   proposedTaxCode
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxCode:str = obj["proposedTaxCode"]
      """  The proposed tax code  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDetailTaxTaxCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDetailTaxTaxDeductable_input:
   """ Required : 
   proposedTaxDeductable
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxDeductable:int = obj["proposedTaxDeductable"]
      """  The proposed tax deductable  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDetailTaxTaxDeductable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDetailTaxTaxPercent_input:
   """ Required : 
   proposedTaxPercent
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxPercent:int = obj["proposedTaxPercent"]
      """  The proposed tax percent  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDetailTaxTaxPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDetailTaxTaxableAmt_input:
   """ Required : 
   proposedTaxableAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxableAmt:int = obj["proposedTaxableAmt"]
      """  The proposed taxable amount  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDetailTaxTaxableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlCommodity_input:
   """ Required : 
   ipCommCode
   ds
   """  
   def __init__(self, obj):
      self.ipCommCode:str = obj["ipCommCode"]
      """  Proposed Commodity Code to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDtlCommodity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlCountryNum_input:
   """ Required : 
   ipCountryNum
   ds
   """  
   def __init__(self, obj):
      self.ipCountryNum:int = obj["ipCountryNum"]
      """  Proposed Country of Origin to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDtlCountryNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlLCIndCost_input:
   """ Required : 
   ipLCIndCost
   LCIndCostSum
   ds
   """  
   def __init__(self, obj):
      self.ipLCIndCost:int = obj["ipLCIndCost"]
      """  Proposed LC Indirect Cose to be validated  """  
      self.LCIndCostSum:int = obj["LCIndCostSum"]
      """  Total amount of Indirect cost on all the lines  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDtlLCIndCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlTaxCatID_input:
   """ Required : 
   taxCatID
   ds
   """  
   def __init__(self, obj):
      self.taxCatID:str = obj["taxCatID"]
      """  Tax Category  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDtlTaxCatID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlTaxExempt_input:
   """ Required : 
   taxExempt
   ds
   """  
   def __init__(self, obj):
      self.taxExempt:str = obj["taxExempt"]
      """  Tax Exempt  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDtlTaxExempt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlUpliftPercent_input:
   """ Required : 
   ipUpliftPercent
   ds
   """  
   def __init__(self, obj):
      self.ipUpliftPercent:int = obj["ipUpliftPercent"]
      """  Proposed Uplift Percentage to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDtlUpliftPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDueDate_input:
   """ Required : 
   ipDueDate
   ds
   """  
   def __init__(self, obj):
      self.ipDueDate:str = obj["ipDueDate"]
      """  Proposed Container Due Date to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDueDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opErrorMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDutyTariffCode_input:
   """ Required : 
   ipTariffCode
   ds
   """  
   def __init__(self, obj):
      self.ipTariffCode:str = obj["ipTariffCode"]
      """  Proposed Tariff Code to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeDutyTariffCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLoadPort_input:
   """ Required : 
   ipLoadPortID
   ds
   """  
   def __init__(self, obj):
      self.ipLoadPortID:str = obj["ipLoadPortID"]
      """  Loading Port ID  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeLoadPort_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscApplyDate_input:
   """ Required : 
   ipApplyDate
   ds
   """  
   def __init__(self, obj):
      self.ipApplyDate:str = obj["ipApplyDate"]
      """  Proposed Apply Date to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscApplyDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscCharge_input:
   """ Required : 
   ipChargeID
   ds
   """  
   def __init__(self, obj):
      self.ipChargeID:str = obj["ipChargeID"]
      """  Proposed PurMisc ID to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscCharge_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscCurrencyCode_input:
   """ Required : 
   ipCurrCode
   ds
   """  
   def __init__(self, obj):
      self.ipCurrCode:str = obj["ipCurrCode"]
      """  Proposed Currency Code to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscDocEstimateAmt_input:
   """ Required : 
   ipDocEstimateAmt
   ds
   """  
   def __init__(self, obj):
      self.ipDocEstimateAmt:int = obj["ipDocEstimateAmt"]
      """  Proposed Estimate Amount in document currency  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscDocEstimateAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscExchangeRate_input:
   """ Required : 
   ipExchangeRate
   ds
   """  
   def __init__(self, obj):
      self.ipExchangeRate:int = obj["ipExchangeRate"]
      """  Proposed Currency Exchange Rate to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscExchangeRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscInvoiceLine_input:
   """ Required : 
   ipInvLine
   ds
   """  
   def __init__(self, obj):
      self.ipInvLine:int = obj["ipInvLine"]
      """  The AP Invoice Line to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscInvoiceLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscInvoiceNum_input:
   """ Required : 
   ipInvNum
   ipVendorNum
   ds
   """  
   def __init__(self, obj):
      self.ipInvNum:str = obj["ipInvNum"]
      """  The AP Invoice Number to be validated  """  
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  The Vendor Number associated with the invoice  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscInvoiceNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscMscNum_input:
   """ Required : 
   ipMscNum
   ds
   """  
   def __init__(self, obj):
      self.ipMscNum:int = obj["ipMscNum"]
      """  The AP Invoice Line Miscellaneous Sequence Number to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscMscNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscPercentage_input:
   """ Required : 
   percentage
   ds
   """  
   def __init__(self, obj):
      self.percentage:int = obj["percentage"]
      """  Percentage Amount  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscPercentage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscRateGrp_input:
   """ Required : 
   ipRateGrpCode
   ds
   """  
   def __init__(self, obj):
      self.ipRateGrpCode:str = obj["ipRateGrpCode"]
      """  Proposed Currency Rate Group Code to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscRateGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscTaxCatID_input:
   """ Required : 
   taxCatID
   ds
   """  
   def __init__(self, obj):
      self.taxCatID:str = obj["taxCatID"]
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscTaxCatID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscTaxFixedAmount_input:
   """ Required : 
   proposedFixedAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedFixedAmt:int = obj["proposedFixedAmt"]
      """  The proposed reportable amount  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscTaxFixedAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscTaxRateCode_input:
   """ Required : 
   proposedRateCode
   ds
   """  
   def __init__(self, obj):
      self.proposedRateCode:str = obj["proposedRateCode"]
      """  The proposed rate code  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscTaxRateCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscTaxRegionCode_input:
   """ Required : 
   taxRegionCode
   ds
   """  
   def __init__(self, obj):
      self.taxRegionCode:str = obj["taxRegionCode"]
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscTaxRegionCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscTaxReportableAmt_input:
   """ Required : 
   proposedReportableAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedReportableAmt:int = obj["proposedReportableAmt"]
      """  The proposed reportable amount  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscTaxReportableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscTaxTaxAmt_input:
   """ Required : 
   proposedTaxAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxAmt:int = obj["proposedTaxAmt"]
      """  The proposed tax amount  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscTaxTaxAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscTaxTaxCode_input:
   """ Required : 
   proposedTaxCode
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxCode:str = obj["proposedTaxCode"]
      """  The proposed tax code  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscTaxTaxCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscTaxTaxDeductable_input:
   """ Required : 
   proposedTaxDeductable
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxDeductable:int = obj["proposedTaxDeductable"]
      """  The proposed tax deductable  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscTaxTaxDeductable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscTaxTaxPercent_input:
   """ Required : 
   proposedTaxPercent
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxPercent:int = obj["proposedTaxPercent"]
      """  The proposed tax percent  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscTaxTaxPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscTaxTaxableAmt_input:
   """ Required : 
   proposedTaxableAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxableAmt:int = obj["proposedTaxableAmt"]
      """  The proposed taxable amount  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscTaxTaxableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscVendor_input:
   """ Required : 
   VendID
   ds
   """  
   def __init__(self, obj):
      self.VendID:str = obj["VendID"]
      """  Proposed vendor ID to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeMiscVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeShipDate_input:
   """ Required : 
   ipShipDate
   ds
   """  
   def __init__(self, obj):
      self.ipShipDate:str = obj["ipShipDate"]
      """  Proposed Container Class Code to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeShipDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeShipStatus_input:
   """ Required : 
   ipShipStat
   ds
   """  
   def __init__(self, obj):
      self.ipShipStat:str = obj["ipShipStat"]
      """  Proposed Shipment Status to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeShipStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opShipLogic:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeShippingDays_input:
   """ Required : 
   ipShippingDays
   ds
   """  
   def __init__(self, obj):
      self.ipShippingDays:int = obj["ipShippingDays"]
      """  Proposed Container Class Code to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeShippingDays_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVendor_input:
   """ Required : 
   VendID
   ds
   """  
   def __init__(self, obj):
      self.VendID:str = obj["VendID"]
      """  Proposed vendor ID to be validated  """  
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangeVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedDetailTaxManual_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangedDetailTaxManual_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedMiscTaxManual_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangedMiscTaxManual_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedPOTransValue_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class OnChangedPOTransValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnUpdateMiscCharge_input:
   """ Required : 
   ipChargeID
   """  
   def __init__(self, obj):
      self.ipChargeID:str = obj["ipChargeID"]
      """  Proposed PurMisc ID to be validated  """  
      pass

class OnUpdateMiscCharge_output:
   def __init__(self, obj):
      pass

class PreUpdateContainer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class PreUpdateContainer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWarnMsg:str = obj["parameters"]
      self.opShipmentClassMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ReceiveContainerLCAmt_input:
   """ Required : 
   inContainerID
   """  
   def __init__(self, obj):
      self.inContainerID:int = obj["inContainerID"]
      pass

class ReceiveContainerLCAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class RefreshLCApplied_input:
   """ Required : 
   ipContainerID
   """  
   def __init__(self, obj):
      self.ipContainerID:int = obj["ipContainerID"]
      pass

class RefreshLCApplied_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opLCApplied:int = obj["parameters"]
      pass

      """  output parameters  """  

class ResetLandedCostDisbursements_input:
   """ Required : 
   ipContainerID
   ipDisburseMethod
   """  
   def __init__(self, obj):
      self.ipContainerID:int = obj["ipContainerID"]
      """  Container ID to reset  """  
      self.ipDisburseMethod:str = obj["ipDisburseMethod"]
      """  Landed Cost Disbursment method  """  
      pass

class ResetLandedCostDisbursements_output:
   def __init__(self, obj):
      pass

class ShipContainer_input:
   """ Required : 
   containerToShip
   """  
   def __init__(self, obj):
      self.containerToShip:int = obj["containerToShip"]
      """  container To Ship  """  
      pass

class ShipContainer_output:
   def __init__(self, obj):
      pass

class SplitContainerShipment_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerDetailToSplitTableset] = obj["ds"]
      pass

class SplitContainerShipment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerDetailToSplitTableset] = obj["ds"]
      self.opContainerID:int = obj["parameters"]
      pass

      """  output parameters  """  

class TransferIndirectCosts_input:
   """ Required : 
   ipTargetContainerID
   ds
   """  
   def __init__(self, obj):
      self.ipTargetContainerID:int = obj["ipTargetContainerID"]
      """  Target Container ID  """  
      self.ds:list[Erp_Tablesets_ContainerMiscToTransferTableset] = obj["ds"]
      pass

class TransferIndirectCosts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerMiscToTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnShipContainer_input:
   """ Required : 
   containerToUnShip
   """  
   def __init__(self, obj):
      self.containerToUnShip:int = obj["containerToUnShip"]
      """  container To UnShip  """  
      pass

class UnShipContainer_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtContainerTrackingTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtContainerTrackingTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateLCAppliedAmt_input:
   """ Required : 
   origLCAmt
   newLCAmt
   ipcontainerID
   ipAppliedAmt
   """  
   def __init__(self, obj):
      self.origLCAmt:int = obj["origLCAmt"]
      self.newLCAmt:int = obj["newLCAmt"]
      self.ipcontainerID:int = obj["ipcontainerID"]
      self.ipAppliedAmt:int = obj["ipAppliedAmt"]
      pass

class UpdateLCAppliedAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totApplied:int = obj["parameters"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateLandedCostDisbursements_input:
   """ Required : 
   ipContainerID
   ds
   """  
   def __init__(self, obj):
      self.ipContainerID:int = obj["ipContainerID"]
      self.ds:list[Erp_Tablesets_ContainerTrackingTableset] = obj["ds"]
      pass

class ValidateLandedCostDisbursements_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lcError:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateShipQty_input:
   """ Required : 
   shipQty
   shipUOM
   ium
   partNum
   poNum
   poLine
   poRelNum
   """  
   def __init__(self, obj):
      self.shipQty:int = obj["shipQty"]
      self.shipUOM:str = obj["shipUOM"]
      self.ium:str = obj["ium"]
      self.partNum:str = obj["partNum"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      self.poRelNum:int = obj["poRelNum"]
      pass

class ValidateShipQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.WarningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

